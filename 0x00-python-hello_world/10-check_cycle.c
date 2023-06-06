#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - checks if the list contains a cycle
 * @list: the list
 * Return: cycles
 */

int check_cycle(listint_t *list)
{
	listint_t *check, *curr;

	if (list == NULL || list->next == NULL)
	{
		return (0);
	}
	curr = list;
	check = curr->next;

	while (curr != NULL && check->next != NULL
		&& check->next->next != NULL)
	{
		if (curr == check)
		{
			return (1);
		}
		curr = curr->next;
		check = check->next->next;
	}
	return (0);
}
