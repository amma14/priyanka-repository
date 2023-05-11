a='priya'
b='amala'
print(a,b,'very good friends')
print(a,b + ' both are duty girls')



# regular expression:regular expresssion is a sequence of characters to form a specified pattern
# regular expression used to check if the string contains specified patterns
# there are 3 types......1.match,2.findall,3.search

# 1.match:match method used to returns to match the starting word or starting character
# match method takes begining of the string only
import re
x='priyanka is very good girl in this world'
m1=re.match(r'p',x)
print(m1)

import re
y="python teaching is very good in our institute"
m2=re.match(r'python',y)
print(m2)
m2=re.match('p',y)
print(m2)
m2=re.match('p',y)
print(m2)


# search:search method used to search the given specified values in our data,and to print how many time that
# word should reated in our data



import re
p="our city is very good to compare with other cities"
p1=re.search(r'e',p)
print(p1)
print(p1.group(0))


# search:search method takes the matched string in the regular expression.....

import re
r='i am daily wake up at 5 clock in every morning,i am going to class every day'
r1=re.search('Z',r)
print(r1)






# findall:findall method used to take to print how many repeat the string ........
# findall method used to take all the matches and returns them as a list of string
# findall method used to take all the matches and returns the list of string



import re
u="ababa bsbsbm mhkkyfbb abnabbjhg yuiwbnmh"
u1=re.findall('a',u)
print(u1)




