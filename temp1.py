class Book:

    def setData(self, title, price, author):
        self.title = title
        self.price = price
        self.author = author

    def printData(self):
        print('제목 : ', self.title)
        print('가격 : ', self.price)
        print('저자 : ', self.author)

    def __init__(self,title, price, author):
        self.setData(title,price,author)
        print('책 객체를 새로 만들었어요~')
        print('무슨책을 살거예요?')

    def __del__(self):
        print("소멸됨")

    def __repr__(self):
        print("프린팅이 뭐야")
        return self.title

class Shape:
    area = 0

    def __add__(self, other):
        return self.area + other.area

    def __sub__(self, other):
        return self.area - other.area

    def __cmp__(self, other):
        if self.area < other.area:
            return -1
        elif self.area == other.area:
            return 0
        else:
            return 1