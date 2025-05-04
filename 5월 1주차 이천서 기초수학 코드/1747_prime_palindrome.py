def is_palindrome(n):
    s = str(n)
    return s == s[::-1]

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

n = int(input())

while True:
    if is_palindrome(n) and is_prime(n):
        print(n)
        break
    n += 1