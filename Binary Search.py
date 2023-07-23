array = [15,27,31,46,59]
f=0
l=4
SK=27

while f<=l:
    mid=(f+l)//2

    if array[mid]<SK:
        f=mid+1

    elif array[mid]>SK:
        l=mid-1

    else:
        print("Item found at index ", mid)
        break;