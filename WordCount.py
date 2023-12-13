user_input = str(input())

words = user_input.split()


my_dict = {}

for word in words:
    word_count = words.count(word)
    
    my_dict[word] = word_count
    
for word in words:
    print(word, my_dict.get(word))