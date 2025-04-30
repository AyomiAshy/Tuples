# Given tuple
t = (1, 2, 3, 3, 2, 1)
# Check if the tuple is the same when reversed
if t == t[::-1]:
    print("The tuple is a palindrome.")
else:
    print("The tuple is not a palindrome.")