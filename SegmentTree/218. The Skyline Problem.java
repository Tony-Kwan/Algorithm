class Solution {
    static class Node {
        Node left, right;
        int leftBound, rightBound, midIndex;
        int value;
        int lazy;

        public Node(int leftBound, int rightBound) {
            this.leftBound = leftBound;
            this.rightBound = rightBound;
            this.midIndex = (leftBound + rightBound) >> 1;
            this.value = this.lazy = 0;
            this.left = this.right = null;
        }
    }

    private Node root = null;
    private Map<Integer, Integer> map = new HashMap<>();

    private void pushUp(Node node) {
        node.value = Math.max(node.left.value, node.right.value);
    }

    private void pushDown(Node node) {
        if (node.left == null) {
            node.left = new Node(node.leftBound, node.midIndex);
        }
        if (node.right == null) {
            node.right = new Node(node.midIndex + 1, node.rightBound);
        }
        if (node.lazy != 0) {
            node.left.lazy = Math.max(node.left.lazy, node.lazy);
            node.right.lazy = Math.max(node.right.lazy, node.lazy);
            node.left.value = Math.max(node.left.value, node.lazy);
            node.right.value = Math.max(node.right.value, node.lazy);
            node.lazy = 0;
        }
    }

    private void update(Node node, int l, int r, int h) {
        if (l <= node.leftBound && node.rightBound <= r) {
            node.lazy = Math.max(node.lazy, h);
            node.value = Math.max(node.value, h);
            return;
        }
        pushDown(node);
        if (l <= node.midIndex) {
            update(node.left, l, r, h);
        }
        if (r > node.midIndex) {
            update(node.right, l, r, h);
        }
        pushUp(node);
    }

    private void travel(Node node, int[] arr) {
        if (node.leftBound == node.rightBound) {
            arr[node.leftBound] = node.value;
            return;
        }
        pushDown(node);
        travel(node.left, arr);
        travel(node.right, arr);
    }

    public List<int[]> getSkyline(int[][] buildings) {
        if (buildings.length == 0) {
            return Collections.emptyList();
        }
        Set<Integer> set = new HashSet<>();
        for (int[] building : buildings) {
            set.add(building[0]);
            set.add(building[1]);
        }
        List<Integer> list = new ArrayList<>(set);
        Collections.sort(list);
        for (int i = 0; i < list.size(); i++) {
            map.put(list.get(i), i);
        }

        this.root = new Node(0, list.size() - 1);
        for (int[] building : buildings) {
            int l = map.get(building[0]);
            int r = map.get(building[1]) - 1;
            update(this.root, l, r, building[2]);
        }

        int[] arr = new int[list.size()];
        travel(this.root, arr);
        int pre = -1;
        List<int[]> ret = new ArrayList<>();
        for (int i = 0; i < arr.length; i++) {
            int h = arr[i];
            if (h != pre) {
                pre = h;
                ret.add(new int[] {list.get(i), h});
            }
        }
        return ret;
    }
}
