def main():
    # read Sbd_Ph.dat -> map sbd->phach
    sbd_to_phach = {}
    with open('Sbd_Ph.dat','r') as f:
        for line in f:
            parts = line.split()
            if len(parts) >= 2:
                sbd = parts[0]
                phach = parts[1]
                sbd_to_phach[sbd] = phach
    # read Sbd_Ten.txt -> map sbd->name
    sbd_to_name = {}
    with open('Sbd_Ten.txt','r', encoding='utf-8') as f:
        for line in f:
            parts = line.strip().split(None, 1)
            if len(parts) == 2:
                sbd, name = parts
                sbd_to_name[sbd] = name
    # read Phieu_Diem.txt -> map phach->score
    phach_to_score = {}
    with open('Phieu_Diem.txt','r') as f:
        for line in f:
            parts = line.split()
            if len(parts) >= 2:
                phach = parts[0]
                try:
                    score = float(parts[1])
                except:
                    score = 0.0
                phach_to_score[phach] = score
    # assemble records: for each sbd present in sbd_to_phach
    records = []
    for sbd, phach in sbd_to_phach.items():
        name = sbd_to_name.get(sbd, '')
        score = phach_to_score.get(phach, 0.0)
        records.append((sbd, name, score))
    # sort by score desc
    records.sort(key=lambda x: x[2], reverse=True)
    # vieT Ketqua.txt
    with open('Ketqua.txt','w', encoding='utf-8') as f:
        for sbd, name, score in records:
            f.write(f"{sbd} {name} {score}\n")
    print('Đã ghi Ketqua.txt')


if __name__ == '__main__':
    main()
