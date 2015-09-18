.py - Regular scripts
.pyc - compiled script (Bytecode)
.pyo - optimized pyc file
.pyd - Python script made as a Windows DLL
.pyx - Cython src to be converted to C/C++

In Python 2.7, -O has the following effect:

- the byte code extension changes to .pyo
- sys.flags.optimize gets set to 1
- __debug__ is False
- strip all asserts statements(The current code generator emits no code for an assert statement when optimization is requested at compile time.)

In addition -OO has the following effect:

- doc strings are not available

To verify the effect for a different release of CPython, grep the source code for Py_OptimizeFlag.

refer:

- [http://stackoverflow.com/questions/8822335/what-does-python-file-extensions-pyc-pyd-pyo-stand-for](http://stackoverflow.com/questions/8822335/what-does-python-file-extensions-pyc-pyd-pyo-stand-for)
- [http://stackoverflow.com/questions/4777113/what-does-python-optimization-o-or-pythonoptimize-do](http://stackoverflow.com/questions/4777113/what-does-python-optimization-o-or-pythonoptimize-do)

