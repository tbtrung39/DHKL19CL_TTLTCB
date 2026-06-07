def main():
    inp = 'inp.txt'
    out = 'out.dat'
    with open(inp,'r') as f:
        data = f.read().strip().split()
    nums = [int(x) for x in data]
    nums.sort()
    with open(out,'w') as f:
        f.write(' '.join(str(x) for x in nums))
    print('Đã ghi', out)


if __name__ == '__main__':
    main()
