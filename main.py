import random


def is_prime(num):
    flag = False

    if num == 1:
        print(num, "is not a prime number")
    elif num > 1:
        # check for factors
        for i in range(2, num):
            if (num % i) == 0:
                # if factor is found, set flag to True
                flag = True
                # break out of loop
                break

    return not flag


def get_random_num(minNum,maxNum):
    return random.randint(minNum,maxNum) 

def get_prime_percent(minNum,maxNum,iterations):
    numOfPrimes = 0 
    numOfNotPrimes = 0
    for x in range(iterations):
        n = get_random_num(minNum,maxNum)
        num_prime = is_prime(n)
    

        if num_prime:
            numOfPrimes += 1
        else:
            numOfNotPrimes += 1

    return ((numOfPrimes/(numOfNotPrimes+numOfPrimes)) * 100)

 # user input (for max and min) print result rounded to 1 decimal place

minNum = int(input("min num"))
maxNum = int(input("max num"))
iterations = int(input("enter num of iterations"))
print (round(get_prime_percent(minNum,maxNum,iterations), 1))
