from calc import *


def print_res(sta, dic):
    '''takes in a list_statement prints it's value'''
    if output_expression(sta) in dic:
        var = dic.get(output_expression(sta))
        print(output_expression(sta) + ' = ' + str(var))
    else:
        val = output_expression(sta)
        print(val)
    return dic


def binary_func(li, dic):
    '''Takes in a list with a condition and executes it'''
    left = binaryexpr_left(li)
    right = binaryexpr_right(li)
    numleft = eval_expression(left, dic)
    numright = eval_expression(right, dic)
    operator = binaryexpr_operator(li)
    if operator == '+':
        return numleft + numright
    elif operator == "-":
        return numleft - numright
    elif operator == "*":
        return numleft * numright
    elif operator == "/":
        if numright == 0:
            raise ValueError("Cant be divided by 0")
        else:
            res = numleft / numright
            return res
    else:
        raise SyntaxError("Invalit binaryoperator")


def eval_expression(expression, dic):
    '''Evaluates a single expression and returns its value or variable'''
    if is_binaryexpr(expression):
        return binary_func(expression, dic)
    elif is_constant(expression):
        return int(expression)
    elif is_variable(expression):
        variable_value = dic.get(expression)
        return variable_value
    else:
        raise TypeError("expression not valid")


def condoper_func(li, dic):
    """Takes in a list with a condoper and returns if the statement is true or false"""
    left = eval_expression(li[0], dic)
    right = eval_expression(li[2], dic)
    if li[1] == "<" and left < right:
        return True
    if li[1] == ">" and left > right:
        return True
    if li[1] == "=" and left == right:
        return True



def selection_func(li, dic):
    """Executes the true or false branch of an if-statement."""
    cond = selection_condition(li)
    if condoper_func(cond, dic):  
        dic = exec_statement([selection_true_branch(li)], dic)
    elif selection_has_false_branch(li):  
        dic = exec_statement([selection_false_branch(li)], dic)
    return dic


def input_func(li, dic):
    '''Lets the user input a value to a variable'''
    var = input_variable(li)
    var_value = int(input("Enter value for " + str(input_variable(li)) + ": "))
    return set_variable(['set', var, var_value], {})


def set_variable(lst, dic):
    '''Assigns a variable to a given value'''
    dic_local = dic.copy()
    variable = assignment_variable(lst)
    value = eval_expression(assignment_expression(lst), dic)
    dic_local[variable] = value
    return dic_local


def repetition(lst, dic):
    '''returns the contitions as long as its true'''
    while condoper_func(repetition_condition(lst), dic):
        dic = exec_statement(lst, dic)
    return dic


def exec_statement(li, dic):
    '''Executes the statements one by one.'''
    if not li:  
        return dic
    for statement in li:
        if is_selection(statement):
            dic = selection_func(statement, dic)
        elif is_output(statement):
            print_res(statement, dic)
        elif is_assignment(statement):
            dic = set_variable(statement, dic)
        elif is_repetition(statement):
            dic = repetition(statement, dic)
        elif is_input(statement):
            dic = input_func(statement, dic)
    return dic


def exec_program(sta, dic=None):
    '''Executes the program if it follows the script (calc)'''
    if dic is None:
        dic = {}
    if empty_statements(sta):
        raise ValueError("empty list")
    elif is_program(sta):
        result = exec_statement(sta, dic)
    else:
        raise SyntaxError("Not a program")
    return result


calc1 = ['calc', ['print', 2], ['print', 4]]
# exec_program(calc1)
calc2 = ['calc', ['if', [3, '>', 5], ['print', 2], ['print', 4]]]
# exec_program(calc2)
calc3 = ['calc', ['if', [5, ">", [2, "+", 4]], ['print', 2], ['print', 4]]]
# exec_program(calc3)

calc4 = ['calc', ['set', 'a', 5], ['print', 'a']]
calc5 = ['calc', ['set', 'x', 7], ['set', 'y', 12], ['set', 'z', ['x', '+', 'y']], ['print', 'x'], ['print', 'y'],
         ['print', 'z']]
calc6 = ['calc', ['read', 'p1'], ['set', 'p2', 47], ['set', 'p3', 179],
         ['set', 'result', [['p1', '*', 'p2'], '-', 'p3']], ['print', 'result']]
calc7 = ['calc', ['read', 'n'], ['set', 'sum', 0],
         ['while', ['n', '>', 0], ['set', 'sum', ['sum', '+', 'n']], ['set', 'n', ['n', '-', 1]]], ['print', 'sum']]

_if_prog = [
        "calc",
        ["read", "x"],
        ["set", "zero", 0],
        ["set", "pos", 1],
        ["set", "nonpos", -1],
        ["if", ["x", "=", 0], ["print", "zero"]],
        ["if", ["x", ">", 0], ["print", "pos"]],
        ["if", ["x", "<", 0], ["print", "nonpos"]],
    ]
_if_set_prog = [
    "calc",
    ["read", "x"],
    ["if", ["x", ">", 0], ["set", "a", 1], ["set", "a", -1]],
    ["if", ["x", "=", 0], ["set", "a", 0]],
]
new_table = exec_program(_if_set_prog)
print(new_table)