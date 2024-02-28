#include <object.h>
#include <listobject.h>
/**
*print_python_list_info - the entry point
*@p: a given pointer
*/

void print_python_list_info(PyObject *p)
{
	long int sz  = PyList_Size(p);
	int a;
	PyListObject *obj = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", sz);
	printf("[*] Allocated = %li\n", obj->allocated);
	for (a = 0; a < s; a++)
		printf("Element %a: %s\n", a, Py_TYPE(obj->ob_item[a])->tp_name);
}
