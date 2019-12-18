#include <Python.h>


/**
 * print_python_list_info - prints the onbject info of a python code
 *
 * @p : the object to be evaluated
 */

void print_python_list_info(PyObject *p)
{
	unsigned int i;

	printf("[*] Size of the Python List = %lu\n", Py_SIZE(p));
	printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
	for (i = 0; i < PyList_Size(p); i++)
	{
		printf("Element %d: %s\n",
i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
	}

}
