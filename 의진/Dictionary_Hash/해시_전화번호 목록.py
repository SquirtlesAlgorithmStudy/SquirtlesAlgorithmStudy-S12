def solution(phone_book): 
    phone_book.sort(key = lambda x:len(x))
    prefix = {}
    prefix[phone_book[0]] = phone_book[0]
    key_size = len(phone_book[0])
    for key in phone_book[1:len(phone_book)]:
        if key[:key_size] in prefix:
            a = prefix[key[:key_size]]
            if key[:len(a)] == a: return False 
        else: prefix[key[:key_size]] = key
    return True
print(solution(["119", "97674223", "1195524421"]))