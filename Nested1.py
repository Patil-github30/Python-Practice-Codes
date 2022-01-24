def outer():        #0X100
    print("Inside outer function")

    def Inner():    #0X200
        print("Inside Inner function")

    return Inner     #0X200   #inner function object return
    #return Inner()     function return hoil
    #return Inner()

def main():
  func_name= outer()    #call for outer function
  func_name()           #call for inner function

if __name__=="__main__":
    main()    


#Output-
#
#15 16 11 12 1 2 7  13 4 5