#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define INF (-(1 << 30))

typedef int (*OP)(int, int);
typedef int T;

//sample operation
T max(T x, T y) {
    return x > y ? x : y;
}

T min(T x, T y) {
    return x < y ? x : y;
}

T sum(T x, T y) {
    return x + y;
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

int query(SegmentTree *st, int leftBound, int rightBound) { 
  if (st->leftBound == leftBound && st->rightBound == rightBound) {
      return st->value;
  }

  int mid = leftBound + (rightBound - leftBound) / 2;
  if (rightBound <= mid) {
      return query(st->leftChild, leftBound, mid);
  } else if (leftBound >= mid + 1) {
      return query(st->rightChild, mid + 1, rightBound);
  } else {
      T leftValue = query(st->leftChild, leftBound, mid);
      T rightValue = query(st->rightChild, mid + 1, rightBound);
      return st->operation(leftValue, rightValue);
  }
}

void replace() {
}

int main() {
    T a[5] = {5, 4, 3, 2, 1};
    SegmentTree *st = build(a, 0, 4, sum);
    printf("%d\n", query(st, 0, 4));
    return 0;
}
