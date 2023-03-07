#include "lists.h"
#include <unistd.h>
#include <stdlib.h>

/**
 * insert_node - inserts a number into a sorted singly linked list.
 *
 * @head: pointer, to an address, of to a singly linked list h
 * @number: number, to insert
 *
 * Return: the address of the new node, or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *tmp;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	tmp = *head;
	new->n = number;
	if (*head == NULL || (*head)->n >= number)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	else
	{
		while (tmp->next != NULL && tmp->next->n < number)
		{
			tmp = tmp->next;
		}
		new->next = tmp->next;
		tmp->next = new;
		return (new);
	}
}
