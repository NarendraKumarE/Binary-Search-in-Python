#Binary search 
pos = -1
def search(list,n):
    l = 0
    u = len (list) -1
    while l<=u:
        mid = (l+u)//2
        if list [mid]==n:
            globals()['pos'] = mid
            return True
        else:
            if list[mid]<n:
                l = mid + 1
            else:
                l = mid - 1
    return False
list = [2,4,7,8,12,99,102]
n = 8
if search (list,n ):
    print("Found at",pos+1)
else:
    print("Not Found")