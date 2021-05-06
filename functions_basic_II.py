def countdown(a):
    if a >= 0:
        print(a)
        countdown(a-1)
    else: return
countdown(5)
def  print_and_return(a,b):
    print(a)
    return b
print(print_and_return(1,2))
def first_plus_length(a):
    x = 0
    for i in a:
        x = a[0] + len(a)
    return x
print(first_plus_length([1,2,3,4,5]))
def greaterthan2(a):
    x = []
    for i in a:
        if i > a[1]:
            x.append(i)
    if len(x) < 2:
        return False
    print(len(x))
    return x
print(greaterthan2([5,2,3,2,1,4]))
def length_and_value(a,b):
    x = []
    while len(x) <= b:
        x.append(a)
    print(x)
    return x
length_and_value(4,7)