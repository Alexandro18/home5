
# Найти наибольшее расстояние между двумя локальными максимумами
if __name__ == '__main__':

    l, li = [1, 2, 1, 3, 4, 2, 1, 1, 3, 2], []
    for i in range(len(l)):
        if l[i-1] < l[i] and l[i] > l[i+1]:
            li.append(i)
    max = 0
    for i in range(1, len(li)):
        if li[i] - li[i-1] > max:
            max = li[i] - li[i-1]
    print(max)