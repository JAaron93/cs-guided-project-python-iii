'''
Task	details:	csFirstUniqueChar

Description:

Given	a	string,	write	a	function	that	returns	the	index	of	the	first	unique	(non-repeating)
character.	If	there	isn't	a	unique	(non-repeating) character, return -1.

Examples:
    - csFirstUniqueChar(input_str	=	"lambdaschool") -> 2
    - csFirstUniqueChar(input_str	=	"ilovelambdaschool") -> 0
    - csFirstUniqueChar(input_str	=	"vvv") -> -1

Notes:
    - input_str	will	only	contain	lowercase	alpha
'''


def csFirstUniqueChar(input_str):
    '''
    Usecase for enumerate.
    Enumerate allows us to access the index of an element in the hash
    '''
    lst = []
    # populates a list with the char of the string
    for index, char in enumerate(input_str):
        lst.append(char)
    # lst.count() is counting the number of char in the string.
    # when count is 1 => it has not repeated => return tindex for that value
    for index,char in enumerate(input_str):
        if lst.count(char) == 1:
            return index
    return -1    
        
# O(N^2)
        
print(csFirstUniqueChar("lambdaschool"))
