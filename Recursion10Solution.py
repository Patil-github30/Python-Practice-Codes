i=0 
def fun():
    global i
    if(i<5):
        print(i)
        i=i+1
        fun()   #Recursive call

def main():
   fun()

if __name__=="__main__":
    main()    


#i is defined outside(globally) so inside function we have to declare it global
