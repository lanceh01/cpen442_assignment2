cipher_text = 'YHZOZJBDACYHQAFDCWZONOZMBOPBRLZQAYHBYACOUQUBLQGZYHQAPQYDCWZONMIGHCIYCVYHZJBNYCHZBOYHZOBRRQYDBNYCQYDZLVGCMMBCHUZBOCHUZBOQDHBLLRZLBYZJHZADHZYHCIFHYQYCWZOBVYZOJBOUDGCMMBQYCGGIOOZUYCHZOYHBYDHZCIFHYYCHBWZJCAUZOZUBYYHQDGCMMBRIYBYYHZYQMZQYBLLDZZMZUEIQYZABYIOBLRIYJHZAYHZOBRRQYBGYIBLLNYCCPBJBYGHCIYCVQYDJBQDYGCBYXCGPZYGCMMBBAULCCPZUBYQYGCMMBBAUYHZAHIOOQZUCAGCMMBBLQGZDYBOYZUYCHZOVZZYGCMMBVCOQYVLBDHZUBGOCDDHZOMQAUYHBYDHZHBUAZWZORZVCOZDZZABOBRRQYJQYHZQYHZOBJBQDYGCBYXCGPZYGCMMBCOBJBYGHYCYBPZCIYCVQYGCMMBBAURIOAQAFJQYHGIOQCDQYNGCMMBDHZOBABGOCDDYHZVQZLUBVYZOQYGCMMBBAUVCOYIABYZLNJBDSIDYQAYQMZYCDZZQYXCXUCJABLBOFZOBRRQYHCLZIAUZOYHZHZUFZ'
our_key = {
    'Y': 't',
    'Z': 'e',
    'B': 'a',
    'C': 'o',
    'H': 'h',
    'O': 'r',
    'Q': 'i',
    'M': 'm',
    'D': 's',
    'G': 'c',
    'A': 'n',
    'U': 'd',
    'I': 'u',
    'L': 'l',
    'R': 'b',
    'J': 'w',
    'V': 'f',
    'P': 'k',
    'N': 'y',
    'F': 'g',
    'W': 'v',
    'X': 'p',
    'S': 'j',
    'E': 'q',
}

output_string = ''


for c in cipher_text:
    if c in our_key:
        output_string += our_key[c]
    else:
        output_string += c

print(f"Output is: {output_string}")