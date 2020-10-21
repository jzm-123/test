import re
string='urn:li:member:103714977'
t=re.findall(r'\d+',string)
print(t)