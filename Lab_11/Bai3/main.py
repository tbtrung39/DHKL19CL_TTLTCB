def main():
    inp = 'f_in.dat'
    out = 'f_out.dat'
    with open(inp,'r') as f:
        data = f.read().strip().split()
    a = [int(x) for x in data]
    extremes = []
    n = len(a)
    for k in range(1, n-1):
        if (a[k] > a[k-1] and a[k] > a[k+1]) or (a[k] < a[k-1] and a[k] < a[k+1]):
            extremes.append(a[k])
    with open(out,'w') as f:
        f.write(str(len(extremes)) + '\n')
        if extremes:
            f.write(' '.join(str(x) for x in extremes))
    print('Đã ghi', out)


if __name__ == '__main__':
    main()
