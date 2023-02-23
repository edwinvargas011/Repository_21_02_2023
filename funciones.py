
def sumar(x1,x2):
    return x1+x2;
    
def es_primo(x1):
    f=True if(len([True for k in range(x1,0,-1) if(x1%k)==0])==2) else False;
    return  f;