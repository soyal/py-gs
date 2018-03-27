# 判定是否是回文

def reverse(text):
  return text[::-1]

def isPalindrome(text):
  return text == reverse(text)

userInput = input('Please enter text:')
if isPalindrome(userInput):
  print('your input is palindrome')
else:
  print('your input is not palindrome')
