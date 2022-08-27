import operator
from typing import Generic, TypeVar, List

from oop_tree import BinaryTree

T = TypeVar("T")


class Stack(Generic[T]):
    def __init__(self) -> None:
        self._container: List[T] = []

    @property
    def empty(self) -> bool:
        return not self._container  # not is true for empty container

    def push(self, item: T) -> None:
        self._container.append(item)

    def pop(self) -> T:
        return self._container.pop()  # LIFO

    def __repr__(self) -> str:
        return repr(self._container)


def _convert_expr_to_list(math_exp: str) -> list:
    operators = ['+', '-', '*', '/', '(', ')']
    splited = []
    memory_alpha = ''
    memory_num = ''
    for symbol in math_exp:
        if memory_alpha and not symbol.isalpha():
            splited.append(memory_alpha)
            memory_alpha = ''
        if memory_num and not symbol.isdigit():
            splited.append(memory_num)
            memory_num = ''
        if symbol in operators:
            splited.append(symbol)
        elif symbol.isdigit():
            memory_num += symbol
        elif symbol.isalpha():
            memory_alpha += symbol
    return splited


def build_parse_tree(math_exp: str) -> BinaryTree:
    tokens_list = _convert_expr_to_list(math_exp)
    print(tokens_list)
    stack = Stack()
    tree: BinaryTree = BinaryTree('')
    stack.push(tree)
    current_tree = tree

    for i in tokens_list:
        if i == '(':
            current_tree.insert_left('')
            stack.push(current_tree)
            current_tree = current_tree.get_left_child()

        elif i in ['+', '-', '*', '/', 'and', 'or', 'not']:
            current_tree.set_root_val(i)
            current_tree.insert_right('')
            stack.push(current_tree)
            current_tree = current_tree.get_right_child()

        elif i == ')':
            current_tree = stack.pop()

        elif i not in ['+', '-', '*', '/', ')', 'and', 'or', 'not']:
            try:
                current_tree.set_root_val(int(i))
                parent = stack.pop()
                current_tree = parent

            except ValueError:
                raise ValueError("token '{}' is not a valid integer".format(i))

    return tree


def evaluate(parse_tree):
    operates = {'+': operator.add, '-': operator.sub, '*': operator.mul,
                '/': operator.truediv, 'and': operator.and_,
                'or': operator.or_, 'not': operator.not_}

    left_c = parse_tree.get_left_child()
    right_c = parse_tree.get_right_child()

    if left_c and right_c:
        fn = operates[parse_tree.get_root_val()]
        return fn(evaluate(left_c), evaluate(right_c))
    else:
        return parse_tree.get_root_val()


def print_exp(tree: BinaryTree) -> str:
    s_val = ""
    if tree:
        s_val = '(' + print_exp(tree.get_left_child()) if not tree.is_leaf()\
            else print_exp(tree.get_left_child())
        s_val = s_val + ' ' + str(tree.get_root_val()) if s_val \
            else s_val + str(tree.get_root_val())
        s_val = s_val + ' ' + print_exp(tree.get_right_child()) + ')' \
            if not tree.is_leaf() else s_val + print_exp(tree.get_right_child())
    return s_val


if __name__ == "__main__":
    pt: BinaryTree = build_parse_tree("((10 +5)*3)")
    print(evaluate(pt))
    # print()
    # pt.pre_order()
    # print()
    # pt.post_order()
    # print()
    # pt.in_order()
    print("__")
    print(print_exp(pt))

    pt2: BinaryTree = build_parse_tree('(3 or 2)')
    print(evaluate(pt2))
    print(print_exp(pt2))


