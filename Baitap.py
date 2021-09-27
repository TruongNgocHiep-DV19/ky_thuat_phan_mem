def tinhtoan(i, j):
    a = i + j
    print(a) 
    if a>0:
        print("Tong duong")
    elif a < 0:
        print("Tong am")
    elif a ==0:
        print("Tong bang khong")
    else:
        print("khong biet")

# if __name__ == "__main__":
#    i = int(input("nhap so i: "))
#    j = int(input("nhap so j: "))
#    tinhtoan(i, j)       

def not_prime(num):
    # define a flag variable , boolean type
    flag = False
    # prime numbers are greater than 1
    if num > 1:
        # check for factors
        for i in range(2, num):
            if (num % i) == 0:
                # if factor is found, set flag to True
                flag = True
                # break out of loop
                break
    return str(flag).lower()

def print_result(k):
    if k=="false":
        print("day la so nguyen to")
    else:
        print('day khong phai la so nguyen to')
if __name__== "__main__":
    i = int(input('nhap so de kiem tra:'))
    print_result(not_prime(i))