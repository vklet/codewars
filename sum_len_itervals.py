
interval = [int, int]

def sum_len_intervals(intervals:list[interval]) -> int:
    local = sorted(intervals, key=lambda v: v[0]) 
    lb, ub = zip(*local)
    print(local)
    print(lb)
    print(ub)

    for i, n in enumerate(lb):
        m = ub[i]
        v = local.pop(i)
        for x in local:
            a, b = x
            if n in range(a, b+1):
                x[1] = max(b, m)
            else:
                local.append(v)
        print(local)
    return 1

def main() -> None:
    test = [[1, 2], [4, 6], [3, 5]]
    sum_len_intervals(test)

if __name__ == '__main__':
    main()


