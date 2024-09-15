print("please enter answer as 'int' 'float' 'boolean' 'string'")
answerlist = []

answer1 = input("What type of variables is 10?\n").lower()
if answer1 == "int":
    answerlist.append(True)
else:
    answerlist.append(False)

answer2 = input("What type of variables is 5.01?\n").lower()
if answer2 == "float":
    answerlist.append(True)
else:
    answerlist.append(False)

answer3 = input("What type of variable is \"Hello World!\"\n").lower()
if answer3 == "string":
    answerlist.append(True)
else:
    answerlist.append(False)

answer4 = input("What type of variable is True/False\n").lower()
if answer4 == "boolean":
    answerlist.append(True)
else:
    answerlist.append(False)

for idx, item in enumerate(answerlist):
    if item:
        print(f"question {idx + 1}: correct")
    else:
        print(f"question {idx + 1}: wrong")


