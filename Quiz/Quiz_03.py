# 문제3. 파이썬 경로명 s = '/usr/local/bin/python' 에서 각각의 디렉토리 경로명을 분리하여 출력하세요.
s = '/usr/local/bin/python'
impor
print(s)

d=s.split('/')
print(d)

for x in d:
    print(x)

d = "-".join(s)
d.partition('python')

print(d)
