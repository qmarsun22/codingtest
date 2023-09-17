
def sequare_digits(n):
    myset = [1]
    while (n not in myset):
        print("doing n =", n)
        n =  sum( int(c) **2 for c in str(n) )
        if(n ==1):
            print("super number")
            return 
        myset.append(n)
        print(f" myset = {myset}")
        print("false")
        return
