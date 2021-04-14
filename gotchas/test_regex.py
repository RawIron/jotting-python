import re


def test_words_space_one():
  line = "two one"
  splitter = re.compile(r'\s+')
  assert sorted(splitter.split(line)) == ["one", "two",]

def test_words_space_many():
  line = "two      one"
  splitter = re.compile(r'\s+')
  assert sorted(splitter.split(line)) == ["one", "two",]

def test_words_dash_one():
  line = "two-one"
  splitter = re.compile(r'\W+')
  assert sorted(splitter.split(line)) == ["one", "two",]

def test_words_dash_ends():
  line = "two-one--"
  splitter = re.compile(r'\W+')
  assert sorted(splitter.split(line)) == ["", "one", "two",]

def test_words_dash_special_many():
  line = "two- !one"
  splitter = re.compile(r'\W+')
  assert sorted(splitter.split(line)) == ["one", "two",]

def test_words_dash_for_underscore():
  line = "two-one_three"
  splitter = re.compile(r'[^a-zA-Z0-9\-]+')
  assert sorted(splitter.split(line)) == ["three", "two-one",]


def test_words_commas():
  line = "two  , one"
  splitter = re.compile(r' *, *')
  assert sorted(splitter.split(line)) == ["one", "two",]


def test_sub_wordbreak():
  line = 'one-\ntwo'
  replacer = re.compile(r'-\n')
  assert replacer.sub('-', line) == "one-two"


def test_exact_2_ones():
    pattern = r'1{2}'
    matches = re.search(pattern, '1211')
    assert(matches.group() == '11')

def test_1_digit_1():
    pattern = r'1[0-9]?1'
    matches = re.search(pattern, '1211')
    assert(matches.group() == '121')
    matches = re.search(pattern, '1121')
    assert(matches.group() == '11')
