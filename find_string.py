def find_string(A: str, B: str)->bool:
    a, b = (A, B) if len(A) > len(B) else (B, A)
    max_len = len(a)
    min_len = len(b)
    start = 0
    end = max_len - (min_len - 1)

    while start <= end:
        if a[start: start+min_len] == b:
            return True
        else:
            start += 1

    return False


if __name__=='__main__':
    print('Exist') if find_string('abcdefgh', 'def') else print('Not Exist')
    print('Exist') if find_string('abcdefgh', 'dewf') else print('Not Exist')
    print('Exist') if find_string('abcdefgh', 'ef') else print('Not Exist')
    print('Exist') if find_string('abcdefgh', 'defsslllskhd') else print('Not Exist')
