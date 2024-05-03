import re

string = '<option class="dropdown-item" value="Gold">Gold</option>'
color =  re.findall('value=\"(.*)\"(?!>Select)', string)
print(color)

