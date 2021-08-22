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

    def update_user_desc(self, desc):
        self.user_desc = desc
        
    def update_no_of_follow(self, followerCount):
        self.no_of_follow = followerCount
        
    def update_user_verified(self, verified):
        self.user_verified = verified
        
    def update_tweet_date(self, date):
        self.tweet_date = date
        
    def update_tweet_list(self, tweet):
        self.tweet_list = tweet

    def print_user(self):
        print ("###########################################################")
        print ("Name = ", self.user_name)
        print ("Code = ", self.user_code)
        print ("Desc = ", self.user_desc)
        print ("No. Of Follow = ", self.no_of_follow, "\n")
        print ("Verified = ", self.user_verified)
        print ("Date = ", self.tweet_date)
        print ("Tweet = ", self.tweet_list)
        print ("###########################################################")

tempUser = User()

def update_user_data(key, value):

    if (key == 'uname.'):
        tempUser.update_user_name(value)
        
    elif (key == 'user_code.'):
        tempUser.update_user_code(value)
        
    elif (key == 'user_desc.'):
        tempUser.update_user_desc(value)
        
    elif (key == 'No. followers.'):
        tempUser.update_no_of_follow(value)
        
    elif (key == 'verified_user?.'):
        tempUser.update_user_verified(value)
        
    elif (key == 'tweet_date.'):
        tempUser.update_tweet_date(value)
        
    elif (key == 'tweet_text.'):
        tempUser.update_tweet_list(value)
        
    else:
        print("unkown key", key, value)


#process each record and make key & value pair
def process_record(record_data):
    #print (record_data)
    
    #extract all the records in a line
    records = record_data.split("$")
    
    #split the record to retrevive the key value pair
    #print ("records" , records)
    for record in records:
        if record != '':
            temp = record.split(":")
            #print ("record", record)
            #print ("Key, value",len(temp), temp)
            if len(temp) > 1:
                key= temp[0]
                value=temp[1]
                for i in range(2,len(temp)):
                    value += ":" + temp[i]
                #print("key=", key , "value=", value);
                update_user_data(key, value)
            else:
                print ("invalid len", temp, len(temp))
    

#read the entire file line by line and find a record (key & value pair)
def read_records():
    #open the file in read mode
    with open ('input.txt', 'r') as reader:

        # Read and print the entire file line by line
        current_line = reader.readline()
        next_line = ''

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
                
        #Process the last line
        process_record(record_data)


read_records()

#process other tags
tempUser.print_user()