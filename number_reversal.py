def reverse(number):
    s = " "
    if type(number) == float:
        raise  ValueError
    else :
        if number < 0 :
            number  = abs(number)
            number = str(number)
        
            for i in range(len(number)) :
                if number[i+1] == '0' and number[len(number) - i - 1] == '0':
                    return -1
                else:
                    for i in range(len(number)):
                        s += number[len(number) - 1 - i]
                    s = int(s)
                    s= -s
                    return s
        else :
            number = str(number)
        
            for i in range(len(number)) :
                if number[i+1] == '0' and number[len(number) - i - 1] == '0':
                    return 1
                else:
                    for i in range(len(number)):
                        s += number[len(number) - 1 - i]
                    s = int(s)
                    
                    return s
