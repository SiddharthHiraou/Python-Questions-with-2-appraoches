def solution1(str):
    words_list=str.split(" ")
    longest_index=0
    for i in range(0,len(words_list)):
      if len(words_list[i])>len(words_list[i-1]):
        new_index=longest_index
        longest_index=i
    print(words_list[new_index],words_list[longest_index])
    
    
def solution2(string):
    words = string.split()
    words.sort(key=len, reverse=True)
    print(words[:2])

#took reference from google for logic of sort