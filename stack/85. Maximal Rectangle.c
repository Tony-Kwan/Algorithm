#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define FOR(i, s, n) for (int i = s; i < n; i++)
#define MAX(a, b) (a) > (b) ? (a) : (b)

int maximalSumArray(int* arr, int n) {
    int ans = arr[0];
    int cur = 0;
    FOR(i, 0, n) {
        cur += arr[i];
        ans = MAX(ans, cur);
        cur = MAX(cur, 0);
    }
    return ans;
}

int maximalRectangle(char** matrix, int n, int m) {
    if (n <= 0 || m <= 0) {
        return 0;
    }
    int ans = 0;
    int INF = n * m;
    int sumMat[n][m];
    FOR(i, 0, n) {
        FOR(j, 0, m) {
            sumMat[i][j] = matrix[i][j] == '1' ? 1 : -INF;
        }
    }
    FOR(i, 1, n) {
        FOR(j, 0, m) {
            sumMat[i][j] += sumMat[i - 1][j];
        }
    }
    int tmp[m];
    FOR(i, 0, n) {
        ans = MAX(ans, maximalSumArray(sumMat[i], m));
        FOR(j, i + 1, n) {
            FOR(k, 0, m) {
                tmp[k] = sumMat[j][k] -  sumMat[i][k];
            }
            ans = MAX(ans, maximalSumArray(tmp, m));
        }
    }
    return ans;
}

int main() {
    {
        char* matrix[] = {"111", "111", "111"};
        printf("%d\n", maximalRectangle(matrix, 3, 3));
    }
    {
        char* matrix[] = {"10100", "10111", "11111", "10010"};
        printf("%d\n", maximalRectangle(matrix, 4, 5));
    }
    return 0;
}