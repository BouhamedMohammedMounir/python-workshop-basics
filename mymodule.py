
def ourfunc(a,b): 
    
    if len(a) != len(b): 
        print(" the lists hasn't the same length")
        
    else: 
        new_dict = dict(zip(a,b))
        return new_dict 