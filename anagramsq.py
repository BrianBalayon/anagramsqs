def is_anagram(s1, s2):
    ''' Takes in 2 string to check if they are anagrams '''
    return True


def is_palindrome(s1, s2):
    ''' Takes in 2 string to check if they are palindromes '''
    str_len = len(s1)
    if (not str_len == len(s2)):
        return False
    for i in range(str_len):
        in_s2 = (str_len-1)-i
        s1_char = s1[i]
        s2_char = s2[in_s2]
        if (not s1_char == s2_char):
            return False
    return True
    

def str_to_key(s):
    ''' Create a dictionary key by taking the sum of their char to int values '''
    ret_val = 0
    for i in range(len(s)):
        ret_val += ord(s[i])
    return ret_val


def sort_to_dicts(arr):
    ret_val = {}
    for elem in arr:
        key = str_to_key(elem)
        print(key)
        if (key in ret_val):
            ret_val[key].append(elem)
        else:
            ret_val[key] = [elem]
    return ret_val


def main():
    file = open()


if __name__ == "__main__":
    main()