cipher = {
    'a':'v',
    'b':'h',
    'c':'r',
    'd':'j',
    'e':'t',
    'f':'x',
    'g':'s',
    'h':'a',
    'i':'e',
    'j':'f',
    'k':'b',
    'l':'n',
    'm':'o',
    'n':'i',
    'o':'g',
    'p':'l',
    'q':'m',
    'r':'z',
    's':'q',
    't':'u',
    'u':'c',
    'v':'k',
    'w':'d',
    'x':'p',
    'y':'y',
    'z':'w',
    ' ': '}',
    '\n': '^',
    ',': '5',
    '!': '[',
    ':':'-',
    ')':'*',
    '.': '%' 
}

encrypted_file = open("encrypted_message_one.txt", 'r')

encrypted_message = encrypted_file.readline()

encrypted_file.close()

# Write code below

#reverse the cipher first
reversed_cipher = {}
for key, value in cipher.items():
    reversed_cipher[value] = key

decrypted_message = "" #initilizes string

for char in encrypted_message:
    decrypted_char = reversed_cipher.get(char,char)  #decrypts every character in reverse cipher 
    decrypted_message += decrypted_char   #appends the decrypted character to the message

print(decrypted_message) #prints the decrypted message