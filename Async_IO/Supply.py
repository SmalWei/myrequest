
## 生成器---数据的生产者



# from time import sleep
# def countdown(n):
#     while n>0:
#         yield n
#         n -= 1
#
#
#
# def main():
#     for num in countdown(5):
#        print(f"Countdown: {num}")
#        sleep(1)
#     print("Countdown Over!")
#
# if __name__ == '__main__':
#     main()

## 生成器管道

# def fib():
#     a,b = 0,1
#     while True:
#         a,b = b ,a+b
#         yield a
#
# def even(gen):
#     for val in gen:
#         if val % 2 ==0:
#             yield val
# def main():
#     gen = even(fib())
#     for _ in range(10):
#         print(next(gen))
# if __name__ == '__main__':
#     main()


## 协程 -- 数据的消费者
from time import sleep


# 生成器 - 数据生产者
def countdown_gen(n, consumer):
    consumer.send(None)
    while n > 0:
        consumer.send(n)
        n -= 1
    consumer.send(None)


# 协程 - 数据消费者
def countdown_con():
    while True:
        n = yield
        if n:
            print(f'Countdown {n}')
            sleep(1)
        else:
            print('Countdown Over!')


def main():
    countdown_gen(5, countdown_con())


if __name__ == '__main__':
    main()