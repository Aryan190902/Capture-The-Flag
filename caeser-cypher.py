text = input("Enter the text to encode: ")
shift = 3
alphabet=["a","b","c","d","e","f","g","h","i","j","k","l",  
    "m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
bigAlphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
decode = ''
for i in range(0, len(text)):
    if text[i] in alphabet:
        decode += alphabet[(alphabet.index(text[i]) + shift)%len(alphabet)]
    elif text[i] in bigAlphabet:
        decode += bigAlphabet[(bigAlphabet.index(text[i]) + shift)%len(bigAlphabet)]
    else:
        decode += text[i]
print(decode)
    
