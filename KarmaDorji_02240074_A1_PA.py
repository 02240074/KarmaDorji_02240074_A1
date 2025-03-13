print("Select a function (1-5) : ")
print("1. Calculate the sum of prime numbers")
print("2. Convert length units")
print("3. Count consonants in string")
print("4. Find min and max numbers")
print("5. Check for palindrome")
print("0. Exit program")

choice = int(input("Enter your choice : "))

def prime_checker(n):
    if n < 2:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

def sum_of_primes():
    start = int(input("Enter the starting number : "))
    end = int(input("Enter the ending number : "))

    sum = 0

    for i in range(start, end+1):
        if prime_checker(i):
            sum += i    
    print(f"Sum of prime number : {sum}")

def convert_length_units():
    choice = input("Enter the unit you want to convert ('M' for meters to feet, 'F' for feet to meters) : ")

    length = float(input("Enter the length : "))

    if choice == 'M':
        m_calc = length * 3.281
        print(f"{length} meters - {round(m_calc, 2)} feet.")
    elif choice == 'F':
        f_calc = length / 3.281
        print(f"{length} feet - {round(f_calc, 2)} meters.")
    else:
        print("Invalid choice.")

def count_consonants():
    string = input("Enter the string : ")
    count = 0
    consonants = "bcdfghjklmnpqrstvwxyz"

    for char in string:
        if char.lower() in consonants:
            count += 1
    print(f"Number of consonants : {count}")

def find_min_max():
    n = int(input("Enter the number of elements : "))
    numbers = []

    for i in range(n):
        num = int(input(f"Enter the number {i+1} : "))
        numbers.append(num)
    
    print(f"Min number : {min(numbers)}")
    print(f"Max number : {max(numbers)}")

def check_palindrome():
    string = input("Enter the string : ")

    if string == string[::-1]:
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")

if choice == 1:
    sum_of_primes()
elif choice == 2:
    convert_length_units()
elif choice == 3:
    count_consonants()
elif choice == 4:
    find_min_max()
elif choice == 5:
    check_palindrome()
elif choice == 0:
    exit()
else:
    print("Invalid choice.")