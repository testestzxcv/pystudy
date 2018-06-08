# func_ex.py
# 함수에 관한 코드

def dummy():
    pass    # 구현은 나중에

def print_hello():
    print("Hello Python")

def times(a, b):
    return a * b

def do_nothing():
    return

# 함수의 호출
dummy() # 리턴 값이 없는 경우
print_hello()
print(times(10,10))
print(do_nothing())

# 여러 개의 값을 반환
def swap(a,b):
    return b,a

s = swap(3, 4)
print("s:",s)
s1, s2 = swap(3,4)
print("s1:",s1,",", "s2:",s2)

# 함수의 인자 전달
print("-------- args")

def func1(t):   # 가정상 t로 list 가 넘어올 것을 기대
    t[0] *= 2

a = [1,2,3]
func1(a)

print("a:",a)

# immutable 를 넘겼을 때는 오류가 발생할 것
#func1((1,2,3))  # TypeError

# 함수의 개선
def func2(t):
    if isinstance(t,list):
        t[0] *= 2
        return True
    else:
        return False
result = func2(a)
print(result, a)

result = func2((1,2,3))
print(result)

# 함수 인수는 필요한 개수만큼 만들 수 있다

# 기본값을 미리 선언해 둘 수 있다
def incr(a, step=1):    # 두 번째 인자를 넘기지 않으면 1값이 기본으로 사용된다
    return a+step

a=10
print(incr(a))  #   step은 기본값 1로 사용
print(incr(a,3))    # step 값은 3

# 가변인수
# 정해지지 않은 개수의 인수값을 받아 사용할 때 : *
def get_total(*args):
    sum = 0
    for num in args:
        sum += num
    return sum

print(get_total(1,3,5,7,9,2,4,6,8,10))

# 사전 키워드 전달: **
def f(a,b,*args,**kwd):
    print(a,b)
    print(args)
    print(kwd)

print(f(10,20)) # a, b 전달
print(f(10,20,30,40))   # a, b, args
print(f(10,20,30,40,option=1, option2=2))   # option1, option2는 키워드 인수

# 함수도 객체다
def plus(a,b):
    return a+b

def minus(a,b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

print(plus(10,20))
print(minus(30,40))

print()
def apply(a, b, *funcs):
    for func in funcs:
        #if isinstance(func, function):     # 확인
            print(func.__name__,func(a,b))

apply(1,2,plus,minus)

# 익명 함수(lambda)
def apply2(a, b, func=plus):
    return func(a, b)

print(apply2(2,3))   # func = plus
print(apply2(2,3,multiply))  # func = multiply

print(apply2(2,3,lambda a, b: a + b))
print(apply2(2,3,lambda a,b: 2* a + b))

# 람다를 이용한 정렬
# 리스트 등 시퀀스 자료형 정렬할 때 key 
strings = ["Hello","World","Python","Java"]
strings.sort()
print(strings)
strings.sort(key = lambda x: len(x))
print(strings)

