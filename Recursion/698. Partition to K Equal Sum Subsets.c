#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

/**
    暴力+剪枝
 */

bool find(int* nums, int* vis, int size, int target, int now, int k, int deep, int s) {
    //printf("t=%d now=%d k=%d deep=%d\n", target, now, k, deep);
    if (deep == size) {
        if (k == 0 && now == 0 && deep == size) {
            return true;
        }
        return false;
    }
    int sum;
    int I = size;
    if (now == 0) {
        for (int i = 0; i < size; i++) {
            if (vis[i] == 0) {
                I = i + 1;
                break;
            }
        }
    }
    for (int i = s; i < I; i++) {
        if (vis[i] == 1) {
            continue;
        }
        sum = now + nums[i];
        if (sum > target) {
            return false;
        } else if (sum == target) {
            vis[i] = 1;
            if (find(nums, vis, size, target, 0, k - 1, deep + 1, 0)) {
                return true;
            }
            vis[i] = 0;
        } else { //sum < target
            vis[i] = 1;
            if (find(nums, vis, size, target, sum, k, deep + 1, i + 1)) {
                return true;
            }
            vis[i] = 0;
        }
    }
    return false;
}

bool canPartitionKSubsets(int* nums, int size, int k) {
    int sum = 0;
    int max = 0;
    for (int i = 0; i < size; i++) {
        sum += nums[i];
        max = nums[i] > max ? nums[i] : max;
    } 
    if (sum % k != 0) {
        return false;
    }
    int target = sum / k;
    if (max > target) {
        return false;
    }
    for (int i = 0; i < size - 1; i++) {
        for (int j = i + 1; j < size; j++) {
            if (nums[j] < nums[i]) {
                int t = nums[j];
                nums[j] = nums[i];
                nums[i] = t;
            }
        }
    }
    int vis[16] = {0};
    return find(nums, vis, size, target, 0, k, 0, 0);
}

int main() {
    {
        int nums[] = {1,2,2,3,3,4,5};
        printf("%d\n", canPartitionKSubsets(nums, sizeof(nums) / sizeof(int), 4));
    }

    {
        int nums[] = {129,17,74,57,1421,99,92,285,1276,218,1588,215,369,117,153,22};
        printf("%d\n", canPartitionKSubsets(nums, sizeof(nums) / sizeof(int), 3));
    }
    return 0;
}
