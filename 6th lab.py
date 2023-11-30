def towerofhanoii(n,source,destination,auxillary):
    if n==1:
        print("move disk 1 from source",source,"to destination",destination)
        return
    towerofhanoii(n-1,source,auxillary,destination)
    print("move disk",n,"from source",source,"to destination",destination)
    towerofhanoii(n-1,auxillary,destination,source)
n=4
towerofhanoii(n,'a','b','c')
