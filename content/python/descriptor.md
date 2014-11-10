Title: python 描述符 
Tags: python, descriptor Date: 2014-11-03 10:00:00

描述符就是对象的一个绑定了行为的特性(attribute with "binding behavior"), 对特性的操作内部转化为相应方法的调用. 默认的特性访问实际是操作(get, set, delete)的对象的__dict__特性(参见[__dict__](/posts/python/magic-object.html)),但特性访问时如果查找出来的对象实现了任意的描述符方法, python就会调用描述符的方法而不是默认的行为.

描述符是一个强大的通用的协议, 也是属性, 方法, 静态方法, 动态方法, super()背后的实现机制. python2.2中引入的新式类也是通过描述符实现的. 描述符简化了底层c代码, 为python程序提供了灵活的工具组.

### descriptor protocal

    descr.__get__(self, obj, type=None) --> value
    descr.__set__(self, obj, value) --> None
    descr.__delete__(self, obj) --> None
定义了以上三个任意的方法的对象就是描述符.如果一个对象只定义了\__get\__(), 被称为非数据描述符(non-data descriptor)(通常用于方法), 如果同时定义了\__get\__和\__set\__()被称为是 数据描述符(data descriptor). 


要创建一个只读描述符, 同时定义\__get\__和\__set\__, \__set\__ 只需要抛出一个AttributeError异常即可.

### 调用描述符
描述符的访问可以直接调用它的方法`type(object).__dict__['descr'].__get__(obj)`, 但是通常是通过访问特性的方式自动进行调用`obj.descr`.  对于obj.descr的访问方式, 遵循[特性查找顺序的](/posts/python/magic-object.html), 具体的调用方式取决与obj是实例还是类(新式类). 

obj是实例, 则在object.\__getattribute\__()中把`obj.descr` into `type(obj).__dict__['descr'].__get__(obj, type(obj))`

obj是类, 则在type.\__getattribute\__()中把`obj.descr` into `obj.__dict__['destr'].__get__(None, obj)`, 参见[特殊方法的查找](/posts/python/special-method-lookup.html).

对于上面的处理方式可以看出: \__get\__()的第一个参数要么是owner的实例, 要么是None. 描述符必须定义为class特性, 如果定义为实例特性, python不会自动调用\__get\__() 和 \__set\__() 方法.

对描述符赋值`obj.descr = 100`, 转化为\__set\__()的调用`type(obj).__dict__['descr'].__set__(obj, 100)`, 第一个参数是句点前的实例, 第二个参数是要赋值的值.
同样的`del obj.descr`则调用__delete__()方法.


refer:

- [0][http://nbviewer.ipython.org/gist/ChrisBeaumont/5758381/descriptor_writeup.ipynb](http://nbviewer.ipython.org/gist/ChrisBeaumont/5758381/descriptor_writeup.ipynb)
- [1][https://docs.python.org/2/howto/descriptor.html](https://docs.python.org/2/howto/descriptor.html)
