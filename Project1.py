# !/usr/bin/env python
# Output file 1
# Opening the exclude_list.tab file in read mode and named it as excl_f
excl_f = open('exclude_list.tab','r')
# Using file.readline() to skip first line which contain headers for exclude_list.tab file
excl_f.readline()
# Generating an empty list to store the headers from exclude_list.tab file
exclude_list = []
# Initiating a for loop to iterate over each line in the file
for line in excl_f:
    # Using split function to split on tab character and uses [0] to access the first element of the line (Header)
    Name = '>' + line.split('\t')[0]
    # Adding name to the list after each iteration
    exclude_list.append(Name)
# Printing the exclude_list to view outcome
print(exclude_list)
# Finding the length of the list to confirm if all the names from exclude_list.tab file has been copied to the list
list_length = len(exclude_list)
print('The number sequences to be excluded from input file are:', list_length)
# Opening input scaffold file
ip_f = open('Scaffolds.fasta', 'r')
# Opening an output file to write after excluding the sequences
op1_f = open('after_excl_Scaffolds.fasta', 'w')
# Giving Header a none and Sequence an empty value before starting the loop
Header = None
Sequence = ''
# initializing a for loop to process till (n-1)th sequence
for line in ip_f:
    # Checking for the header
    if line.startswith('>'):
        # Checking if header and sequence have some value
        if Header != None and Sequence != '':
            # Checking if the header in the input file is not in the exclude list
            if exclude_list.count(Header) == 0 :
                # If not, write to output file
                op1_f.write(Header+'\n')
                op1_f.write(Sequence+'\n')
        Header = line.rstrip().split()[0]
        # Assigning empty value to the string
        Sequence = ''
    else:
        Sequence += line.strip()
# Using else block to process nth sequence
else:
    if Header != None and Sequence != '':
        # Checking if the header in the input file is not in the exclude list
        if exclude_list.count(Header) == 0:
            # If not, write to output file
            op1_f.write(Header + '\n')
            op1_f.write(Sequence + '\n')
# Closing the input and output files
excl_f.close()
ip_f.close()
op1_f.close()
# Checking if the job was done successfully by counting the number of sequences excluded
# Number of sequences in the exclude list were identified to be 1124. It was given a variable list_length
list_length = 1124
# Opening the files to be counted
ip_f = open('Scaffolds.fasta', 'r')
op1_f = open('after_excl_Scaffolds.fasta', 'r')
# Counting number of '>' characters in input Scaffolds.fasta file
count_input = 0
for line in ip_f:
    for char in line:
        if char == '>':
            count_input += 1
print('The total number of sequences in input Scaffolds.fasta file is:',count_input)
# Counting number of '>' characters in output file
count_output = 0
for line in op1_f:
    for item in line:
        if item == '>':
            count_output += 1
print('The total number of sequences in output file, after_excl_Scaffolds.fasta, is:',count_output)
# Checking for the difference in number of sequences between both files
x = count_input - count_output
# If difference is equal to length of list exclude_list, then job's done
if x == list_length:
    print('All sequences listed in the exclude_list.tab file were excluded successfully')
ip_f.close()
op1_f.close()


# Output file 2
# Initialize an empty dictionary to store the data.
trim_dict = {}
# Open the file and read line by line
with open('trim_list.tab', 'r') as trim_file:
    # Skip the header line
    trim_file.readline()
    # Process each line
    for line in trim_file:
        # Stripping line to remove any leading or trailing whitespace
        line = line.strip()
        # Splitting the line by tab character to get the individual elements
        data = line.split('\t')
        sequence_name = data[0]
        length = data[1]
        span = data[2]
        source = data[3]
        # Create a dictionary for the sequence with data divided into keys and their respective values
        sequence_info = {'length': int(length), 'span': span.split(','), 'source': source}
        # Add the sequence dictionary to the main dictionary with sequence name as the key
        trim_dict[sequence_name] = sequence_info
print(trim_dict)
# Opening input file in read and output file in write mode
ip2_f = open('after_excl_Scaffolds.fasta', 'r')
op2_f = open('trim_not_mark_mito.fasta', 'w')
# A threshold is defined, which could be used in later part of the program while writing to output file as a filter
threshold = 200
# Giving Header and Sequence a None value before starting the loop
Header = None
Sequence = ''
# Initiating a for loop
for line in ip2_f:
    # Checking for the header using'>' sign
    if line.startswith('>'):
        # Checking if header and sequence have some value
        if Header != None and Sequence != '':
            # Checking if the header in the input file is labelled for source as mitochondrion-not_cleaned in trim dictionary
            if Header in trim_dict and trim_dict[Header]['source'] != 'mitochondrion-not_cleaned':
                # Remove span from the sequence and printing out fragments left after trimming to an output file
                # Initializing start and end of sequence to be written to 0
                start = 0
                end = 0
                # Defining span by extracting from the trim dictionary for particular header
                span = trim_dict[Header]['span']
                for s in span:
                    # Extracting coordinates from the span by using split function on '..'
                    coordinates = s.split('..')
                    # Checking if first coordinate is beginning of the sequence
                    # Using int() since the coordinates are strings
                    if int(coordinates[0]) == 1:
                        # If yes, start is defined to be the coordinate[1]
                        start = int(coordinates[1])
                        # Using continue statement to direct program to else block of for loop in order to print out
                        continue
                    # Checking if second coordinate in the list is equal to length of the sequence
                    elif int(coordinates[1]) == trim_dict[Header]['length']:
                        # If yes, end is defined to first coordinate
                        end = int(coordinates[0])
                        # Using continue statement to direct program to else block of for loop in order to print out
                        continue
                    # Checking if the span to be trimmed is in between beginning and end of the sequence
                    else:
                        # If yes, end is set to first coordinate
                        end = int(coordinates[0])
                    # Removing N's at the beginning and end of trimmed sequence
                    final_sequence = Sequence[start:end].strip('N').strip()
                    # Checking if the trimmed sequence pass the threshold filter
                    if len(final_sequence) >= threshold:
                        # If yes, write to output file
                        op2_f.write('>'+Header +' ' + 'seqcoord:' + str(start) + '..' + str(end) + '\n')
                        op2_f.write(final_sequence+'\n')
                    # Setting start to coordinate 1 at this point of time in program before proceeding to next s in span
                    start = int(coordinates[1])
                else:
                    # Checking at this moment of the program, if start have a value greater than end
                    if start > end:
                        # If yes, end is set to length of the sequence
                        end = len(Sequence)
                    # Removing N's at the beginning and end of trimmed sequence
                    final_sequence = Sequence[start:end].strip('N').strip()
                    # Checking if the trimmed sequence pass the threshold filter
                    if len(final_sequence) >= threshold:
                        # If yes, write to output file
                        op2_f.write('>'+Header + ' ' + 'seqcoord:'+str(start) + '..' + str(end) + '\n')
                        op2_f.write(final_sequence+'\n')
            else:
                # If, write to output file
                # remove N's
                op2_f.write('>'+Header+'\n')
                op2_f.write(Sequence.strip('N')+'\n')
        # Defining header by removing any white spaces at the end and '>' at beginning of the line
        Header = line.lstrip('>').split()[0].strip()
        # Assigning empty value to the string
        Sequence = ''
    # If line doesn't start with '>'
    else:
        # add line of sequence to previous one
        Sequence += line.strip()
# Closing input and output files
ip2_f.close()
op2_f.close()


# Output file 3
# Opening input file in read and output file in write mode
ip2_f = open('after_excl_Scaffolds.fasta', 'r')
op3_f = open('trimmed_all.fasta', 'w')
# A threshold is defined, which could be used in later part of the program while writing to output file as a filter
threshold = 200
# Giving Header and Sequence a None value before starting the loop
Header = None
Sequence = ''
for line in ip2_f:
    # Checking for the header using'>' sign
    if line.startswith('>'):
        # Checking if header and sequence have some value
        if Header != None and Sequence != '':
            # Checking if the header in the input file is labelled for source as mitochondrion-not_cleaned in trim dictionary
            if Header in trim_dict:
                # remove span from the sequence
                # Initializing start and stop of sequence to be written to 0
                start = 0
                end = 0
                # Defining span by extracting from the trim dictionary for particular header
                span = trim_dict[Header]['span']
                for s in span:
                    # Extracting coordinates from the span by using split function on '..'
                    coordinates = s.split('..')
                    # Checking if first coordinate is beginning of the sequence
                    if int(coordinates[0]) == 1:
                        # If yes, start is defined to be the coordinate[1]
                        # Using int() since the coordinates are strings
                        start = int(coordinates[1])
                        # Using continue statement to direct program to else block of for loop in order to print out
                        continue
                    # Checking if second coordinate in the list is equal to length of the sequence
                    elif int(coordinates[1]) == trim_dict[Header]['length']:
                        # If yes, end is defined to first coordinate
                        end = int(coordinates[0])
                        # Using continue statement to direct program to else block of for loop in order to print out
                        continue
                    # Checking if the span to be trimmed is in between beginning and end of the sequence
                    else:
                        # If yes, end is set to first coordinate
                        end = int(coordinates[0])
                    # Removing N's at the beginning and end of trimmed sequence
                    final_sequence = Sequence[start:end].strip('N').strip()
                    # Checking if the trimmed sequence pass the threshold filter
                    if len(Sequence[start:end].strip('N')) >= threshold:
                        # If yes, write to output file
                        op3_f.write('>'+Header + ' ' +'seqcoord:'+str(start) + '..' + str(end) + '\n')
                        op3_f.write(final_sequence+'\n')
                    # Setting start to coordinate 1 at this point of time in program before proceeding to next s in span
                    start = int(coordinates[1])
                else:
                    # Checking at present, if start have a value greater than end
                    if start > end:
                        # If yes, end is set to length of the sequence
                        end = len(Sequence)
                    # Removing 'NNNN' at the beginning and end of trimmed sequence
                    final_sequence = Sequence[start:end].strip('N').strip()
                    # Checking if the trimmed sequence pass the threshold filter
                    if len(final_sequence) >= threshold:
                        # If yes, write to output file
                        op3_f.write('>'+Header + ' ' +'seqcoord:'+str(start) + '..' + str(end) + '\n')
                        op3_f.write(final_sequence+'\n')
            else:
                # If, write to output file
                # remove N's at the beginning and end of the sequence
                op3_f.write('>'+Header+'\n')
                op3_f.write(Sequence.strip('N')+'\n')
        # Defining header
        Header = line.lstrip('>').split()[0].strip()
        # Assigning empty value to the string
        Sequence = ''
    # If line doesn't start with '>'
    else:
        # add line of sequence to previous one
        Sequence += line.strip()
# Closing input and output files
ip2_f.close()
op3_f.close()