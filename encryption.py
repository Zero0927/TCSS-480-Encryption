import random

# Generates and returns a random key
def keyGen(alpha):      
    key = ""
    for i in range(len(alpha)):
        index = random.randint(0, 25-i)
        key = key + alpha[index]
        alpha = alpha[:index] + alpha[index+1:]
    return key


# Encrypts plaintext using a random key and a Caeser cipher
def caesar(plainText):

    # __________________________
    # header for function caesar that takes plainText as an argument
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    key = keyGen(alphabet)
    print("Random key: ")
    print(alphabet)
    print(key)
    # ___________________  convert plainText to all lowercase letters
    cipherText = ""
    for ch in plainText:
        idx = alphabet.find(ch.lower())
        #_______________
        # if index is positive
        # append to cipherText a character sitting in key[idx]
        if idx > 0:
            cipherText += key[idx]
        else:
            # else if index is negative but ch is a digit
            # append that digit to cipherText
            if ch.isdigit():
                cipherText += ch
            # else if index is negative but ch is not a digit
            # append a blank to cipherText
            else:
                cipherText += ' '
        
    return cipherText


# Encrypts plaintext using transposition cipher
def trans(plainText):
	
    #_________________________
    # extract all chars sitting in even positions into evenChars string
    evenChars = ''.join([plainText[i] for i in range(len(plainText)) if i % 2 == 0])
    # extract all chars sitting in odd positions into oddChars string
    oddChars = ''.join([plainText[i] for i in range(len(plainText)) if i % 2 == 1])
    cipherText = oddChars + evenChars
    return cipherText


# Encrypts plaintext using ASCII shift
def ascii_shift(plainText):

    shift = random.randint(1, 25)
    print "Shift: ", shift
    # _____________
    # construct and return cipherText as plainText in which 
    # each char is replaced with old char + shift (look up chr and ord functions)
    cipherText = ''.join([chr(ord(ch) + shift) for ch in plainText])
    return cipherText


# Driver
def my_main():

    while 1:
        # ___________________________
        # get message
        message = raw_input('Enter a message to encrypt: ')
        # ___________________________
        # get choice
        print('Which encryption do you want to use?')
        choice = raw_input('Enter 1 for random Caeser cipher, 2 for transposition, 3 for an ASCII shift: ')
        # ___________________________
        # while statement that is entered if choice contains more than just digits
        # or int_choice is not within the range [1, 3] 
        while not choice.isdigit():
            print('Invalid input - try again')
            choice = raw_input('Enter 1 for random Caeser cipher, 2 for transposition, 3 for an ASCII shift: ')
        int_choice = int(choice)
        # _______________________
        # based on the user's choice (1, 2 or 3)  call appropriate encryption function and
        # store the result into variable cipherText
        if int_choice == 1:
            cipherText = caesar(message)
        elif int_choice == 2:
            cipherText = trans(message)
        elif int_choice == 3:
            cipherText = ascii_shift(message)
        print 'The encrypted message is: ', cipherText
        repeat = raw_input('Repeat? Enter y to repeat or q to quit: ')
        while repeat != 'y' and repeat != 'q':
            repeat = raw_input('Repeat? Enter y to repeat or q to quit: ')
        if repeat == 'q':
            break


if __name__ == '__main__':
    my_main()

        
    
    


