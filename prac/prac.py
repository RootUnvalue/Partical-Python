#12
mod3 = ""
mod7 = ""

for i in range(1, 21):
    if i % 3 == 0:
        mod3 += str(i) + ", "
    elif i % 7 == 0:
        mod7 += str(i) + ", "

print(f"1 부터 20까지의 수중\n3의 배수인 : {mod3}\n7의 배수인 수: {mod7}")
        
        
