


#=============================================================================#
# REGular EXpressions #
#=====================#

import re

line = 'lala@lalala'

# delete given part from the string
line = re.sub('@', '', line)



#==========================================#
# Cut string in place of pattern occurance #
#==========================================#

line = 'lala@lalala'

# Divide string into parts. String is divided by first occurance of '@' string
line.partition('@')

# get part of the string until '@'
line.partition('@')[0]

