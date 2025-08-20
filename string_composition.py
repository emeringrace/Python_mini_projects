def string_composition(input):
    if not isinstance(input, str):
        raise ValueError("Invalid input type. Expecting a String.")
    

    u = 0
    l = 0
    nn = 0
    no = 0
    

    for char in input:
        
        if char.isupper():
            u += 1
        elif char.islower():
            l += 1
        elif char.isdigit():
            nn += 1
        else:
            no += 1
    return [u, l, nn, no]
