"""
OscarGonzalez1987/python3_2020
is licensed under the
GNU General Public License v3.0
--------------------------------------
Permissions of this strong copyleft
license are conditioned on making
available complete source code of
licensed works and modifications,
which include larger works using a
licensed work, under the same license.

Copyright and license notices must
be preserved.

Contributors provide an express
grant of patent rights.
--------------------------------------
"""


import os
os.system('clear')

def bloque_1000000(saldo):
    if(saldo >= 1000000 and saldo <= 1999999):
        millon()
        salida = saldo - 1000000
    else:
        salida = saldo
    return salida

def bloque_100000(saldo):
    if(saldo == 100000):
        cien()
        mil()
        salida = saldo - 100000
    if(saldo >= 100000 and saldo <= 199999):
        rango_100(saldo)
        salida = saldo - 100000
    elif(saldo >= 200000 and saldo <= 299999):
        rango_200(saldo)
        salida = saldo - 200000
    elif(saldo >= 300000 and saldo <= 399999):
        rango_100(saldo)
        salida = saldo - 300000
    elif(saldo >= 400000 and saldo <= 499999):
        cuatrocientos()
        mil()
        salida = saldo - 400000
    elif(saldo >= 500000 and saldo <= 599999):
        quinientos()
        mil()
        salida = saldo - 500000
    elif(saldo >= 600000 and saldo <= 699999):
        seiscientos()
        mil()
        salida = saldo - 600000
    elif(saldo >= 700000 and saldo <= 799999):
        setecientos()
        mil()
        salida = saldo - 700000
    elif(saldo >= 800000 and saldo <= 899999):
        ochocientos()
        mil()
        salida = saldo - 800000
    elif(saldo >= 900000 and saldo <= 999999):
        novecientos()
        mil()
        salida = saldo - 900000         
    else:
        salida = saldo
    return salida

def bloque_10000(saldo):
    if(saldo >= 10000 and saldo <= 19999):
        diez()
        mil()
        salida = saldo - 10000
        
    if(saldo >= 20000 and saldo <= 29999):
        veinte()
        mil()
        salida = saldo - 20000
        
    if(saldo >= 30000 and saldo <= 39999):
        treinta()
        mil()
        salida = saldo - 30000
        
    if(saldo >= 40000 and saldo <= 49999):
        cuarenta()
        mil()
        salida = saldo - 40000
        
    if(saldo >= 50000 and saldo <= 59999):
        cincuenta()
        mil()
        salida = saldo - 50000
        
    if(saldo >= 60000 and saldo <= 69999):
        sesenta()
        mil()
        salida = saldo - 60000
        
    if(saldo >= 70000 and saldo <= 79999):
        setenta()
        mil()
        salida = saldo - 70000
        
    if(saldo >= 80000 and saldo <= 89999):
        ochenta()
        mil()
        salida = saldo - 80000
        
    if(saldo >= 90000 and saldo <= 99999):
        noventa()
        mil()
        salida = saldo - 90000
        
    else:
        salida = saldo
    return salida
    
    
    
    
  
def bloque_1000(saldo):   
    if(saldo >= 1000 and saldo <= 1999):
        salida = rango_1000(1000)
    else:
        salida = saldo
    return salida
    
def bloque_100(saldo):
    if(saldo >= 100 and saldo <= 199):
        salida = rango_100(saldo)
    elif(saldo >= 200 and saldo <= 299):
        salida = rango_200(saldo)
    elif(saldo >= 300 and saldo <= 399):
        salida = rango_300(saldo)
    elif(saldo >= 400 and saldo <= 499):
        salida = rango_400(saldo)
    elif(saldo >= 500 and saldo <= 599):
        salida = rango_500(saldo)
    elif(saldo >= 600 and saldo <= 699):
        salida = rango_600(saldo)
    elif(saldo >= 700 and saldo <= 799):
        salida = rango_700(saldo)
    elif(saldo >= 800 and saldo <= 899):
        salida = rango_800(saldo)
    elif(saldo >= 900 and saldo <= 999):
        salida = rango_900(saldo)
    else:
        salida = saldo
    return salida

def bloque_10(saldo):
    if(saldo == 10):
        diez()
        salida = 0
    elif(saldo == 11):
        once()
        salida = 0
    elif(saldo == 12):
        doce()
        salida = 0
    elif(saldo == 13):
        trece()
        salida = 0
    elif(saldo == 14):
        catorce()
        salida = 0
    elif(saldo == 15):
        quince()
        salida = 0
    elif(saldo == 16):
        dieciseis()
        salida = 0
    elif(saldo == 17):
        diecisiete()
        salida = 0
    elif(saldo == 18):
        dieciocho()
        salida = 0
    elif(saldo == 19):
        diecinueve()
        salida = 0
    elif(saldo == 20):
        veinte()
        salida = 0
    elif(saldo == 21):
        ventiuno()
        salida = 0
    elif(saldo == 22):
        ventidos()
        salida = 0
    elif(saldo == 23):
        ventitres()
        salida = 0        
    elif(saldo == 24):
        venticuatro()
        salida = 0        
    elif(saldo == 25):
        venticinco()
        salida = 0
    elif(saldo == 26):
        ventiseis()
        salida = 0 
    elif(saldo == 27):
        ventisiete()
        salida = 0 
    elif(saldo == 28):
        ventiocho()
        salida = 0 
    elif(saldo == 29):
        ventinueve()
        salida = 0
    elif(saldo >= 30 and saldo <= 39):
        salida = rango_30(saldo)
    elif(saldo >= 40 and saldo <= 49):
        salida = rango_40(saldo)
    elif(saldo >= 50 and saldo <= 59):
        salida = rango_50(saldo)
    elif(saldo >= 60 and saldo <= 69):
        salida = rango_60(saldo)
    elif(saldo >= 70 and saldo <= 79):
        salida = rango_70(saldo)
    elif(saldo >= 80 and saldo <= 89):
        salida = rango_80(saldo)
    elif(saldo >= 90 and saldo <= 99):
        salida = rango_90(saldo)        
    else:
        salida = saldo
    return salida
#/////////////////////////////////////////////
def bloque_0(saldo):
    if(saldo == 1):
        uno()
    if(saldo == 2):
        dos()
    if(saldo == 3):
        tres()
    if(saldo == 4):
        cuatro()
    if(saldo == 5):
        cinco()
    if(saldo == 6):
        seis()
    if(saldo == 7):
        siete()
    if(saldo == 8):
        ocho()
    if(saldo == 9):
        nueve()
    return 0
    
    
    
    
#/////////////////////////////////////////////
def rango_1000(saldo):
    if(saldo == 1000):
        mil()
    saldo -= 1000
    return saldo
    
#/////////////////////////////////////////////
def rango_100(saldo):
    if(saldo == 100):
        cien()
    elif(saldo > 100):
        ciento()
    saldo -= 100
    return saldo
    
def rango_200(saldo):
    if(saldo >= 200):
        doscientos()
    saldo -= 200
    return saldo
    
def rango_300(saldo):
    if(saldo >= 300):
        trescientos()
    saldo -= 300
    return saldo 
    
def rango_400(saldo):
    if(saldo >= 400):
        cuatrocientos()
    saldo -= 400
    return saldo 
    
def rango_500(saldo):
    if(saldo >= 500):
        quinientos()
    saldo -= 500
    return saldo
    
def rango_600(saldo):
    if(saldo >= 600):
        seiscientos()
    saldo -= 600
    return saldo 
    
def rango_700(saldo):
    if(saldo >= 700):
       setecientos()
    saldo -= 700
    return saldo
    
    
def rango_800(saldo):
    if(saldo >= 800):
        ochocientos()
    saldo -= 800
    return saldo
    
def rango_900(saldo):
    if(saldo >= 900):
        novecientos()
    saldo -= 900
    return saldo
    
#/////////////////////////////////////////////
def rango_30(saldo):
    if(saldo == 30):
        treinta()
    elif(saldo > 30):
        treinta_y()
    saldo -= 30
    return saldo

def rango_40(saldo):
    if(saldo == 40):
        cuarenta()
    elif(saldo > 40):
        cuarenta_y()
    saldo -= 40
    return saldo

def rango_50(saldo):
    if(saldo == 50):
        cincuenta()
    elif(saldo > 50):
        cincuenta_y()
    saldo -= 50
    return saldo

def rango_60(saldo):
    if(saldo == 60):
        sesenta()
    elif(saldo > 60):
        sesenta_y()
    saldo -= 60
    return saldo

def rango_70(saldo):
    if(saldo == 70):
        sesenta()
    elif(saldo > 70):
        sesenta_y()
    saldo -= 70
    return saldo

def rango_80(saldo):
    if(saldo == 80):
        ochenta()
    elif(saldo > 80):
        ochenta_y()
    saldo -= 80
    return saldo
    
def rango_90(saldo):
    if(saldo == 90):
        noventa()
    elif(saldo > 90):
        noventa_y()
    saldo -= 90
    return saldo
#/////////////////////////////////////////////
def mil():
    print("mil")
def millon():
    print("millon")
#/////////////////////////////////////////////
def cien():
    print("cien")
def doscientos():
    print("doscientos")
def trescientos():
    print("trescientos")
def cuatrocientos():
    print("cuatrocientos")
def quinientos():
    print("quinientos")
def seiscientos():
    print("seiscientos")
def setecientos():
    print("setecientos")
def ochocientos():
    print("ochocientos")
def novecientos():
    print("novecientos")
#/////////////////////////////////////////////
def ciento():
    print("ciento")
#///////////////////////////////////////////// 
def diez():
    print("diez")
def once():
    print("once")
def doce():
    print("doce")
def trece():
    print("trece")
def catorce():
    print("catorce")
def quince():
    print("quince")
def dieciseis():
    print("dieciséis")
def diecisiete():
    print("diecisiete") 
def dieciocho():
    print("dieciocho") 
def diecinueve():
    print("diecinueve") 
#/////////////////////////////////////////////
def veinte():
    print("veinte")
def ventiuno():
    print("ventiuno")
def ventidos():
    print("ventidos")
def ventitres():
    print("ventitres")
def venticuatro():
    print("venticuatro")
def venticinco():
    print("venticinco")
def ventiseis():
    print("ventiseis")
def ventisiete():
    print("ventisiete")
def ventiocho():
    print("ventiocho")
def ventinueve():
    print("ventinueve")
#/////////////////////////////////////////////	

def treinta():
    print("treinta")
def treinta_y():
    print("treinta y ")

def cuarenta():
    print("cuarenta")
def cuarenta_y():
    print("cuarenta y ")
    
def cincuenta():
    print("cincuenta")
def cincuenta_y():
    print("cincuenta y ")
    
def sesenta():
    print("sesenta")
def sesenta_y():
    print("sesenta y ")
    
def setenta():
    print("setenta")
def setenta_y():
    print("setenta y ")
    
def ochenta():
    print("ochenta")
def ochenta_y():
    print("ochenta y ")
    
def noventa():
    print("noventa")
def noventa_y():
    print("noventa y ") 
    
#/////////////////////////////////////////////
def cero():
    print("cero")
#/////////////////////////////////////////////
def uno():
    print("un")
def dos():
    print("dos")
def tres():
    print("tres")
def cuatro():
    print("cuatro")
def cinco():
    print("cinco")
def seis():
    print("seis")
def siete():
    print("siete")
def ocho():
    print("ocho")
def nueve():
    print("nueve")
#/////////////////////////////////////////////
while(True):
    os.system('clear')
    saldo = int(input("número: "))
    saldo = bloque_1000000(saldo)
    saldo = bloque_100000(saldo)
    saldo = bloque_10000(saldo)
    saldo = bloque_1000(saldo)
    saldo = bloque_100(saldo)
    saldo = bloque_10(saldo)
    saldo = bloque_0(saldo)
    pare = input()


a=input()







"""

elif(saldo > 100 && saldo <= 199):
    ciento()
    saldo -= 100
        
elif(saldo >= 200 && saldo <= 299):
    dos()
    cientos()
    saldo -= 200

elif(saldo >= 300 && saldo <= 399):
    tres()
    cientos()
    saldo -= 300

elif(saldo >= 400 && saldo <= 499):
    cuatro()
    cientos()
    saldo -= 400

elif(saldo >= 500 && saldo <= 599):
    quinientos()
    saldo -= 500

elif(saldo >= 600 && saldo <= 699):
    seis()
    cientos()
    saldo -= 600
      
elif(saldo >= 700 && saldo <= 799):
    setecientos()
    saldo -= 700
        
elif(saldo >= 800 && saldo <= 899):
    ocho()
    cientos()
    saldo -= 800
        
elif(saldo >= 900 && saldo <= 999):
    novecientos()
    saldo -= 900

else()
"""








"""
def rango_(saldo > 100 && saldo <= 199):
    ciento()
    saldo -= 100
        
elif(saldo >= 200 && saldo <= 299):
    dos()
    cientos()
    saldo -= 200

elif(saldo >= 300 && saldo <= 399):
    tres()
    cientos()
    saldo -= 300

elif(saldo >= 400 && saldo <= 499):
    cuatro()
    cientos()
    saldo -= 400

elif(saldo >= 500 && saldo <= 599):
    quinientos()
    saldo -= 500

elif(saldo >= 600 && saldo <= 699):
    seis()
    cientos()
    saldo -= 600
      
elif(saldo >= 700 && saldo <= 799):
    setecientos()
    saldo -= 700
        
elif(saldo >= 800 && saldo <= 899):
    ocho()
    cientos()
    saldo -= 800
        
elif(saldo >= 900 && saldo <= 999):
    novecientos()
    saldo -= 900

else()









analisis

uno=1
dos=2
tres=3
cuatro=4
cinco=5
seis=6
siete=7
ocho=8
nueve=9


diez=10
cien=100
mil=1000
diezmil= diez + mil
cienmil= cien + mil
millon=1000000


veinte=20
doscientos=200
dosmil= dos + mil
veintemil= veinte + mil
doscientosmil= dos + cientos + mil


treinta=30
trescientos=300
tresmil=3000
treintamil=30000
trescientosmil=300000


cuarenta=40
cuatrocientos=400
cuatromil=3000
cuarentamil=30000
cuatrocientosmil=300000


cincuenta=50
quinientos=500
cincomil=5000
cincuentamil=50000
quinientosmil=300000











constantes extraordinarias

quinientos
cientos
setecientos


"""













