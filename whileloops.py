#While loops material and examples

####>>> num = 2
#>>> while num < 100:
#        num = num * 2
#        print(num)


#4
#8
#16
#32
#64
#128

def up_to_vowel(word):
    '''(str)-> str
    Prints the characters of the str word up to the first vowel of word.

    >>>p_to_vowel('xyz')
    x
    y
    z
    >>>p_to_vowel('babc')
    b
    >>>p_to_vowel('bbcabc')
    b
    b
    c
    '''

    i=0
    while i<len(word) and not (word[i] in 'aeiouAEIOU'):
        print(word[i])
        i=i+1
    



def get_answer(prompt):
    ''' (str) -> str

    Use prompt to ask the user for a "yes" or "no"
    answer and continue asking until the user gives
    a valid response. Return the answer.
    '''

    answer = input(prompt)

    while not (answer == 'yes' or answer == 'no'):
        answer = input(prompt)

    return answer


        
def up_to_vowel(s):
    ''' (str) -> str

    Return a substring of s from index 0 up to but
    not including the first vowel in s.

    >>> up_to_vowel('hello')
    'h'
    >>> up_to_vowel('there')
    'th'
    >>> up_to_vowel('cs')
    'cs'
    '''

    before_vowel = ''
    i = 0

    while i < len(s) and not (s[i] in 'aeiouAEIOU'):
        before_vowel = before_vowel + s[i]
        i = i + 1

    return before_vowel
