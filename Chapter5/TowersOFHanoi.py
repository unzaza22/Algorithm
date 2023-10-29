def towerOfHanoi(n, source, destination, intermediate):
    if n == 1:
        print("Move disk 1 from rod", source, "to rod", destination)
        return
    towerOfHanoi(n-1, source, intermediate, destination)
    print("Move disk", n, "from rod", source, "to rod", destination)
    towerOfHanoi(n-1, intermediate, destination, source)


towerOfHanoi(5,1,3,2)