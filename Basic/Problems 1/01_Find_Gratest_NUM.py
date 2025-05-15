a = int(input("Enter NUM 1: "))
b = int(input("Enter NUM 2: "))


# with if else 
if a>b:
    print(f'{a} is Grater')

elif a == b:
    print(f'{a} & {b} is Equal')

else:
    print(f'{b} is Grater')


# without if else 
print(f'a is grater than b is: {a>b}')
    