#include <stdio.h>
#include <stdlib.h>
#include <Python.h>
#include <listobject.h>

/**
 * print_python_list_info - Prints a Python list
 * @p: a python object
 * Return: void
 */


void print_python_list_info(PyObject *p)
{
	Py_ssize_t s, i, alloc;
	PyObject *object;

	s = PyList_Size(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %ld\n", s);
	printf("[*] Allocated = %ld\n", alloc);
	for (i = 0; i < s; i++)
	{
		object = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(object)->tp_name);
	}
}
