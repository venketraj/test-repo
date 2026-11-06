import ast
import operator


_BINARY_OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.FloorDiv: operator.floordiv,
    ast.Mod: operator.mod,
    ast.Pow: operator.pow,
}
_UNARY_OPERATORS = {
    ast.UAdd: operator.pos,
    ast.USub: operator.neg,
}


def calculate(expression: str) -> int | float:
    """Evaluate a basic arithmetic expression without executing arbitrary code."""
    try:
        tree = ast.parse(expression, mode="eval")
    except SyntaxError as error:
        raise ValueError("Enter a valid arithmetic expression.") from error

    def evaluate(node: ast.AST) -> int | float:
        if isinstance(node, ast.Constant) and type(node.value) in (int, float):
            return node.value
        if isinstance(node, ast.BinOp) and type(node.op) in _BINARY_OPERATORS:
            left = evaluate(node.left)
            right = evaluate(node.right)
            if isinstance(node.op, ast.Pow) and abs(right) > 1000:
                raise ValueError("Exponent must be between -1000 and 1000.")
            return _BINARY_OPERATORS[type(node.op)](left, right)
        if isinstance(node, ast.UnaryOp) and type(node.op) in _UNARY_OPERATORS:
            return _UNARY_OPERATORS[type(node.op)](evaluate(node.operand))
        raise ValueError("Use numbers, parentheses, and arithmetic operators only.")

    return evaluate(tree.body)


def main():
    print("Calculator: enter an expression, or 'q' to quit.")
    while True:
        expression = input("> ").strip()
        if expression.lower() in {"q", "quit", "exit"}:
            print("Goodbye!")
            break
        if not expression:
            continue
        try:
            print(calculate(expression))
        except (ValueError, ArithmeticError, OverflowError) as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()
    print("Calculator: enter an expression, or 'q' to quit.")
