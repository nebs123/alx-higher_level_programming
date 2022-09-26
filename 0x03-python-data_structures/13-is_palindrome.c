#include "lists.h"

/**
 * is_palindrome - returns if a list is palindrome
 * @head: pointer to a pointer to the head of the list
 *
 * Return: 1 if list is palindrome or 0 if it is not
 */
int is_palindrome(listint_t **head)
{
	return (helper_palindrome(*head, list_len(*head)));
}
/**
 * helper_palindrome - helper to is_palindrome
 * @head: pointer to head of the list
 * @len: pointer to length of the list
 * Return: 1 if list is palindrome or 0 if it is not
 */
int helper_palindrome(listint_t *head, size_t len)
{
	listint_t *ptr;
	size_t i;

	if (len == 0 || len == 1)
		return (1);
	ptr = head;
	for (i = 0; i < len - 1; i++)
	{
		ptr = ptr->next;
	}
	if (ptr->n != head->n)
		return (0);
	else
		return (helper_palindrome(head->next, len - 2));
}

/**
 * list_len - returns length of list
 * @head: pointer to list
 *
 * Return: length of the list
 */
size_t list_len(listint_t *head)
{
	size_t len = 0;
	while (head)
	{
		len++;
		head = head->next;
	}
	return (len);
}
