val=0
Sum=0
while True:
    val=raw_input("Enter Value: ")
    if val=='':
        break
    elif val.isdigit()==True:
        i=int(val)
        Sum=Sum+i
print(Sum)
