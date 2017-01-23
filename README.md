# python  package and _ _init _ _.py



#quick start 


##the simplest package struct tree 
```
testpackage.
 ├── example.py
 ├── example.pyc
 ├── __init__.py
 ├── __init__.pyc
 └── subpackage
      ├── example1.py
      ├── example1.pyc
      ├── __init__.py
      └── __init__.pyc
```
##project  struct tree
```
python_import_package
 ├── hello.py
 ├── README.md
 ├── status
 └── testpackage
     ├── example.py
     ├── example.pyc
     ├── __init__.py
     ├── __init__.pyc
     └── subpackage
          ├── example1.py
          ├── example1.pyc
          ├── __init__.py
          └── __init__.pyc
```
## hello.py import package 
```
#Inspired by #http://mikegrouchy.com/blog/2012/05/bepythonic__init__py.html


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
```


##python hello.py output
```
i love python
i love python
i love python
i love python
i love python
i love python
```









