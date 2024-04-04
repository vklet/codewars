

def green_num():
    n = 0
    while True:
        n += 1
        nsq = n**2
        if int(str(nsq)[-len(str(n)):])==n:  
            yield nsq


def get_green_number(nth:int) -> int:
    n = green_num()
    return [next(n) for _ in range(nth)][-1]


if __name__ == '__main__':
    print(get_green_number(5000))
