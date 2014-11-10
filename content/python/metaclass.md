Title: python 元类
Tags: python, metaclass
Date: 2014-11-02 20:00:00
元类就是用来创建类的“东西”, 类是其元类的实例(a class is an instance of its metaclass), type就是Python在背后用来创建所有类的元类(参见[python type system](/posts/python/type.html)), 下面代码展示了type的基本用法.

    >>> MyClass = MetaClass()

    >>> class Foo(object): 
            pass

    >>> def echo_bar(self):
            print self.bar
       
    >>> FooChild = type('FooChild', (Foo,), {'echo_bar': echo_bar}) # Foo is base class
    >>> hasattr(Foo, 'echo_bar')
    False
    >>> hasattr(FooChild, 'echo_bar')
    True
    >>> my_foo = FooChild()
    >>> my_foo.echo_bar()
    True

### 为什么要使用元类
元类的主要目的就是为了当创建类时能够自动地改变类, 一般来说根本就用不上它。
> “元类就是深度的魔法，99%的用户应该根本不必为此操心。如果你想搞清楚究竟是否需要用到元类，那么你就不需要它。那些实际用到元类的人都非常清楚地知道他们需要做什么，而且根本不需要解释为什么要用元类。”  —— Python界的领袖 Tim Peters

### __metaclass__属性

当你写如下代码时 :

        class Foo(Bar):
           __metaclass__ = something
           [...]

Python做了如下的操作:
Foo中有__metaclass__这个属性吗？如果是，Python会在内存中通过__metaclass__创建一个名字为Foo的类对象（我说的是类对象，请紧跟我的思路）。如果Python没有找到__metaclass__，它会继续在Bar（父类）中寻找__metaclass__属性，并尝试做和前面同样的操作。如果Python在任何父类中都找不到__metaclass__，它就会在模块层次中去寻找__metaclass__，并尝试做同样的操作。如果还是找不到__metaclass__,Python就会用内置的type来创建这个类对象。

现在的问题就是，你可以在__metaclass__中放置些什么代码呢？答案就是：可以创建一个类的东西。那么什么可以用来创建一个类呢？type，或者任何使用到type或者子类化type的东东都可以。

### 自定义元类

\__metaclass\__ 可以是任意可以被调用的对象(callable object), 并不一定要是个类. 下面代码创建的元类目的是要把类的属性都改成大写形式.

    # 函数表示形式
    # 元类会自动将你通常传给‘type’的参数作为自己的参数传入
    def upper_attr(future_class_name, future_class_parents, future_class_attr):
        '''返回一个类对象，将属性都转为大写形式'''
        #  所有不以'__'开头的属性
        attrs = ((name, value) for name, value in future_class_attr.items() if not name.startswith('__'))

        uppercase_attr = dict((name.upper(), value) for name, value in attrs)
     
        # 通过'type'来做类对象的创建
        return type(future_class_name, future_class_parents, uppercase_attr)
     
    __metaclass__ = upper_attr  #  这会作用到这个模块中的所有类
     
    class Foo(object):
        bar = 'bip'

    if __name__ == '__main__':
        print hasattr(Foo, 'bar')
        # 输出: False
        print hasattr(Foo, 'BAR')
        # 输出:True

    # 类表示形式
    class UpperAttrMetaClass(type):
        # __new__ 是在__init__之前被调用的特殊方法
        def __new__(cls, future_class_name, future_class_parents, future_class_attr):
            attrs = ((name, value) for name, value in future_class_attr.items() if not name.startswith('__'))
            uppercase_attr = dict((name.upper(), value) for name, value in attrs)
            return type.__new__(cls, future_class_parents, uppercase_attr)


__metaclass__虽然可以接受任何可调用的对象，但是类相对于函数有以下好处:

- 意图会更加清晰。当你读到UpperAttrMetaclass(type)时(*从type继承*)，你知道接下来要发生什么。
- 你可以使用OOP编程。元类可以从元类中继承而来，改写父类的方法。元类甚至还可以使用元类。
- 你可以把代码组织的更好。当你使用元类的时候肯定不会是像我上面举的这种简单场景，通常都是针对比较复杂的问题。将多个方法归总到一个类中会很有帮助，也会使得代码更容易阅读。
- 你可以使用__new__, __init__以及__call__这样的特殊方法。它们能帮你处理不同的任务。就算通常你可以把所有的东西都在__new__里处理掉，有些人还是觉得用__init__更舒服些。


Python中的一切都是对象，它们要么是类的实例，要么是元类的实例，除了type。type实际上是它自己的元类，在纯Python环境中这可不是你能够做到的，这是通过在实现层面耍一些小手段做到的。其次，元类是很复杂的。对于非常简单的类，你可能不希望通过使用元类来对类做修改。你可以通过其他两种技术来修改类：

- Monkey patching
- class decorators

当你需要动态修改类时，99%的时间里你最好使用上面这两种技术.

refer:

- [0][http://blog.jobbole.com/21351/](http://blog.jobbole.com/21351/)
- [1][http://stackoverflow.com/questions/100003/what-is-a-metaclass-in-python](http://stackoverflow.com/questions/100003/what-is-a-metaclass-in-python)
