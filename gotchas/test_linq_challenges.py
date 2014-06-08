
# Challenge 2: Indexed Filtering
# Find all the names in the array "names" where the length of the 
# name is less than or equal to the index of the element + 1.

def test_challenge2():
  names = ["Sam", "Pamela", "Dave", "Pascal", "Erik"]
  matches = [name for index, name in enumerate(names) if len(name) <= index+1]
  assert  sorted(matches) == ["Erik"]


# Challenge 3: Selecting/Mapping
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


