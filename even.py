def even(start, n):
    L = []
    i=1
    for i in range(start,n+i):
        L.append(2*i)
    return L
    
    for i in range(start,n+i):
        L.append(3*i)
    return []

if __name__ == '__main__':
    
    start = 1
    n = int(input("Enter the any integer of your choices :- "))
    print("The integer you had given is even : ",even(start,n))
