wins = [1, 2, 3, 4, 5, 6, 7, 8, 123, 124, 145, 156, 157, 158, 1223125, 2128437, 2128500, 2741001, 4567687, 4567690, 4567890, 4567891, 7495938, 9314543, 9324543, 9325555, 9335555, 9345555,9345555]
my_ticket = 1
left = 0
right = len(wins)
def get_mid(left, right):
    result = (left + right) // 2
    return result
mid = get_mid(left,right)
print("before",left,right,mid)
while left != right:
    if wins[mid] > my_ticket:
        print("1",left, right)
        right = mid
        mid = get_mid(left,right)
    elif wins[mid] == my_ticket:
        print("2",left, right,"my tickets found in index", mid)
        exit()
    else:
        print("3", left, right)
        left = mid
        mid = get_mid(left,right)
