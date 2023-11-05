import math 

def decorator(func):
    def wrapper():
        print(f" dang chay {func.__name__}...")
        func()
    return wrapper

@decorator
def giai_ptb1():

    try: 
        bien_a = float(input("Nhap a: "))
        bien_b = float(input("Nhap b: "))

    except ValueError:
        print("cac bien phai la mot so: ")

    else:
        print(f"phuong trinh cua ban la: y = {bien_a}x + {bien_b}")
        result = (bien_a*2)/bien_b

    return f"ket qua cua phuong trinh la: x = {result}"

@decorator
def giai_ptb2():
    
    try: 
        bien_a = float(input("Nhap a: "))
        bien_b = float(input("Nhap b: "))
        bien_c = float(input("Nhap c: "))
    
    except ValueError:
        print("Cac bien phai la mot so: ")

    else: 
        print(f"phuong trinh cua ban la: y = {bien_a}x^2 + {bien_b}x + {bien_c}")
        
        if bien_a + bien_b + bien_c == 0:
            result_1 = 1
            result_2 = bien_c/bien_a
            print(f"x1 = {result_1}")
            print(f"x2 = {result_2}")

        elif bien_a + bien_b - bien_c == 0:
            result_1 = -1
            result_2 = -(bien_c)/bien_a
            print(f"x1 = {result_1}")
            print(f"x2 = {result_2}")

        else:
            delta = (bien_b**2) - 4*bien_a*bien_c
            if delta > 0:
                print("phuong trinh co hai nghiem phan biet")
                print("tu giai not de")
            elif delta < 0:
                print("phuong trinh vo nghiem?")
            else:
                print("phuong trinh co nghiem kep")


@decorator
def Invalid_Input():
    pass

while True:
    match input("hay chon giai ptb1 hoac ptb2(1/2): "):
        case "1":
            giai_ptb1()
        case "2":
            giai_ptb2()
        case _:
            Invalid_Input()