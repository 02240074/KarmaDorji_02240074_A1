while True:
    print("""Select a function (1-5) : 
        1. Calculate the sum of prime numbers
        2. Convert length units
        3. Count consonants in string
        4. Find min and max numbers
        5. Check for palindrome
        6. Word counter
        0. Exit program""")

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

    def word_counter(filename, words):
        # Open the file and read its content
        with open(filename, 'r') as file:
            text = file.read().lower()  # Convert text to lowercase for case-insensitive search

        # Split the text into individual words
        word_list = text.split()

        # Initialize a dictionary to store the word counts
        word_count = {word: 0 for word in words}

        # Count the occurrences of each word in the text
        for word in word_list:
            # Remove punctuation from the word (optional)
            cleaned_word = word.strip(".,!?\"'()[]{}:;")
            if cleaned_word in word_count:
                word_count[cleaned_word] += 1

        return word_count

    # Menu-driven logic (updated for option 6)
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
    elif choice == 6:
        filename = input("Enter the filename: ")  # Changed from URL to filename
        words_to_find = ['and', 'the', 'was']
        try:
            result = word_counter(filename, words_to_find)
            for word in result:
                print(f"{word} : {result[word]}")
        except FileNotFoundError:
            print("Error: File not found. Please check the filename.")
    elif choice == 0:
        exit()
    else:
        print("Invalid choice.")

    exit_code = input("Do you want to use this again?(Y if yes and N if Not):").strip().upper()
    if exit_code !="Y":
      print("BYE!")
        
