// 有点不一样的线段树(line:78)

class RangeModule {

    static class Node {
        Node left;
        Node right;
        int leftBound;
        int midIndex;
        int rightBound;
        int value;
        int lazy;

        public Node(int leftBound, int rightBound) {
            this.left = this.right = null;
            this.leftBound = leftBound;
            this.rightBound = rightBound;
            this.midIndex = (leftBound + rightBound) >> 1;
            this.value = 0;
            this.lazy = -1;
        }
    }

    private static final int N = 1000000000;

    private Node root;

    public RangeModule() {
        this.root = new Node(0, N);
    }

    private void pushUp(Node node) {
        node.value = (node.left.value == node.right.value) ? node.left.value : -1;
    }

    private void pushDown(Node node) {
        if  (node.left == null) {
            node.left = new Node(node.leftBound, node.midIndex);
            node.left.value = node.value;
        }
        if (node.right == null) {
            node.right = new Node(node.midIndex + 1, node.rightBound);
            node.left.value = node.value;
        }
        if (node.lazy != -1) {
            node.left.lazy = node.right.lazy = node.lazy;
            node.left.value = node.right.value = node.lazy;
            node.lazy = -1;
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

    public void addRange(int left, int right) {
        update(this.root, left, right - 1, 1);
    }

    public void removeRange(int left, int right) {
        update(this.root, left, right - 1, 0);
    }

    private int query(Node node, int l, int r) {
        // 不一样的地方
        if (node.leftBound <= l && r <= node.rightBound && node.value != -1) {
            return node.value;
        }
        if (l == node.leftBound && node.rightBound == r) {
            return node.value;
        }
        pushDown(node);
        if (r <= node.midIndex) {
            return query(node.left, l, r);
        } else if (l > node.midIndex) {
            return query(node.right, l, r);
        } else {
            int q1 = query(node.left, l, node.midIndex);
            int q2 = query(node.right, node.midIndex + 1, r);
            return q1 == q2 ? q1 : -1;
        }
    }

    public boolean queryRange(int left, int right) {
        return query(this.root, left, right - 1) == 1;
    }
}
