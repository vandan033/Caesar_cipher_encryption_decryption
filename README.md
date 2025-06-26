# Caesar_cipher_encryption_decryption
python project

This Python script implements a Caesar Cipher, a classic encryption technique that shifts each letter in the message by a specified number of positions in the alphabet.

🔐 How It Works
The script converts all letters in the input message to uppercase.
Each alphabetical character is shifted by the Shift Key value provided by the user.
The alphabet wraps around if the shift goes past 'Z' or before 'A'.
Non-alphabetic characters (e.g., punctuation, spaces, digits) remain unchanged.
📄 Code Features
Alphabet range constants: Defines ASCII range for capital letters (A-Z).
caesar_cipher(message, shift): Core function that performs encryption.
User Input: Prompts the user to enter a message and a shift key.
🛠 Notes Only uppercase letters are processed for encryption.

The cipher is symmetrical, meaning you can decrypt by using the negative of the original shift value.

💻 Usage
Run the Script
python caesar_cipher.py
Decryption To decrypt a message, simply use the negative of the shift key used during encryption.

Example ------> caesar_cipher("KHOOR, ZRUOG!", -3) # Output: HELLO, WORLD!
