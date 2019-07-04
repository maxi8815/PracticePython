pos  = -1


def search(lista, num):
    lower = 0
    upper = len(lista)-1

    while lower <= upper:
        mid = (lower+upper)//2

        if lista[mid] == num:
            globals()['pos']=mid
            return True
        else:
            if lista[mid] < num:
                lower = mid
            else:
                upper = mid


lista = [15,16,39,41,90]
num=15

if search(lista,num): print ("found at" ,pos+1)
else: print("not found")
