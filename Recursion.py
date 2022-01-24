def Display():
    print("using for loop")
    for i in range(4):
        print("marvellous")

def DisplayX():
    print("using while loop")
    i=0
    while(i<4):
        print("marvellous")
        i=i+1

def DisplayRecursion():
    print("marvellous")
    DisplayRecursion()      #Recursive Call

def main():     #caller
   Display()    #callie

   DisplayX()   #callie

   DisplayRecursion()
 
if __name__=="__main__":
    main()    


