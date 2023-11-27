#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - Checks if a linked list has a cycle.
 * @list: A pointer to the head of the linked list.
 *
 * Return: 1 if the linked list has a cycle, 0 otherwise.
 */
int check_cycle(listint_t *list)
{
	listint_t *turtle, *hare;

	turtle = list->next;
	hare = list->next->next;

	while (turtle && hare && hare->next)
	{
		if (turtle == hare)
			return (1);

		turtle = turtle->next;
		hare = hare->next->next;
	}

	return (0);
}
