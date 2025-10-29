
"""A function that: 
-checks whether a user given string is fully binary
-creats all possible patterns for the text_string length
-sums up how often all patterns are included in said string
-returns how often the substring patterns are included with some very fancy text"""

def pattern_check (text):
    #casting text into a string and defining some variables
    pattern_counter = 0
    text_string =str(text)

    #Checking for non binary string
    for i in range(len(text_string)):
        if text_string[i] not in ['0','1']:
            return print('Fehler')
    
    #creating patterns based on the lenght of the text_string
    
    pattern_list= []
    for i in range(2, len(text_string)+1,2):
        split = int(i/2)
        pattern_list.append('1'*split +'0'*split)
        pattern_list.append('0'*split +'1'*split)

    #check how often a pattern is included
    for i in pattern_list:
        pattern_counter= pattern_counter+text_string.count(i)

    return print('Es gibt ', pattern_counter, ' balancierte Substrings.')
    
#Asking for user input (doesn't matter if input is int or str) and process the input with the function above
print('Gib einen binären String ein: ', end='')
variable = input()
pattern_check(variable)