def la_so_chan(n):
    if n % 2 == 0:
        return True
    else:
        return False
ds_chan = []
for i in range(1, 101):
    if la_so_chan(i):
        ds_chan.append(i)
print("Danh sach so chan:", ds_chan)