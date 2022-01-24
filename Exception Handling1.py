def Division(A,B):
    ans=0.0
    try:
        ans=A/B         #exception prone code
    except ZeroDivisionError:
        print("Exception occured")
    return ans

def main():
    no1=int(input("enter first number: "))
    no2=int(input("enter second number: "))
   
    ret=Division(no1,no2)
    print("Division is :",ret)

if __name__=="__main__":
    main()    



