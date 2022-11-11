def es_bisiesto(fecha):
    if not fecha % 4 and (fecha % 100 or not fecha % 400):
        print("Es año es bisiesto")
    else: 
        print("No es año es bisiesto")


es_bisiesto(2012)
es_bisiesto(2010)
es_bisiesto(2000)
es_bisiesto(1900)
