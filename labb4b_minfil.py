def interpret(expression, dict):
    '''interpretes expression if it atches dict'''
    
    if isinstance(expression, str): 
        if expression == "true":
            return "true"
        elif expression == "false":
            return "false"
        else:
            return dict.get(expression, "false") 
    
    if isinstance(expression, list) and len(expression) == 2 and expression[0] == "NOT":
        value_to_change = interpret(expression[1], dict)
        if value_to_change == "true":
            return "false"
        else: 
            return "true"
        
    if isinstance(expression, list) and len(expression) == 3 and expression[1] == "AND":
        left_result = interpret(expression[0], dict)
        right_result = interpret(expression[2],dict)
        if left_result == "true" and right_result == "true":
           return "true"
        else:
           return "false"
    
    if isinstance(expression, list) and len(expression) == 3 and expression[1] == "OR":
        left_result = interpret(expression[0], dict)
        right_result = interpret(expression[2], dict)
        if left_result == "true" or right_result == "true":
           return "true"
        else:
           return "false"
