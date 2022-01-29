#define PY_SSIZE_T_CLEAN

#include "D:\Python37\Python\includePython.h"


int fib(int n)
{
  if (n <= 1)
    return n;
  return fib(n-1) + fib(n-2);
}


PyObject* c_fib(PyObject* self, PyObject* args)
{
  int n;
  PyArg_ParseTuple(args, "i", &n);
  n = fib(n);
  return PyLong_FromLong(n);
}

PyMethodDef module_methods[] = 
{
    {"c_fib", c_fib, METH_VARARGS, "Method description"},
    {NULL} // this struct signals the end of the array
};

struct PyModuleDef c_module =
{
    PyModuleDef_HEAD_INIT, // Always initialize this member to PyModuleDef_HEAD_INIT
    "c_module", // module name
    "Module description", // module description
    -1, // module size (more on this later)
    module_methods // methods associated with the module
};

PyMODINIT_FUNC PyInit_c_module()
{
    return PyModule_Create(&c_module);
}