bracket_string='((()()))'
test=[]
def brac(bracket_string):
    for a in bracket_string:
        if a=='(':
            test.append(a)
        if a==')':
            if '(' in test:
                test.remove('(')
    return len(test)

#print(brac(bracket_string))

def almost_palindromes(str1):
    str2=str1[::-1]
    cnt=0
    
    for i in range(len(str1)//2):
        if str1[i]!=str1[len(str1)-i-1]:
            cnt+=2
    if len(str1)%2!=0:
        cnt-=2

    return cnt

print(almost_palindromes('aaabbb'))

def ascii_deletion_distance(str1, str2):
    str1=sorted(str1)
    str2=sorted(str2)
    cnt=0
    if len(str1)>len(str2):
        min=str2
        max=str1
    else:
        min=str1
        max=str2
    maxTemp=max.copy()
    minTemp=min.copy()
    for x in min:
        if x in max:
            max.remove(x)
    print('max:',max)

    for x in max:
        cnt+=ord(x)

    min=minTemp
    max=maxTemp
    print('min:',min,' max:',max)
    for x in max:
        if x in min:
            min.remove(x)
    print('min:',min)

    for x in min:
        cnt+=ord(x)

    return cnt

#print(ascii_deletion_distance('cat','at'))



def four_letter_words(sentence):
    temp=sentence.split(' ')
    cnt=0
    for x in temp:
        if len(x)==4:
            cnt+=1
    return cnt

#print(four_letter_words('This sentence is fine'))