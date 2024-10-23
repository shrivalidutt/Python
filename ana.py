# Function to check if two strings are anagrams
def are_anagrams(s1, s2):
    # Sort both strings and compare
    return sorted(s1) == sorted(s2)


# Test cases
if __name__ == "__main__":
    str1 = "listen"
    str2 = "silent"

    if are_anagrams(str1, str2):
        print("True")
    else:
        print("False")

    str1 = "gram"
    str2 = "arm"

    if are_anagrams(str1, str2):
        print("True")
    else:
        print("False")
