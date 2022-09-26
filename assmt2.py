ciphertext = "YHZOZJBDACYHQAFDCWZONOZMBOPBRLZQAYHBYACOUQUBLQGZYHQAPQYDCWZONMIGHCIYCVYHZJBNYCHZBOYHZOBRRQYDBNYCQYDZLVGCMMBCHUZBOCHUZBOQDHBLLRZLBYZJHZADHZYHCIFHYQYCWZOBVYZOJBOUDGCMMBQYCGGIOOZUYCHZOYHBYDHZCIFHYYCHBWZJCAUZOZUBYYHQDGCMMBRIYBYYHZYQMZQYBLLDZZMZUEIQYZABYIOBLRIYJHZAYHZOBRRQYBGYIBLLNYCCPBJBYGHCIYCVQYDJBQDYGCBYXCGPZYGCMMBBAULCCPZUBYQYGCMMBBAUYHZAHIOOQZUCAGCMMBBLQGZDYBOYZUYCHZOVZZYGCMMBVCOQYVLBDHZUBGOCDDHZOMQAUYHBYDHZHBUAZWZORZVCOZDZZABOBRRQYJQYHZQYHZOBJBQDYGCBYXCGPZYGCMMBCOBJBYGHYCYBPZCIYCVQYGCMMBBAURIOAQAFJQYHGIOQCDQYNGCMMBDHZOBABGOCDDYHZVQZLUBVYZOQYGCMMBBAUVCOYIABYZLNJBDSIDYQAYQMZYCDZZQYXCXUCJABLBOFZOBRRQYHCLZIAUZOYHZHZUFZ"

ciphertext = ciphertext.replace("GCMMB", ", ")
ciphertext = ciphertext.replace("Y", "t")
ciphertext = ciphertext.replace("H", "h")
ciphertext = ciphertext.replace("Z", "e")
ciphertext = ciphertext.replace("C", "o")
ciphertext = ciphertext.replace("B", "a")
ciphertext = ciphertext.replace("M", "m")
ciphertext = ciphertext.replace("G", "c")


print(ciphertext)

dictionary = dict()

for i, c in enumerate(ciphertext):
  if ciphertext[i:i+6] in list(dictionary.keys()):
    s = ciphertext[i:i+6]
    dictionary[s] = dictionary.get(s) + 1
  else:
    s = ciphertext[i:i+6]
    dictionary[s] = 1

print(dict(sorted(dictionary.items(), key=lambda item: item[1])))
