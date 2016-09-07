from rx import Observable, Observer


class ConsoleWriter(Observer):
  def on_next(self, x):
    print x
  def on_error(self, x):
    print x
  def on_completed(self):
    print "DONE writer"


class Grouper(Observer):
  def on_next(self, x):
    x \
      .map(lambda x: (x[0],1)) \
      .reduce(lambda acc, x: (x[0], acc[1]+x[1])) \
      .subscribe(ConsoleWriter())
  def on_error(self, x):
    print x
  def on_completed(self):
    print "DONE grouper"


def stream():
  return Observable.from_iterable([(0,1), (0,3), (1,4)])


events = stream()

events \
  .group_by( \
    lambda x: x[0],
    None,
    None
  ) \
  .subscribe(Grouper())

