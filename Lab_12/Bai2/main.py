import sys


def validate(s):
    if not s.isalpha():
        raise ValueError('Lỗi ký tự !!!')
    # consecutive checks
    for k in range(2,6):
        for i in range(len(s)-k+1):
            if all(s[i+j]==s[i] for j in range(k)):
                if k==2:
                    raise ValueError('Lỗi nhập liệu !!!')
                if k==4:
                    raise ValueError('Lỗi nhập lặp lại !!!')
                if k==5:
                    raise ValueError('Lỗi nhập trùng lặp!!!')
    return True


def main():
    s=input('Nhập chuỗi: ')
    try:
        validate(s)
    except Exception as e:
        print(e)
        return
    print('Nhập hợp lệ')

if __name__=='__main__':
    main()
