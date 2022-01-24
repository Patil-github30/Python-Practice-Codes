#overriding
class Base:
    def __init__(self):
        self.i=10
        self.j=20

    def fun(self):            
        print("base fun")  

    def gun(self):            
        print("base gun")        

class Derived(Base):
    def __init__(self):
        self.a=11
        self.b=21

    def fun(self):            
        print("derived fun")

    def sun(self):            
        print("derived sun")    

def main():
    bobj=Base()
    dobj=Derived()

    bobj.fun()      #output-base fun
    dobj.fun()      #output-derived fun

    dobj.sun()      #output-derived sun
    dobj.gun()      #output-base gun

if __name__=="__main__":
    main()    



