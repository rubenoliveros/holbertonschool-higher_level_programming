#include "lists.h"
/**
 * check_cycle - function to check if it is a singly linked list or it has a
 * cycle in it
 * @list: list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *current = list, *nextnode = list;

	while (current && nextnode && nextnode->next)
	{
		current = current->next;
		nextnode = nextnode->next->next;
		if (current == nextnode)
			return (1);
	}
	return (0);
}
