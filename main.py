def check_palindrome(str1):
	if str1[::-1]==str1:
		return True
	return False
str1=input()
if check_palindrome(str1)==True
	print("palindrome")
else:
	print("not palindrome")