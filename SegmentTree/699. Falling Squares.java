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

    private static final int N = 101000000;

    private Node root;

    public Solution() {
        this.root = new Node(0, N);
    }

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
            node.left.lazy = node.right.lazy = node.lazy;
            node.left.value = node.right.value = node.value;
            node.lazy = 0;
        }
    }

    private void update(Node node, int l, int r, int value) {
        if (l <= node.leftBound && node.rightBound <= r) {
            node.lazy = value;
            node.value = value;
            return;
        }
        pushDown(node);
        if (l <= node.midIndex) {
            update(node.left, l, r, value);
        }
        if (r > node.midIndex) {
            update(node.right, l, r, value);
        }
        pushUp(node);
    }

    private int query(Node node, int l, int r) {
        if (l <= node.leftBound && node.rightBound <= r) {
            return node.value;
        }
        pushDown(node);
        int ret = 0;
        if (l <= node.midIndex) {
            ret = query(node.left, l, r);
        }
        if (r > node.midIndex) {
            ret = Math.max(ret, query(node.right, l, r));
        }
        return ret;
    }

    public List<Integer> fallingSquares(int[][] positions) {
        List<Integer> ret = new ArrayList<>(positions.length);
        for (int[] position : positions) {
            int l = position[0];
            int r = position[0] + position[1] - 1;
            int max = query(this.root, l, r) + position[1];
            update(this.root, l, r, max);
            ret.add(this.root.value);
        }
        return ret;
    }
}
