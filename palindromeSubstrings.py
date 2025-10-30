# Robert Jerye studonid: uz67izax

#user input
print('Gib einen binären String ein: ' , end='')
variable = input()

#check if the string in binary
err_count = 0
for i in range(len(variable)):
    if variable[i] in ['1','0']:
        err_count = err_count +1

#if string is okay loop over the double for loop otherwise error messages
if err_count == len(variable):
    counter = 0
    #start at the first element and build a subspace of the string 
    for i in range(0,len(variable)):
        for j in range(4,len(variable)-i+1,2):
            #substring
            stringy =variable[i:j+i]
            #exclude all mono palindroms
            if stringy.count('1') == len(stringy): continue
            elif stringy.count('0') == len(stringy): continue
            #slice substring into first (fh) and last half and invert the last half (lhr)
            fh = stringy[:len(stringy)//2]
            lhr = stringy[len(stringy)//2:][len(stringy[len(stringy)//2:])::-1]
            #if first part and the reversed last part are identical trigger counter
            if fh == lhr: counter = counter + 1
    #output the amount of matches
    print('Es gibt', counter, 'Palindrom-Substrings.')
else : print('Fehler')
