user_score = 0
simon_pattern = input()
user_pattern  = input()


i = 0
for letter in simon_pattern:
    print('letter is:',letter)
    print('user letter is:', user_pattern[i])
    if user_pattern[i] == letter:
        user_score += 1
    else:
        break
    i += 1

print('User score:', user_score)