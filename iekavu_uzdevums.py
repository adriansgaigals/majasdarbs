list = []
while True:
  user_input = input("Enter a '(' or ')' character (or multiple characters): ")
  if user_input == 'stop':
    break
  for char in user_input:
    if char == '(':
      list.append(char)
    elif char == ')':
      if len(list) > 0:
        list.pop()
        continue
  if len(list) == 0:
    print('saraksts ir tukšs')
  else:
    print('sarakstā ir palikuši dati')
    print (len(list))
  
  