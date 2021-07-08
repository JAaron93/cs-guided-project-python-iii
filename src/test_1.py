'''
Task	details:	csTimeComplexity

Description:
Using	Big	O	notation,	what	is	the	correct	classification	of	time	complexity	forthe	function	below?
'''
# def do_lots_of_things(items):
#     last	=	len(items)	-	1
#     print(items[last])
    
#     middle	=	len(items)	/	2
#     i	=	0
#     while	i	<	middle:
#         print(items[i])
#         i	+=	1
        
#     for	num	inrange(100):
#         print(num)

'''
Task	details:	csSpaceComplexity


Description:
Using  Big	O notation, what is	the	correct	classification	of	space	complexity	forthe	function	below?
'''

# def do_a_couple_things(n):
#     my_list	=	[]
#     my_second_list	=	[0]	*	26

#     for	_ inrange(n):
#         my_list.append("lambda")
#         print(my_second_list[n	%	25])

#         return my_list

'''
Answer: 0(n)
'''



'''
Task	details:	csLongestPossible

Description:
Given	two	strings	that	include	only	lowercase	alpha	characters,	str_1	and	str_2, write	a
function	that	returns	a	new	sorted	string	that	contains	any	character(only	once)	that
appeared	in	str_1	or	str_2.

Examples:

- csLongestPossible("aabbbcccdef",	"xxyyzzz")	->	"abcdefxyz"
- csLongestPossible("abc",	"abc")	-> "abc"
'''

# def	csLongestPossible(str_1, str_2):				
#     return	''.join(sorted(''.join((dict.fromkeys((
#             ''.join(dict.fromkeys(str_1))+
#             ''.join(dict.fromkeys(str_2))))))))

# O (1)


'''
Task details:	csSortedTwoSum

Description: Given	a	sorted	array	(in	ascending	order)	of	integers	and	a	target,	write	a
function that	finds	the	two	integers	that	add	up	to the target.

Examples:
    - csSortedTwoSum([3,8,12,16],	11)	->	[0]
    - csSortedTwoSum([3,4,5], 8)	-> [0, 2]
    - csSortedTwoSum([0,1],	1)	->	[0, 1]

Notes:
    - Each	input	will	have	exactly
    - You	may	not	use	the	same	element twice
'''
def	csSortedTwoSum(numbers,	target):		
  # create an empty dictionary 'd'
  d = {}  # O(1)
  # iterate over nums using 'i' as the index.
  for i in range(len(numbers)):  # O(n)
    # set 'd' at key of 'nums' at the index of 'i' to 'i'
    d[numbers[i]] = i  # O(1)
    # iterate over nums using 'i' as the index.
    for i in range(len(numbers) - 1):   # O(n)
      # set a var 'c' to equal 'target' minus 'nums' at index of 'i'
      c = target - numbers[i]
      # check if 'v' is in 'd' and if the 'd' at the key of 'c' is not equal to 'i'
      if c in d and d[c] != i:
        # return a list ['i', 'd' at key of 'c']
        return sorted([i, d[c]])
    # return an empty list
  return []  # O(1)   

print(csSortedTwoSum([3,4,5], 8))
print(csSortedTwoSum([0,1],	1))