# ---- QUESTION --
# Find XOR of all numbers to left of slash diagonal.
# For example, for start = 0, length = 3
# | 0 1 2 / |
# | 3 4 / 5 |
# | 6 / 7 8 |
# XOR = 0^1^2^3^4^6 = 2 (Soln)

# ---- CORRECT SOLUTION USING XOR REDUCTION ----
  
def xor(a, b):
    if(a % 2 == 0):
        xor_rotation = [b, 1, b + 1, 0]
    else:
        xor_rotation= [a, a ^ b, a - 1, (a - 1) ^ b]
    return xor_rotation[(b - a) % 4]

def solution(start, length):
    checksum = 0

    for i in range(0, length):
        checksum ^= xor(start + (length * i), start + (length * i) + (length - i) - 1)

    return checksum

print('Checksum:', solution(0, 3))


# ---- INITIAL WRONG SOLUTION ( PARTIALLY CORRECT ) ----

# def solution(start, length):
#     # Your code here
#     num1 = start
#     checksum = num1

#     count = 1
#     skip = 1

#     if length == 1:
#       return checksum
    
#     while(True):

#       if count < length:
#         num2 = num1 + 1
#         checksum ^= num2
#         num1 += 1
#         count += 1
#       else:
#         num1 += skip
#         checksum ^= num1
#         count = 1
#         length -= 1
#         skip += 1

#       if length == 1: # Termination condn
#         break


#     return checksum