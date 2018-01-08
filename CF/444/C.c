#include<stdio.h>
#include<stdlib.h>

typedef long long LL;

const int MAXN = 100000;

int n, m;
int col[MAXN << 2] = {0};
LL sum[MAXN << 2] = {0};
LL lazy[MAXN << 2] = {0};
    
void pushUp(int rt) {
    col[rt] = col[rt << 1] == col[rt << 1 | 1] ? col[rt << 1] : 0;
    sum[rt] = sum[rt << 1] + sum[rt << 1 | 1];
}

void pushDown(int L, int R, int rt) {
    if (lazy[rt] != 0) {
        lazy[rt << 1] += lazy[rt];
        lazy[rt << 1 | 1] += lazy[rt];
        col[rt << 1] = col[rt << 1 | 1] = col[rt];
        int m = (L + R) >> 1;
        sum[rt << 1] += lazy[rt] * (m - L + 1);
        sum[rt << 1 | 1] += lazy[rt] * (R - m);
        lazy[rt] = 0;
    }
}

void build(int l, int r, int rt) {
    if (l == r) {
        col[rt] = l;
        return;
    }
    int m = (l + r) >> 1;
    build(l, m, rt << 1);
    build(m + 1, r, rt << 1 | 1);
    pushUp(rt);
}

void update(int L, int R, int rt, int l, int r, int color) {
    if (l <= L && R <= r) {
        if (col[rt] == color) {
            return;
        }
        if (col[rt] != 0) {
            LL diff = abs(col[rt] - color);
            lazy[rt] += diff;
            sum[rt] += diff * (R - L + 1);
            col[rt] = color;
            return;
        }
    }
    pushDown(L, R, rt);
    int m = (L + R) >> 1;
    if (r <= m) {
        update(L, m, rt << 1, l, r, color);
    } else if (l > m) {
        update(m + 1, R, rt << 1 | 1, l, r, color);
    } else {
        update(L, m, rt << 1, l, m, color);
        update(m + 1, R, rt << 1 | 1, m + 1, r, color);
    }
    pushUp(rt);
}

LL query(int L, int R, int rt, int l, int r) {
    if (L == l && R == r) {
        return sum[rt];
    }
    pushDown(L, R, rt);
    int m = (L + R) >> 1;
    if (r <= m) {
        return query(L, m, rt << 1,  l, r);
    } else if (l > m) {
        return query(m + 1, R, rt << 1 | 1, l, r);
    }
    return query(L, m, rt << 1, l, m) + query(m + 1, R, rt << 1 | 1, m + 1, r);
}

int main() {
    scanf("%d%d", &n, &m);
    build(1, n, 1);

    int t, l, r, c;
    while(m--) {
        scanf("%d", &t);
        if (t == 1) {
            scanf("%d%d%d", &l, &r, &c); 
            update(1, n, 1, l, r, c);
        } else {
            scanf("%d%d", &l, &r);
            printf("%I64d\n", query(1, n, 1, l, r));
        }
    }
}
