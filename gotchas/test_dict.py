
def test_dict_update():
  a_dict = {}
  a_dict["egg"] = 0.12
  a_dict["egg"] = 0.15
  assert a_dict["egg"] == 0.15


def test_dict_uniqlist():
  a_list = ["egg", "apple", "bread", "egg",]
  a_dict = dict([(food,1) for food in a_list])
  assert a_dict == {"apple":1, "bread":1, "egg":1,}

def test_dict_keeps_latest():
  a_list = [("egg", 0.12), ("egg", 0.34),]
  assert dict(a_list) == {"egg": 0.34,}

def test_sort_tuples():
  names = ["john", "emil", "ed",]
  names_len = [(len(name), name) for name in names]
  assert sorted(names_len) == [(2,"ed"), (4,"emil"), (4,"john"),]
