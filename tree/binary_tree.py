
class Expression:
    pass


class Multiplication(Expression):

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return '(' + str(self.left) + '*' + str(self.right) + ')'

    def eval(self, variables):
        return self.left.eval(variables) * self.right.eval(variables)


class Degree(Expression):

    def __init__(self, number, degree):
        self.number = number
        self.degree = degree

    def __str__(self):
        return str(self.number) + '^' + str(self.degree)

    def eval(self, variables):
        return self.number.eval(variables) ** self.degree.eval(variables)


class Plus(Expression):

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return '(' + str(self.left) + '+' + str(self.right) + ')'

    def eval(self, variables):
        return self.left.eval(variables) + self.right.eval(variables)


class Minus(Expression):

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return '(' + str(self.left) + '-' + str(self.right) + ')'

    def eval(self, variables):
        return self.left.eval(variables) - self.right.eval(variables)


class Division(Expression):

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return '(' + str(self.left) + '/' + str(self.right) + ')'

    def eval(self, variables):
        return self.left.eval(variables) / self.right.eval(variables)


class Constant(Expression):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

    def eval(self, variables):
        return self.value


class Variable(Expression):

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return str(self.name)

    def eval(self, variables):
        return variables[self.name]


def main():
    variables = {
        'x': 2,
        'y': 4
    }

    expression_1 = Multiplication(Constant(3), Plus(Variable('y'), Variable('x')))

    expression_2 = Plus(Variable('x'), Multiplication(Constant(3), Variable('y')))

    numerator3 = Multiplication(Constant(5), Multiplication(
        Plus(Variable('x'), Constant(1)),
        Minus(Variable('y'), Constant(1))
    ))
    denominator3 = Minus(Variable('x'), Constant(1))
    expression_3 = Division(numerator3, denominator3)

    rezult1 = expression_1.eval(variables)
    rezult2 = expression_2.eval(variables)
    rezult3 = expression_3.eval(variables)

    print(expression_1, '=', rezult1)
    print(expression_2, '=', rezult2)
    print(expression_3, '=', rezult3)

    numerator4 = Plus(Variable('x'), Multiplication(Constant(5),
        Degree(Variable('x'), Constant(3))
    ))
    denominator4 = Minus(Degree(Variable('y'), Constant(2)), Constant(5))
    expression_4 = Division(numerator4, denominator4)

    rezult_4 = expression_4.eval(variables)
    print(expression_4, '=', rezult_4)

if __name__ == '__main__':
    main()