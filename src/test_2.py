'''
Task	details:	csFindAddedLetter

Description:

You	are	given	two	strings,	str_1	and	str_2,	where	str_2	is	generated	by	randomly
shuffling	str_1	and	then	adding	one	letter	at	a	random position.

Write	a	function	that	returns	the	letter	that	was	added	to	str_2.

Examples:
    - csFindAddedLetter(str_1	=	"bcde",	str_2	=	"bcdef") -> "f"
    - csFindAddedLetter(str_1	=	"",	str_2	= "z") -> "z"
    - csFindAddedLetter(str_1	=	"b",	str_2	= "bb") -> "b"
    - csFindAddedLetter(str_1	=	"bf",	str_2	=	"bfb") -> "b"

Notes:
    - str_1	and	str_2	both	consist	of	only	lowercase	alpha characters.
'''

def	csFindAddedLetter(str_1,	str_2):
    for	i	in	range(0,	len(str_1)):
        # This	if	statement	returns	the	last	character.
        # Otherwise	return	str_2[-1]	would suffice.
        if	str_1[i]	!=	str_2[i]:
            return	str_2[i]
    return	str_2[-1]

# O(n)

print(csFindAddedLetter(str_1 =	"bcde",	str_2	=	"bcdef"))
print(csFindAddedLetter(str_1 =	"",	str_2	= "z"))