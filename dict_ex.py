# dict_ex.py

# 사전
# 순서 없고, key-value 매칭 자료형
# len(), in, not in

# 사전 만들기
d = dict()  # 빈 사전
print(d,type(d))

# 방법2 : {}를 이용하여 만들기
d = {}
print(d,type(d))

# 방법3 : key-value arg 를 이용하여 만들기
d = dict(one = 1, two = 2)
print(d,type(d))

# 방법4 : key, value 리스트들이 따로 있을때
keys = ("one", "two","three")
values = (1,2,3)

d = dict(zip(keys, values))
print(d,type(d))

# 사전의 키
print("----------Key")
# 변경 불가 자료형을 사용

d = {}
d[10] = "10"
d["baseball"] = 9
d[("kim", 10)] = "학생"

print(d, type(d))

#d[["lee",30]] = "근로자"    # TypeError

# 사전 메서드
print("---------- Methods")

d = {'basketball' : 5, 'soccer' : 11, 'baseball':9}
print(d,type(d))

# 키 목록을 가져와 보겠습니다. : keys()
print(d.keys())
# 값의 목록 : values()
print(d.values())
# 키와 값의 쌍의 목록 : items()
print(d.items())

# 값 가져오기
print(d['baseball'])
#print(d['handball'])    # KeyError
# 값 가져오기2: get
print(d.get('handball'))    # None
print(d.get('handball', "?"))   # 기본값을 ?

# 값의 삭제: del 함수
del d['soccer']
print(d)

# 사전 비우기
d.clear()
print(d)

# 사전의 순회
print("----------- 순회")

d = {'basketball' : 5, 'soccer' : 11, 'baseball':9}
print(d)
# 방법1 : 키값을 순회하면서 받아와서 내용 처리
#for key in d:
for key in d.keys():
    print(key, ":", d[key])

# 방법 2: 키와 값을 함께 받아와서 활용 : items()
for key, values in d.items():
    print("{0}:{1}".format(key,values), end=" ")
else:
    print()    
