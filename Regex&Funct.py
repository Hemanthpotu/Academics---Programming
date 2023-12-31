# !/usr/bin/env python3
import re
# Question 1
##############################################
def recursive_function(Fn):
    '''
    Based on the conditions provided:
        If Fn=0, n=0
        If Fn=1, n=1 and
        If Fn>1, n=(Fn-1+Fn-2)
    A recursive function is generated when Fn>1
    '''
    # Since according to the rules of fibonacci sequence if Fn = 0, sum should be 0 so a if statement is used to return 0 when Fn=0
    if Fn == 0:
        return 0
    # Similarly when Fn=1, returning 1 for the fibonacci sequence
    elif Fn == 1:
        return 1
    # If Fn>1, I defined output as sum of outputs of Fn-1 and Fn-2 in accordance to the rule
    else:
        # Using current function such that n = n-1 + n-2
        return recursive_function(Fn-1)+recursive_function(Fn-2)
#################################################
# Defining Fn
Fn=6
# An empty list is generated to store output after each value of Fn in the range (0,Fn)
List = []
# A for loop is used to append each output to the sequence list
for i in range(Fn):
    List.append(recursive_function(i))
# Printing the fibonacci sequence as a list
print('The fibonacci sequence for n=6 is:',List)



# Question 2
###################################################################################################
# a. Function for compression of DNA
def compress_dna(DNA_string):
    '''
    Taking a DNA string and compressing it based on the number of repeated nucleotides
    If Sequence is AACCTGGG, compression should be A2C2T1G3
    '''
    # Creating a empty list to store string 'nucleotide+number of times of repeat' after each interation
    compression = []
    # Initializing count to 1
    count = 1
    # Defining the first character of DNA_string as previous_nucleotide and starting comparing from 2nd nucleotide
    previous_nucleotide = DNA_string[0]
    # Initializing a for loop to iterate over every nucleotide from second position in the inout nucleotide
    for nucleotide in DNA_string[1:]:
        # Checking if two consecutive nucleotides are same in the sequence
        if nucleotide == previous_nucleotide:
            # If yes, increase count by one
            count += 1
        # If they are not same
        else:
            # Appending the previous_nucleotide to the list with added count
            compression.append(previous_nucleotide+str(count))
            # resetting count to one
            count = 1
            # Incrementing to next nucleotide in the nucleotide input string
            previous_nucleotide = nucleotide
    # For appending last nucleotide to the list
    compression.append(previous_nucleotide+str(count))
    # Converting the list with strings to a complete string
    return ''.join(compression)
####################################################################################################
DNA_string = 'ACAAGATGCCATTGTCCCCCGGCCTCCTGCTGCTGCTGCTCTCCGGGGCCACGGCCACCG'
print('The DNA_string after compression:',compress_dna(DNA_string))

# b. Function for decompression of DNA
####################################################################################################
def decompress_dna(compressed_dna):
    '''
    Taking compressed DNA as input string and converting it into a complete DNA sequence string
    '''
    # Creating an empty list to store a partial repetitive nucleotide strings
    decompressed_dna = []
    # Initializing nucleotide as an empty string
    nucleotide = ''
    # Initializing count as an empty string
    count = ''
    # Starting a for loop to iterate over every alphabetical character
    for i in range(0, len(compressed_dna), 2):
        # Defining nucleotide
        nucleotide = compressed_dna[i]
        # defining count as integer value of character next to nucleotide
        count = int(compressed_dna[i + 1])
        # Multiplying the nucleotide with count and appending it to the list
        decompressed_dna.append(nucleotide * count)
    # returning the decompressed DNA string by converting the list into a string
    return ''.join(decompressed_dna)
###################################################################################################
input_string = 'A1C1A2G1A1T1G1C2A1T2G1T1C5G2C2T1C2T1G1C1T1G1C1T1G1C1T1G1C1T1C1T1C2G4C2A1C1G2C2A1C2G1'
print('The DNA input_string after decompressing:',decompress_dna(input_string))



# Question 3
###################################################################
'''
     Encryption program
         pig latin (encrypt and decrypt)
         shift (ceaser) cipher
'''
def encrypt_pig_latin(statement):
     '''
     If starting letter of word in statement is vowel, add 'ay' to the end of the word
     If starting letter of word in statement is not a vowel, move the letter to end of that particular word and add 'ay'
     '''
     # Generating empty string for output
     encrypt_statement = ""
     # A for lop was used to iterate over every word in the input statement
     for word in statement.split(" "):
         # Regex was used to find the words starting with vowels in the statement
         pattern=re.compile(r'[aeiou]', re.I)
         # If words starts with vowel, 'ay' is added to the end
         if pattern.match(word):
             word = word+'ay'
         # If doesn't, the first letter in the word is shifted to end of the word and 'ay' is added
         else:
             word = word[1:]+word[0]+'ay'
        # Finishing encrypt statement after all words are processed
         if (len(encrypt_statement)):
             encrypt_statement =encrypt_statement+" "+word
         else:
             encrypt_statement = word
     return encrypt_statement
########################################################################
# Input statement
statement = "pig latin statement to encrypt"
print(statement)
# printing out result
print (encrypt_pig_latin(statement))
#####################################################################
# 3a. Pig-latin decryption function
def pig_latin_decrypt(encrypt_statement):
    # Creating an empty statement to store decrypt statement
     decrypt_statement = ""
    # Using for loop to iterate over every word of input statement
     for word in encrypt_statement.split(" "):
         # Regex was used to find the words starting with vowels in the statement
         pattern = re.compile(r'[aeiou]', re.I)
         # Checking if the letter in the last third index is a vowel or not
         if word[-3] != pattern.match(word) :
             # If it is not a vowel, it is shifted to the beginning of the word and writing rest of the word till -3 index but not including it
             word = word[-3]+word[0:-3]
         else:
             # If it is vowel, then the word is written as it is removing last 'ay' from the word
             word = word[0:-2]
         # Finishing decrypt statement after all words are processed
         if (len(decrypt_statement)):
             decrypt_statement = decrypt_statement+" "+word
         else:
             decrypt_statement = word
     return (decrypt_statement)
######################################################################
# Input statement
encrypt_statement = "ymay amenay isay emanthhay otupay"
print(encrypt_statement)
# Printing out the result
print(pig_latin_decrypt(encrypt_statement))

# 3b. Encrypting using shift cipher
########################################################################
def shift_cipher(Statement, N):
    '''
    When a statement is given, this function encrypts it by ascending through N indices in the alphabets
    For example, abc will be encrypted to cde by increment. All other non-alphabetical characters will remain same
    The input N is the increment of letter in the statement needed
    '''
    # A string of alphabets in lower case was created
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    # An empty string was generated to store the final output encrypted statement
    encrypted_cipher = ''
    # A for loop was used to iterate over each letter in the input statement
    for char in Statement:
        # Checking if the letter in the statement is in the string of the alphabets
        if char.lower() in alphabets:
            # If yes, the index was defined as index of that particular letter in lower case + 2 increments
            index = (alphabets.index(char.lower()) + N) % 26
            # A new letter variable was defined and given value of alphabet at the index position in alphabet string
            new_letter = alphabets[index]
            # If the letter is in upper case in original input statement, change the new letter to upper case too
            if char == char.upper():
                new_letter = new_letter.upper()
            # Adding new letter thus obtained added to empty final string
            encrypted_cipher += new_letter
        # If the character in the statement is not an alphabet, then add directly to the output string
        else:
            encrypted_cipher += char
    return encrypted_cipher
###############################################################################
# Input statement
Statement = "My name is Hemanth Potu 1995"
# Increment
N = 2
# printing out the result
print('Shift-cipher encrypt of the given statement is:', shift_cipher(Statement, N))

# 3c. Decrypting shift cipher encrypt statement
################################################################################
def cipher_decrypt(encrypt, N):
    '''
    This function take the shift cipher encrypted statement as input and decrypts it by decrementing by the index decrement defined by the user
    The decrement value is N
    '''
    # A string of alphabets in lower case was created
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    # An empty string was generated to store the final output decrypted statement
    decrypted_cipher = ''
    # A for loop was used to iterate over each letter in the input statement
    for char in encrypt:
        # Checking if the letter in the statement is in the string of the alphabets
        if char.lower() in alphabets:
            # If yes, the index was defined as index of that particular letter in lower case - 2 increments
            index = (alphabets.index(char.lower())-N)%26
            # A new letter variable was defined and given value of alphabet at the index position in alphabet string
            new_letter = alphabets[index]
            # If the letter is in upper case in original input statement, change the new letter to upper case too
            if char == char.upper():
                new_letter = new_letter.upper()
            # Adding new letter thus obtained added to empty final string
            decrypted_cipher += new_letter
        # If the character in the statement is not an alphabet, then add directly to the output string
        else:
            decrypted_cipher += char
    return decrypted_cipher
##################################################################################
# Input statement
encrypt = "Oa pcog ku Jgocpvj Rqvw 1995"
# Decrement
N=2
# Printing out the result
print('Decrypt of shift cipher encrypt statement is:',cipher_decrypt(encrypt, N))



# Question 4
formula = 'Fe2(SO4)3'
# The pattern of molecules in brackets with their multiplier was used to separate them from the rest of the compound
bracketed_molecule = re.findall(r'\(([A-Za-z0-9]+)\)(\d*)', formula)
# Printing the result to cross confirm
print('The molecules in the brackets are:',bracketed_molecule)
# Defining the first object in the tuple as bracketed_element and second one as a multiplier
for bracketed_element, multiplier in bracketed_molecule:
    multiplier = int(multiplier) if multiplier else 1
    new_substring = bracketed_element * multiplier
    # Using the below pattern to find the part of string to be replaced
    replacement_pattern = '(' + bracketed_element + ')'
    if multiplier != 1:
        replacement_pattern += str(multiplier)
    formula = formula.replace(replacement_pattern, new_substring)
# Printing formula to check
print('The new formula after multiplying the bracketed molecules with their multipliers is:',formula)
# Extracting elements and their counts
# Finding pattern in the new formula
pattern = re.compile(r'([A-Z][a-z]*)(\d*)')
m = pattern.findall(formula)
print('Molecules and their respective counts:',m)
# An empty dictionary was created
element_counts = {}
# The first element in each tuple is labelled as molecule and second one as count
for molecule, count in pattern.findall(formula):
    # If there is no corresponding count for a molecule, count is defined to 1
    if count == '':
        count = 1
    # else count is defined integer of count
    else:
        count = int(count)
    # Using .get() function on the dictionary to find the total count of molecule in the dictionary
    element_counts[molecule] = element_counts.get(molecule, 0) + count
# Printing the outcome
for element, number in element_counts.items():
    print(element + ':' + str(number))



# Question 5
# Input statement
Input_string = "Peter Piper picked a peck of pickled peppers. Did Peter Piper pick a peck of pickled peppers? If Peter Piper picked a peck of pickled peppers, where's the peck of pickled peppers Peter Piper picked?"
# Using Regex to find the pattern using word boundaries character \bp to detect the word starting with p
# a word pattern [A-Za-z]* used to identify entire word followed by another word boundary
# argument re.IGNORECASE was used to define case insensitiveness
pattern = re.compile(r'\bp[A-Za-z]*\b', re.IGNORECASE)
m=pattern.findall(Input_string)
# Printing outcome
print (m)