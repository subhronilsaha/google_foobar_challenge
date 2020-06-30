# ---- QUESTION ----
# Find number of salutes occuring on a corridoor.
# '<' = Soldier going left
# '<' = Soldier going left
# '-' = Empty space

def solution(s):
  
  toLeft = []
  toRight = []
  salutes = 0

  for i in range(len(s)):
    if s[i] == '<':
      toLeft.append(i+1)
    elif s[i] == '>':
      toRight.append(i+1)
  
  for i in range(len(toRight)):
    for j in range(len(toLeft)):
      if toRight[i] < toLeft[j]:
        salutes += 1

  return ('To Right:', toRight, 'To Left:', toLeft, 'Salutes:', salutes*2)

print(solution("--->-><-><-->-"))