string = input('Введите несколько слов\n')
srt = string.split()
print(srt)
rts = ''
for i in reversed(srt):
    rts += i + " "
     
print(rts)