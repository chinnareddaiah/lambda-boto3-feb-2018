data = ['1','2ab','3','5']

x = 1

for d in data:
    try:
        y = int(d)
        x = x * y
    except Exception:
        pass

print(x)