#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * get_nodeint_at_index - gets the node at Nth position
 *
 * @head: the pointer to the first node
 * @index: the node to look for
 * Return: the pointer if index is found or NULL if not
 */

listint_t *get_nodeint_at_index(listint_t *head, unsigned int index)
{
	unsigned int count = 0;

	while (head != NULL)
	{
		if (count == index)
			return (head);
		count++;
		head = head->next;
	}

	return (NULL);
}
/**
 * is_palindrome - cheks if a linked list is a palindrome
 *
 * @head: the pointer to the first node
 *
 * Return: 1 if its pal 0 if not
 */


int is_palindrome(listint_t **head)
{
	int len = 0;
	listint_t *last = *head, *tmp, *tmp2;

	while (last != NULL)
	{
		last = last->next;
		len++;
	}
	tmp2 = *head;
	while (len--)
	{
		tmp = get_nodeint_at_index(*head, len);
		if (tmp->n != tmp2->n)
			return (0);
		tmp2 = tmp2->next;
	}
	return (1);
}
