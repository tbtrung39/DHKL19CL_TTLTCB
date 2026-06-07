def is_valid_username(s):
    if not s:
        return False
    for c in s:
        if not (c.isalnum()):
            return False
    return True

def main():
    company='@companyname.com'
    users=[]
    while True:
        s=input('Nhập username (enter để kết thúc): ').strip()
        if s=='':
            break
        if not is_valid_username(s):
            print('Lỗi username')
            continue
        users.append(s+company)
    print('Emails:', users)

if __name__=='__main__':
    main()
