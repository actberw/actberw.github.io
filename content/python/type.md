Title: python  type system
Tags: python, type, object model, class
Date: 2014-11-02 14:00:00

Up to Python 2.1 the concept of class was unrelated to the concept of type, and old-style classes were the only flavor available. For an old-style class, the statement x.__class__ provides the class of x, but type(x) is always <type 'instance'\>. This reflects the fact that all old-style instances, independent of their class, are implemented with a single built-in type, called instance. New-style classes were introduced in Python 2.2 to unify the concepts of class and type. The term type is equivalent to the term class, a new-style class is simply a user-defined type. If x is an instance of a new-style class, then type(x) is typically the same as x.__class__ . this post is about new-style class or type.

### object defination  
We define an object by saying it has:
    - Identity
    - A value
    - A type
    - One or more bases

In python, everything is an object.

### object and relationship
These are the subclass-superclass relationship (a.k.a. specialization or inheritance, "man is an animal", etc.) and the type-instance relationship (a.k.a instantiation, "Joe is a man", etc.). <type 'type'\> and <type 'object'\> are two primitive objects of the system. If an object is an instance of <type 'type'\>, then it is a type, otherwise it is not a type(参见[python元类](/posts/python/metaclass.html)). <type 'type'\> is an instance of itself and a subclass of <type 'object'\>. <type 'object'\> is an instance of <type 'type'\> and a subclass of no object. 

    >>> isinstance(object, object) 1
    True
    >>> isinstance(type, object) 2
    True
Type objects share the following traits:

    - They are used to represent abstract data types in programs
    - They can be subclassed
    - They can be instantiated
    - The type of any type object is <type 'type'>.

### more built-in types
![built-in types](/img/builtin_types.png)  
solid line means inheritance from, dashed line means an instance of.  
If we created a new object by subclassing <type 'type'\> it would be in the leftmost space, and would also be both a subclass and instance of <type 'type'\>

refer:

- [0][http://www.cafepy.com/article/python_types_and_objects/python_types_and_objects.html](http://www.cafepy.com/article/python_types_and_objects/python_types_and_objects.html)
