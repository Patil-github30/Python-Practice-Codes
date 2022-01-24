#avoid such coding

from functools import reduce

def main():
    data=[5,7,6,8,4]

    print("original data",data)

               
    newdata = list(filter(lambda no : (no % 2 ==0),data))

    
    incrementdata=list(map(lambda no : no+2 ,newdata))
    print("data after map",incrementdata)
    
    print("Data after filter",newdata)

    #reduce(function,list)
    ret=reduce(lambda a,b : a+b,incrementdata)
    print("reduced data is",ret)

if __name__=="__main__":
    main()     