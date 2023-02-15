# Вывести все элементы, которые больше предыдущего

if __name__ == '__main__':
    n = int(input())
    l = [int(input()) for i in range(n)]
    for i in range(1, n):
        if l[i-1] < l[i]:
            print(l[i], end =' ')