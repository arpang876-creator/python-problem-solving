count = 10

def func():
    global count
    count = count + 5
    print(count)

func()