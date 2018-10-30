input1str = input('Please enter a list of numbers separated by commas only\n')
input1strlist = input1str.split(',')
input1 = list(map(int, input1strlist))
input2str = input('Please enter a second list of numbers separated by commas only\n')
input2strlist = input2str.split(',')
input2 = list(map(int, input2strlist))

input1length = len(input1)
input2length = len(input2)

shortestlength = min(input1length,input2length)

longerinput = max(input1,input2)
longerlength = max(input1length,input2length)

def addlist(a, b):
    c = a + b
    return c

x = list(map(addlist, input1, input2))
x.extend(longerinput[shortestlength:longerlength])
print(x)
