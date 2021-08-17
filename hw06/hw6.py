# The decimal number, 585 = 1001001001 in binary, is palindromic in both bases.
# Find the sum of all numbers, less than one million, which are palindromic in
# base 10 and base 2. (Please note that the palindromic number,
# in either base, may not include leading zeros.)
def ispalindrome(number):
    string = str(number)
    return string == string[::-1]
answer = 0
# No leading zero => младший разряд тоже не может быть нулем => число нечетное
for i in range(1, 1000000, 2):
    if ispalindrome(i) & ispalindrome(f"{i:b}"):
        answer += i
        print(i, f"{i:b}")
print(answer)
