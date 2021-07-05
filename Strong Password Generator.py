import random
import array

# You can set the maximum length as per your convinience 
MAX_LEN = 12
DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                     'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                     'z']

UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                     'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                     'Z']

SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
           '*', '(', ')', '<']

Combined_list = DIGITS + LOCASE_CHARACTERS + UPCASE_CHARACTERS + SYMBOLS

rand_digit = random.choice(DIGITS)
rand_upper = random.choice(UPCASE_CHARACTERS)
rand_lower = random.choice(LOCASE_CHARACTERS)
rand_symbol = random.choice(SYMBOLS)

#This is to ensure that the generated password will have atleast one of each.
temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol

#Now the passsword length will reduce so max - 4.
for x in range(MAX_LEN-4):
    temp_pass = temp_pass + random.choice(Combined_list)
    temp_pass_list = array.array('u',temp_pass)
    #Shuffle in order to ensure a pattern is not repeated.
    random.shuffle(temp_pass_list)

password = ""
for i in temp_pass_list:
    password += i

print(password)
