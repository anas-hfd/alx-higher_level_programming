#include "lists.h"

/**
 * is_palindrome - checks if the list is palind
 * @head: ptr to ptr to head
 * Return: int
 */

int is_palindrome(listint_t **head)
{
	listint_t *curr = *head, *palind = *head;
	int count = 0, i = 0, j = 0;

	if (!*head)
		return (1);

	while (curr)
	{
		curr = curr->next;
		count++;
	}
	curr = *head;
	for (i = 1; i <= count; i++)
	{
		for (j = i; j <= count - i; j++)
			palind = palind->next;
		if (curr->n != palind->n)
			return (0);
		curr = curr->next;
		palind = curr;
	}
	return (1);
}
