#include "lists.h"
/**
 * check_cycle - checking if linked list have cycled
 * @list: linked list given to check
 * Return: 1 if the list has a cycle otherwise 0
 */
int check_cycle(listint_t *list)
{
listint_t *slw = list;
listint_t *fst = list;

if (!list)
return (0);

while (slw && fst && fst->next)
{
slw = slw->next;
fst = fst->next->next;
if (slw == fst)
return (1);
}
return (0);
}
