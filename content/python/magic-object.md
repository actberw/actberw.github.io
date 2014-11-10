Title: python magic object
Tags: python, __init__
Date: 2014-11-03 10:00:00

### \_\_dict\_\_

The default behavior for attribute access is to get, set, or delete the attribute from an object’s dictionary. For instance, a.x has a lookup chain starting with `a.__dict__['x']`, then `type(a).__dict__['x']`, and continuing through the base classes of type(a) excluding metaclasses. 

### Customizing attribute access

\_\_getattr\_\_, \_\_setattr\_\_, \_\_delattr\_\_, \_\_getattribute\_\_(new-style class)
A key difference between \_\_getattr\_\_ and \_\_getattribute\_\_ is that \_\_getattr\_\_ is only invoked if the attribute wasn't found the usual ways. It's good for implementing a fallback for missing attributes, and is probably the one of two you want

When retrieving an attribute from an object (print objectname.attrname) Python follows these steps(参见[mro](/posts/python/mro.html)和refer[0]):

 - If attrname is a special (i.e. Python-provided) attribute for objectname, return it.
 - Check `objectname.__class__.__dict__` for attrname. If it exists and is a data-descriptor, return the descriptor result. Search all bases of `objectname.__class__` for the same case.
 - Check `objectname.__dict__` for attrname, and return if found. If objectname is a class, search its bases too. If it is a class and a descriptor exists in it or its bases, return the descriptor result.
 - Check `objectname.__class__.__dict__` for attrname. If it exists and is a non-data descriptor, return the descriptor result. If it exists, and is not a descriptor, just return it. If it exists and is a data descriptor, we shouldn't be here because we would have returned at point 2. Search all bases of `objectname.__class__` for same case.
 - Raise AttributeError

`type.__getattribute__` 实现了上面的类搜索, `object.__getattribute__`实现了实例搜索, 参见[特殊方法的查找](/posts/python/special-method-lookup.html).

### \_\_slots\_\_
By default, instances of both old and new-style classes have a dictionary for attribute storage. This wastes space for objects having very few instance variables. The space consumption can become acute when creating large numbers of instances.

The default can be overridden by defining \_\_slots\_\_ in a new-style class definition. The \_\_slots\_\_ declaration takes a sequence of instance variables and reserves just enough space in each instance to hold a value for each variable. Space is saved because \_\_dict\_\_ is not created for each instance.

### Customizing instance and subclass checks
The following methods are used to override the default behavior of the isinstance() and issubclass() built-in functions.\_\_instancecheck\_\_ and \_\_subclasscheck\_\_

### \_\_call\_\_
alled when the instance is “called” as a function; if this method is defined, x(arg1, arg2, ...) is a shorthand for x.\_\_call\_\_(arg1, arg2, ...).

    class A(object):
        def __init__(self):
            print "init"
            
        def __call__(self):
            print "call"

    if __name__ == '__main__':
        a = A()
        # print init
        a()
        # print call

refer:

- [0][http://www.cafepy.com/article/python_attributes_and_methods/python_attributes_and_methods.html](http://www.cafepy.com/article/python_attributes_and_methods/python_attributes_and_methods.html)
