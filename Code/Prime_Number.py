def is_prime(num):
    if num < 2:
        return False
    i = 2
    while i * i < num : 
        if num % i == 0:
            return False 
        i += 1
    return True  

print(is_prime(11))
print(is_prime(14))
print(is_prime(23))
print(is_prime(31))   

# python .\Code\Prime_Number.py