"""

Author: Parthasarathi.R.V

"""
def main():
    
    #opens and gets the input
    fp=open("small network data.txt",'r')
    n = fp.readline()
    n = int(n)
    count=n
    network = []
    for i in range(n):
        network.append([])
    assert n>0
    while True:
        a=list(fp.readline(n))
        if a == []:
            break
        else:
            i=int(a[0])
            j=int(a[2])
            network[i].append(j)
            network[j].append(i)
    print("==================================================================")
    print("Friends Details")
    print("==================================================================")
    for i in range(count):
        print(i," : ",network[i])
    
    #creates a matrix with null value
    matrix = []
    for row in range(n):  # for each of the n rows
        matrix.append([])  # create the row and initialize as empty
        for column in range(n):
            matrix[row].append(0)  # append a 0 for each of the n columns

    #checks and replaces the value of the matrix
    i=j=0
    for s in range(count):
        for i in range(count):
            if j!=count:
                i_len=len(network[i])
                j_len=len(network[j])
                for k in range(i_len):
                    for h in range(j_len):
                        if network[i][k]== network[j][h]:
                            matrix[i][s]=matrix[i][s]+1

        j=j+1
    print("==================================================================")
    print("Mutual friends...")
    print("==================================================================")
    for i in range(count):
        print(i," : ",matrix[i])
        
    print("==================================================================")
    print("Recommendation")
    print("==================================================================")

    for i in range(count):
        for j in range(len(matrix[i])):
            if j+1!=count:
                if i!=j:
                    value=0
                    if matrix[i][j] > matrix[i][j+1]:
                        if value<matrix[i][j]:
                            value=matrix[i][j]
                            place=j
        print("Recomendation for ",i," user : ",place," user")
if __name__ == "__main__":
    main()
    input("Enter any key to exit ...")

