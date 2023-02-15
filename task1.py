#Выведите все четные элементы массива

if __name__ == '__main__':
    n = int(input())
    l = [int(input()) for i in range(n)]
    for i in range(n):
        if l[i] % 2 == 0:
            print(l[i], end = ' ')



