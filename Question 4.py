def solution1(list):
    variables_repeated=[]
    for i in range(len(list)):
        for j in range(i+1,len(list)):
            if list[i]==list[j]:
                variables_repeated.append(list[i])
    print(variables_repeated)
    
def solution2(list):
    uniqueList = []
    duplicateList = []
    for i in list:
        if i not in uniqueList:
            uniqueList.append(i)
        elif i not in duplicateList:
            duplicateList.append(i)
    print(duplicateList)

#took reference from geek for geeks for solution2