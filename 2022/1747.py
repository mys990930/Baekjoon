def is_prime(n):
    if n == prime_list[-1]: return True
    else:
        for num in range(int(len(prime_list)**0.5)):
            if n % prime_list[num] == 0:
                return False
        prime_list.append(n)
        return True

def is_palindrome(a):
    num = -1
    for i in a:
        if i == a[num]:
            num -= 1
            continue
        else: return False
    return True

def init_primes(n):
    prime_list = [2]
    if n == 1 or n == 2: return prime_list
    p = 3
    can_append = False
    while p <= n:
        for num in range(int(len(prime_list)**0.5)):
            can_append = True
            if p % prime_list[num] == 0:
                can_append = False
                break
        if can_append: prime_list.append(p)
        p += 1
    return prime_list

a = input()
n = int(a)
if n == 1: n = 2
prime_list = init_primes(n)

while True:
    if is_prime(n) and is_palindrome(a):
        print(n)
        break
    n += 1
    a = str(n)