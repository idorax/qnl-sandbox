#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "libsort.h"

int g_isint = true;

void
list_init(list_t **head, list_t *node)
{
	if (*head == NULL) {
		*head = node;
		return;
	}

	list_t *q = *head;
	for (list_t *p = *head; p != NULL; p = p->next)
		q = p;
	q->next = node;
}

void
list_fini(list_t *head)
{
	list_t *p = head;
	while (p != NULL) {
		list_t *q = p;
		p = p->next;
		free(q);
	}
}

void
list_show(list_t *head)
{
	if (head == NULL)
		return;

	for (list_t *p = head; p != NULL; p = p->next)
		printf("%d ", p->data);
	printf("\n");
}

void
list_insert(list_t **head, list_t *node)
{
	if (*head == NULL) {
		*head = node;
		return;
	}

	/* get both prev and next of the node to insert */
	list_t *node_prev = *head;
	list_t *node_next = NULL;
	for (list_t *p = *head; p != NULL; p = p->next) {
		if (p->data < node->data) {
			node_prev = p;
			continue;
		}

		node_next = p;
		break;
	}

	if (node_next == NULL) { /* append node to the tail */
		node_prev->next = node;
	} else {
		if (node_next == node_prev) { /* == *head */
			node->next = *head;
			*head = node;
			return;
		}

		/* node_prev -> node -> node_next */
		node_prev->next = node;
		node->next = node_next;
	}
}

void
list_sort(list_t **head)
{
	if (*head == NULL)
		return;

	list_t *headp = *head; /* copy *head to headp before snip headp->next */
	list_t *p = headp->next; /* init p (move forward) before cut-off */
	headp->next = NULL;      /* now cut off headp->next */

	while (p != NULL) {
		list_t *this = p;  /* copy p to this before snip this->next */
		p = p->next;       /* move p forward before cut-off */
		this->next = NULL; /* now cut off this->next */
		list_insert(&headp, this); /* insert this node to list headp */
	}

	*head = headp; /* always save headp back even if headp == *head */
}

/*
 * Exchange two element of array
 */
void
exchange(int a[], int i, int j)
{
	int t = a[i];
	a[i] = a[j];
	a[j] = t;
}

/*
 * Init the value of global var g_isint
 */
void
init_gvar_isint()
{
	char *s = getenv("ISINT");
	if (s != NULL && strncmp(s, "true", 4) == 0)
		g_isint = true;
	else if (s != NULL && strncmp(s, "false", 4) == 0)
		g_isint = false;
	else
		g_isint = true;
}

void
init_array(char *src[], int *dst, int n)
{
	if (g_isint) {
		for (int i = 0; i < n; i++)
			*(dst + i) = atoi(src[i]);
	} else {
		for (int i = 0; i < n; i++)
			*(dst + i) = src[i][0];
	}
}

void
show_index(int n)
{
	printf("                ");
	for (int i = 0; i < n; i++)
		printf("%-2x ", i);
	printf("\n");
}

void
show_array(const char *prefix, int a[], int n)
{
	printf("%s", prefix);
	if (g_isint) {
		for (int i = 0; i < n; i++)
			printf("%-2d ", a[i]);
	} else {
		for (int i = 0; i < n; i++)
			printf("%-2c ", a[i]);
	}
#define NEWLINE	"" /* default is '\n' */
	printf("%s", NEWLINE);
}
