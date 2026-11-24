def f(x):
    return -x**2 + 6*x + 9

x = 0
step = 1

print("States visited:")

while True:
    print(x, "->", f(x))

    if f(x + step) > f(x):
        x += step
    elif f(x - step) > f(x):
        x -= step
    else:
        break

print("Maximum value:", f(x))
print("Best state:", x)
