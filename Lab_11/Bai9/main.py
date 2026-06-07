def main():
    with open('PASSENGERS.IN','r') as f:
        lines = [line.strip() for line in f if line.strip()!='']
    count = int(lines[0])
    limits = []
    # next line maybe common limit? some examples include 20.5 but assume next lines are passenger data; if a line is single float treat as extra info ignore
    idx = 1
    # if second line is a single float, skip it (example shows 20.5)
    if len(lines[1].split())==1 and count+1==len(lines)-1:
        idx = 2
    weights = []
    for i in range(count):
        parts = lines[idx+i].split()
        nums = [float(x) for x in parts]
        weights.append(nums)
    totals = [sum(w) for w in weights]
    with open('WEIGHT.OUT','w') as f:
        for t in totals:
            f.write(f"{t:.2f}\n")
    canceled = []
    for i, w in enumerate(weights):
        if sum(w) > 23 or len(w) > 5:
            canceled.append(i+1)
    with open('CANCELED.OUT','w') as f:
        for c in canceled:
            f.write(str(c) + '\n')
    print('Đã ghi WEIGHT.OUT và CANCELED.OUT')

if __name__ == '__main__':
    main()
