#PIG LATIN
#if worrd  starts with vowel the add 'ay' end of the word
#if word start not with vowel then reverse the word and then add 'ay' to that word

def pig_latin(word):
    first_latter=word[0]
    if first_latter in 'aeiou':
        pig_word= word+'ay'
    else:
        pig_word = word[::-1]+'ay'
    return pig_word

print (pig_latin("humen"))
