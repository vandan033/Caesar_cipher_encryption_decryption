FIRST_LETTER = ord('A') 
LAST_LETTER = ord('Z') 
CHAR_RANGE = LAST_LETTER - FIRST_LETTER+1 # 26 letters in the alphabet


def caesar_cipher(message, shift):
    result = "" 

    for char in message.upper():

        if char.isalpha():
            # To convert the letter to its ASCII code
            char_code = ord(char)
            # Shift the letter by the specified amount\
            new_char_code = char_code + shift

            if new_char_code > LAST_LETTER:
                new_char_code -= CHAR_RANGE
            
            # If the new character code is less than 'A', wrap around
            if new_char_code < FIRST_LETTER:
                new_char_code += CHAR_RANGE

            new_char= chr(new_char_code)

            result += new_char
        else:
            # If the character is not a letter, just add it to the result
            result += char
    print(result)


usr_message = input("Enter message to be encrypted: ")
usr_shift_key = int(input("Enter Shift Key value: "))

caesar_cipher(usr_message, usr_shift_key)