
"""
@brief Packet: a basic data structure to hold data and represent related objects
@details javascript like implementation of an object, {}, using key value pairs
"""
class Packet:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
    
    def __str__(self): # {'name': 'A', 'age': 1}
        return self.__dict__.__str__()   
    
    def __repr__(self): #this implements default behavior {'outer': <__main__.Packet object at 0x104671910>}
        return object.__repr__(self)
