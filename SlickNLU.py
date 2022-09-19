import re

class Token:
  def __init__(self, word: str) -> None:
    m = re.match("([\w']*)([\.,;:!\?]*)", word)
    self.word = m.group(1).upper()
    self.display_word = m.group(1)
    self.post_punctuation = m.group(2)
    self.entity_type = None
    self.entity_start = False
    self.entity_end = False
    self.entity_value = None
    self.entity_match = None
    self.match_specificity = 0
    
  def clear_tags(self) -> None:
    self.entity_type = None
    self.entity_start = False
    self.entity_end = False
    self.entity_value = None
    self.entity_match = None
    self.match_specificity = 0
    

  def __str__(self) -> str:
    if (self.entity_end):
      if (self.entity_value == self.entity_match.keyword):
        return "{}{}]({}){}".format("[" if self.entity_start else "", self.display_word, self.entity_type, self.post_punctuation)
      else:
        return "{}{}]({}: {}){}".format("[" if self.entity_start else "", self.display_word, self.entity_type, self.entity_value, self.post_punctuation)
    return "{}{}{}".format("[" if self.entity_start else "", self.display_word, self.post_punctuation)

  def __repr__(self) -> str:
    return str(self)

class MatchCandidate:
  def __init__(self, keyword: str, canonical: str) -> None:
    self.keyword = keyword if keyword != "" else canonical
    self.canonical = canonical
    self.tokens = self.keyword.upper().split(" ")

  def __str__(self) -> str:
    if (self.keyword == self.canonical):
      return self.keyword
    return "{}=>{}".format(self.keyword, self.canonical)

  def __repr__(self) -> str:
    return str(self)

class SlickNLU:
  def __init__(self, dictionaries, keyword_last: bool = False) -> list[Token]:
    self.dictionaries = {}
    configurations = {entity_type: [rows for rows in config_text.split("\n") if rows != ""] for entity_type, config_text in dictionaries.items()}
    for (entity_type, rows) in configurations.items():
      self.dictionaries[entity_type] = []
      for row in rows:
        keywords = [kw.strip() for kw in re.split("[:,]+", row)]
        canonical = keywords.pop(-1 if keyword_last else 0)
        if len(keywords) == 0:
          self.dictionaries[entity_type].append(MatchCandidate(canonical, canonical))
        for keyword in keywords:
          self.dictionaries[entity_type].append(MatchCandidate(keyword, canonical))
  
  def interpret(self, transcript: str) -> None:
    transcript_tokens = [Token(word) for word in transcript.split(" ") if word != ""]
    
    for (entity_type, entities) in self.dictionaries.items():
      for term in entities:
        self.match_tokens(transcript_tokens, entity_type, term)
    return transcript_tokens
    
  
  def match_tokens(self, transcript_tokens, entity_type, match_candidate) -> None:
    i = 0
    tokens = match_candidate.tokens
    match_specificity = len(tokens)
    while i <= len(transcript_tokens) - len(tokens):
      j = 0
      match = True
      while match and j < len(tokens):
        if (transcript_tokens[i + j].match_specificity < match_specificity):
          if (transcript_tokens[i + j].word == tokens[j]):
            j += 1
            continue
        match = False
      if match:
        # Mark words
        j = 0
        while j < len(tokens):
          transcript_tokens[i + j].clear_tags()
          transcript_tokens[i + j].entity_type = entity_type
          transcript_tokens[i + j].match_specificity = match_specificity
          j += 1
        # Mark first word
        transcript_tokens[i].entity_start = True
        # Mark last word
        transcript_tokens[i + len(tokens) - 1].entity_end = True
        transcript_tokens[i + len(tokens) - 1].entity_match = match_candidate
        transcript_tokens[i + len(tokens) - 1].entity_value = match_candidate.canonical
      i += 1

def interpret(nlu: SlickNLU, transcript: str) -> str:
  tagged_tokens = nlu.interpret(transcript)
  tagged_transcript = " ".join([str(token) for token in tagged_tokens])
  print ("--")
  print (transcript)
  print ()
  print (tagged_transcript)
  print ()
