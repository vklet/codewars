
def largest_rect(lines:list[int]):
    widths = sorted(set(lines))
    areas = []
    rects = []
    for w in widths:
        c = 0
        for i, n in enumerate(lines):
            if n >= w:
                c += 1
            elif max(lines[i:]) < w:
                 rects.append((w, c))
                 areas.append(w*c)
                 break
            else:
                c = 0
        else:
            rects.append((w, c))
            areas.append(w*c)
    
    print(rects)

    return areas

def main():
    # test = [9, 7, 5, 4, 2, 5, 6, 7, 7, 5, 7, 6, 4, 4, 3, 2]
    # test = [3, 5, 12, 4, 10]
    test = [6, 2, 5, 4, 5, 1, 6]

    print(largest_rect(test))


if __name__ == '__main__':
    main()
