def calculate_love_score(name1, name2):
    # Convert both names to lowercase to make it case-insensitive
    name1 = name1.lower()
    name2 = name2.lower()

    # Count the occurrences of letters in "TRUE"
    true_count = 0
    for letter in "true":
        true_count += name1.count(letter) + name2.count(letter)

    # Count the occurrences of letters in "LOVE"
    love_count = 0
    for letter in "love":
        love_count += name1.count(letter) + name2.count(letter)

    # Combine the results into a two-digit number
    love_score = int(f"{true_count}{love_count}")

    print(love_score)


# Call the function with hard-coded values
calculate_love_score("Kanye West", "Kim Kardashian")
