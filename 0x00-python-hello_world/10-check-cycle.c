#include "lists.h"

/**
 * check_cycle - checks if asingly linked list has a cycle in it
 *
 * @list: the pointer to the first node of the list
 * Return: 0 if there is no cycle 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *tortoise = head;
	listint_t *hare = head;

	if (list == NULL)
		return (0);

	while (tortoise && hare && hare->next)
	{
		if (tortoise == hare)
			return (1);

		tortoise = tortoise->next;
		hare = hare->next->next;

	}
	return (0)
}
