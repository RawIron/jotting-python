
def test_append_to_empty_list():
  a_list = []
  a_list.append(1)
  assert a_list[0] == 1
  assert len(a_list) == 1


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


def intersect_comprehension(a, b):
  if len(a) < len(b):
    return [item for item in a if item in b]
  else:
    return [item for item in b if item in a]

intersect = intersect_lookup


def test_intersect_many_elements():
  a_list = [1,2,3]
  b_list = [2,5,1,8,]
  assert sorted(intersect(a_list, b_list)) == [1,2]
  assert sorted(intersect(b_list, a_list)) == [1,2]

def test_intersect_empty():
  a_list = [1,2,3]
  b_list = []
  assert sorted(intersect(a_list, b_list)) == []
  assert sorted(intersect(b_list, a_list)) == []

def test_intersect_one_element():
  a_list = [1,2,3]
  b_list = [2]
  assert sorted(intersect(a_list, b_list)) == [2]
  assert sorted(intersect(b_list, a_list)) == [2]

