import math
def encrypt(plaintext, key):
    if len(key)==0:
        raise ValueError("Key cannot be empty.")
    length=len(plaintext)
    if len(key)!=length:
        d=(length-len(key))/len(key)
        key=key+(key*(math.ceil(d)))
        key=key[0:length]
    new_text=""
    for j in range(0,length):
        key_index=ord(key[j])-ord("a")
        current_index=ord(plaintext[j]) - ord('a')
        new_index = (current_index + key_index) % 26
        new_text=new_text+ chr(new_index + ord('a'))
        
    return new_text

def decrypt(ciphertext, key):
    if len(key)==0:
        raise ValueError("Key cannot be empty.")
    length=len(ciphertext)
    if len(key)!=length:
        d=(length-len(key))/len(key)
        key=key+(key*(math.ceil(d)))
        key=key[0:length]
    new_text=""
    for j in range(0,length):
        key_index=ord(key[j])-ord("a")
        current_index=ord(ciphertext[j]) - ord('a')
        new_index = (current_index - key_index) % 26
        new_text=new_text+ chr(new_index + ord('a'))
        
    return new_text
