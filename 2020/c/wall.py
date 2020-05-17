def solve(r, c, wall):
    seqs = list(wall[0])
    for _r in range(1, r):
        for _c in range(c):
            v = wall[_r][_c]
            if v != seqs[_c][-1]:
                if v in seqs[_c]:
                    return -1
                seqs[_c] += v

    out_inv = ''
    for s in seqs:
        lss = len(set(s))
        if lss == 1:
            if s in out_inv:
                continue
            out_inv += s
        if lss < len(s):
            return -1
        out_inv = merge(out_inv, s)

    return out_inv[::-1]


def merge(a, b):
    i = 0
    j = 0
    out = ""
    while i < len(a) or j < len(b):
        if i == len(a):
            out += b[j]
            j += 1
        elif j == len(b):
            out += a[i]
            i += 1
        else:
            if a[i] in b[j]:
                out += a[i]
                i += 1
                j += 1
            elif a[i] in b:
                out += b[j]
                j += 1
            else:
                out += a[i]
                i += 1

    return out


if __name__ == "__main__":
    t = int(input())  # read number of tests
    for t_i in range(1, t + 1):
        sr, sc = input().split()
        r = int(sr)
        c = int(sc)
        wall = [input() for _ in range(r)]
        print("Case #{}: {}".format(t_i, solve(r, c, wall)))
