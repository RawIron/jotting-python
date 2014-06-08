import re


def test_words_space_one():
  line = "two one"
  splitter = re.compile('\\W*')
  assert sorted(splitter.split(line)) == ["one", "two",]

def test_words_space_many():
  line = "two      one"
  splitter = re.compile('\\W*')
  assert sorted(splitter.split(line)) == ["one", "two",]

def test_words_dash_one():
  line = "two-one"
  splitter = re.compile('\\W*')
  assert sorted(splitter.split(line)) == ["one", "two",]


def test_words_commas():
  line = "two  , one"
  splitter = re.compile(' *, *')
  assert sorted(splitter.split(line)) == ["one", "two",]
