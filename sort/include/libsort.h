#ifndef _LIBSORT_H
#define _LIBSORT_H

#ifdef	__cplusplus
extern "C" {
#endif

#define VALIDATE(p) do { if (p == NULL) return -1; } while (0)
#define FREE(p)     do { free(p); p = NULL; } while (0)

typedef enum bool_s {
	false,
	true
} bool_t;

typedef struct list_s {
	int data;
	struct list_s *next;
} list_t;

extern int g_isint;

extern void exchange(int a[], int i, int j);
extern void init_gvar_isint();
extern void init_array(char *src[], int *dst, int n);
extern void show_index(int n);
extern void show_array(const char *prefix, int a[], int n);
extern void list_init(list_t **head, list_t *node);
extern void list_fini(list_t *head);
extern void list_show(list_t *head);
extern void list_insert(list_t **head, list_t *node);
extern void list_sort(list_t **head);

#ifdef __cplusplus
}
#endif

#endif /* _LIBSORT_H */
