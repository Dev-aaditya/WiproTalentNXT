def ispalindrome(name):
    if name == name[::-1]:
        print("Yes it is a palindrome.")
    else:
        print("No it is not a palindrome.")


def count_the_vowels(name):
    vowels = "aeiouAEIOU"
    count = 0

    for ch in name:
        if ch in vowels:
            count += 1

    print("No of vowels:", count)


def frequency_of_letters(name):
    freq = {}

    for ch in name:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1

    print("Frequency of letters:")
    for key, value in freq.items():
        print(f"{key}-{value}", end="  ")
    print()