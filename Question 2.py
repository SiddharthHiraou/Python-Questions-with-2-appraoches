def solution1(str):
    file=open(str,"r")
    data=file.readlines()
    data.sort()
    print(data[-1])
    
def solution2(str):
    file=open(str,"r")
    data=file.readlines()
    print(max(data))

#sort is faster
    