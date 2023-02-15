# Найти количество положительных элемнтов листа

if __name__ == '__main__':
    n = int(input())
    l = [int(input()) for i in range(n)]
    count = 0
    for i in range(n):
        if l[i] > 0:
            count += 1
    print(count)