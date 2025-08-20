def substitute(letter, n):

    if len(letter) != 1 or not letter.isalpha():
        raise ValueError
    
    letter = letter.lower()
    
    current_position = ord(letter) - ord('a')  
    new_position = (current_position + n) % 26 
    new_letter = chr(ord('a') + new_position)  
    
    return new_letter
