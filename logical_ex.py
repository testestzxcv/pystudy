# 논리합 (or) : 둘 줄 하나면 True면 True
a = 2
b = 3

print(a % 2 == 0 or b % 3 == 0)

# 논리곱 (and) : 둘 다 True여야 True
print(a > 0 and b < 0)

# 논리 부정 (not) : 논리값을 반대로 True -> False, False -> Treu
print(a > 10)   # False
print(not a > 10)   # 논리 부정
print(not(a % 2 == 0 and b % 3 == 0))   # 일괄 부정