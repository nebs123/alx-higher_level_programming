#include "lists.h"

/**
 * check_cycle - checks if the list has cycle
 * @list: list to be checked for cycles
 *
 * Return: 0 if there is no cycle or 1 if there is cycle
 */
int check_cycle(listint_t *list)
{
	int len = 0;
	listint_t *ptr = list;

	while (ptr != NULL)
	{
		int counter = 0;
		listint_t *past = list;

		while (counter < len)
		{
			if (past == ptr)
				return (1);
			past = past->next;
			counter++;
		}
		len++;
		ptr = ptr->next;
	}
	return (0);
}
