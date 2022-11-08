#--------R2-4-------------
class Flower:
    def __init__(self,flower_name:str,num_petals:int,flower_price:float):
        """Initialize the flower properties"""
        self.__flower_name = flower_name
        self.__num_petals = num_petals
        self.__flower_price = flower_price
        
    def setflowername(self,flower_name:str):
        if isinstance(flower_name, str):
            self.__flower_name = flower_name
        else:
            print('flower name should be string')
            
    def setnumofpetals(self,num_petals: int):
        if isinstance(num_petals, int):
            self.__num_petals = num_petals
        else:
            print('flower petals should be int')
            
    def setflowerprice(self,flower_price:float):
        if isinstance(flower_price, float):
            self.__flower_price = flower_price
        else:
            print('flower price should be float')
            
    def getflowername(self):
        return self.__flower_name            
    
    def getnumofpetals(self):
        return self.__num_petals
    
    def getflowerprice(self):
        return self.__flower_price 

if __name__ == '__main__':
    f = Flower('rose',23,'13.4')
    f.setflowername('lotus')
    f.setflowerprice(12)
    print(f.getflowername(), f.getnumofpetals(), f.getflowerprice())