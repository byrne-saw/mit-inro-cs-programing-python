def isIN(str1, str2):
    """ Assumes str1 and str2 are both strings
        Returns True if either srt1 is in str2 or str2 in str1
            Else returns False"""  
    if str1 in str2:
        return True
    if str2 in str1:
        return True
    return False

print(isIN('hello', 'password'))
print(isIN('telephone', 'phone'))
print(isIN('neat', 'neato'))
