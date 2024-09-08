encrypted_file = open("encrypted_message_two.txt", 'r')

encrypted_message = encrypted_file.readline()

encrypted_file.close()

# Write Code Here
#turns hidden message to a list
key = list(encrypted_message)

# performs decryption by picking the second letter, going halfway through the line, and moving 2 letters at a time.
for index in range(1, len(key) // 2, 2):
    # brings the character index from the opposite direction
    ending_index = len(key) - index - 1
    
    # swaps characters
    key[index], key[ending_index] = key[ending_index], key[index]

# joins the list and creates a string
decrypted_message = ''.join(key)

print(decrypted_message)