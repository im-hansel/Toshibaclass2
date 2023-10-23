# Exception Handling-so it does not need to throw an exception

jina="python exception"

for j in jina:
    if (j!=1):
        print(j)

x=["Python" , "Exceptions","Try and except"]

try:
    for i in range(5):
        print(f"The index and elements from list is {i,x[i]}")
except:
    print("index out of range")