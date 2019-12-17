#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - cheks if a linked list is a palindrome
 *
 * @head: the pointer to the first node
 *
 * Return: 1 if its pal 0 if not
 */


int is_palindrome(listint_t **head)
{
	unsigned int len = 0;
	listint_t *tmp = *head, *tmp2 = *head, *tmp3 = *head;
	unsigned int count;

	while (tmp != NULL)
	{
		tmp = tmp->next;
		len++;
	}

	while (len--)
	{
		count = 0;
		tmp3 = *head;
		while (tmp3 != NULL)
		{
			if (count == len)
				break;
			count++;
			tmp3 = tmp3->next;
		}

		if (tmp3->n != tmp2->n)
			return (0);
		tmp2 = tmp2->next;
	}
	return (1);
}
