# Name: Lora Chisholm
# Lab: W13 Encryption Lab
# Cipher: Rail Fence Cipher - password Derived Rails


# Algorithm Description
# The Rail Fence cipher is a transposition cipher that writes the plaintext in a zigzag pattern across a defined number of "rails"(rows), determined from a password.
#The message is written diagonally down and then up across the rails until all characters are placed.  The ciphertext is obtained by reading the characters row by row.

#Algorithm
# 1. Derive the number of rails from the password
# 2. Write the plaintext in a zigzag pattern across the rails
# 3. Concatenate characters from each rail to form the ciphertext

# Encryption
# 1. Derive the number of rails from the password
# 2. Write the plaintext in a zigzag pattern across the rails
# 3. Concatenate characters from each rail to form the ciphertext

# Decryption
# 1. Derive the number of rails from the password
# 2. Determine the zigzag path positions based on the message length
# 3. Fill the rails in row wise order.
# 4. Reconstruct the plaintext by traversing the zigzag pattern

# Note: The same password must be used for both encryption and decryption to ensure reversibility

def get_pseudocode():
    return (
        "Encryption Pseudocode (Rail Fence Cipher with Password-Derived Rails):\n"
        "-----------------------------------------------------------------------\n"
        "   REMOVE all spaces from password\n"
        "   CONVERT password into a number of rails\n"
        "   INITIALIZE rails as a list of empty strings\n"
        "   SET direction_down TO True\n"
        "   SET current_rail TO 0\n"
        "   FOR each character IN plaintext DO\n"
        "       APPEND character TO rails[current_rail]\n"
        "       IF direction_down THEN\n"
        "           INCREMENT current_rail\n"
        "           IF current_rail EQUALS num_rails THEN\n"
        "               SET direction_down TO False\n"
        "               SET current_rail TO num_rails - 2\n"
        "       ELSE\n"
        "       DECREMENT current_rail LESS THAN 0 THEN\n"
        "           SET direction_down TO True\n"
        "           SET current_rail TO 1\n"
        "   CONCATENATE all strings in rails TO form ciphertext\n"
        "   RETURN ciphertext\n\n"
        "Decryption Pseudocode (Rail Fence Cipher with Password-Derived Rails):\n"
        "-----------------------------------------------------------------------n"
        "FUNCTION DECRYPT(ciphertext, password)\n"
        "   REMOVE all spaces from password\n"
        "   CONVERT password into number of rails\n"
        "   INITIALIZE pattern list with length of ciphertext\n"
        "   SET direction_down TO True\n"
        "   SET current_rail TO True\n"
        "   FOR each position IN cipertext indices DO \n"
        "       SET pattern[position] TO current_rail\n"
        "       IF direction_down THEN\n"
        "           INCREMENT current_rail\n"
        "           IF current_rail EQUALS num_rails THEN\n"
        "               SET direction_down TO False\n"
        "               SET current_rail TO num_rails - 2\n"
        "   ELSE\n"
        "       DECREMENT current_rail\n"
        "       IF current_rail LESS THAN 0 THEN\n"
        "           SET direction_down TO True\n"
        "           SET current_rail TO 1\n"
        "   INITIALIZE rails as empty lists\n"
        "   FOR rail_number FROM 0 TO numb_rails - 1 DO\n"
        "       Assign next character of ciphertext TO rails[rail_number]\n"
        "   INITIALIZE plaintext TO empty string\n"
        "   FOR each index IN pattern DO\n"
        "       APPEND next character from corresponding rail TO plaintext\n"
        "   RETURN plaintext\n"
    )
    # The Rail Fence Cipher is a symmetric transposition cipher that writes plaintext in a zigzag pattern across multiple horizontal lines, called rails.
    # The number of rails is derived from the password, allowing the same password to be used for both encryption and decryption.
    # During encryption, the message is written diagonally down and up across the rails, then the ciphertext is formed by reading row by row.  
    # Decryption uses the same rail count to reconstruct the zigzag pattern and retrieve the original message.    
    

def get_author():
    return "Lora Chisholm"

def get_cipher_name():
    return "Rail Fence Cipher - Password Derived Rails"

def get_cipher_citation():
    return (
        "Samarth Godara, Shakti Kundu, Ravi Kaler, “An Improved Algorithmic Implementation of Rail Fence Cipher,” "
        "International Journal of Future Generation Communication and Networking, Vol. 11, No. 2, 2018. "
        "URL: https://www.researchgate.net/publication/324240381_An_Improved_Algorithmic_Implementation_of_Rail_Fence_Cipher\n"
        "Reddyvari Venkateswara Reddy et al., “Encrypting Images Using Repetitive Rail Fence Cipher,” IJERT, 2023. "
        "URL: https://www.ijert.org/research/encrypting-images-using-repetitive-rail-fence-cipher-IJERTV13IS030082.pdf"
    )


def encrypt(plaintext, password):
    # This removes any spaces from the password for consistent key processing
    password = password.replace(" ", "")
    
    # Now I convert the password into a number of rails using ASCII values
    #Ensuring at least 3 rails and cap it at 10 for simplicity, ord(c) gets the ASCII value of each character, the sum is modded by 9 and then we add 2
    # so the number of the rails will always be between 2 and 10, because we want to make sure it's usable and consistent for both encryption and decryption.
    num_rails = sum(ord(c) for c in password) % 9 + 2
    
    # Create a list to hold the strings for each rail
    rails = [""] * num_rails
    
    # Then we initialized the current rail position and direction - downward to start, rails holds each row as a string,
    # the current_rail tracks which rail we are on, the direction_down tells us whether to move down or up through the rails.
    current_rail = 0
    direction_down = True
    
    # so now we will loop through each character in the plaintext and append it to the correct rail, moving down and up in a zigzag
    
    for char in plaintext:
        # Append the character to the current rail
        rails[current_rail] += char
        
        # Move to the next rail (zigzag )
        if direction_down:
            current_rail +=1
            if current_rail == num_rails:
                #Reverse direction if we get to the bottom
                direction_down = False
                current_rail = num_rails - 2
        else:
            current_rail-= 1
            if current_rail < 0:
                # Reverse direction if we hit the top
                direction_down = True
                current_rail = 1
    
    # Combine all the rails to form the ciphertext 
    ciphertext = ''.join(rails)
    
    # Return the encrypted message
    return ciphertext

def decrypt(ciphertext, password):
    #remove any spaces from the password to ensure consistent key usage
    password = password.replace(" ", "")
    
    #Drive the number of rails from the password
    num_rails = sum(ord(c) for c in password) % 9 + 2
    
    #create a list to track the rail index (pattern) for each character position
    pattern = []
    current_rail = 0 
    direction_down = True
    
    #Loop through each position in the ciphertext and record the rail index
    for i in range(len(ciphertext)):
        pattern.append(current_rail)
        
        #Update current rail based on zigzag direction
        if direction_down:
            current_rail += 1
            if current_rail == num_rails:
                direction_down = False
                current_rail = num_rails - 2
        else:
            current_rail -= 1
            if current_rail < 0:
                direction_down = True
                current_rail = 1

# List of empty strings for each rail to hold the characters
rails = [""] * num_rails

# Count how many characters belong to each rail using the pattern
rail_lengths = [pattern.count(r) for r in range(num_rails)]

# Fill each rail with the appropriate number of characters from the ciphertext
# creates placholders for each rail, counts how many character should go in each rail, slices the ciphertext into segments that match length
index = 0
for rail_num in range(num_rails):
    length = rail_lengths[rail_num]
    rails[rail_num] = ciphertext[index:index + length]
    index += length
    
    
# Reconstruct the original plaintext by reading from the rails in zigzag order
rail_pointers = [0] * num_rails # Track how many characters we've used from each rail
plaintext = "" # Final output
    
# Follow the same zigzag pattern to pull characters from each rail
for rail_index in pattern:
    # append the next charcter from the correct rail
    plaintext += rails[rail_index][rail_pointers[rail_index]]
    rail_pointers[rail_index] += 1
        
return plaintext
    

    
    