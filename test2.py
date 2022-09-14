a = int(input())
b = int(input())
c = int(input())

D = b*b - 4*a*c
x1 = (-b+pow(D, 0.5))/(2*a)
x2 = (-b-pow(D, 0.5))/(2*a)

if ( D > 0):
    print(x1,x2)
elif (D == 0):
    print(x1)
elif(D<0):
    print('Нет действительных корней')
