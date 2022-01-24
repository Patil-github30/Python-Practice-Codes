def Division(A,B):      #0X00
    Ans=0.0
    Ans=A/B
    return Ans

def SmartDivision(func_name):   #func_name->0X100
    def Inner(A,B):     #0X200
        if A < B:
            A,B=B,A         #Multi variable #swapping logic
        return func_name(A,B)   #return 0X100(____,___)

    return Inner        #return 0X200

Division=SmartDivision(Division)        

def main():
    No1=0
    No2=0

    No1=int(input("enter first number: "))
    No2=int(input("enter second number: "))
    ret=Division(No1,No2)   #0X200(5,10)
    print("division is ",ret)
 
if __name__=="__main__":
    main()    


