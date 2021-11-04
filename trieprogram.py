trie = []
# Trie is a list to allow users to add and delete words.

def add(): #This is the function to add words to the trie.
    word = input("Add a word to the trie. Separate multiple words by commas.") #The words are taken as user input.
    word = word.lower() #To keep the trie consistent, all words are turned lowercase.
    SpecialCharacters = '! 1234567890@#$%^&*()=+`~[]{}\|";:/?.><*-_\'' #Special characters accidentally added by the user are removed keeping the words strings.
    for SpecialCharacters in SpecialCharacters:
        if SpecialCharacters in word:
            word = word.replace(SpecialCharacters,'')
    word = word.split(',') #Using .split the words are separated into a list.
    for words in word:
        if words == '': #For the words in the list word, empty words from the previous special character filter are removed.
            print("No special characters and numbers are allowed.")
            word.remove(words)
    for words in word:  #The third for loop, makes sure that the word does not repeat in the trie list.
        if words in trie:
            print(words + ' is already in the trie.')
            word.remove(words)
    for words in word:  #The last loop finally appends the inputted word in the trie.
            trie.append(words)
            print('You added the word ' + words)
            #Several for loops are used, because without them, the for loop stops when it removes words from word instead of continuing with the other words.

def delete(): #This is the function to delete words from the trie.
    word = input("Delete a word from the trie. Separate multiple words by commas.") #The words are taken as user input.
    word = word.lower() #The trie is all in lowercase, so all words are turned lowercase.
    SpecialCharacters = '! 1234567890@#$%^&*()=+`~[]{}\|";:/?.><*-_\'' #Special characters accidentally added by the user are removed keeping the words strings.
    for SpecialCharacters in SpecialCharacters:
        if SpecialCharacters in word:
            word = word.replace(SpecialCharacters,'')
    word = word.split(',') #
Using .split the words are separated into a list.
    for words in word: 
        if words == '': #For the words in the list word, empty words from the previous special character filter are removed.
            print("No special characters and numbers are allowed.")
            word.remove(words)
    for words in word:  #The third for loop, makes sure that the word does not repeat in the trie list.
        if words not in trie:
            print(words + ' is not in the trie.')
            word.remove(words)
    for words in word:  #The last loop finally appends the inputted word in the trie.
            trie.remove(words)
            print('You deleted the word ' + words)
            # Several for loops are used, because without them, the for loop stops when it removes words from word instead of continuing with the other words.

def search(): #This is the function to search for words in the trie.
    word = input("Enter words to search for in the trie. Separate multiple words by commas.") #The words are taken as user input.
    word = word.lower() #The trie is all in lowercase, so all words are turned lowercase.
    SpecialCharacters = '! 1234567890@#$%^&*()=+`~[]{}\|";:/?.><*-_\'' #Special characters accidentally added by the user are removed keeping the words strings.
    for SpecialCharacters in SpecialCharacters:
        if SpecialCharacters in word:
            word = word.replace(SpecialCharacters,'')
    word = word.split(',') #Using .split the words are separated into a list.
    for words in word:
        if words in trie:
            print(words + ' is in the trie.')
        else:
            print(words + ' is not in the trie.')
            # Using the for loop, each word inputted by the user is searched for in the list. The result is printed for the user.
            
 def autocomplete(): #This is the function to autocomplete for words in the trie.
    word = input("Enter a prefix.") #The words are taken as user input.
    word = word.lower() #The trie is all in lowercase, so all words are turned lowercase.
    SpecialCharacters = '! 1234567890@#$%^&*()=+`~[]{}\|";:/?.><*-_\'' #Special characters accidentally added by the user are removed keeping the words strings.
    for SpecialCharacters in SpecialCharacters:
        if SpecialCharacters in word:
            word = word.replace(SpecialCharacters,'')
    word = word.split(',') #Using .split the words are separated into a list.
    for words in word:
        for tries in trie:
            index = tries.find(words) #For each words search each input word in the trie using .find to see if the input word is in the trie word (if the index is zero)
            if index == 0:
                print(tries + ' -> prefix-' + words)
                
 def display():
    letters = [] #to hold different letters that the words in the trie can start with
    starting=[] #to hold the letters that do not have a firstword yet
    firstwords = [] #to hold different words in the trie that each start with a different letter in the letters list
    for words in trie: 
        if words[0] not in letters:
            letters.append(words[0]) #adding unique first letters 
    for letter in letters:
        for words in trie:
            if words[0] not in starting:
                starting.append(words[0]) 
                firstwords.append(words)
                trie.remove(words) #remove the words that will be displayed first from the trie
    for firstword in firstwords: #display the firstwords
        print('\n'*2)
        for char in firstword:
            print('——————' + char, end=' ')
        for addword in trie: #start displaying the other words in the trie based on the firstword 
            if (len(firstword)) >= (len(addword)):
                if firstword.find(addword) != 0: #if addword is found in firstword
                        i = 0
                        while firstword[i] == addword[i]: #if both words begin with the same letter
                            i += 1
                        print('\n')
                        print('        '*i + '\\' + addword[i], end=' ')
                        addword = addword[(i+1):]
                        for chara in addword:
                                            print('——' + chara, end=' ') #print the addword in relative to the base or firstword's position
                else:
                    if firstword[0] == addword[0]: #if addword is in firstword, extend the base firstword
                        i = 0
                        indexfirstword = len(firstword)
                        indexaddword = len(addword)
                        index = indexfirstword - indexaddword
                        firstword = firstword[-index:]
                        for chara in firstword:
                                            print('——' + chara, end=' ')
            else:
                if addword.find(firstword) != 0: #if firstword is not found in addword
                    if firstword[0] == addword[0]:
                        i = 0
                        while firstword[i] == addword[i]:
                            i += 1
                        print('\n')
                        print('        '*(i) + '\\' + addword[i], end=' ')
                        addword = addword[(i+1):]
                        for chara in addword:
                                            print('——' + chara, end=' ')
                else:
                    if firstword[0] == addword[0]:
                        i = 0
                        indexfirstword = len(firstword)
                        indexaddword = len(addword)
                        index = indexaddword - indexfirstword
                        addword = addword[-index:]
                        for chara in addword:
                                            print('——' + chara, end=' ')
