array = [('바나나', 3), ('오렌지', 5), ('사과', 1)]

def setting(data):
    return data[1]

result = sorted(array, key=setting)
print(result)