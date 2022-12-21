s, last_s = '', []

def textEditor(op: str):
    t, w = op.split(" ") if len(op) > 1 else (op, "")
    global last_s, s
    if t == '1':
        last_s.append(s)
        s = f'{s}{w}'
    if t == '2':
        last_s.append(s)
        s = s[:len(s) - int(w)]
    if t == '3':
        if s:
            print(s[int(w)-1])
    if t == '4':
        s = last_s.pop()

if __name__ == '__main__':
    Q = int(input().strip())
    ops = list()

    for i in range(Q):
        ops.append(input().rstrip())

    for op in ops:
        textEditor(op)


