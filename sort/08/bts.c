/*
 * Bucket Sort
 *
 * NOTE:
 *	Bucket sort(or bin sort), is a sorting algorithm that works by
 *	distributing the elements of an array into a number of buckets.
 *	Each bucket is then sorted individually, either using a different
 *	sorting algorithm, or by recursively applying the bucket sorting
 *	algorithm.
 *
 *	Typically, bucket sort works as follows:
 *	1. Set up an array of initially empty "buckets"
 *	2. Scatter: go over the original array, putting each object in
 *	            its bucket
 *	3. Sort each non-empty bucket
 *	4. Gather : visit the buckets in order and put all elements back
 *	            into the original array
 *
 *	Right here we just use insertion sorting algorithm to sort a single
 *	linked list.
 *
 *	In addition, we define N(=10) buckets, and use such hash algorithm in
 *	the following,
 *		a) get max number of a[] as MAX
 *		b) get width of the max number (i.e. MAX) as WIDTH
 *		   e.g. MAX = 9,   WIDTH = 1;
 *		        MAX = 99,  WIDTH = 2;
 *		        MAX = 999, WIDTH = 3;
 *		c) index = a[i] * N / (10 ** WIDTH)
 *	then we can dispatch a[i] to buckets[index]
 *
 * REFERENCES:
 *	1. http://www.cs.usfca.edu/~galles/visualization/BucketSort.html
 *	2. https://en.wikipedia.org/wiki/Bucket_sort
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "libsort.h"

/*
 * Get width of a number
 * e.g.
 *   for i in [  0 .. 9  ] // width = 1
 *   for i in [ 10 .. 99 ] // width = 2
 *   for i in [100 .. 999] // width = 3
 *   ...
 */
static int
get_width_of_num(int num)
{
	int w = 1;
	for (int q = num / 10; q != 0; q /= 10)
		w++;
	return w;
}

/*
 * Get max int of an array
 */
static int
get_max_int(int a[], size_t n)
{
	int max = a[0];

	for (int i = 0; i < n; i++) {
		if (max < a[i]) {
			max = a[i];
		}
	}

	return max;
}

static int
get_hash_base(int a[], size_t n)
{
	int max = get_max_int(a, n);

	/* get hash base which is 10**N, N=1, 2, ... */
	int base = 1;
	for (int i = 0; i < get_width_of_num(max); i++)
		base *= 10;

	return base;
}

static void
scatter(list_t **buckets, size_t m, int a[], size_t n)
{
	int base = get_hash_base(a, n);

	for (int i = 0; i < n; i++) {
		/* 1. new a node for a[i] */
		list_t *nodep = NULL;
		nodep = (list_t *)malloc(sizeof (list_t));
		if (nodep == NULL) /* error: failed to malloc */
			return;

		nodep->data = a[i];
		nodep->next = NULL;

		/* 2. dispatch the new node to bucket[j] */
		int j = a[i] * m / base;
		list_init(&(buckets[j]), nodep);
	}
}

static void
gather(list_t **buckets, size_t m, int a[], size_t n)
{
	int k = 0;
	for (int i = 0; i < m; i++) {
		if (buckets[i] == NULL)
			continue;

		for (list_t *p = buckets[i]; p != NULL; p = p->next) {
			a[k++] = p->data;

			if (k >= n) /* overflow */
				break;
		}

		list_fini(buckets[i]);
	}
}

void
bucketsort(int a[], size_t n)
{
	/* alloc buckets[] */
#define BUCKETS_NUM 10
	list_t **buckets = (list_t **)malloc(sizeof (list_t *) * BUCKETS_NUM);
	if (buckets == NULL) /* error: failed to malloc */
		return;
	for (int i = 0; i < BUCKETS_NUM; i++)
		buckets[i] = NULL;

	/* scatter elements in a[] to buckets[] */
	scatter(buckets, BUCKETS_NUM, a, n);

	/* walk buckets[] and sort */
	for (int i = 0; i < BUCKETS_NUM; i++) {
		if (buckets[i] == NULL)
			continue;
		list_sort(&buckets[i]);
#ifdef _DEBUG_LIST
		printf("DEBUG::buckets[%d]>\t", i);
		list_show(buckets[i]);
#endif
	}

	/* gather a[] by walking buckets[] */
	gather(buckets, BUCKETS_NUM, a, n);

	free(buckets);
}

int
main(int argc, char *argv[])
{
	if (argc < 2) {
		fprintf(stderr, "Usage: %s <C1> [C2] ...\n", argv[0]);
		return -1;
	}

	argc--;
	argv++;

	int n = argc;
	int *a = (int *)malloc(sizeof(int) * n);
	VALIDATE(a);

	init_gvar_isint();
	init_array(argv, a, n);

	show_index(n);
	show_array("Before sorting: ", a, n); printf("\n");
	bucketsort(a, n);
	show_array("After  sorting: ", a, n); printf("\n");

	FREE(a);
	return 0;
}
