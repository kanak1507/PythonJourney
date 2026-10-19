print ("Enter the number:")
n = int(input())

# Python Program to print table of a number

def printTable(n):

    for i in range (1, 11): 

        # multiples from 1 to 10
        print (n * i, end = " ")


if __name__ == "__main__":
  printTable(n)