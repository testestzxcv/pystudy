def try_f1():
    try:
        lst = [1,3,5,7,9]
        lst[5]  # IndexError
    except:
        print("Error")

# try_f1()

def try_f2():
    try:
        value = int("10a")  # ValueError
    except ValueError as e:
        print("변환할 수 없습니다.")
    except Exception as e:
        print("Exception e:",e)
        print("type e:",type(e))


# try_f2()

def try_f3():
    result = 4/0    # ZeorDivisionError

#try_f3()

def example():
    num1 = input("첫 번째 숫자를 입력해 주세요:")
    num2 = input("두 번째 숫자를 입력해 주세요:")

    try:
        num1 = int(num1)
        num2 = int(num2)
        result = num1 / num2
    except ValueError as e:
        print("정수형이 아니예요.")
    except ZeroDivisionError as e:
        print("0으로는 나눌 수 없어요.")
    except Exception as e:
        print("e:",e)
    else:   # 오류가 없을 때만 실행
        print("{} / {} = {}".format(num1,num2,result))
    finally:    # 오류 여부 상관 없이 마지막에 실행
        print("예외처리 완료")

# example()

# 특정 경우에는 일부러 예외를 발생시키기도 합니다
def beware_dog(animal):
    if animal == "dog":
        # 예외 발생
        raise RuntimeError("멍멍")
    else:
        print("어서오세요")

try:
    beware_dog("cow")
    beware_dog("cat")
    beware_dog("dog")
except RuntimeError as e:
    print(e)
    print(type(e))
    