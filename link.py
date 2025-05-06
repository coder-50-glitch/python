def macth_word(word):
    ctr=0
    lst =[]
    for i in word:
        print(len(word))
        if (len(i)>1 and i[0]== i[-1]):            
            ctr+=1
            lst.append(i)
    print("list of word having first n last character same \n",lst)
    return ctr
count = macth_word(['aba', '234', '12221', 'abbba','567'])
print("no of words having first n last character same", count)
        