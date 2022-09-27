#include "lists.h"
#include <stdlib.h>

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
	int *arr = malloc(sizeof(int) * len), left, right;
	size_t i = 0;

	while (head)
	{
		*(arr + i) = head->n;
		head = head->next;
		i++;
	}

	if (len % 2 == 0)
	{
		left = len / 2 - 1;
		right = len / 2;
	} else
	{
		left = len / 2;
		right = len / 2;
	}
	while (left >= 0 && right < (int)len)
	{
		if (arr[left] != arr[right])
			return (0);
		left--;
		right++;
	}
	return (1);
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
