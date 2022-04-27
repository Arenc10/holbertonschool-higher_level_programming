#include "lists.h"
/**
 * check_cycle - Function that checks whetehr is a cycle on a linked list
 * @list: First operand a node
 * Return: 0 if there is no cyce or 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *fast, *slow;

	if (list == NULL)
		return (0);
	fast = list->next;
	slow = list;

	while (fast != NULL && fast->next && slow != NULL)
	{
		if (fast == slow)
			return (1);
		fast = fast->next->next;
		slow = slow->next;
	}
	return (0);
}
