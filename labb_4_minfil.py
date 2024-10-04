def split_it(message):
    first_word = []  
    second_word = []  
    
    for elem in message:
        if elem.islower() or elem == "_" or elem == ".":
            first_word.append(elem)  
        elif elem.isupper() or elem == "|" or elem == " ":
            second_word.append(elem)

    result = "".join(first_word), "".join(second_word)
    return result


first_word, second_word = split_it("'lMiED)teD5E,_hLAe;Nm,0@Dli&Eg ,#4aI?rN@T§&e7#4E #<(S0A?<)NT8<0'")


print(first_word, second_word)  
  


def split_rec(message, n=0):
    first_word = []
    second_word = [] 
    if n >= len(message):
        return '', ''
    
    letter_1 = message[n]
    first_word, second_word = split_rec(message, n+1)
    
    if letter_1.islower() or letter_1 == "_" or letter_1 == "." or letter_1 == ",":
        return letter_1 + first_word, second_word
    elif letter_1.isupper() or letter_1 == "|" or letter_1 == " ":
        return first_word, letter_1 + second_word
    
    return first_word, second_word


first_part, second_part = split_rec("'lMiED)teD5E,_hLAe;Nm,0@Dli&Eg ,#4aI?rN@T§&e7#4E #<(S0A?<)NT8<0'")
print(first_part, second_part)