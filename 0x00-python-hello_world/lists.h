#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct listint_ - linked list
 * @i: integer
 * @nt: points to the next node
 *
 * Description: singly linked list struct
 */
typedef struct listint_
{
	int i;
	struct listint *nt;
} listint;

size_t print_listint(const listint_t *k);
listint_t *add_nodeint(listint**head, const int k);
void free_listint(listint *h);
int check(listint_t *l);

#endif /* LISTS_H */

