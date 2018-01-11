def countWords(string):
    count = 1 if len(string) > 0 else 0
    
    for s in string:
        if 65 <= ord(s) < 91:
            count += 1
            
    return count
    
print( countWords('saveTheChildren') )
print( countWords('') )
print( countWords('save') )