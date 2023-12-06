# # !/usr/bin/env python
#
# # Question 1
# # Defining strings and assigning a variable to them
# stringA = "GGGCCGTTGGT"
# stringB = "GGACCGTTGAC"
# # Using if loop to check if strings have equal length
# if len(stringA) != len(stringB):
#     print("Strings must have the same length")
# distance = 0
# # Using for loop to iterate through each pair of corresponding characters in two strings
# for char1, char2 in zip(stringA, stringB):
#     if char1 != char2:
#         distance = distance+1
# print("Hamming distance between strings GGGCCGTTGGT and GGACCGTTGAC is ", distance)
#
#
#
# # Question 2
# # Reading the input file
# ip2_f = open('contigs.fasta', 'r')
# # Creating an output file and opening it to write
# op2_f = open('output2.fasta', 'w')
# # Using a while loop for defining lines of input file as Header2 and Sequence2
# while True:
#     Header2 = ip2_f.readline()
#     # Using break statement to cut the loop when header is not the line
#     if not Header2:
#         break
#     # Writing the header without any change to an output fasta file
#     op2_f.write(Header2)
#     # Reading the sequence line
#     Sequence2 = ip2_f.readline().strip()
#     # Initializing for loop to break line of sequence into lines of length 80 and writing it to an output fasta file
#     for i in range(0, len(Sequence2), 80):
#         op2_f.write(Sequence2[i:i+80] + '\n')
# # Closing the inout and output files
# ip2_f.close()
# op2_f.close()
#
#
#
# # Question 3
# # importing and opening the fastq input file
# ip3_f = open('example.fastq.txt', 'r')
# # Creating an output file and opening it to write
# op3_f = open('output3.fasta.txt', 'w')
# # input fastq file is read and each line was labelled as variable with following names
# for line in ip3_f:
#     Header3 = line
#     Sequence3 = ip3_f.readline().strip()
#     Identifier3 = ip3_f.readline()
#     Quality3 = ip3_f.readline().strip()
#     # Converting '@' of headers in fastq file format to '>' in fasta format
#     Header3 = '>' + Header3[1:]
#     op3_f.write(Header3)
#     op3_f.write(Sequence3 + '\n')
# # Closing the input and output files
# ip3_f.close()
# op3_f.close()
#
#
#
# # Question 4
# # importing and opening the fastq input file
# ip4_f =open('example.fastq.txt','r')
# # Creating an output file and opening it to write
# op4_f = open('output4.fastq', 'w')
# # Phred33 dictionary is created using the picture shared in assignment page
# Phred33_Dict = {'!':0, '"':1, '#':2, '$':3, '%':4, '&':5, "'":6, '(':7, ')':8, '*':9, '+':10, ',':11, '-':12, '.':13, '/':14,
#            '0': 15, '1': 16, '2': 17, '3': 18, '4':19, '5':20, '6':21, '7':22, '8':23, '9':24, ':':25, ';':26, '<':27, '=':28,
#            '>':29, '?':30, '@':31, 'A':32, 'B':33, 'C':34, 'D':35, 'E':36, 'F':37, 'G':38, 'H':39, 'I':40, 'J':41}
# # The minimum quality score (q) is set to 20 (as we generally avoid bases with the phred+33 score < 20)
# Quality_score = 20
# # The minimum length (n) was set to 50
# min_len = 50
# # input fastq file is read and each line was labelled as variable with following names
# for line in ip4_f:
#     Header4 = line
#     Sequence4 = ip4_f.readline().strip()
#     Identifier4 = ip4_f.readline()
#     Quality4 = ip4_f.readline().strip()
# # Trimming Sequence4 from both ends
# # Labelling the trim index. Left starts from index 0 and right starts from the end of the sequence (index len(Sequence4))
#     left_trim = 0
#     right_trim = len(Sequence4)
#     # trimming from the left end of the sequence
#     for i in range(0, len(Sequence4)):
#         if Phred33_Dict[Quality4[i]] < Quality_score:
#             continue
#         else:
#             Sequence4 = Sequence4[i:]
#             Quality4 = Quality4[i:]
#             break
#     # trimming from right end of the sequence
#     for i in range((len(Sequence4) - 1), 0, -1):
#         if Phred33_Dict[Quality4[i]] < Quality_score:
#             continue
#         else:
#             Sequence4 = Sequence4[:i+1]
#             Quality4 = Quality4[:i+1]
#             break
#     trimmed_sequence = Sequence4[left_trim:right_trim]
#     if len(trimmed_sequence) >= min_len:
#         op4_f.write(Header4)
#         op4_f.write(trimmed_sequence + '\n')
#         op4_f.write(Identifier4)
#         op4_f.write(Quality4[left_trim:right_trim ] + '\n')
# # Closing the input and output files
# ip4_f.close()
# op4_f.close()
#
#
#
# # Question 5
# # Phred33 dictionary is created using the picture shared in assignment page
# Phred33_Dict = {'!':0, '"':1, '#':2, '$':3, '%':4, '&':5, "'":6, '(':7, ')':8, '*':9, '+':10, ',':11, '-':12, '.':13, '/':14,
#            '0': 15, '1': 16, '2': 17, '3': 18, '4':19, '5':20, '6':21, '7':22, '8':23, '9':24, ':':25, ';':26, '<':27, '=':28,
#            '>':29, '?':30, '@':31, 'A':32, 'B':33, 'C':34, 'D':35, 'E':36, 'F':37, 'G':38, 'H':39, 'I':40, 'J':41}
# # Threshold is set to 20 as in the case of Question 4
# Threshold = 20
# # importing and opening the fastq input file
# ip5_f =open('example.fastq.txt','r')
# # Creating output files and opening them to write
# # Output file for those sequences with average quality less than threshold
# op5_belowT_f = open('output5_belowT.fastq', 'w')
# # Output file for those sequences with average quality at least equal to threshold
# op5_atleastT_f = open('output5_atleastT.fastq', 'w')
# # input fastq file is read and each line was labelled as variable with following names
# for line in ip5_f:
#     Header5 = line
#     Sequence5 = ip5_f.readline().strip()
#     Identifier5 = ip5_f.readline()
#     Quality5 = ip5_f.readline().strip()
#     # Average quality is measured by following function
#     avg_quality = sum(Phred33_Dict[i] for i in Quality5) / len(Quality5)
#     # Checking if average quality of sequence is below the indicated threshold
#     if avg_quality < Threshold:
#         # if yes, write to the output file op5_belowT_f
#         op5_belowT_f.write(Header5)
#         op5_belowT_f.write(Sequence5+'\n')
#         op5_belowT_f.write(Identifier5)
#         op5_belowT_f.write(Quality5+'\n')
#     else:
#         # if no, write to the output file op5_atleastT_f
#         op5_atleastT_f.write(Header5)
#         op5_atleastT_f.write(Sequence5+'\n')
#         op5_atleastT_f.write(Identifier5)
#         op5_atleastT_f.write(Quality5+'\n')
# # Closing the input and output files
# ip5_f.close()
# op5_belowT_f.close()
# op5_atleastT_f.close()
#
#
#
# # Question 6
# # Defining the string
# DNA_string = "TGTCAGCTACCTTGATGGATTGAGTTTGTTTCGGTCGATGCTCCATCGGGAGAGAGTCTGCGTCCTGGTCCGAGCAAGTCCCACCAAGTGGCACTTGGCGGCGCCATGTCCTATCTAGTGCCACCATGTCCGAGGACTTTGATGGCACATGGTGGCACTTGATTTGCCCAAGTCCCACCTGCTCCGACGTGGACCGACTTCGTGGCACATCGCTATCACCCACTCTACCGTTGAAAAGCCGAAGTCAAGCGCCGAAAGCTGATCGATTTGCGGTGTGATACGTTGCCAGTGATTCGTTCCGTGGTTTATGCTTGGCGCACCTACCGCGTCCCCGACGCATCGACTCCGCCGCCATTGCGCGGCACAAAACGGCCTTCGATCCTTCCGTACGGAGGGGTACTGCAGGGCTCACTGTTCATGCCGGAAATTGCACCGGCTTTTTTTTCAATCAAATCAAGTGGACCGTGTCGGATAGTGAGGACACCGGACACCGCGATACCAAGCCGATTGGCGGTCTGTTTGTGAAAATAGACCGTAGTGCGGACAATTCCGAAGCCGGACACCGGACAGGTGCTCTGTGGAAATTCCGCGTATGCCCGACACCCTTACAGCCGCGTGGCTGGGTGCGGATCACGAAGCCCAAAACACTGCGGCGGGGATGATCTGACTTTGGGGTGGGGAGCTGCTTTGCGTGCCGAATGACGGCGAACGCAGGCTTCTGAGCAAATATCGATCCGGGGGGCGCCACCGGTACCAGAACGGCGCAACAGGTAATCACCCATCACGGCAAGGGCCGCAGGCGTGTGGACGCAATCCACGCGAAGGCAGGCTCGCATCCAGAGATGCACCGGATAGGGTGGCCGCGCAAGCGGTGCGTGAGGCGAGAGCCTTGCATGTTCGCGAAGCGGACGGTCACGACGCATTGCTTCCATGCTCAGGGCCGATCGGTTTGGCATCGCTAAAGGACCGGAAGAGTGGTTGTAGGACCGGCAGGGTGGGCCGGCAAGCTGGGGGTGGTACCCCGGTGCACCAAGCGGGCAGGGCCAATTCGGGGTTGGCGCCGCCGAGAATTGGGTTGCGCAGATTTGCGCGGCCGGCGGGATGCGCTTAGCGCGAATAGGAATCCGTC"
# # The maximum number of longest repeats possible for any given string is 2 i.e., half of the string
# # The length of the longest possible repeat of the string given is
# print("The length of the given string of DNA is", len(DNA_string))
# # used int() since half_string is a float value
# Half_string = int(len(DNA_string)/2)
# # generating an empty string to store the repeat
# repeat_string = ""
# # creating a for loop for iterating through a window of size j
# for j in range(Half_string,3,-1):
#     # initiating a nested loop
#     for i in range (0,len(DNA_string)-j+1):
#         # checking if substring appears more than once in the DNA_string
#         if DNA_string.count(DNA_string[i:i+j]) > 1:
#             repeat_string = DNA_string[i:i+j]
#             break
#     if repeat_string:
#         break
# print("The longest repeat in the string DNA_string is", repeat_string)
#
#
# # Question 7
# # Defining an example string 'CGATAGC' as a variable
# F_seq = 'CGATAGC'
# # Function to obtain the reversed string
# R_seq = ''.join(reversed(F_seq))
# # Using if statement to check if both strings are same
# if F_seq == R_seq:
#     # Printing the result
#     print("The string given is a palindrome")
# if F_seq != R_seq:
#     print("The string given is not a palindrome")
#
#
#
# # Question 8
# import random
# random_no = random.randint(1,10)
# g = random_no
# while True:
#     # Ask user to guess a number
#     guess = int(input("Number guessed: "))
#     if guess == g:
#         print("Guess is exactly right")
#         break
#     elif guess < g:
#         print(" Guess is too low, please try again")
#     else:
#         print('Guess is too high, please try again')
#
#
#
# # Question 9
# # Creating a dictionary  D of codons for translation
# D = {"UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L",
#      "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
#      "UAU": "Y", "UAC": "Y", "UAA": "*", "UAG": "*",
#      "UGU": "C", "UGC": "C", "UGA": "*", "UGG": "W",
#      "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
#      "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
#      "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
#      "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
#      "AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M",
#      "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
#      "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K",
#      "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R",
#      "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
#      "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
#      "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E",
#      "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G"}
# # Labelling RNA string as a variable s
# s = 'ACCAAGCGAAACAAGUAGCUGCUCUGCACUACCUGCAGUUACAUUGAGACCACCAACGGACGUAGUAAAAGUAACGAUAACUCCGUUGAAACUACCAGAGAUAUCAUCAAGUUGACGGUACUGACCUGCUGUUGGUUGGACGCCGAUGUAUGACACAGGAUAAAACUCUAUCUAGUACCUGUAGUUUAAAUCAGGUUACCUGAGGCCCUUAUUUUAUCAGUCAACAUCAAAGCUAUCGUCUUCCACGAGUGGAUACUGAGGCUUGAUUUCCACCUGGGGUUCGAAUUUAGCAGAGAUACCAUCGAGUACUUCCAGGGUCAGGUCGAGGCUCAGUUCUUGCUCUCCAUUAAUGGUAUCCAGGAAGAGGGGAUCUUCCAGGAGGUCAUCGAGGGUGAAGAUGAUGGCAUUGAUCUUCUCGAGGAUAGACUCAAAGCGUUUUUCGACCGAUUCGCUUUUAGCCAUGGUUCGAACUGCGUAGGUGUAUAGGUUCAUUGAAGUGUAGCUCCCUUUACUUCUGUUGGCUACUGUCAAGCCACGGUGCUUUGAUUUGAAGUGUUCCUCCUAACAAUUCCUGGGCUUUUGAUCCGUCUGGUUCGUGUUCGACGAUGAUGGGCGUUACCC'
# # Generating an empty string to add translated protein
# protein_seq = ''
# # Initiating a for loop to loop through string s by an increment of 3 while leaving the reminder of bases at the end of the sequence that are not divisible by 3 as each codon is a group of three nucleotides
# for i in range(0, len(s)-(len(s)%3),3):
#      # Initializing a for loop to break the translation, if it encounter a stop codon that translates tp * in the dictionary D
#      if D[s[i:i + 3]] == "*":
#           break
#      # Adding the translated amino acids to the protein string from previous loop of i
#      protein_seq = protein_seq + D[s[i:i + 3]]
# # Printing the protein sequence
# print('The aminoacid sequence of the protein encoded by the RNA string-s is', protein_seq)
