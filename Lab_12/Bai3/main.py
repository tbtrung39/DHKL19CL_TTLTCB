import shutil


def main():
    name=input('Tên tệp cần đọc: ')
    try:
        with open(name,'r') as f:
            data=f.read()
    except Exception as e:
        print('Lỗi: không tìm thấy tệp')
        return
    with open('copy.dat','w') as out:
        out.write(data)
    print('Đã sao chép sang copy.dat')

if __name__=='__main__':
    main()
