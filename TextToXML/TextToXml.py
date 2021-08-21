import os, re


def process_record(record_data):
    print (record_data)

#read the entire file line by line and find a record (key & value pair)
def read_records():
    #open the file in read mode
    with open ('input.txt', 'r') as reader:

        # Read and print the entire file line by line
        current_line = reader.readline()

        while current_line != '':  # The EOF char is an empty string

            #store the current line in the record data
            record_data=current_line
            #print(current_line, end='')
            next_line = reader.readline()

            #check if record is on single line or multiple lines
            if next_line != '' and next_line[0] == '$':
                #process the record if it is fully read
                process_record(record_data)
            else:
                #if it is a multiple line record. append the data
                record_data += next_line

            #move to next line
            current_line = next_line
                
                


read_records()
