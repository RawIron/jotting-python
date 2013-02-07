#!/usr/bin/python

import setuptools
import sys

import playground as w
from playground.aModule import simple, A
import utils


a = [23, 45,]
b = "34.454"
c = "45"
x = b.split('.')
print x

simple()
w.forAll()
w._ds.store()

dir()
print sys.path
