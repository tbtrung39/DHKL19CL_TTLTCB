def main():
    src=input('Tên tệp nguồn: ')
    dst=input('Tên tệp đích: ')
    try:
        with open(src,'r') as f, open(dst,'w') as g:
            for line in f:
                g.write(line)
    except Exception as e:
        print('Lỗi mở tệp:', e)
        return
    print('Đã ghi', dst)

if __name__=='__main__':
    main()
