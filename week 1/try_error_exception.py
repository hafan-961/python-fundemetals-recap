# try:
#     # Code that might raise an exception
#     result = 10 / 0 
#     print(result)
# except ZeroDivisionError:
#     # Code to run if a ZeroDivisionError occurs
#     print("Error: Cannot divide by zero.")


# def update(list):
#     list.append(10)
# nums = [1,2,3]
# update(nums)
# print(nums)


# s = (1,2,3,4,5,6)
# print(len(s))


# i = 1
# while i < 10:
#     i *= 3
#     print(i)



# for i in range(3):
#     print(i)
# else:
#     print("done")

# try:
#     print("A")
#     10/0
#     print("0")

# except:
#     print("C")
# print("D")




# nums = [0,1,2,3,4]
# result = []
# zero_count = 0
# for n in nums:
#     if n == 0:
#         zero_count += 1
#     else:
#         result.append(n)

# for i in range(zero_count):
#     result.append(0)
# print(result)



# text = "malayalam"
# left = 0 
# right  = len(text) - 1

# isPalindrome = True

# while left < right:
#     if text[left] != text[right]:
#         isPalindrome = False
#         break
#     left += 1
#     right -= 1
# if isPalindrome == True:
#     print("palindrome")
# else:
#     print("not palindrome")





# sentence = "python makes problem solving fun"
# words = sentence.split()
# longest = ""
# for i in words:
#     if len(i) > len(longest):
#         longest = i

# print(longest)



# a = [1,2,3,4,5]
# target = 9

# i = 0 
# while i < len(a):
#     need = target - i
#     if(need == i):
#         print(a[i])
#     else:
#         print("not found")
    # i

# nums = [2,7,11,15]
# target = 9
# for i in range(len(nums)):
#     for j in range(i+1,len(nums)):
#         if nums[i] + nums[j] == target:
#             print(nums[i] , nums[j])




