class Solution {
    static class Elem {
        int index;
        int value;
        int count;

        public Elem(int index, int value, int count) {
            this.index = index;
            this.value = value;
            this.count = count;
        }

        @Override
        public String toString() {
            return String.format("(%d, %d)", this.value, this.count);
        }
    }

    public List<Integer> countSmaller(int[] nums) {
        if (nums.length == 0) {
            return Collections.emptyList();
        }
        Elem[] arr = new Elem[nums.length];
        for (int i = 0; i < nums.length; i++) {
            arr[i] = new Elem(i, nums[i], 0);
        }
        mergeSort(0, nums.length - 1, arr);

        Arrays.sort(arr, (e1, e2) -> e1.index - e2.index);
        List<Integer> ret = new ArrayList<>(nums.length);
        for (Elem elem : arr) {
            ret.add(elem.count);
        }
        return ret;
    }

    private void mergeSort(int l, int r, Elem[] arr) {
        if (l == r) {
            return;
        }
        int m = (l + r) >> 1;
        mergeSort(l, m, arr);
        mergeSort(m + 1, r, arr);

        int idxL = l, idxR = m + 1;
        Elem[] tmp = new Elem[r - l + 1];
        int i = 0;
        while (idxL <= m && idxR <= r) {
            Elem e1 = arr[idxL];
            Elem e2 = arr[idxR];
            if (e1.value <= e2.value) {
                tmp[i++] = e1;
                e1.count += idxR - (m + 1);
                idxL++;
            } else {
                tmp[i++] = e2;
                idxR++;
            }
        }
        while (idxL <= m) {
            arr[idxL].count += r - m;
            tmp[i++] = arr[idxL++];
        }
        while (idxR <= r) {
            tmp[i++] = arr[idxR++];
        }
        System.arraycopy(tmp, 0, arr, l, i);
    }
}
