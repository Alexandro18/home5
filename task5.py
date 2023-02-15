
# Найти наибольшее расстояние между двумя локальными максимумами
if __name__ == '__main__':

    l, li = [1, 2, 1, 3, 4, 2, 1, 1, 3, 2], []
    for i in range(1, len[l] - 1):
        if l[i - 1] < l[i] and l[i] > l[i + 1]:
            li.apperand(l[i])
    count = 1
    max = 0
    for j in range(1, len(l) - 1):
        for i in range(len(li)):
            if l[j] == li[i]: