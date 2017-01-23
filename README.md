# python  package and _ _init _ _.py

# quick start 
## download the project 
```
git clone https://github.com/oxfordyang2016/python_import_package.git
```

Note: this is a projetc including a package consisted by some moudles and a subpackage including some moudles

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


## _ _ init _ _.py(testpackage)
```
from example import testexample
__all__=['example']
```
## _ _ init _ _.py(testpackage.subpackage)

```
from example1 import testexample1
__all__=['example1']
```
## about _  _ init _ _  .py
```
1.__init__.py is the indicator of  a package 
2.when __all__=['example']in __init__.py,
  you can use the below method in hello.py: 
  from testpackage import * 
  example.testexample()#'i love python'
3.when add `from example import example1` in __init__.py ,you can use 
  'from testpackage import example1' in hello.py  
4.usual call is valid such as 'from testpackage import example'  
5.__init__.py can be a empty file and you need import moudle in usual method.
6.imported things is moudle ,function ,name ,classs or more low level things.
```
## hello.py import package 
```
#Inspired by #http://mikegrouchy.com/blog/2012/05/bepythonic__init__py.html

#usual import
from testpackage import *
example.testexample()
from testpackage.subpackage import example1
example1.testexample1()

#about __init__.py
from  testpackage import testexample
testexample()
from testpackage import *
example.testexample()
from testpackage.subpackage import *
example1.testexample1()
from testpackage.subpackage import testexample1
testexample1()
```
####  Notice the difference between '__all__' name and 'from testpackage import *.


## python hello.py output
```
i love python
i love python
i love python
i love python
i love python
i love python
```

###  Please feel free to ask any question in the post !





