path = "excerpt.txt"
with open(path, "r") as f:
    lst = [line.strip() for line in f if line.strip()]
    for i in lst:
        print(i,"\n")