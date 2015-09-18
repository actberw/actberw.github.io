
gcc -fpic -c phash.c  -I /usr/include/python2.7/
gcc -shared -lpython2.7 -o  phash.so phash.o


    #include <Python.h>

    static PyObject* wrap_ph_dct_imagehash(PyObject* self, PyObject* args) {
        int result;
        char *file_name;
        uint64_t hash = 0;
        if (!PyArg_ParseTuple(args, "s:wrap_ph_dct_imagehash", &file_name))
            return NULL;
        printf("the file name: %s", file_name);
        Py_INCREF(Py_None);
        return Py_None;
    }

    static PyMethodDef Methods[] =
    {
        {"phash", wrap_ph_dct_imagehash, METH_VARARGS, "Caculate phash!"},
        {NULL, NULL}
    };

    void initphash()
    {
        PyObject* m;
        m = Py_InitModule("phash", Methods);
    }


    #include <Python.h>
    #include <pHash.h>

    #ifdef __cplusplus
    extern "C" {
    #endif

    static PyObject* wrap_ph_dct_imagehash(PyObject* self, PyObject* args) {
        int result;
        const char *file_name;
        uint64_t hash = 0;
        if (!PyArg_ParseTuple(args, "s:wrap_ph_dct_imagehash", &file_name))
            return NULL;

        result = ph_dct_imagehash(filen_name, &hash);
        if (result == 0)
            return Py_BuildValue('i', hash);

        return Py_BuildValue('i', result);
    }

    static PyMethodDef exampleMethods[] =
    {
        {'phash', wrap_ph_dct_imagehash, METH_VARARGS, "Caculate phash!"},
        {NULL, NULL}
    };

    void initpHash() {
        PyObject* m;
        m = Py_InitModule("pHash", exampleMethods);
    }

    #ifdef __cplusplus
    }
    #endif

refer:

- [http://www.ibm.com/developerworks/cn/linux/l-pythc/](http://www.ibm.com/developerworks/cn/linux/l-pythc/)
