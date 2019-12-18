#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * palindromechecker - cheks if a linked list is a palindrome
 *
 * @left: the pointer to the that moves to the left
 * @right: pointer that moves right
 * Return: 1 if its pal 0 if not
 */
int palindromechecker(listint_t **left, listint_t *right)
{
	int isp;

	if (right == NULL)
		return (1);

	isp = palindromechecker(left, right->next);
	if (isp == 0)
		return (0);
	isp = (right->n == (*left)->n);
	*left = (*left)->next;

	return (isp);
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
	int a = palindromechecker(head, *head);

	return (a);
}
