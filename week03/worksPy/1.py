#1
print("안녕하세요?")

print()
#2
print("100")
print("%d" % 100)

print()
#3
print("100 + 100")
print("%d" % (100+100))

print()
#4
print("%d / %d = %5.1f" % (100, 200, 0.5))

print()
#5
print("%d / %d = %f" % (100, 200, 0.5))

print()
#6
print("%d" % 123)
print("%5d" % 123)
print("%05d" % 123)
      
print("%f" % 123.45)
print("%7.1f" % 123.45)
print("%7.3f" % 123.45)

print("%s" % "Python")
print("%10s" % "Python")

print()
#7
print("%d %5d %05d" % (123, 123, 123))
print("{0:d} {1:5d} {2:05d}".format(123, 123, 123))

print()
#8
print("{2:d} {1:d} {0:d}".format(100, 200, 300))

print()
#9
print("\n줄바꿈\n연습")
print("탭키\t연습")
print("글자가 \"강조\"되는 효과1")
print("글자가 \'강조\'되는 효과2")
print("\\\\\\ 역슬래시 세 개 출력")
print(r"\n \t \" \\를 그대로 출력")
