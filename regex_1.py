'''
regexone.com

regular expression let us search for patterns within text
'''
import re

# we can use regex just like regular search terms
my_string = "hello, how are you?"

result = re.search('ello', my_string)

# get the matching string
print(result.group())

# get the start of the match
print(result.start())
# get the end
print(result.end())
# print both
print(result.span())