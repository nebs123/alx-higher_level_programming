#include "lists.h"

/**
 * check_cycle - checks if the list has cycle
 * @list: list to be checked for cycles
 *
 * Return: 0 if there is no cycle or 1 if there is cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *ptr = list, *ptr2 = list;

	if (ptr2 != NULL)
		ptr2 = ptr2->next;

	while (ptr != NULL && ptr2 != NULL)
	{
		if (ptr == ptr2)
			return (1);
		ptr = ptr->next;
		ptr2 = ptr2->next;
		if (ptr2 != NULL)
			ptr2 = ptr2->next;

	}
	return (0);
}
