"""
Identify and fix unintentional infinite loops

Expected run ->246
"""

result = ""
count = 2

while(count<8):
    result += str(count)
    print(result)
    count += 2
