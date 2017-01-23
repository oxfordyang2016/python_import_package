#Inspired by http://mikegrouchy.com/blog/2012/05/be-pythonic-__init__py.html


from testpackage import *
example.testexample()
from testpackage.subpackage import example1

example1.testexample1()

from  testpackage import testexample

testexample()

from testpackage import *

example.testexample()

from testpackage.subpackage import *

example1.testexample1()

from testpackage.subpackage import testexample1
testexample1()









