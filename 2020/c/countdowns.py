def solve(n, k, seq):
    prev = None
    in_seq = False
    cnt = 0
    for sc in seq.split():
        c = int(sc)
        if in_seq:
            if c != prev - 1:
                in_seq = False
            elif c == 1:
                in_seq = False
                cnt += 1
        if c == k:
            in_seq = True

        prev = c

    return cnt


if __name__ == "__main__":
    t = int(input())  # read number of tests
    for t_i in range(1, t + 1):
        ns, ks = input().split()
        print("Case #{}: {}".format(t_i, solve(int(ns), int(ks), input())))
