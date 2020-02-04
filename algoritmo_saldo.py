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

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
clear()

#/////////////////////////////////////////////
def bloque_100000(saldo):
    if(saldo >= 100000 and saldo <= 1999999):
        salida = rango_100000(saldo)
    elif(saldo >= 200000 and saldo <= 299999):
        salida = rango_200000(saldo)
    elif(saldo >= 300000 and saldo <= 399999):
        salida = rango_300000(saldo)
    elif(saldo >= 400000 and saldo <= 499999):
        salida = rango_400000(saldo)
    elif(saldo >= 500000 and saldo <= 599999):
        salida = rango_500000(saldo)
    elif(saldo >= 600000 and saldo <= 699999):
        salida = rango_600000(saldo)
    elif(saldo >= 700000 and saldo <= 799999):
        salida = rango_700000(saldo)
    elif(saldo >= 800000 and saldo <= 899999):
        salida = rango_800000(saldo)
    elif(saldo >= 900000 and saldo <= 999999):
        salida = rango_900000(saldo)
    else:
        salida = saldo
    return salida


def bloque_10000(saldo):
    if(saldo >= 10000 and saldo <= 19999):
        salida = rango_10000(saldo)
    elif(saldo >= 20000 and saldo <= 29999):
        salida = rango_20000(saldo)
    elif(saldo >= 30000 and saldo <= 39999):
        salida = rango_30000(saldo)
    elif(saldo >= 40000 and saldo <= 49999):
        salida = rango_40000(saldo)
    elif(saldo >= 50000 and saldo <= 59999):
        salida = rango_50000(saldo)
    elif(saldo >= 60000 and saldo <= 69999):
        salida = rango_60000(saldo)
    elif(saldo >= 70000 and saldo <= 79999):
        salida = rango_70000(saldo)
    elif(saldo >= 80000 and saldo <= 89999):
        salida = rango_80000(saldo)
    elif(saldo >= 90000 and saldo <= 99999):
        salida = rango_90000(saldo)
    else:
        salida = saldo
    return salida

def bloque_1000(saldo):
    if(saldo >= 1000 and saldo <= 1999):
        salida = rango_1000(saldo)
    elif(saldo >= 2000 and saldo <= 2999):
        salida = rango_2000(saldo)
    elif(saldo >= 3000 and saldo <= 3999):
        salida = rango_3000(saldo)
    elif(saldo >= 4000 and saldo <= 4999):
        salida = rango_4000(saldo)
    elif(saldo >= 5000 and saldo <= 5999):
        salida = rango_5000(saldo)
    elif(saldo >= 6000 and saldo <= 6999):
        salida = rango_6000(saldo)
    elif(saldo >= 7000 and saldo <= 7999):
        salida = rango_7000(saldo)
    elif(saldo >= 8000 and saldo <= 8999):
        salida = rango_8000(saldo)
    elif(saldo >= 9000 and saldo <= 9999):
        salida = rango_9000(saldo)
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
     
        
def rango_10000(saldo):
    if(saldo >= 10000 and saldo <= 10999):
        diez()
        mil()
        saldo -= 10000
    elif(saldo >= 11000 and saldo <= 11999):
        once()
        mil()
        saldo -= 11000
    elif(saldo >= 12000 and saldo <= 12999):
        doce()
        mil()
        saldo -= 12000
    elif(saldo >= 13000 and saldo <= 13999):
        trece()
        mil()
        saldo -= 13000
    elif(saldo >= 14000 and saldo <= 14999):
        catorce()
        mil()
        saldo -= 14000
    elif(saldo >= 15000 and saldo <= 15999):
        quince()
        mil()
        saldo -= 15000
    elif(saldo >= 16000 and saldo <= 16999):
        dieciseis()
        mil()
        saldo -= 16000
    elif(saldo >= 17000 and saldo <= 17999):
        diecisiete()
        mil()
        saldo -= 17000
    elif(saldo >= 18000 and saldo <= 18999):
        dieciocho()
        mil()
        saldo -= 18000
    elif(saldo >= 19000 and saldo <= 19999):
        diecinueve()
        mil()
        saldo -= 19000
    return saldo
        
def rango_20000(saldo):
    if(saldo >= 20000 and saldo <= 20999):
        veinte()
        mil()
        saldo -= 20000
    elif(saldo >= 21000 and saldo <= 21999):
        ventiuno()
        mil()
        saldo -= 21000
    elif(saldo >= 22000 and saldo <= 22999):
        ventidos()
        mil()
        saldo -= 22000
    elif(saldo >= 23000 and saldo <= 23999):
        ventitres()
        mil()
        saldo -= 23000
    elif(saldo >= 24000 and saldo <= 24999):
        venticuatro()
        mil()
        saldo -= 24000
    elif(saldo >= 25000 and saldo <= 25999):
        venticinco()
        mil()
        saldo -= 25000
    elif(saldo >= 26000 and saldo <= 26999):
        ventiseis()
        mil()
        saldo -= 26000
    elif(saldo >= 27000 and saldo <= 27999):
        ventisiete()
        mil()
        saldo -= 27000
    elif(saldo >= 28000 and saldo <= 28999):
        ventiocho()
        mil()
        saldo -= 28000
    elif(saldo >= 29000 and saldo <= 29999):
        ventinueve()
        mil()
        saldo -= 29000         
    return saldo        
     
        
        
def rango_30000(saldo):
    if(saldo >= 30000 and saldo <= 30999):
        bloque_10(30)
        mil()
        saldo -= 30000
    elif(saldo >= 31000 and saldo <= 31999):
        bloque_10(31)
        bloque_0(1)
        mil()
        saldo -= 31000
    elif(saldo >= 32000 and saldo <= 32999):
        bloque_10(32)
        bloque_0(2)
        mil()
        saldo -= 32000
    elif(saldo >= 33000 and saldo <= 33999):
        bloque_10(33)
        bloque_0(3)
        mil()
        saldo -= 33000
    elif(saldo >= 34000 and saldo <= 34999):
        bloque_10(34)
        bloque_0(4)
        mil()
        saldo -= 34000
    elif(saldo >= 35000 and saldo <= 35999):
        bloque_10(35)
        bloque_0(5)
        mil()
        saldo -= 35000
    elif(saldo >= 36000 and saldo <= 36999):
        bloque_10(36)
        bloque_0(6)
        mil()
        saldo -= 36000
    elif(saldo >= 37000 and saldo <= 37999):
        bloque_10(37)
        bloque_0(7)
        mil()
        saldo -= 37000
    elif(saldo >= 38000 and saldo <= 38999):
        bloque_10(38)
        bloque_0(8)
        mil()
        saldo -= 38000
    elif(saldo >= 39000 and saldo <= 39999):
        bloque_10(39)
        bloque_0(9)
        mil()
        saldo -= 39000 
    return saldo


def rango_40000(saldo):
    if(saldo >= 40000 and saldo <= 40999):
        bloque_10(40)
        mil()
        saldo -= 40000
    elif(saldo >= 41000 and saldo <= 41999):
        bloque_10(41)
        bloque_0(1)
        mil()
        saldo -= 41000
    elif(saldo >= 42000 and saldo <= 42999):
        bloque_10(42)
        bloque_0(2)
        mil()
        saldo -= 42000
    elif(saldo >= 43000 and saldo <= 43999):
        bloque_10(43)
        bloque_0(3)
        mil()
        saldo -= 43000
    elif(saldo >= 44000 and saldo <= 44999):
        bloque_10(44)
        bloque_0(4)
        mil()
        saldo -= 44000
    elif(saldo >= 45000 and saldo <= 45999):
        bloque_10(45)
        bloque_0(5)
        mil()
        saldo -= 45000
    elif(saldo >= 46000 and saldo <= 46999):
        bloque_10(46)
        bloque_0(6)
        mil()
        saldo -= 46000
    elif(saldo >= 47000 and saldo <= 47999):
        bloque_10(47)
        bloque_0(7)
        mil()
        saldo -= 47000
    elif(saldo >= 48000 and saldo <= 48999):
        bloque_10(48)
        bloque_0(8)
        mil()
        saldo -= 48000
    elif(saldo >= 49000 and saldo <= 49999):
        bloque_10(49)
        bloque_0(9)
        mil()
        saldo -= 49000 
    return saldo


def rango_50000(saldo):
    if(saldo >= 50000 and saldo <= 50999):
        bloque_10(50)
        mil()
        saldo -= 50000
    elif(saldo >= 51000 and saldo <= 51999):
        bloque_10(51)
        bloque_0(1)
        mil()
        saldo -= 51000
    elif(saldo >= 52000 and saldo <= 52999):
        bloque_10(52)
        bloque_0(2)
        mil()
        saldo -= 52000
    elif(saldo >= 53000 and saldo <= 53999):
        bloque_10(53)
        bloque_0(3)
        mil()
        saldo -= 53000
    elif(saldo >= 54000 and saldo <= 54999):
        bloque_10(54)
        bloque_0(4)
        mil()
        saldo -= 54000
    elif(saldo >= 55000 and saldo <= 55999):
        bloque_10(55)
        bloque_0(5)
        mil()
        saldo -= 55000
    elif(saldo >= 56000 and saldo <= 56999):
        bloque_10(56)
        bloque_0(6)
        mil()
        saldo -= 56000
    elif(saldo >= 57000 and saldo <= 57999):
        bloque_10(57)
        bloque_0(7)
        mil()
        saldo -= 57000
    elif(saldo >= 58000 and saldo <= 58999):
        bloque_10(58)
        bloque_0(8)
        mil()
        saldo -= 58000
    elif(saldo >= 59000 and saldo <= 59999):
        bloque_10(59)
        bloque_0(9)
        mil()
        saldo -= 59000 
    return saldo


def rango_60000(saldo):
    if(saldo >= 60000 and saldo <= 60999):
        bloque_10(60)
        mil()
        saldo -= 60000
    elif(saldo >= 61000 and saldo <= 61999):
        bloque_10(61)
        bloque_0(1)
        mil()
        saldo -= 61000
    elif(saldo >= 62000 and saldo <= 62999):
        bloque_10(62)
        bloque_0(2)
        mil()
        saldo -= 62000
    elif(saldo >= 63000 and saldo <= 63999):
        bloque_10(63)
        bloque_0(3)
        mil()
        saldo -= 63000
    elif(saldo >= 64000 and saldo <= 64999):
        bloque_10(64)
        bloque_0(4)
        mil()
        saldo -= 64000
    elif(saldo >= 65000 and saldo <= 65999):
        bloque_10(65)
        bloque_0(5)
        mil()
        saldo -= 65000
    elif(saldo >= 66000 and saldo <= 66999):
        bloque_10(66)
        bloque_0(6)
        mil()
        saldo -= 66000
    elif(saldo >= 67000 and saldo <= 67999):
        bloque_10(67)
        bloque_0(7)
        mil()
        saldo -= 67000
    elif(saldo >= 68000 and saldo <= 68999):
        bloque_10(68)
        bloque_0(8)
        mil()
        saldo -= 68000
    elif(saldo >= 69000 and saldo <= 69999):
        bloque_10(69)
        bloque_0(9)
        mil()
        saldo -= 69000 
    return saldo


def rango_70000(saldo):
    if(saldo >= 70000 and saldo <= 70999):
        bloque_10(70)
        mil()
        saldo -= 70000
    elif(saldo >= 71000 and saldo <= 71999):
        bloque_10(71)
        bloque_0(1)
        mil()
        saldo -= 71000
    elif(saldo >= 72000 and saldo <= 72999):
        bloque_10(72)
        bloque_0(2)
        mil()
        saldo -= 72000
    elif(saldo >= 73000 and saldo <= 73999):
        bloque_10(73)
        bloque_0(3)
        mil()
        saldo -= 73000
    elif(saldo >= 74000 and saldo <= 74999):
        bloque_10(74)
        bloque_0(4)
        mil()
        saldo -= 74000
    elif(saldo >= 75000 and saldo <= 75999):
        bloque_10(75)
        bloque_0(5)
        mil()
        saldo -= 75000
    elif(saldo >= 76000 and saldo <= 76999):
        bloque_10(76)
        bloque_0(6)
        mil()
        saldo -= 76000
    elif(saldo >= 77000 and saldo <= 77999):
        bloque_10(77)
        bloque_0(7)
        mil()
        saldo -= 77000
    elif(saldo >= 78000 and saldo <= 78999):
        bloque_10(78)
        bloque_0(8)
        mil()
        saldo -= 78000
    elif(saldo >= 79000 and saldo <= 79999):
        bloque_10(79)
        bloque_0(9)
        mil()
        saldo -= 79000 
    return saldo


def rango_80000(saldo):
    if(saldo >= 80000 and saldo <= 80999):
        bloque_10(80)
        mil()
        saldo -= 80000
    elif(saldo >= 81000 and saldo <= 81999):
        bloque_10(81)
        bloque_0(1)
        mil()
        saldo -= 81000
    elif(saldo >= 82000 and saldo <= 82999):
        bloque_10(82)
        bloque_0(2)
        mil()
        saldo -= 82000
    elif(saldo >= 83000 and saldo <= 83999):
        bloque_10(83)
        bloque_0(3)
        mil()
        saldo -= 83000
    elif(saldo >= 84000 and saldo <= 84999):
        bloque_10(84)
        bloque_0(4)
        mil()
        saldo -= 84000
    elif(saldo >= 85000 and saldo <= 85999):
        bloque_10(85)
        bloque_0(5)
        mil()
        saldo -= 85000
    elif(saldo >= 86000 and saldo <= 86999):
        bloque_10(86)
        bloque_0(6)
        mil()
        saldo -= 86000
    elif(saldo >= 87000 and saldo <= 87999):
        bloque_10(87)
        bloque_0(7)
        mil()
        saldo -= 87000
    elif(saldo >= 88000 and saldo <= 88999):
        bloque_10(88)
        bloque_0(8)
        mil()
        saldo -= 88000
    elif(saldo >= 89000 and saldo <= 89999):
        bloque_10(89)
        bloque_0(9)
        mil()
        saldo -= 89000 
    return saldo
    
    
    
def rango_90000(saldo):
    if(saldo >= 90000 and saldo <= 90999):
        bloque_10(90)
        mil()
        saldo -= 90000
    elif(saldo >= 91000 and saldo <= 91999):
        bloque_10(91)
        bloque_0(1)
        mil()
        saldo -= 91000
    elif(saldo >= 92000 and saldo <= 92999):
        bloque_10(92)
        bloque_0(2)
        mil()
        saldo -= 92000
    elif(saldo >= 93000 and saldo <= 93999):
        bloque_10(93)
        bloque_0(3)
        mil()
        saldo -= 93000
    elif(saldo >= 94000 and saldo <= 94999):
        bloque_10(94)
        bloque_0(4)
        mil()
        saldo -= 94000
    elif(saldo >= 95000 and saldo <= 95999):
        bloque_10(95)
        bloque_0(5)
        mil()
        saldo -= 95000
    elif(saldo >= 96000 and saldo <= 96999):
        bloque_10(96)
        bloque_0(6)
        mil()
        saldo -= 96000
    elif(saldo >= 97000 and saldo <= 97999):
        bloque_10(97)
        bloque_0(7)
        mil()
        saldo -= 97000
    elif(saldo >= 98000 and saldo <= 98999):
        bloque_10(98)
        bloque_0(8)
        mil()
        saldo -= 98000
    elif(saldo >= 99000 and saldo <= 99999):
        bloque_10(99)
        bloque_0(9)
        mil()
        saldo -= 99000 
    return saldo
    
    
    
    
    
    
    
    
    
    
#/////////////////////////////////////////////
def rango_1000(saldo):
    if(saldo == 1000):
        mil()
    elif(saldo > 1000):
        mil()
    saldo -= 1000
    return saldo
    
def rango_2000(saldo):
    if(saldo >= 2000):
        dos()
        mil()
    saldo -= 2000
    return saldo
    
def rango_3000(saldo):
    if(saldo >= 3000):
        tres()
        mil()
    saldo -= 3000
    return saldo 
    
def rango_4000(saldo):
    if(saldo >= 4000):
        cuatro()
        mil()
    saldo -= 4000
    return saldo 
    
def rango_5000(saldo):
    if(saldo >= 5000):
        cinco()
        mil()
    saldo -= 5000
    return saldo
    
def rango_6000(saldo):
    if(saldo >= 6000):
        seis()
        mil()
    saldo -= 6000
    return saldo 
    
def rango_7000(saldo):
    if(saldo >= 7000):
       siete()
       mil()
    saldo -= 7000
    return saldo
    
    
def rango_8000(saldo):
    if(saldo >= 8000):
        ocho()
        mil()
    saldo -= 8000
    return saldo
    
def rango_9000(saldo):
    if(saldo >= 9000):
        nueve()
        mil()
    saldo -= 9000
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
    clear()
    saldo = int(input("número: "))
    saldo = bloque_10000(saldo)
    saldo = bloque_1000(saldo)
    saldo = bloque_100(saldo)
    saldo = bloque_10(saldo)
    saldo = bloque_0(saldo)
    pare = input()
a=input()
