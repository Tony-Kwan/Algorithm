#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <assert.h>

#define INF (-(1 << 30))

typedef int T;
typedef T(*OP)(T, T);

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

  assert(st->leftChild && st->rightChild);

  if (rightBound <= st->leftChild->rightBound) {
      return query(st->leftChild, leftBound, st->leftChild->rightBound);
  } else if (leftBound >= st->rightChild->leftBound) {
      return query(st->rightChild, st->rightChild->leftBound, rightBound);
  } else {
      T leftValue = query(st->leftChild, leftBound, st->leftChild->rightBound);
      T rightValue = query(st->rightChild, st->rightChild->leftBound, rightBound);
      return st->operation(leftValue, rightValue);
  }
}

void replace(SegmentTree *st, int index, T value) {
   if (st->leftBound == st->rightBound) {
       st -> value = value;
       return;
   }

   assert(st->leftChild && st->rightChild);

   if (index <= st->leftChild->rightBound) {
       replace(st->leftChild, index, value);
   } else if (index >= st->rightChild->leftBound) {
       replace(st->rightChild, index, value);
   }
   st->value = st->operation(st->leftChild->value, st->rightChild->value);
}

int main(int argc, char* argv[]) {
    T a[5] = {5, 4, 3, 2, 1};
//    SegmentTree *st = build(a, 0, 4, max);
//    SegmentTree *st = build(a, 0, 4, min);
    SegmentTree *st = build(a, 0, 4, sum);
    printf("%d\n", query(st, 1, 4));
    
    replace(st, 4, 10);
    printf("%d\n", query(st, 1, 4));
    printf("%d\n", query(st, 0, 3));
    return 0;
}
