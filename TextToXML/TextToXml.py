import os, re

class User:
    def __init__(self):
            self.user_name = ''
            self.user_code =  ''
            self.user_desc = ''
            self.no_of_follow = ''
            self.user_verified = ''
            self.tweet_date = ''
            self.tweet_list = ''
            
    def update_user_name(self, name):
        self.user_name = name

    def update_user_code(self, code):
        self.user_code = code

    def print_user(self):
        print ("name = ", self.user_name)
        print ("code = ", self.user_code)


tempUser = User()

def update_user_data(key, value):

    if (key == '$uname.'):
        print("username found", key, value)
        tempUser.update_user_name(value)
    elif (key == '$user_code.'):
        print("user_code found", key, value)
        tempUser.update_user_code(value)
        
    #process other tags
    tempUser.print_user()


#process each record and make key & value pair
def process_record(record_data):
    #print (record_data)
    #split the record to retrevive the key value pair
    temp=record_data.split(":")
    key= temp[0]
    value=temp[1]
    #print("key=", key , "value=", value);
    update_user_data(key, value)
    

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
