def solution1(str):
    answer_list=[]
    words_list=str.split(" ")
    
    for i in range(len(words_list)):
        temp_sublist=[]
        temp_sublist.append(words_list[i])
        
        for j in range(i+1,len(words_list)):
            if words_list[i][:1]==words_list[j][:1]:
                temp_sublist.append(words_list[j])
                
        answer_list.append(temp_sublist)
    
    print(answer_list)
    
def solution2(str):
    words_list = str.split()
    groups_dict={}
    for word in words_list:
        first_char = word[0].lower()
        if first_char in groups_dict:
            groups_dict[first_char].append(word)
        else:
            groups_dict[first_char] = [word]
    return list(groups_dict.values())

#took reference from real python.com for dictionary logic