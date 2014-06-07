
def test_append_to_empty_list():
  a_list = []
  a_list.append(1)
  assert a_list[0] == 1
  assert len(a_list) == 1


def test_append_in_function():
  def append_to(a):
    a.append(2)
    return a
  a_list = [1]
  assert append_to(a_list) == [1,2]
  assert id(append_to(a_list)) == id(a_list)


def test_split():
  a_list = [1,2,3,4]
  head_list = []
  tail_list = []
  head_list = a_list[:1]
  tail_list = a_list[1:]
  assert head_list == [1]
  assert tail_list == [2,3,4]


def intersect_lookup(a, b):
  if len(a) < len(b):
    outer = a
    inner = b
  else:
    outer = b
    inner = a

  intersect = []
  for item in outer:
    if item in inner:
      intersect.append(item)
  return intersect


def intersect_merge(a,b):
  if len(a) < len(b):
    outer = sorted(a)
    inner = sorted(b)
  else:
    outer = sorted(b)
    inner = sorted(a)

  intersect = []
  i = 0
  for item in outer:
    while (i < len(inner) and item != inner[i]):
      i += 1
    if i < len(inner):
      intersect.append(item)
    elif i == len(inner):
      break
  return intersect


def intersect_comprehension(a, b):
  if len(a) < len(b):
    return [item for item in a if item in b]
  else:
    return [item for item in b if item in a]

intersects = [intersect_lookup, intersect_comprehension, intersect_merge]


def test_intersect_many():
  a_list = [1,2,3]
  b_list = [2,5,1,8,]
  for intersect in intersects:
    assert sorted(intersect(a_list, b_list)) == [1,2]
    assert sorted(intersect(b_list, a_list)) == [1,2]

def test_intersect_identical():
  a_list = [1,2,3]
  b_list = [1,2,3]
  for intersect in intersects:
    assert sorted(intersect(a_list, b_list)) == [1,2,3]

def test_intersect_empty():
  a_list = [1,2,3]
  b_list = []
  for intersect in intersects:
    assert sorted(intersect(a_list, b_list)) == []
    assert sorted(intersect(b_list, a_list)) == []

def test_intersect_one():
  a_list = [1,2,3]
  b_list = [2]
  for intersect in intersects:
    assert sorted(intersect(a_list, b_list)) == [2]
    assert sorted(intersect(b_list, a_list)) == [2]


def union_mutable(a,b):
  a.extend(b)
  return a

def union_immutable(a,b):
  return (a + b)

unions = [union_mutable, union_immutable,]

def test_union_empty():
  for union in unions:
    a_list = [1,2,3]
    b_list = []
    assert sorted(union(a_list, b_list)) == [1,2,3,]

def test_union_many():
  for union in unions:
    a_list = [1,2,3]
    b_list = [2,5,1,8,]
    assert sorted(union(a_list, b_list)) == [1,1,2,2,3,5,8,]

