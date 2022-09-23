#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - insert node with n=number into a sorted linked list
 * @head: pointer to the head pointer of the linked list
 * @number: the number to assign to the newly inserted node
 *
 * Return: NULL on failure otherwise returns newly inserted node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = malloc(sizeof(listint_t));
	listint_t *prev = NULL;
	listint_t *ptr = *head;

	if (node == NULL)
		return (NULL);
	node->n = number;

	while (ptr)
	{
		if (ptr->n > number)
			break;

		prev = ptr;
		ptr = ptr->next;
	}

	node->next = ptr;
	if (prev == NULL)
		*head = node;
	else
		prev->next = node;

	return (node);
}
