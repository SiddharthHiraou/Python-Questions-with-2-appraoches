def solution1(list):
    for i in range(0,len(list)-1):
        if list[i]>42:
            continue
        else:
            del list[i]
    print(list)


def solution2(list):
    i=0
    answer_list=[]
    while(i!=len(list)):
        if list[i]>42:
            answer_list.append(list[i])
        i=i+1
    print(answer_list)