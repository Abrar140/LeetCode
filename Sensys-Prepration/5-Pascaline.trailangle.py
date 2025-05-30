output=[]
rows=5
for i  in range(rows):
    output.append([1]*(i+1))

for i in range(2, rows):
    for j in range(1, i):
        print(i,j)
        output[i][j]=output[i-1][j-1]+output[i-1][j]
print(output)
