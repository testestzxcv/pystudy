# 문제2. 키보드로 정수 수치를 입력 받아 짝수인지 홀수 인지 판별하는 코드를 작성하세요.
try:
    a = int(input("수를 입력하세요:"))

    if a % 2== 0:
        print("짝수 입니다.")
    elif a % 2 == 1:
        print("홀수 입니다.")
    else:
        print("다시 입력하세요.")
except ValueError:
    print("숫자만 입력하세요.")

