
# Challenge 2: Indexed Filtering
#
# Find all the names in the array "names" where the length of the 
# name is less than or equal to the index of the element + 1.

def test_challenge2():
  names = ["Sam", "Pamela", "Dave", "Pascal", "Erik"]
  matches = [name for index, name in enumerate(names) if len(name) <= index+1]
  assert  sorted(matches) == ["Erik"]


# Challenge 3: Selecting/Mapping
#
# Say we have a list of names and we would like to print "Hello" in 
# front of all the names:
# List<string> nameList1 = new List(){ "Anders", "David", "James",
# nameList1.Select(c => "Hello! " + c).ToList()
#         .ForEach(c => Console.WriteLine(c));

def test_challenge3_comprehension():
  names = ["Sam", "Pamela",]
  messages = ["Hello, " + name for name in names]
  assert  messages == ["Hello, Sam", "Hello, Pamela",]

def test_challenge3_map():
  names = ["Sam", "Pamela",]
  messages = map(lambda x: "Hello, " + x, names)
  assert  messages == ["Hello, Sam", "Hello, Pamela",]


# Challenge 12: Grouping by a Criterium
#
# Group the elements of a collection of strings by their length.

def test_challenge12_forloop():
  names = ["Sam", "Samuel", "Samu", "Ravi", "Ratna", "Barsha"]
  groups = {}
  for name in names:
    if len(name) in groups:
      groups[len(name)].append(name)
    else:
      groups[len(name)] = [name,]
  assert groups[4] == ["Samu", "Ravi",]

def test_challenge12_forloop_short():
  names = ["Sam", "Samuel", "Samu", "Ravi", "Ratna", "Barsha"]
  groups = {}
  for name in names:
    groups.setdefault(len(name),[]).append(name)
  assert groups[4] == ["Samu", "Ravi",]
  assert groups[3] == ["Sam",]
  assert 1 not in groups

def test_challenge12_collections():
  names = ["Sam", "Samuel", "Samu", "Ravi", "Ratna", "Barsha"]
  from collections import defaultdict
  groups = defaultdict(list)
  for name in names:
    groups[len(name)].append(name)
  assert groups[4] == ["Samu", "Ravi",]
  assert 1 not in groups

def test_challenge12_itertools():
  names = ["Sam", "Samuel", "Samu", "Ravi", "Ratna", "Barsha"]
  from itertools import groupby
  names_len = [(len(name), name) for name in names]
  groups = {}
  for k,iter in groupby(sorted(names_len), key=lambda s:s[0]):
    groups.setdefault(k, list(v[1] for v in iter))
  assert groups[4] == ["Ravi", "Samu",]
  assert 1 not in groups


# Challenge 13: Filter Distinct Elements
# 
# Obtain all the distinct elements from a collection.

def test_challenge13_set():
  songs = ["Song#1", "Song#2", "Song#2", "Song#2", "Song#3", "Song#1"]
  uniq_songs = set(songs)
  assert sorted(uniq_songs) == ["Song#1", "Song#2", "Song#3",]

