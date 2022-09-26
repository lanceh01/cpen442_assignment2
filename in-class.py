from collections import defaultdict
ct = "YHZOZJBDACYHQAFDCWZONOZMBOPBRLZQAYHBYACOUQUBLQGZYHQAPQYDCWZONMIGHCIYCVYHZJBNYCHZBOYHZOBRRQYDBNYCQYDZLVGCMMBCHUZBOCHUZBOQDHBLLRZLBYZJHZADHZYHCIFHYQYCWZOBVYZOJBOUDGCMMBQYCGGIOOZUYCHZOYHBYDHZCIFHYYCHBWZJCAUZOZUBYYHQDGCMMBRIYBYYHZYQMZQYBLLDZZMZUEIQYZABYIOBLRIYJHZAYHZOBRRQYBGYIBLLNYCCPBJBYGHCIYCVQYDJBQDYGCBYXCGPZYGCMMBBAULCCPZUBYQYGCMMBBAUYHZAHIOOQZUCAGCMMBBLQGZDYBOYZUYCHZOVZZYGCMMBVCOQYVLBDHZUBGOCDDHZOMQAUYHBYDHZHBUAZWZORZVCOZDZZABOBRRQYJQYHZQYHZOBJBQDYGCBYXCGPZYGCMMBCOBJBYGHYCYBPZCIYCVQYGCMMBBAURIOAQAFJQYHGIOQCDQYNGCMMBDHZOBABGOCDDYHZVQZLUBVYZOQYGCMMBBAUVCOYIABYZLNJBDSIDYQAYQMZYCDZZQYXCXUCJABLBOFZOBRRQYHCLZIAUZOYHZHZUFZ".lower()
common_freq = "etaoinshrdlcumwfgypbvkjxqz"
runs = defaultdict(int)
frequency = defaultdict(int)

def swap(s,a,b):
    x = s.replace(a,"@")
    x = x.replace(b, "!")
    x = x.replace("@",b)
    return x.replace("!",a)

for i in range(len(ct)-3):
    runs[ct[i:i+3]] += 1
for i in range(len(ct)):
    frequency[ct[i]] += 1

sorted_runs = sorted([(value,key) for (key,value) in runs.items()], reverse=True)
print(sorted_runs)
# print(ct.replace(sorted_runs[1][1]," the "))

sorted_freq = sorted([(value,key) for (key,value) in frequency.items()], reverse=True)
table = {}
common_freq = swap(common_freq,"t","e")
common_freq = swap(common_freq,"i","h")
common_freq = swap(common_freq, "m","i")
common_freq = swap(common_freq, "c","d")
common_freq = swap(common_freq, "r","n")
common_freq = swap(common_freq, "l", "n")
common_freq = swap(common_freq, "w", "f")
common_freq = swap(common_freq, "l", "s")
common_freq = swap(common_freq, "l", "i")
common_freq = swap(common_freq, "g", "b")
common_freq = swap(common_freq, "u", "l")
common_freq = swap(common_freq, "y", "k")

for original,sub in zip(common_freq,sorted_freq):
    table.update({ord(sub[1]):original})
print(sorted_freq)
# print(table)
print(table)
print(ct.translate(table))
