#overloading
class Demo:
    def __init__(self):
        self.i=10
        self.j=20
    #function defination
    def Add(self,a):            #self lihyla lagta to tell that it is instance method
        print("inside add with one parameter")
    #overloaded function defination
    def Add(self,a,b):
        print("inside add with two parameter")

        
def main():
  obj=Demo()
  obj.Add(11)
  obj.Add(10,20)

if __name__=="__main__":
    main()    

#error is generated.Python does not support method overloading
#line 10 la call gela ki adhichi method nighun jate.tyamule overloading is not supported
