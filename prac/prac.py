#16
a = int(input("a 값을 20아래의 수를 압력하세요"))
b = int(input("b 값을 20아래의 수를 압력하세요"))
 
if a < 20 and b < 20:
    print("a와 b 둘다 20보다 작은 값이군요")
    if a < b:
        print("b가 더 큰값이군요")
    else:
        print("a가 더 큰값이군요")

elif a > 20 and b > 20:
    print("a와b 모두 20보다 큰 값이군요")

else:
    print("a와b 둘중 하나는 20보다 큰 값이군요")
