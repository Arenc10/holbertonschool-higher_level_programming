#include "lists.h"
#include <stdlib.h>

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp, *new;
	int key;

	new = malloc(sizeof(listint_t));
	new->n = number;
	new->next = NULL;
	key = number;

	if (*head == NULL || key < (*head)->n)
	{
		new->next = *head;
		*head = new;
	}
	else
	{
		temp = *head;
		while (temp->next != NULL && temp->next->n < key)
			temp = temp->next;
		new->next = temp->next;
		temp->next = new;
	}
	return (*head);

}
