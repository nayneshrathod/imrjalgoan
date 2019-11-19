string = input("Enter any string: ")
if string == 'x':
    exit()
else:
    word = input("Enter word to be delete: ")
    print("Deleted word is: ",word)
    print("New String is: ")
    word_list = string.split()
    print(' '.join([i for i in word_list if i not in word]))

