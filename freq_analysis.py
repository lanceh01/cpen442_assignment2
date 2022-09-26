cipher_text = input("Enter original ciphertext: ")
old_char = input("Enter char we want to replace: ")
new_char = input("Enter new char we want to: ")

output_string = ''

for c in cipher_text:
    if c == old_char:
        output_string += new_char
    else: 
        output_string += c

print(f"Output is: {output_string}")
    
        