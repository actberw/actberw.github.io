Title: 特殊方法的查找
Tags: python, method
Date: 2014-11-03 21:00:00
For old-style classes, special methods are always looked up in exactly the same way as any other method or attribute. This is the case regardless of whether the method is being looked up explicitly as in `x.__getitem__(i)` or implicitly as in `x[i]`.

For new-style classes, implicit invocations of special methods are only guaranteed to work correctly if defined on an object’s *type*, not in the object’s instance dictionary.
     
    class A(object):
        n = 1

对于上面定义的类A, `A.n` 实际上调用的是`type.__getattribute__`, `A().n`实际调用的是`object.__getattribute__`(参见[特性的搜索顺序](/posts/python/magic-object.html)).

Implicit special method lookup generally also bypasses the \__getattribute\__() method even of the object’s metaclass.Bypassing the \__getattribute\__() machinery in this fashion provides significant scope for speed optimisations within the interpreter, at the cost of some flexibility in the handling of special methods

refer:

- [0][https://docs.python.org/2/reference/datamodel.html#special-method-lookup-for-new-style-classes](https://docs.python.org/2/reference/datamodel.html#special-method-lookup-for-new-style-classes)
- [1][http://stackoverflow.com/questions/24150894/what-is-the-difference-between-type-getattribute-and-object-getattribute](http://stackoverflow.com/questions/24150894/what-is-the-difference-between-type-getattribute-and-object-getattribute)
