#fibonacci 
a = int(input("Nhập số n:"))
fb = []

if a == 1 :
    fb.append(1)
elif a == 2 : 
    for i in range(a):
        fb.append(1)
else : 
    fb.append(1)
    fb.append(1)
    for i in range(a-2):
        fb.append(fb[i]+fb[i+1])
print("Dãy",a,"số fibonnaci đầu tiên:")
print(fb)