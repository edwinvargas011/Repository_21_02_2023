from funciones import sumar
from funciones import es_primo


def test_sumar():
    assert sumar(2,3)==5;
    assert sumar(2,2)==4;
    assert sumar(1,2)==3;
    
def test_es__primo():
    assert es_primo(5)==True;
    assert es_primo(4)==False;
    assert es_primo(3)==True;
    