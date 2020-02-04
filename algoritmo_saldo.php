<?php

/*
  OscarGonzalez1987/python3_2020
  is licensed under the
  GNU General Public License v3.0
  --------------------------------------
  Permissions of this strong copyleft
  license are conditioned on making
  available complete source code of
  licensed works && modifications,
  which include larger works using a
  licensed work, under the same license.

  Copyright && license notices must
  be preserved.

  Contributors provide an express
  grant of patent rights.
  --------------------------------------
 */

function bloque_100000($saldo) {
    if ($saldo >= 100000 && $saldo <= 1999999) {
        $salida = rango_100000($saldo);
    } elseif ($saldo >= 200000 && $saldo <= 299999) {
        $salida = rango_200000($saldo);
    } elseif ($saldo >= 300000 && $saldo <= 399999) {
        $salida = rango_300000($saldo);
    } elseif ($saldo >= 400000 && $saldo <= 499999) {
        $salida = rango_400000($saldo);
    } elseif ($saldo >= 500000 && $saldo <= 599999) {
        $salida = rango_500000($saldo);
    } elseif ($saldo >= 600000 && $saldo <= 699999) {
        $salida = rango_600000($saldo);
    } elseif ($saldo >= 700000 && $saldo <= 799999) {
        $salida = rango_700000($saldo);
    } elseif ($saldo >= 800000 && $saldo <= 899999) {
        $salida = rango_800000($saldo);
    } elseif ($saldo >= 900000 && $saldo <= 999999) {
        $salida = rango_900000($saldo);
    } else {
        $salida = $saldo;
    }
    return $salida;
}

function bloque_10000($saldo) {
    if ($saldo >= 10000 && $saldo <= 19999) {
        $salida = rango_10000($saldo);
    } elseif ($saldo >= 20000 && $saldo <= 29999) {
        $salida = rango_20000($saldo);
    } elseif ($saldo >= 30000 && $saldo <= 39999) {
        $salida = rango_30000($saldo);
    } elseif ($saldo >= 40000 && $saldo <= 49999) {
        $salida = rango_40000($saldo);
    } elseif ($saldo >= 50000 && $saldo <= 59999) {
        $salida = rango_50000($saldo);
    } elseif ($saldo >= 60000 && $saldo <= 69999) {
        $salida = rango_60000($saldo);
    } elseif ($saldo >= 70000 && $saldo <= 79999) {
        $salida = rango_70000($saldo);
    } elseif ($saldo >= 80000 && $saldo <= 89999) {
        $salida = rango_80000($saldo);
    } elseif ($saldo >= 90000 && $saldo <= 99999) {
        $salida = rango_90000($saldo);
    } else {
        $salida['numero'] = $saldo;
    }
    return $salida;
}

function bloque_1000($saldo) {
    if ($saldo >= 1000 && $saldo <= 1999) {
        $salida = rango_1000($saldo);
    } elseif ($saldo >= 2000 && $saldo <= 2999) {
        $salida = rango_2000($saldo);
    } elseif ($saldo >= 3000 && $saldo <= 3999) {
        $salida = rango_3000($saldo);
    } elseif ($saldo >= 4000 && $saldo <= 4999) {
        $salida = rango_4000($saldo);
    } elseif ($saldo >= 5000 && $saldo <= 5999) {
        $salida = rango_5000($saldo);
    } elseif ($saldo >= 6000 && $saldo <= 6999) {
        $salida = rango_6000($saldo);
    } elseif ($saldo >= 7000 && $saldo <= 7999) {
        $salida = rango_7000($saldo);
    } elseif ($saldo >= 8000 && $saldo <= 8999) {
        $salida = rango_8000($saldo);
    } elseif ($saldo >= 9000 && $saldo <= 9999) {
        $salida = rango_9000($saldo);
    } else {
        $salida = $saldo;
    }
    return $salida;
}

function bloque_100($saldo) {
    if ($saldo >= 100 && $saldo <= 199) {
        $salida = rango_100($saldo);
    } elseif ($saldo >= 200 && $saldo <= 299) {
        $salida = rango_200($saldo);
    } elseif ($saldo >= 300 && $saldo <= 399) {
        $salida = rango_300($saldo);
    } elseif ($saldo >= 400 && $saldo <= 499) {
        $salida = rango_400($saldo);
    } elseif ($saldo >= 500 && $saldo <= 599) {
        $salida = rango_500($saldo);
    } elseif ($saldo >= 600 && $saldo <= 699) {
        $salida = rango_600($saldo);
    } elseif ($saldo >= 700 && $saldo <= 799) {
        $salida = rango_700($saldo);
    } elseif ($saldo >= 800 && $saldo <= 899) {
        $salida = rango_800($saldo);
    } elseif ($saldo >= 900 && $saldo <= 999) {
        $salida = rango_900($saldo);
    } else {
        $salida = $saldo;
    }
    return $salida;
}

function bloque_10($saldo) {
    if ($saldo == 10) {
        $salida['texto'] = diez();
        $salida['numero'] = 0;
    } elseif ($saldo == 11) {
        $salida['texto'] = once();
        $salida['numero'] = 0;
    } elseif ($saldo == 12) {
        $salida['texto'] = doce();
        $salida['numero'] = 0;
    } elseif ($saldo == 13) {
        $salida['texto'] = trece();
        $salida['numero'] = 0;
    } elseif ($saldo == 14) {
        $salida['texto'] = catorce();
        $salida['numero'] = 0;
    } elseif ($saldo == 15) {
        $salida['texto'] = quince();
        $salida['numero'] = 0;
    } elseif ($saldo == 16) {
        $salida['texto'] = dieciseis();
        $salida['numero'] = 0;
    } elseif ($saldo == 17) {
        $salida['texto'] = diecisiete();
        $salida['numero'] = 0;
    } elseif ($saldo == 18) {
        $salida['texto'] = dieciocho();
        $salida['numero'] = 0;
    } elseif ($saldo == 19) {
        $salida['texto'] = diecinueve();
        $salida['numero'] = 0;
    } elseif ($saldo == 20) {
        $salida['texto'] = veinte();
        $salida['numero'] = 0;
    } elseif ($saldo == 21) {
        $salida['texto'] = ventiuno();
        $salida['numero'] = 0;
    } elseif ($saldo == 22) {
        $salida['texto'] = ventidos();
        $salida['numero'] = 0;
    } elseif ($saldo == 23) {
        $salida['texto'] = ventitres();
        $salida['numero'] = 0;
    } elseif ($saldo == 24) {
        $salida['texto'] = venticuatro();
        $salida['numero'] = 0;
    } elseif ($saldo == 25) {
        $salida['texto'] = venticinco();
        $salida['numero'] = 0;
    } elseif ($saldo == 26) {
        $salida['texto'] = ventiseis();
        $salida['numero'] = 0;
    } elseif ($saldo == 27) {
        $salida['texto'] = ventisiete();
        $salida['numero'] = 0;
    } elseif ($saldo == 28) {
        $salida['texto'] = ventiocho();
        $salida['numero'] = 0;
    } elseif ($saldo == 29) {
        $salida['texto'] = ventinueve();
        $salida['numero'] = 0;
    } elseif ($saldo >= 30 && $saldo <= 39) {
        $salida['numero'] = rango_30($saldo);
    } elseif ($saldo >= 40 && $saldo <= 49) {
        $salida['numero'] = rango_40($saldo);
    } elseif ($saldo >= 50 && $saldo <= 59) {
        $salida['numero'] = rango_50($saldo);
    } elseif ($saldo >= 60 && $saldo <= 69) {
        $salida['numero'] = rango_60($saldo);
    } elseif ($saldo >= 70 && $saldo <= 79) {
        $salida['numero'] = rango_70($saldo);
    } elseif ($saldo >= 80 && $saldo <= 89) {
        $salida['numero'] = rango_80($saldo);
    } elseif ($saldo >= 90 && $saldo <= 99) {
        $salida['numero'] = rango_90($saldo);
    } else {
        $salida['texto'] = "";
        $salida['numero'] = $saldo;
    }
    return $salida;
}

#/////////////////////////////////////////////

function bloque_0($saldo) {
    if ($saldo == 1) {
        $salida['texto'] = uno();
    } elseif ($saldo == 2) {
        $salida['texto'] = dos();
    } elseif ($saldo == 3) {
        $salida['texto'] = tres();
    } elseif ($saldo == 4) {
        $salida['texto'] = cuatro();
    } elseif ($saldo == 5) {
        $salida['texto'] = cinco();
    } elseif ($saldo == 6) {
        $salida['texto'] = seis();
    } elseif ($saldo == 7) {
        $salida['texto'] = siete();
    } elseif ($saldo == 8) {
        $salida['texto'] = ocho();
    } elseif ($saldo == 9) {
        $salida['texto'] = nueve();
    } else{
        $salida['texto'] = "";
        $salida['numero'] = 0;
        
    }
    
     return $salida;
}

function rango_10000($saldo) {
    if ($saldo >= 10000 && $saldo <= 10999) {
        diez();
        mil();
        $saldo -= 10000;
    } elseif ($saldo >= 11000 && $saldo <= 11999) {
        once();
        mil();
        $saldo -= 11000;
    } elseif ($saldo >= 12000 && $saldo <= 12999) {
        doce();
        mil();
        $saldo -= 12000;
    } elseif ($saldo >= 13000 && $saldo <= 13999) {
        trece();
        mil();
        $saldo -= 13000;
    } elseif ($saldo >= 14000 && $saldo <= 14999) {
        catorce();
        mil();
        $saldo -= 14000;
    } elseif ($saldo >= 15000 && $saldo <= 15999) {
        quince();
        mil();
        $saldo -= 15000;
    } elseif ($saldo >= 16000 && $saldo <= 16999) {
        dieciseis();
        mil();
        $saldo -= 16000;
    } elseif ($saldo >= 17000 && $saldo <= 17999) {
        diecisiete();
        mil();
        $saldo -= 17000;
    } elseif ($saldo >= 18000 && $saldo <= 18999) {
        dieciocho();
        mil();
        $saldo -= 18000;
    } elseif ($saldo >= 19000 && $saldo <= 19999) {
        diecinueve();
        mil();
        $saldo -= 19000;
    }
    return $saldo;
}

function rango_20000($saldo) {
    if ($saldo >= 20000 && $saldo <= 20999) {
        veinte();
        mil();
        $saldo -= 20000;
    } elseif ($saldo >= 21000 && $saldo <= 21999) {
        ventiuno();
        mil();
        $saldo -= 21000;
    } elseif ($saldo >= 22000 && $saldo <= 22999) {
        ventidos();
        mil();
        $saldo -= 22000;
    } elseif ($saldo >= 23000 && $saldo <= 23999) {
        ventitres();
        mil();
        $saldo -= 23000;
    } elseif ($saldo >= 24000 && $saldo <= 24999) {
        venticuatro();
        mil();
        $saldo -= 24000;
    } elseif ($saldo >= 25000 && $saldo <= 25999) {
        venticinco();
        mil();
        $saldo -= 25000;
    } elseif ($saldo >= 26000 && $saldo <= 26999) {
        ventiseis();
        mil();
        $saldo -= 26000;
    } elseif ($saldo >= 27000 && $saldo <= 27999) {
        ventisiete();
        mil();
        $saldo -= 27000;
    } elseif ($saldo >= 28000 && $saldo <= 28999) {
        ventiocho();
        mil();
        $saldo -= 28000;
    } elseif ($saldo >= 29000 && $saldo <= 29999) {
        ventinueve();
        mil();
        $saldo -= 29000;
    }
    return $saldo;
}

function rango_30000($saldo) {
    if ($saldo >= 30000 && $saldo <= 30999) {
        bloque_10(30);
        mil();
        $saldo -= 30000;
    } elseif ($saldo >= 31000 && $saldo <= 31999) {
        bloque_10(31);
        bloque_0(1);
        mil();
        $saldo -= 31000;
    } elseif ($saldo >= 32000 && $saldo <= 32999) {
        bloque_10(32);
        bloque_0(2);
        mil();
        $saldo -= 32000;
    } elseif ($saldo >= 33000 && $saldo <= 33999) {
        bloque_10(33);
        bloque_0(3);
        mil();
        $saldo -= 33000;
    } elseif ($saldo >= 34000 && $saldo <= 34999) {
        bloque_10(34);
        bloque_0(4);
        mil();
        $saldo -= 34000;
    } elseif ($saldo >= 35000 && $saldo <= 35999) {
        bloque_10(35);
        bloque_0(5);
        mil();
        $saldo -= 35000;
    } elseif ($saldo >= 36000 && $saldo <= 36999) {
        bloque_10(36);
        bloque_0(6);
        mil();
        $saldo -= 36000;
    } elseif ($saldo >= 37000 && $saldo <= 37999) {
        bloque_10(37);
        bloque_0(7);
        mil();
        $saldo -= 37000;
    } elseif ($saldo >= 38000 && $saldo <= 38999) {
        bloque_10(38);
        bloque_0(8);
        mil();
        $saldo -= 38000;
    } elseif ($saldo >= 39000 && $saldo <= 39999) {
        bloque_10(39);
        bloque_0(9);
        mil();
        $saldo -= 39000;
    }
    return $saldo;
}

function rango_40000($saldo) {
    if ($saldo >= 40000 && $saldo <= 40999) {
        bloque_10(40);
        mil();
        $saldo -= 40000;
    } elseif ($saldo >= 41000 && $saldo <= 41999) {
        bloque_10(41);
        bloque_0(1);
        mil();
        $saldo -= 41000;
    } elseif ($saldo >= 42000 && $saldo <= 42999) {
        bloque_10(42);
        bloque_0(2);
        mil();
        $saldo -= 42000;
    } elseif ($saldo >= 43000 && $saldo <= 43999) {
        bloque_10(43);
        bloque_0(3);
        mil();
        $saldo -= 43000;
    } elseif ($saldo >= 44000 && $saldo <= 44999) {
        bloque_10(44);
        bloque_0(4);
        mil();
        $saldo -= 44000;
    } elseif ($saldo >= 45000 && $saldo <= 45999) {
        bloque_10(45);
        bloque_0(5);
        mil();
        $saldo -= 45000;
    } elseif ($saldo >= 46000 && $saldo <= 46999) {
        bloque_10(46);
        bloque_0(6);
        mil();
        $saldo -= 46000;
    } elseif ($saldo >= 47000 && $saldo <= 47999) {
        bloque_10(47);
        bloque_0(7);
        mil();
        $saldo -= 47000;
    } elseif ($saldo >= 48000 && $saldo <= 48999) {
        bloque_10(48);
        bloque_0(8);
        mil();
        $saldo -= 48000;
    } elseif ($saldo >= 49000 && $saldo <= 49999) {
        bloque_10(49);
        bloque_0(9);
        mil();
        $saldo -= 49000;
    }
    return $saldo;
}

function rango_50000($saldo) {
    if ($saldo >= 50000 && $saldo <= 50999) {
        bloque_10(50);
        mil();
        $saldo -= 50000;
    } elseif ($saldo >= 51000 && $saldo <= 51999) {
        bloque_10(51);
        bloque_0(1);
        mil();
        $saldo -= 51000;
    } elseif ($saldo >= 52000 && $saldo <= 52999) {
        bloque_10(52);
        bloque_0(2);
        mil();
        $saldo -= 52000;
    } elseif ($saldo >= 53000 && $saldo <= 53999) {
        bloque_10(53);
        bloque_0(3);
        mil();
        $saldo -= 53000;
    } elseif ($saldo >= 54000 && $saldo <= 54999) {
        bloque_10(54);
        bloque_0(4);
        mil();
        $saldo -= 54000;
    } elseif ($saldo >= 55000 && $saldo <= 55999) {
        bloque_10(55);
        bloque_0(5);
        mil();
        $saldo -= 55000;
    } elseif ($saldo >= 56000 && $saldo <= 56999) {
        bloque_10(56);
        bloque_0(6);
        mil();
        $saldo -= 56000;
    } elseif ($saldo >= 57000 && $saldo <= 57999) {
        bloque_10(57);
        bloque_0(7);
        mil();
        $saldo -= 57000;
    } elseif ($saldo >= 58000 && $saldo <= 58999) {
        bloque_10(58);
        bloque_0(8);
        mil();
        $saldo -= 58000;
    } elseif ($saldo >= 59000 && $saldo <= 59999) {
        bloque_10(59);
        bloque_0(9);
        mil();
        $saldo -= 59000;
    }
    return $saldo;
}

function rango_60000($saldo) {
    if ($saldo >= 60000 && $saldo <= 60999) {
        bloque_10(60);
        mil();
        $saldo -= 60000;
    } elseif ($saldo >= 61000 && $saldo <= 61999) {
        bloque_10(61);
        bloque_0(1);
        mil();
        $saldo -= 61000;
    } elseif ($saldo >= 62000 && $saldo <= 62999) {
        bloque_10(62);
        bloque_0(2);
        mil();
        $saldo -= 62000;
    } elseif ($saldo >= 63000 && $saldo <= 63999) {
        bloque_10(63);
        bloque_0(3);
        mil();
        $saldo -= 63000;
    } elseif ($saldo >= 64000 && $saldo <= 64999) {
        bloque_10(64);
        bloque_0(4);
        mil();
        $saldo -= 64000;
    } elseif ($saldo >= 65000 && $saldo <= 65999) {
        bloque_10(65);
        bloque_0(5);
        mil();
        $saldo -= 65000;
    } elseif ($saldo >= 66000 && $saldo <= 66999) {
        bloque_10(66);
        bloque_0(6);
        mil();
        $saldo -= 66000;
    } elseif ($saldo >= 67000 && $saldo <= 67999) {
        bloque_10(67);
        bloque_0(7);
        mil();
        $saldo -= 67000;
    } elseif ($saldo >= 68000 && $saldo <= 68999) {
        bloque_10(68);
        bloque_0(8);
        mil();
        $saldo -= 68000;
    } elseif ($saldo >= 69000 && $saldo <= 69999) {
        bloque_10(69);
        bloque_0(9);
        mil();
        $saldo -= 69000;
    }
    return $saldo;
}

function rango_70000($saldo) {
    if ($saldo >= 70000 && $saldo <= 70999) {
        bloque_10(70);
        mil();
        $saldo -= 70000;
    } elseif ($saldo >= 71000 && $saldo <= 71999) {
        bloque_10(71);
        bloque_0(1);
        mil();
        $saldo -= 71000;
    } elseif ($saldo >= 72000 && $saldo <= 72999) {
        bloque_10(72);
        bloque_0(2);
        mil();
        $saldo -= 72000;
    } elseif ($saldo >= 73000 && $saldo <= 73999) {
        bloque_10(73);
        bloque_0(3);
        mil();
        $saldo -= 73000;
    } elseif ($saldo >= 74000 && $saldo <= 74999) {
        bloque_10(74);
        bloque_0(4);
        mil();
        $saldo -= 74000;
    } elseif ($saldo >= 75000 && $saldo <= 75999) {
        bloque_10(75);
        bloque_0(5);
        mil();
        $saldo -= 75000;
    } elseif ($saldo >= 76000 && $saldo <= 76999) {
        bloque_10(76);
        bloque_0(6);
        mil();
        $saldo -= 76000;
    } elseif ($saldo >= 77000 && $saldo <= 77999) {
        bloque_10(77);
        bloque_0(7);
        mil();
        $saldo -= 77000;
    } elseif ($saldo >= 78000 && $saldo <= 78999) {
        bloque_10(78);
        bloque_0(8);
        mil();
        $saldo -= 78000;
    } elseif ($saldo >= 79000 && $saldo <= 79999) {
        bloque_10(79);
        bloque_0(9);
        mil();
        $saldo -= 79000;
    }
    return $saldo;
}

function rango_80000($saldo) {
    if ($saldo >= 80000 && $saldo <= 80999) {
        bloque_10(80);
        mil();
        $saldo -= 80000;
    } elseif ($saldo >= 81000 && $saldo <= 81999) {
        bloque_10(81);
        bloque_0(1);
        mil();
        $saldo -= 81000;
    } elseif ($saldo >= 82000 && $saldo <= 82999) {
        bloque_10(82);
        bloque_0(2);
        mil();
        $saldo -= 82000;
    } elseif ($saldo >= 83000 && $saldo <= 83999) {
        bloque_10(83);
        bloque_0(3);
        mil();
        $saldo -= 83000;
    } elseif ($saldo >= 84000 && $saldo <= 84999) {
        bloque_10(84);
        bloque_0(4);
        mil();
        $saldo -= 84000;
    } elseif ($saldo >= 85000 && $saldo <= 85999) {
        bloque_10(85);
        bloque_0(5);
        mil();
        $saldo -= 85000;
    } elseif ($saldo >= 86000 && $saldo <= 86999) {
        bloque_10(86);
        bloque_0(6);
        mil();
        $saldo -= 86000;
    } elseif ($saldo >= 87000 && $saldo <= 87999) {
        bloque_10(87);
        bloque_0(7);
        mil();
        $saldo -= 87000;
    } elseif ($saldo >= 88000 && $saldo <= 88999) {
        bloque_10(88);
        bloque_0(8);
        mil();
        $saldo -= 88000;
    } elseif ($saldo >= 89000 && $saldo <= 89999) {
        bloque_10(89);
        bloque_0(9);
        mil();
        $saldo -= 89000;
    }
    return $saldo;
}

function rango_90000($saldo) {
    if ($saldo >= 90000 && $saldo <= 90999) {
        bloque_10(90);
        mil();
        $saldo -= 90000;
    } elseif ($saldo >= 91000 && $saldo <= 91999) {
        bloque_10(91);
        bloque_0(1);
        mil();
        $saldo -= 91000;
    } elseif ($saldo >= 92000 && $saldo <= 92999) {
        bloque_10(92);
        bloque_0(2);
        mil();
        $saldo -= 92000;
    } elseif ($saldo >= 93000 && $saldo <= 93999) {
        bloque_10(93);
        bloque_0(3);
        mil();
        $saldo -= 93000;
    } elseif ($saldo >= 94000 && $saldo <= 94999) {
        bloque_10(94);
        bloque_0(4);
        mil();
        $saldo -= 94000;
    } elseif ($saldo >= 95000 && $saldo <= 95999) {
        bloque_10(95);
        bloque_0(5);
        mil();
        $saldo -= 95000;
    } elseif ($saldo >= 96000 && $saldo <= 96999) {
        bloque_10(96);
        bloque_0(6);
        mil();
        $saldo -= 96000;
    } elseif ($saldo >= 97000 && $saldo <= 97999) {
        bloque_10(97);
        bloque_0(7);
        mil();
        $saldo -= 97000;
    } elseif ($saldo >= 98000 && $saldo <= 98999) {
        bloque_10(98);
        bloque_0(8);
        mil();
        $saldo -= 98000;
    } elseif ($saldo >= 99000 && $saldo <= 99999) {
        bloque_10(99);
        bloque_0(9);
        mil();
        $saldo -= 99000;
    }
    return $saldo;
}

#/////////////////////////////////////////////

function rango_1000($saldo) {
    if ($saldo == 1000) {
        mil();
    } elseif ($saldo > 1000) {
        mil();
        $saldo -= 1000;
        return $saldo;
    }
}

function rango_2000($saldo) {
    if ($saldo >= 2000) {
        dos();
        mil();
        $saldo -= 2000;
        return $saldo;
    }
}

function rango_3000($saldo) {
    if ($saldo >= 3000) {
        tres();
        mil();
        $saldo -= 3000;
        return $saldo;
    }
}

function rango_4000($saldo) {
    if ($saldo >= 4000) {
        cuatro();
        mil();
        $saldo -= 4000;
        return $saldo;
    }
}

function rango_5000($saldo) {
    if ($saldo >= 5000) {
        cinco();
        mil();
        $saldo -= 5000;
        return $saldo;
    }
}

function rango_6000($saldo) {
    if ($saldo >= 6000) {
        seis();
        mil();
        $saldo -= 6000;
        return $saldo;
    }
}

function rango_7000($saldo) {
    if ($saldo >= 7000) {
        siete();
        mil();
        $saldo -= 7000;
        return $saldo;
    }
}

function rango_8000($saldo) {
    if ($saldo >= 8000) {
        ocho();
        mil();
        $saldo -= 8000;
        return $saldo;
    }
}

function rango_9000($saldo) {
    if ($saldo >= 9000) {
        nueve();
        mil();
        $saldo -= 9000;
        return $saldo;
    }
}

#/////////////////////////////////////////////

function rango_100($saldo) {
    if ($saldo == 100) {
        cien();
    } elseif ($saldo > 100) {
        ciento();
        $saldo -= 100;
        return $saldo;
    }
}

function rango_200($saldo) {
    if ($saldo >= 200) {
        doscientos();
        $saldo -= 200;
        return $saldo;
    }
}

function rango_300($saldo) {
    if ($saldo >= 300) {
        trescientos();
        $saldo -= 300;
        return $saldo;
    }
}

function rango_400($saldo) {
    if ($saldo >= 400) {
        cuatrocientos();
        $saldo -= 400;
        return $saldo;
    }
}

function rango_500($saldo) {
    if ($saldo >= 500) {
        quinientos();
        $saldo -= 500;
        return $saldo;
    }
}

function rango_600($saldo) {
    if ($saldo >= 600) {
        seiscientos();
        $saldo -= 600;
        return $saldo;
    }
}

function rango_700($saldo) {
    if ($saldo >= 700) {
        setecientos();
        $saldo -= 700;
        return $saldo;
    }
}

function rango_800($saldo) {
    if ($saldo >= 800) {
        ochocientos();
        $saldo -= 800;
        return $saldo;
    }
}

function rango_900($saldo) {
    if ($saldo >= 900) {
        novecientos();
        $saldo -= 900;
        return $saldo;
    }
}

#/////////////////////////////////////////////

function rango_30($saldo) {
    if ($saldo == 30) {
        treinta();
    } elseif ($saldo > 30) {
        treinta_y();
        $saldo -= 30;
        return $saldo;
    }
}

function rango_40($saldo) {
    if ($saldo == 40) {
        cuarenta();
    } elseif ($saldo > 40) {
        cuarenta_y();
        $saldo -= 40;
        return $saldo;
    }
}

function rango_50($saldo) {
    if ($saldo == 50) {
        cincuenta();
    } elseif ($saldo > 50) {
        cincuenta_y();
        $saldo -= 50;
        return $saldo;
    }
}

function rango_60($saldo) {
    if ($saldo == 60) {
        sesenta();
    } elseif ($saldo > 60) {
        sesenta_y();
        $saldo -= 60;
        return $saldo;
    }
}

function rango_70($saldo) {
    if ($saldo == 70) {
        sesenta();
    } elseif ($saldo > 70) {
        sesenta_y();
        $saldo -= 70;
        return $saldo;
    }
}

function rango_80($saldo) {
    if ($saldo == 80) {
        ochenta();
    } elseif ($saldo > 80) {
        ochenta_y();
        $saldo -= 80;
        return $saldo;
    }
}

function rango_90($saldo) {
    if ($saldo == 90) {
        noventa();
    } elseif ($saldo > 90) {
        noventa_y();
        $saldo -= 90;
        return $saldo;
    }
}

#/////////////////////////////////////////////

function mil() {
    $texto = "mil ";
    return $texto;
}

function millon() {
    $texto = "millon ";
    return $texto;
}

function cien() {
    $texto = "cien ";
    return $texto;
}

function doscientos() {
    $texto = "doscientos ";
    return $texto;
}

function trescientos() {
    $texto = "trescientos ";
    return $texto;
}

function cuatrocientos() {
    $texto = "cuatrocientos ";
    return $texto;
}

function quinientos() {
    $texto = "quinientos ";
    return $texto;
}

function seiscientos() {
    $texto = "seiscientos ";
    return $texto;
}

function setecientos() {
    $texto = "setecientos ";
    return $texto;
}

function ochocientos() {
    $texto = "ochocientos ";
    return $texto;
}

function novecientos() {
    $texto = "novecientos ";
#/////////////////////////////////////////////
    return $texto;
}

function ciento() {
    $texto = "ciento ";
#/////////////////////////////////////////////
    return $texto;
}

function diez() {
    $texto = "diez ";
    return $texto;
}

function once() {
    $texto = "once ";
    return $texto;
}

function doce() {
    $texto = "doce ";
    return $texto;
}

function trece() {
    $texto = "trece ";
    return $texto;
}

function catorce() {
    $texto = "catorce ";
    return $texto;
}

function quince() {
    $texto = "quince ";
    return $texto;
}

function dieciseis() {
    $texto = "dieciseis ";
    return $texto;
}

function diecisiete() {
    $texto = "diecisiete ";
    return $texto;
}

function dieciocho() {
    $texto = "dieciocho ";
    return $texto;
}

function diecinueve() {
    $texto = "diecinueve ";
#/////////////////////////////////////////////
    return $texto;
}

function veinte() {
    $texto = "veinte ";
    return $texto;
}

function ventiuno() {
    $texto = "ventiun ";
    return $texto;
}

function ventidos() {
    $texto = "ventidos ";
    return $texto;
}

function ventitres() {
    $texto = "ventitres ";
    return $texto;
}

function venticuatro() {
    $texto = "venticuatro ";
    return $texto;
}

function venticinco() {
    $texto = "venticinco ";
    return $texto;
}

function ventiseis() {
    $texto = "ventiseis ";
    return $texto;
}

function ventisiete() {
    $texto = "ventisiete ";
    return $texto;
}

function ventiocho() {
    $texto = "ventiocho ";
    return $texto;
}

function ventinueve() {
    $texto = "ventinueve ";
#/////////////////////////////////////////////
    return $texto;
}

function treinta() {
    $texto = "treinta ";
    return $texto;
}

function treinta_y() {
    $texto = "treinta y ";
    return $texto;
}

function cuarenta() {
    $texto = "cuarenta ";
    return $texto;
}

function cuarenta_y() {
    $texto = "cuarenta y ";
    return $texto;
}

function cincuenta() {
    $texto = "cincuenta ";
    return $texto;
}

function cincuenta_y() {
    $texto = "cincuenta y ";
    return $texto;
}

function sesenta() {
    $texto = "sesenta ";
    return $texto;
}

function sesenta_y() {
    $texto = "sesenta y ";
    return $texto;
}

function setenta() {
    $texto = "setenta ";
    return $texto;
}

function setenta_y() {
    $texto = "setenta y ";
    return $texto;
}

function ochenta() {
    $texto = "ochenta ";
    return $texto;
}

function ochenta_y() {
    $texto = "ochenta y ";
    return $texto;
}

function noventa() {
    $texto = "noventa ";
    return $texto;
}

function noventa_y() {
    $texto = "noventa y ";

#/////////////////////////////////////////////
    return $texto;
}

function cero() {
    $texto = "cero ";
#/////////////////////////////////////////////
    return $texto;
}

function uno() {
    $texto = "un ";
    return $texto;
}

function dos() {
    $texto = "dos ";
    return $texto;
}

function tres() {
    $texto = "tres ";
    return $texto;
}

function cuatro() {
    $texto = "cuatro ";
    return $texto;
}

function cinco() {
    $texto = "cinco ";
    return $texto;
}

function seis() {
    $texto = "seis ";
    return $texto;
}

function siete() {
    $texto = "siete ";
    return $texto;
}

function ocho() {
    $texto = "ocho ";
    return $texto;
}

function nueve() {
    $texto = "nueve ";
    return $texto;
}

#/////////////////////////////////////////////
$saldo = 29;


if ($saldo == 0) {
    cero();
} else {
    $texto = " ";
    $medio = bloque_10($saldo);
    $texto = $texto ." ". $medio['texto'];
    $medio = bloque_0($medio['numero']);
    echo $medio['texto'];
    echo $medio['numero'];
    $texto = $texto ." ". $medio['texto'];
    echo $texto;
}
?>
