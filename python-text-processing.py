


#=============================================================================#
# REGular EXpressions #
#=====================#

import re

line = 'lala@lalala'

# delete given part from the string
line = re.sub('@', '', line)


#=================#
# String trimming #
#=================#

# get first 2 signs of the string    
"lalala"[:2]


#===========================================#
# Cut string in place of pattern occurrence #
#===========================================#

line = 'lala@lalala'

# Divide string into parts. String is divided by first occurrence of '@' string
line.partition('@')

# get part of the string until '@'
line.partition('@')[0]


#====================================#
# Check if string contains substring #
#====================================#

'one' in 'one two three'


'one' in 'one two three' in 'one two three four'


#=======================#
# string transformation #
#=======================#

# transform all letters to lowercase
'Lala@'.lower()
