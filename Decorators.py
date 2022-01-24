def Division(A,B):
    Ans=0.0
    Ans=A/B
    return Ans

def main():
    N01=0
    No2=0

    No1=int(input("enter first number: "))
    No2=int(input("enter second number: "))

    ret=Division(No1,No2)

    print("division is ",ret)
 
if __name__=="__main__":
    main()    


