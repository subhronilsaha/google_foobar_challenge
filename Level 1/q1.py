# ---- QUESTION ----
# We need to decode a string whose lowercase alphabets are switched 
# as follows :- [a, b , ... , y ,z] = [z , y,  ... , b , a]. Other letters remain 
# exactly same.

def solution(x):

  decodedString = ''

  for i in x:
    asciiValue = ord(i)
    if i.islower():
      offset = asciiValue - 97 # Calculate offset from 'a'
      letter = chr(122 - offset) # Calculate corresponding letter from reverse
    decodedString += letter
    else:
      decodedString += i
      #print(decodedString)
  
  return decodedString

print(solution('vmxAbkgrlm'))