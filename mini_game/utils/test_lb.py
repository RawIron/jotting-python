_MAX_ENTRIES = 2


class Node(object):

  def __init__(self):
    self.scores = []
    self.children = []

root = None


def create_root():
  global root
  root = Node()

def search(node):
  for idx, v in enumerate(node.scores):
    if score == v:
      return True, None
    if score < v:
      return False, node.children[idx]

def update(node, score):
  if len(node.scores) < _MAX_ENTRIES:
    node.scores.append(score)
    node.scores.sort()
  else:
    child = Node()
    child.scores.append(node.scores[0])
    child.scores.sort()
    node.children.append(child)
    node.scores[0] = score
    node.scores.sort()
  return

def highscore(node):
  if node.scores:
    return node.scores[-1]
  else:
    return 0



def test_no_scores():
  create_root()
  assert root.scores == []
  assert highscore(root) == 0

def test_one_scores():
  create_root()
  update(root, 2)
  assert root.scores == [2,]
  assert highscore(root) == 2

def test_root_overflow():
  create_root()
  update(root, 2)
  update(root, 5)
  update(root, 7)
  assert root.scores == [5,7]
  assert highscore(root) == 7

def test_top_10():
  pass

