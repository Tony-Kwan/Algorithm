class Solution {
    private final BinaryOperator<Integer> ADD = (a, b) -> a + b;
    private final BinaryOperator<Integer> SUB = (a, b) -> a - b;
    private final BinaryOperator<Integer> MUL = (a, b) -> a * b;
    private final BinaryOperator<Integer> DIV = (a, b) -> a / b;
    private final List<String> OP = Arrays.asList("+", "-", "*", "/");
    private final List<BinaryOperator<Integer>> OP_FUNC = Arrays.asList(ADD, SUB, MUL, DIV);

    public int evalRPN(String[] tokens) {
        if (tokens == null || tokens.length == 0) {
            return 0;
        }
        Stack<Integer> s = new Stack<>();
        for (String t: tokens) {
            if (OP.contains(t)) {
                int nr = s.pop();
                int nl = s.pop();
                s.push(OP_FUNC.get(OP.indexOf(t)).apply(nl, nr));
            } else {
                s.push(Integer.parseInt(t));
            }
        }
        return s.pop();
    }
}