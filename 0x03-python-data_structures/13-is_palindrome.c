#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * is_palindrome - check if it is a palindorme.
 * @head: pointer to head of list
 * Return: 0 if it is not a palindrome or 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *current;
	int buff[2048], valueNum = 0, i = 0;

	if (!(*head))
		return (1);

	current = *head;
	while (current != NULL)
	{
		buff[valueNum] = current->n;
		current = current->next;
		valueNum++;
	}

	while (i < valueNum)
	{
		if (buff[i] == buff[valueNum - 1])
		{
			valueNum--;
			i++;
		}
		else
			return (0);
	}
	return (1);
}
