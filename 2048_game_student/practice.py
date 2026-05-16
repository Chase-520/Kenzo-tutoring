import random
test = []
for c in range(4):
    row = []
    for r in range(4):
        row.append(random.randint(0,10))

    test.append(row)

def printLS(sss):
    for i in sss:
        print(i)

printLS(test)

print("###############")

def rotate_ccw(list_in):
  
    row_index = 0
    list_out = []
    for i in range(4):
        list_out.append([0,0,0,0])
    print(list_out)
    while(row_index<len(list_in)):
        row = list_in[row_index]
        element_index = 0
        while(element_index<len(row)):
            element = row[element_index]
            # print(f"{3-element_index}, {row_index}")
            # print(element)
            list_out[3-element_index][row_index] = element

            element_index += 1
        row_index += 1
        
    print("###############")
    for i in list_out:
        print(i)

rotate_ccw(test)