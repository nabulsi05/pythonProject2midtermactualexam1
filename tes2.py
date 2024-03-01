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

