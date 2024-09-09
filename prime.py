primes = []


for num in range(2, 11):
    
    is_prime = True
    
    
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break  
    
    
    if is_prime:
        primes.append(num)

print("Prime numbers between 1 and 10:", primes)
