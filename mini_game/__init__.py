import sys,os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import players.player
import players.datastore as _ds

__all__ = ['forAll',]

def forAll():
  print('eeh')

def _invisible():
  print('not here')

def do():
  print("g called")

class A():
  pass

print('__init__ loaded')
