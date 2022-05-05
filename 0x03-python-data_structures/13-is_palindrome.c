#include "lists.h"
/**
 * is_palindrome - Function that checks if the list is a palindrome or not
 * @head: Head of a linked list
 * Return: 0 if False, 1 if True
 */
int is_palindrome(listint_t **head)
{
	int size = 0, idx = 0;
	int list[2048];
	
	if (*head == NULL || (*head)->next == NULL)
		return (1);
	while (*head != NULL)
	{
		list[size] = (*head)->n;
		*head = (*head)->next;
		size++;
	}
	while (size >= idx)
	{
		if (list[size - 1] != list[idx])
			return (0);
		size --;
		idx++;
	}
	return (1);
}
