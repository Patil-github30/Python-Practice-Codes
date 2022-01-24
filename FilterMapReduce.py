from functools import reduce
def CheckEven(no):
    if(no%2==0):
        return True
    else:
        return False

def Increment(no):
    return no+2

def Addition(a,b):
    return a+b                

def main():
    data=[5,7,6,8,4]

    print("original data",data)

                 # filter(function,list)
    newdata = list(filter(CheckEven,data))

    #map(function,list)
    incrementdata=list(map(Increment,newdata))
    print("data after map",incrementdata)
    
    print("Data after filter",newdata)

    #reduce(function,list)
    ret=reduce(Addition,incrementdata)
    print("reduced data is",ret)

if __name__=="__main__":
    main()     