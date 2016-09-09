import string


s = input().strip()

bad_chars = set(string.punctuation + string.whitespace)
unique_letters = set(s.lower()) - bad_chars

if ''.join(sorted(unique_letters)) == string.ascii_lowercase:
    print('pangram')
else:
    print('not pangram')
