#1
a = 10
a = a + 2
print(a*2)
a = 19
print(a+3)
a = a // 2
print(a)

#2

print((2+3)*6/2 and 18.0)
#3
import datetime

a = 7
b = 2
today = datetime.datetime.today()
day_of_week = today.weekday()
month_of_year = today.month
a = a + day_of_week
b += month_of_year

print(a)
print(b)
c = a + b
print(c)
d = "xyz" * (c // 3)
print(d)
#4
def palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False
print(palindrome("5485839837501070045005400701057389385845"))
print(palindrome("6593036601359343374664733439531066303956"))
print(palindrome("7489617719749244646336564429479177169847"))
print(palindrome("8025833559061079503003059701609553385208"))
#5
def count_bob_patterns(text):
    count = 0  # Counter for the number of matches
    length = len(text)

    # Iterate through the text
    for i in range(length):
        # Check if the current position starts with 'b'
        if text[i] == 'b':
            # Check every substring starting with 'b' to see if it ends with 'Bob'
            for j in range(i + 1, length):
                if text[i:j + 1].endswith('Bob'):
                    count += 1
                    break  # Once 'Bob' is found, move to the next 'b'

    return count
#6
small_list = [1, 2, 3]
print("list1:", small_list)
small_list[0] = 100
print("list2:", small_list)
#-
my_string = "yillow"
try:
    my_string[0] = "P"
except TypeError as e:
    print("Error:", e)
print("Original string:", my_string)
new_string = "P" + my_string[1:]
print("New string:", new_string)
# 7
import random
random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(1, 100))
a = [num * 2 for num in random_numbers if num % 2 == 0]
print(a)
#8
def is_valid_url(url):
    # Check if the URL starts with 'http://' or 'https://'
    if url.startswith('http://') or url.startswith('https://'):
        return True
    # If any of the conditions aren't met, it's not considered a valid URL
    return False
url = "https://www.nytimes.com/games/wordle/index.html"
if is_valid_url(url):
    print("this is a valid URl")
else:
    print(" this Url is no valid")
#9
def days_since_birthday(birthday):
    birth_year = int(birthday.split('-')[2])
    current_year = 2023
    full_years = current_year - birth_year - 1
    days_passed = full_years * 365
    return days_passed
birthday = "15-04-2005"
print(f"Days passed since your birthday: {days_since_birthday(birthday)}")
