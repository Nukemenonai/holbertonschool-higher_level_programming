#include "lists.h"

/**
 * insert_node - inserts a node
 *
 * @head: the pointer to the head of the linked list
 * @number: the number to include in the n node field
 * Return: pointer to the new node else NULL
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *tmp;
	listint_t *tmp2;

	new = malloc(sizeof(listint_t));
	if ( new == NULL)
		return (NULL);

	new->n = number;
	tmp = *head;
	while(tmp->next != NULL)
	{
		if (tmp->n > number)
		{
			tmp2->next = new;
			new->next = tmp;
			return (new);
		}

		tmp2 = tmp;
		tmp = tmp->next;
	}
	return (NULL);
}
