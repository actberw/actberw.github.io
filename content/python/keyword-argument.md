There are two kinds of argument:

- keyword arguments of the form kwarg=value or passed as a value in a dictionary preceded by **.

    complex(real=3, imag=5)
    complex(**{'real': 3, 'imag': 5})

- positional argumen



"**kwargs" in the function definition, kwargs receives a dictionary containing all the keyword arguments beyond the formal parameter list. Remember 'kwargs' will be a dictionary. 


refer:

- [http://agiliq.com/blog/2012/06/understanding-args-and-kwargs/](http://agiliq.com/blog/2012/06/understanding-args-and-kwargs/)
- [http://stackoverflow.com/questions/1419046/python-normal-arguments-vs-keyword-arguments](http://stackoverflow.com/questions/1419046/python-normal-arguments-vs-keyword-arguments)
