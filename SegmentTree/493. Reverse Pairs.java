class Solution {
    private int ans = 0;

    private void mergeSort(int l, int r, int[] nums) {
        if (l == r) {
            return;
        }
        int m = (l + r) >> 1;
        mergeSort(l, m, nums);
        mergeSort(m + 1, r, nums);
        merge(l, m, r, nums);
    }

    private static int binarySearch(int[] arr, int l, int r, int key) {
        if (arr[l] >= key) {
            return 0;
        }
        if (arr[r] < key) {
            return r - l + 1;
        }
        int L = l, R = r;
        while (L < R) {
            int m = (L + R) >> 1;
            if (key == arr[m]) {
                R = m;
            } else if (key < arr[m]) {
                R = m;
            } else {  // arr[m] < key
                L = m + 1;
            }
        }
        return L - l;
    }

    private void merge(int l, int m, int r, int[] nums) {
        int[] tmp = new int[r - l + 1];
        int L = l, R = m + 1;

        for (int i = L; i < R; i++) {
            ans += binarySearch(nums, R, r, (nums[i] + 1) >> 1);
        }

        int i = 0;
        while (L <= m && R <= r) {
            int v1 = nums[L];
            int v2 = nums[R];
            if (v1 < v2) {
                tmp[i++] = v1;
                L++;
            } else {
                tmp[i++] = v2;
                R++;
            }
        }
        while (L <= m) {
            tmp[i++] = nums[L++];
        }
        while (R <= r) {
            tmp[i++] = nums[R++];
        }
        System.arraycopy(tmp, 0, nums, l, tmp.length);
    }

    public int reversePairs(int[] nums) {
        if (nums.length != 0) {
            mergeSort(0, nums.length - 1, nums);
        }
        return ans;
    }
}
