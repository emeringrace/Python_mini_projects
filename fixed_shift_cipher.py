def f_substitute(letter):

    if len(letter) != 1 or not letter.isalpha():
        raise ValueError("Input must be a single letter from the English alphabet.")
    

    letter = letter.lower()
    

    new_position = (ord(letter) - ord('a') + 5) % 26
    new_letter = chr(ord('a') + new_position)
    
    return new_letter
