import re 
#adding the phone number which will check the number to using re 
Phone_number=input()
a=re.fullmatch('[6-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]',Phone_number)
if a!=None:
    print("the Phone number is valid")
else:
    print("The phone number is not valid ")
