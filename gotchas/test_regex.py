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
  splitter = re.compile('\\W+')
  assert sorted(splitter.split(line)) == ["one", "two",]

def test_words_dash_ends():
  line = "two-one--"
  splitter = re.compile('\\W+')
  assert sorted(splitter.split(line)) == ["", "one", "two",]

def test_words_dash_special_many():
  line = "two- !one"
  splitter = re.compile('\\W+')
  assert sorted(splitter.split(line)) == ["one", "two",]

def test_words_dash_for_underscore():
  line = "two-one_three"
  splitter = re.compile('[^a-zA-Z0-9\-]+')
  assert sorted(splitter.split(line)) == ["three", "two-one",]


def test_words_commas():
  line = "two  , one"
  splitter = re.compile(' *, *')
  assert sorted(splitter.split(line)) == ["one", "two",]


def test_sub_wordbreak():
  line = 'one-\ntwo'
  replacer = re.compile('-\n')
  assert replacer.sub('-', line) == "one-two"
