# Enter your code here. Read input from STDIN. Print output to STDOUT
inputline=input()
#print(inputline)
(mycount,fpct)=inputline.split(" ")
mysum=0;
if(int(mycount) >= 7):
    mycount=7
for line in range(0,int(mycount)):
    inputline=input()
    #print(inputline)
    (tlist)=inputline.split(" ")
    tlist.pop(0)
    #print(tlist)
    res = [eval(i) for i in tlist]
    #print("Modified list is: ", res, max(res))
    mysum = mysum + max(res) ** 2
    #print(mysum)

print(mysum % int(fpct))
