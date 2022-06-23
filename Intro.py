from unicodedata import decimal
import pandas as pd

# 0.1 Traces of the ID
# You gain access to the office station's surveillance system and recover some video material of the coffee kitchen. 
# There you find a person taking your mug from the dish washer. 
# Unfortunately, you cannot see their face, but only a part of their ID batch on the jacket. 
# You can clearly read that the ID contains the number sequence 814.
# Scan through the database and find all people, whose ID contains the substring 814.
# To confirm you solved the puzzle correctly, compute the solution code and enter it in the box below.
# Solution code: the sum of the ID numbers of all people in question.

df = pd.read_csv('office_database.txt')
df.columns = ["Username", "ID", "AccessKey", "FirstLoginTime"]
print(df)
sum = 0
for i in range(len(df)):
    if '814' in str(df['ID'][i]):
        # print(df['ID'][i]) #for debug
        sum = sum + df['ID'][i]
    # else:
    #     df = df.drop(i)
print('Sum of ID of ppl has 814 = ', sum) #56503155
# df = df.reset_index(drop= True)

# 0.2 Access Codes
# Your second piece of evidence is the station's access system.
#  Each person only has access to some parts of the station. The parts a person can enter are encoded in their access key.
# The office station is divided into 8 modules (1, 2, 3, ..., 8). 
# For each module, a person can either have access (encoded as a 1), 
# or no access (encoded as a 0). The eight binary values are concatenated into an 
# eight-digit binary number and then stored in decimal representation in the database.
# Example: A person with access to module 3 and 7 will have a binary number 00100010 (with a 1 in 3rd and 7th position). 
# So this person's access key is 34 (the decimal representation of 00100010).
# Your coffee kitchen is located in module 5. Scan through the database and find all people, who have access to module 5.
# Solution code: the sum of the ID numbers of all people in question.
sum = 0
for i in range(len(df)):
    Access = df['AccessKey'][i]
    Access = f'{Access:08b}' # format string to 8 digit binary
    # print(Access) #for debug
    if '1' in Access[4]: # module 5 is the 4th index of the binary
        sum = sum + df['ID'][i]
    # else:
    #     df = df.drop(i)
print('Sum of ID of ppl has access to Mod5 = ', sum) #53905239
# df = df.reset_index(drop= True)

# 0.3 Alibi
# Your last piece of evidence is the time at which the mug was stolen. 
# When you checked the kitchen at 7:14, the mug was already stolen. 
# This means the culprit must have logged into the office station earlier than that.
# In your dataset, the column First Login Time stores the time at which people logged into 
# the office station for the first time today. Time is stored in the format hh:mm. 
# If a person has not yet logged in today, the column contains the value 99:99. 
# For your solution, you may assume that all times are in the morning (no a.m./p.m. confusion) 
# and that all times lie between 5:00 and 11:00.
# Scan through the dataset and find all people who logged in before 7:14.
# Solution code: the sum of the ID numbers of all people in question.
sum = 0
for i in range(len(df)):
    hours, minutes = map(int, df['FirstLoginTime'][i].split(':'))1
    if hours <= 7 and minutes < 14:
        sum = sum + df['ID'][i]
print('Sum of ID of ppl had accessed before 7:14 = ', sum) #18824468


# Find the thief
for i in range(len(df)):
    Access = df['AccessKey'][i]
    Access = f'{Access:08b}' # format string to 8 digit binary
    hours, minutes = map(int, df['FirstLoginTime'][i].split(':'))
    if '814' in str(df['ID'][i]) and (hours <= 7 and minutes < 14) and '1' in Access[4]:
        print('The thief is: ',df['Username'][i])