# Drill 1: Valid Palindrome
# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

def is_palindrome(s):
    # Two pointer approach, O(1) space
    left, right = 0, len(s) - 1
    
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
            
        if s[left].lower() != s[right].lower():
            return False
            
        left += 1
        right -= 1
        
    return True

if __name__ == "__main__":
    print(is_palindrome("A man, a plan, a canal: Panama")) # Expected: True
