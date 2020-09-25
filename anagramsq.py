def to_dict(s):
    ret_val = {}
    for i in range(len(s)):
        key = s[i]
        if (key in ret_val):
            ret_val[key] += 1
        else:
            ret_val[key] = 1
    return ret_val


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
    ''' 
    Create a dictionary key by taking the sum of their char to int values. 
    Handles checking if 2 strings are anagrams by producing the same key despite letter order.
    '''
    
    ret_val = 0
    for i in range(len(s)):
        ret_val += ord(s[i])
    return ret_val


def sort_to_dicts(arr):
    ret_val = {}
    for elem in arr:
        key = str_to_key(elem)
        if (key in ret_val):
            ret_val[key].append(elem)
        else:
            ret_val[key] = [elem]
    return ret_val


def drop_singles(d):
    '''
    Removes any dictionary entries with 1 member in the array
    '''
    ret_val = d.copy()
    keys = d.keys()
    for k in keys:
        arr = ret_val[k]
        if (len(arr)<2):
            ret_val.pop(k)
    return ret_val


def main():
    file = open("./p098_words.txt", "r")
    all_words = file.read()
    file.close
    all_words = all_words.replace("\"","")
    all_words = all_words.replace(" ","")
    arr = all_words.split(",")
    dicts = sort_to_dicts(arr)
    pruned = drop_singles(dicts)
    keys = pruned.keys()
    # for k in keys:


if __name__ == "__main__":
    main()