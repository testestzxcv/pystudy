# 문제3. 파이썬 경로명 s = '/usr/local/bin/python' 에서 각각의 디렉토리 경로명을 분리하여 출력하세요.
import string
s = '/usr/local/bin/python'
s = s.split('/')
del s[0]

for i in s:
    print("'"+i+"'", end="")
    if i == 'python':
        break
    print(",",end="")

print()

print("'",end="")
for i in s:
    if i == 'python':
        print("', '"+i+"'",end="")
        break
    print("/"+i,end="")