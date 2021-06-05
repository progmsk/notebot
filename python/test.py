import re 

match = re.search(r'\d\d\D\d\d', r'Телефон 123-12-12') 

#print(match[0] if match else 'Not found') 
# -> 23-12 
#match = re.search(r'\d\d\D\d\d', r'Телефон 1231212')