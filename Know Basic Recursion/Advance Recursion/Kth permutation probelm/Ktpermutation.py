# We know the fact(n) = no of permutation
# n= 4 then fact(4) = 24 permutations
# we need 17th permutation ( then k = 17-1 = 16) 0 based indexing
# n= 4 means => 1, 2, 3, 4 (1.2nd index value pick up we get this 16//6 )
# 1 + (2+3+4)/ fact(3) 3 number i.e. 6 => 0-6
# 2+ (1+3+4) => 7-11
# 3 + (1+2+4) =>12-17  = kth = 17  so first number
# 4 + (1+2+3) => 18-24
# if 3,_,_,_ we remove => 1,2,4 no in list
# again  # 16//6 = 2  , 16%6 = 4
#  1 + (2+3) => 0-3
#  2 + (3+1) =>4-7
# 3 + (1+2) => 8-12
# again 4//2 = 2 , 4%2 = 0 so now pick 2nd index
# if 3,4,_,_ we remove => 1,2 no in list
# 1 + (2) => 0-1
# 2 + (1) = 1-2
# again 0//2 = 0 , 0%2 = 0
# if 3,4,1,_ we remove => 2 no in list
# remaining number is 2 so _,_,_,_ => 3,4,1,2 = kth permutation

def kth_permutation(n,k):
    fact = 1
    number = []
    for i in range(1, n):
        fact = fact * i
        number.append(i)
    number.append(n)
    ans =''
    k = k - 1
    while True:
        ans = ans + str(number[k//fact])
        number.remove(number[k//fact])
        if len(number) == 0:
            break
        k =k%fact
        fact = fact // len(number)
    return ans

print(kth_permutation(4,17))



