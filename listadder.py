def addlist(a, b):
    c = a + b
    return c
def listadder(input1,input2):
    input1length = len(input1)
    input2length = len(input2)

    shortestlength = min(input1length,input2length)

    longerinput = max(input1,input2)
    longerlength = max(input1length,input2length)

    x = list(map(addlist, input1, input2))
    x.extend(longerinput[shortestlength:longerlength])
    return x
