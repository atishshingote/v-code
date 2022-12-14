letter = '''Dear <|NAME|>,
Greeting from ABC coding house. i am happy to tell you about your selection 
You are selected !
have a great day ahead !
Date <|DATE|>
'''
name = input("Enter Your Name\n")
date = input("Enter Date\n")
letter = letter.replace("<|NAME|>",name)
letter = letter.replace("<|DATE|>",date)
print(letter)