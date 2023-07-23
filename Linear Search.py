array = [25,41,26,89,12]
SK = 899
num = 0

for i in array:
    if(i == SK):
        print("Item found at index ", num)
        break;
    num+=1

if(num==5):
    print("Item not found")