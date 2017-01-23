# python  package and _ _init _ _.py

# quick start 
## download the project 
```
git clone https://github.com/oxfordyang2016/python_import_package.git
```

Note: this is a projetc including a package consisted by some moudles and a suboackage including some moudles

## the simplest package struct tree 
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
## project  struct tree
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


## __init__.py(testpackage)
```
from example import testexample
__all__=['example']

```
## __init__.py(testpackage.subpackage)

```
from example1 import testexample1
__all__=['example1']

```
## about _ _init_ _.py
```
1.__init__.py is the indicator of  a package 
2.when __all__=['example']in __init__.py,
  you can use the below method in hello.py: 
  from testpackage import * 
  example.testexample()#'i love python'
3.when add `from example import example1` in __init__.py ,you can use 
  'from testpackage import example1' in hello.py  
4.usual call is valid such as 'from testpackage import example'  

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



## python hello.py output
```
i love python
i love python
i love python
i love python
i love python
i love python
```

###  Please feel free to aks any question in the post !





