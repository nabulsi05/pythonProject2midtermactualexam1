small_list = [1, 2, 3]
print("list1:", small_list)
small_list[0] = 100
print("list2:", small_list)
#2
my_string = "yillow"
try:
    my_string[0] = "P"
except TypeError as e:
    print("Error:", e)
print("Original string:", my_string)
new_string = "P" + my_string[1:]
print("New string:", new_string)

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


    def find_bob_patterns(text):
        count = 0  # Initialize a counter for matches
        length = len(text)

        for i in range(length):
            # Check if the current slice starts with 'b' and ends with 'Bob'
            if text[i] == 'b' and text[i:].endswith('Bob'):
                count += 1  # Increment the counter for each match

        return count

