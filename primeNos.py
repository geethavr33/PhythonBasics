def generate(l1):
   
    for num in range(2, l1):
        for i in range(2, num):
            
            if num % i == 0:
                break
        else:
            yield num
      

limit = int(input("Enter a number: "))
prime_numbers = generate(limit)
#for j in prime_numbers:
#    print(j)

for prime in prime_numbers:
    print(prime, end=" ")
        
