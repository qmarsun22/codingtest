import sys
if __name__ == '__main__':
    N = int(input())
    mylist=[]
    for i in range(0,N):
        inputline=input()
        if("insert" in inputline):
            (cmd,i,e)=inputline.split(" ")
            mylist.insert(int(i),int(e))
        elif ("remove" in inputline):
            (cmd,e)=inputline.split(" ")
            mylist.remove(int(e))
        elif ("append" in inputline):
            (cmd,e)=inputline.split(" ")
            mylist.append(int(e))
        elif ("print" in inputline):
            print(mylist)
        elif ("sort" in inputline):
            mylist.sort()
        elif ("pop" in inputline):
            mylist.pop()
        elif ("reverse" in inputline):
            mylist.reverse()
