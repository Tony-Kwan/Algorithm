class MyCalendarThree {

    static class Node {
        Node left = null;
        Node right = null;
        int leftBound;
        int midIndex;
        int rightBound;
        int value = 0;
        int lazy = 0;

        public Node(int leftBound, int rightBound) {
            this.leftBound = leftBound;
            this.rightBound = rightBound;
            this.midIndex = (leftBound + rightBound) >> 1;
        }
    }

    private static final int N = 1000000000;
    private Node root;

    public MyCalendarThree() {
        this.root = new Node(0, N);
    }

    public int book(int start, int end) {
        update(this.root, start, end - 1);
        return this.root.value;
    }

    private void pushUp(Node node) {
        int max = 0;
        if (node.left != null) {
            max = Math.max(max, node.left.value);
        }
        if (node.right != null) {
            max = Math.max(max, node.right.value);
        }
        node.value = max;
    }

    private void pushDown(Node node) {
        if (node.left == null) {
            node.left = new Node(node.leftBound, node.midIndex);
        }
        if (node.right == null) {
            node.right = new Node(node.midIndex + 1, node.rightBound);
        }
        if (node.lazy != 0) {
            node.left.lazy += node.lazy;
            node.right.lazy += node.lazy;
            node.left.value += node.lazy;
            node.right.value += node.lazy;
            node.lazy = 0;
        }
    }

    private void update(Node node, int l, int r) {
        if (l <= node.leftBound && node.rightBound <= r) {
            node.lazy++;
            node.value++;
            return;
        }
        pushDown(node);
        if (l <= node.midIndex) {
            update(node.left, l, r);
        }
        if (r > node.midIndex) {
            update(node.right, l, r);
        }
        pushUp(node);
    }
}
