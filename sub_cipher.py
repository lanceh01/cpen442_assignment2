cipher_text = input("Enter ciphertext: ")

char_dict = {}

for c in cipher_text:
    if c in char_dict:
        char_dict[c] += 1
    else:
        char_dict[c] = 1


# https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
sorted_dict = {k: v for k, v in sorted(char_dict.items(), key=lambda item: item[1])}


print(sorted_dict)
