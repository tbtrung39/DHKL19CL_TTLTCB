balance = 0
while True:
    s = input()
    if not s: break
    op, amt = s.split()
    balance += int(amt) if op == 'D' else -int(amt)
print(balance)