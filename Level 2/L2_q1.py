# ---- QUESTION ----

# Arrange elevator version numbers in ascending order.
# Example, ["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"] => ["1.0", "1.0.2", "1.0.12", "1.1.2", "1.3.3" ]

def solution(l):

  splitList = []
  finalList = []
  s = ' '

  for i in l:
    version = list(map(int, i.split('.')))
    splitList.append(version)

  splitList = sorted(splitList)

  for i in splitList:
    s = '.'.join(map(str, i))
    finalList.append(s)

  #print(splitList) 
  return finalList

print(solution(["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"]))

print(solution(["1", "1.0", "1.0.0"]))