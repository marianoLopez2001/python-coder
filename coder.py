def es_bisiesto(fecha):
    isInt = True
    if isInt != isinstance(fecha, int):
        print("El dato ingresado no es correcto")
    elif not fecha % 4 and (fecha % 100 or not fecha % 400):
        print("Es año es bisiesto")
    else:
        print("No es año es bisiesto")


es_bisiesto(2012)
es_bisiesto(2010)
es_bisiesto(2000)
es_bisiesto(1900)
es_bisiesto(19.20)
es_bisiesto("asdasd")
