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
typedef struct {
    T value;
    int leftBound, rightBound;
    struct SegmentTree *leftChild, *rightChild;
    OP operation;
} SegmentTree; 

SegmentTree* build(T array[], int leftBound, int rightBound, OP operation) {
    SegmentTree *st = (SegmentTree*)malloc(sizeof(SegmentTree));
    st -> value = INF;
    st -> leftBound = leftBound;
    st -> rightBound = rightBound;
    st -> operation = operation;
    st -> leftChild = st -> rightChild = NULL;

    if (leftBound == rightBound) {
        st.value = array[leftBound];
        return st;
    } else {
        int mid = leftBound + (rightBound - leftBound) / 2;
    }

    return st;
}

int query(int startIdx, int endIdx, OP op) {
    return op(1<<11, 1<<20);
}

int main() {
    T a[5] = {1, 2, 3, 4, 5};
    SegmentTree *st = build(a, 0, 4 ,min);
    printf("%p\n", st);
    return 0;
}
