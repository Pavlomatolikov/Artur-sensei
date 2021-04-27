# this task implements printing of Fibonacci sequence in selected tange
# sequence definition was taken here https://ru.wikipedia.org/wiki/%D0%A7%D0%B8%D1%81%D0%BB%D0%B0_%D0%A4%D0%B8%D0%B1%D0%BE%D0%BD%D0%B0%D1%87%D1%87%D0%B8

def fibonacci(limit = int(input('Enter limit for sequence (positive or negative integer): '))):
    seq = [0,1]
    if limit > 0:
        while seq[-1] < limit:
            seq.append(seq[-1] + seq[-2])
            if seq[-1] > limit:
               seq.pop()
               break
           
    elif limit < 0:
        while seq[-1] > limit:
            seq.append(seq[-2] - seq[-1])
            if abs(seq[-1]) > abs(limit):
               seq.pop()
               break
    else:
        seq = [0]
    for i in seq:
        print(i)
fibonacci()