#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define INF (-(1 << 30))

typedef int (*OP)(int, int);
typedef int T;

//sample operation
T min(T x, T y) {
    return x < y ? x : y;
}

// --------  Segment Tree  --------
typedef struct SegmentTree {
    T value;
    int leftBound, rightBound;
    struct SegmentTree *leftChild, *rightChild;
    OP operation;
} SegmentTree; 

SegmentTree* build(T array[], int leftBound, int rightBound, OP operation) {
    SegmentTree *st = (SegmentTree*)malloc(sizeof(SegmentTree));
    st->value = INF;
    st->leftBound = leftBound;
    st->rightBound = rightBound;
    st->operation = operation;
    st->leftChild = st -> rightChild = NULL;

    if (leftBound == rightBound) {
        st->value = array[leftBound];
    } else {
        int mid = leftBound + (rightBound - leftBound) / 2;
        st->leftChild = build(array, leftBound, mid, operation);
        st->rightChild = build(array, mid + 1, rightBound, operation);
        st->value = operation(st->leftChild->value, st->rightChild->value);
    }

    return st;
}

int query(int startIdx, int endIdx, OP op) {
    return op(1<<11, 1<<20);
}

int main() {
    T a[5] = {11, 12, 13, 14, 15};
    SegmentTree *st = build(a, 0, 4 ,min);
    printf("%d\n", st->value);
    return 0;
}
