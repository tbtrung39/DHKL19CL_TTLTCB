def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            if i not in factors:
                factors.append(i)
    if n > 1:
        if n not in factors:
            factors.append(n)
    return factors


def main():
    with open('f_in.dat','r') as f:
        lines = f.read().strip().splitlines()
    nums = []
    for line in lines:
        line=line.strip()
        if not line:
            continue
        try:
            nums.append(int(line))
        except:
            pass
    out_lines = []
    for x in nums:
        if x <= 1:
            out_lines.append('')
        else:
            pf = prime_factors(x)
            out_lines.append(' '.join(str(p) for p in pf))
    with open('f_out.dat','w') as f:
        f.write('\n'.join(out_lines))
    print('Đã ghi f_out.dat')


if __name__ == '__main__':
    main()
