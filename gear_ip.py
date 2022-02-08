import cmath
import math
import numpy as np


def PBS11(EL, S):
    PBS1 = EL / S
    return PBS1
    pass


def TBS11(Wt, Kv, Ko, Km, Kf, b, Y, m, J):
    TBS1 = ((Wt * Kv * Ko * Km) / (Kf * (b) * Y1 * m * J1))
    return TBS1
    pass


def asfs11(sfs, S):
    asfs3 = sfs / S
    return asfs3
    pass


def cs11(Cp, Wt, Kv, Ko, Km, b, D, I):
    cs3 = Cp * (cmath.sqrt(((Wt * Kv * Ko * Km) / (b * D * I))))
    return cs3
    pass


def Kv1(m):
    if m < 5:
        Kv3 = 1
    elif m > 5:
        Kv3 = 0.85
    return Kv3


def e1(m):
    if m <= 4 * 0.001:
        e3 = 0.051
    elif m == 5 * 0.001:
        e3 = 0.055
    elif m == 6 * 0.001:
        e3 = 0.065
    elif m == 7 * 0.001:
        e3 = 0.071
    elif m == 8 * 0.001:
        e3 = 0.078
    elif m == 9 * 0.001:
        e3 = 0.085
    elif m == 10 * 0.001:
        e3 = 0.089
    elif m == 12 * 0.001:
        e3 = 0.097
    elif m == 14 * 0.001:
        e3 = 0.104
    elif m == 16 * 0.001:
        e3 = 0.110
    elif m == 18 * 0.001:
        e3 = 0.114
    elif m == 20 * 0.001:
        e3 = 0.117
    else:
        e3 = 0.120
    return e3


def Km2(b):
    if 0 <= b <= 50 * 0.001:
        Km3 = 1.3
    elif b == 150 * 0.001:
        Km3 = 1.4
    elif b == 225 * 0.001:
        Km3 = 1.5
    elif b > 400 * 0.001:
        Km3 = 1.8
    else:
        Km3 = 2.2
    return Km3


def Kv1(V):
    if V > 12.5:
        Kv3 = 3. / (3 + V)
    elif 12.5 <= V <= 20:
        Kv3 = 6. / (6 + V)
    else:
        Kv3 = 0.75 / (0.75 + math.sqrt(V))
    return Kv3


def Kt1(Temp):
    if Temp <= 350:
        Kt3 = 1
    elif 350 < Temp <= 500:
        Kt3 = 0.5
    else:
        Kt3 = 0
    return Kt3


def Ks1(sigmau):
    if sigmau <= 400000000:
        Ks2 = 0.8
    elif sigmau == 400000000 - 600000000:
        Ks2 = 0.78
    elif sigmau == 600000000 - 800000000:
        Ks2 = 0.76
    elif sigmau == 800000000 - 1000000000:
        Ks2 = 0.72
    elif sigmau == 1000000000 - 1200000000:
        Ks2 = 0.68
    elif sigmau == 1200000000 - 1400000000:
        Ks2 = 0.64
    elif sigmau == 1400000000 - 1600000000:
        Ks2 = 0.63
    elif sigmau == 1600000000 - 1800000000:
        Ks2 = 0.62
    elif sigmau == 1800000000 - 2000000000:
        Ks2 = 0.619
    elif sigmau >= 2000000000:
        Ks2 = 0.61
    else:
        Ks2 = 0.6
    return Ks2


def R1(R):
    if R == '0.5':
        Kr1 = 1
    elif R == '0.9':
        Kr1 = 0.897
    elif R == '0.95':
        Kr1 = 0.868
    elif R == '0.99':
        Kr1 = 0.814
    elif R == '0.999':
        Kr1 = 0.753
    elif R == '0.9999':
        Kr1 = 0.702
    else:
        Kr1 = 0
    return Kr1


def Km11(sigmau):
    if sigmau <= 1400000000:
        Km2 = 1.33
    elif sigmau == 1400000000 - 1600000000:
        Km2 = 1.4
    elif sigmau == 1600000000 - 1800000000:
        Km2 = 1.45
    elif sigmau == 1800000000 - 2000000000:
        Km2 = 1.47
    elif sigmau == 2000000000 - 2200000000:
        Km2 = 1.5
    elif sigmau == 2200000000 - 2400000000:
        Km2 = 1.53
    elif sigmau == 2400000000 - 2600000000:
        Km2 = 1.57
    elif sigmau >= 2600000000:
        Km2 = 1.6
    else:
        Km2 = 0
    return Km2


def Ko1(sop, todm):
    if sop == 1 and todm == 1:
        Ko2 = 1
    elif sop == 2 and todm == 1:
        Ko2 = 1.25
    elif sop == 3 and todm == 1:
        Ko2 = 1.5
    elif sop == 1 and todm == 2:
        Ko2 = 1.25
    elif sop == 2 and todm == 2:
        Ko2 = 1.5
    elif sop == 3 and todm == 2:
        Ko2 = 1.75
    elif sop == 1 and todm == 3:
        Ko2 = 1.75
    elif sop == 2 and todm == 3:
        Ko2 = 2
    elif sop == 3 and todm == 3:
        Ko2 = 2.25
    else:
        Ko2 = 0
    return Ko2


def KL1(KL):
    if top == 1:
        KL2 = 1
    else:
        KL2 = 0.3
    return KL2


def I11(pi, G):
    I3 = ((math.sin(pi) * math.cos(pi)) / 2) * (G / (G + 1))
    return I3


def Tp11(Aw, pi, G):
    Tp3 = (2 * Aw) / (G *
                      (math.sqrt(1 + ((1 / G) * ((1 / G) + 2)) *
                                 (math.sin(pi) * math.sin(pi))) - 1))
    return Tp3


def Yp11(Tp):
    Yp3 = 0.124 - (0.684 / Tp)
    return Yp3


def k11(sigmaes, pi, Ep, Eg):
    k3 = ((sigmaes * sigmaes * math.sin(pi) * math.sin(pi)) / 1.4) * ((1 / Ep) + (1 / Eg))
    return k3


def C11(k, e, Ep, Eg):
    C3 = ((k * (e / 1000)) / ((1 / Ep) + (1 / Eg)))
    return C3


def E1(material):
    if material == 1:
        E3 = 207000000
    elif material == 2:
        E3 = 131000000
    elif material == 3:
        E3 = 121000000
    else:
        E3 = 110000000
    return E3


def Cp1(gm, pm):
    mu = 0.3
    Cp3 = 0.564 * math.sqrt(1 / ((1 - mu * mu) / E1(gm)) + (1 - mu * mu) / E1(pm))
    return Cp3


def sigmaee1(material):
    if material == 1:
        sigmaee3 = 0.5 * 400000000
    elif material == 2:
        sigmaee3 = 0.45 * 200000000
    elif material == 3:
        sigmaee3 = 0.4 * 680000000
    else:
        sigmaee3 = 0.4 * 265000000
    return sigmaee3


def sigmao1(material):
    if material == 1:
        sigmao3 = 400000000 / 3
    elif material == 2:
        sigmao3 = 105000000
    elif material == 3:
        sigmao3 = 250000000
    else:
        sigmao3 = 84000000
    return sigmao3


def sigmau1(material):
    if material == 1:
        sigmau3 = 400000000
    elif material == 2:
        sigmau3 = 200000000
    elif material == 3:
        sigmau3 = 680000000
    else:
        sigmau3 = 265000000
    return sigmau3


def sigmasff1(material):
    if material == 1:
        sigmasff3 = 69000000
    elif material == 2:
        sigmasff3 = 379000000
    elif material == 3:
        sigmasff3 = 207000000
    else:
        sigmasff3 = 448000000
    return sigmasff3


def sigmaH1(material):
    if material == 1:
        sigmaH3 = 207000000
    elif material == 2:
        sigmaH3 = 131000000
    elif material == 3:
        sigmaH3 = 121000000
    else:
        sigmaH3 = 110000000
    return sigmaH3


def sigmaes1(material):
    if material == 1:
        sigmaes3 = 350000000
    elif material == 2:
        sigmaes3 = 630000000
    elif material == 3:
        sigmaes3 = 630000000
    else:
        sigmaes3 = 630000000
    return sigmaes3


def sigmae1(material):
    if material == 1:
        sigmae3 = 350000000
    elif material == 2:
        sigmae3 = 84000000
    elif material == 3:
        sigmae3 = 168000000
    else:
        sigmae3 = 350000000
    return sigmae3


m = input("enter  gear module in a range of [6,20]")
m = int(m)
G = input("enter  gear ratio in a range of [4,40]")
G = int(G)
T = input("enter  Torque value in a range of [500,5000]")
T = int(T)
pi1 = input("enter required gear teeth sytem for gear 14.5 or 20")
pi2 = input("enter required gear teeth sytem for pinion 14.5 or 20")
b = input("enter  face width value in a range of [0.38,0.75]")
b = float(b)
L = input("enter length of drive shaft to driven shaft value in a range of [0.1,1]")
L = float(L)
V = input("enter velcoity of pinion in range of [0.1,1] ")
V = float(V)
gm = input("enter gear material: 1 for Steel, 2 for castiron, 3 for tinbronze, 4 for 3")
gm = int(gm)
pm = input("enter gear material: 1 for Steel, 2 for castiron, 3 for tinbronze, 4 for 3")
pm = int(pm)
top = input(" enter type of load: 1 for continuous, 2 for impact 3 for pulsating")
top = int(top)
sop = input("enter type of application 1 for uniform, 2 for lightshock, 3 for mediumshock")
sop = int(sop)
todm = input("enter type of delivery 1 for uniform, 2 for moderateshock, 3 for heavyshock")
todm = int(todm)
R = input("enter reliability from ['0.5', '0.9', '0.95', '0.99', '0.999', '0.9999']")
temp = 150
Kt = Kt1(temp)
mu = 0.3
K1 = 0.107
Kf = 1
Tt = 1.5703 * m
D = 500
e = e1(m)

Q = (2 * G) / (1 + G)
Wt = 2 * T / D

if pi1 == 14.5:
    Aw = 1.0 * m
    De = 1.25 * m
    d = 2 * m
    Md = 2.25 * m
    Mc = 0.25 * m
    Fr = 0.4 * m
    Tp1 = Tp11(Aw, pi1, G)
    Tg1 = G * Tp1
    Yp1 = Yp11(Tp1)
    Yg1 = Yp11(Tg1)
else:
    pi1 = 20
    Aw = 0.8 * m
    De = 1 * m
    d = 1.6 * m
    Md = 1.8 * m
    Tt = 1.5708 * m
    Mc = 0.2 * m
    Fr = 0.4 * m
    Tp1 = Tp11(Aw, G, pi1)
    Tg1 = G * Tp1
    Yp1 = Yp11(Tp1)
    Yg1 = Yp11(Tg1)
I1 = I11(pi1, G)
Wn1 = Wt / math.cos(pi1)
Wr1 = Wn1 * math.sin(pi1)


if pi2 == 14.5:
    Aw = m
    De = 1.25 * m
    d = 2 * m
    Md = 2.25 * m
    Mc = 0.25 * m
    Fr = 0.4 * m
    Tp2 = Tp11(Aw, G, pi2)
    Tg2 = G * Tp2
    Yp2 = 0.154 - (0.912 / Tp2)
    K2 = 0.111
    Yg2 = 0.154 - (0.912 / Tg2)
else:
    pi2 = 20
    Aw = 0.8 * m
    De = 1 * m
    d = 1.6 * m
    Md = 1.8 * m
    Tt = 1.5708 * m
    Mc = 0.2 * m
    Fr = 0.4 * m
    K2 = 0.115
    Tp2 = Tp11(Aw, G, pi2)
    Tg2 = G * Tp2
    Yg2 = 0.175 - (0.841 / Tg2)
    Yp2 = 0.175 - (0.841 / Tp2)
I2 = I11(pi2, G)
Wn2 = Wt / math.cos(pi2)
Wr2 = Wn2 * math.sin(pi2)
Km = Km2(b)
Dp = 2 * L / (1 + G)
Dg = G * Dp
Kv = Kv1(V)
Vp = 3.14 * Dp * V / 60
Ng = V / G
Vg = 3.14 * Dg * Ng / 60
Powertransmitted = Wt * V / 1000
Egm = E1(gm)
Epm = E1(pm)
Cp = Cp1(gm, pm)
if sigmao1(gm) > sigmao1(pm):
    D = Dp
    V = Vp
    Y1 = Yp1
    Y2 = Yp2
    J1 = Y1 / Kf
    J2 = Y2 / Kf
    sigmae = sigmae1(pm)
    sigmaes = sigmaes1(pm)
    sigmasff = sigmasff1(pm)
    sigmaee = sigmaee1(pm)
    sigmau = sigmau1(pm)
    sigmao = sigmao1(pm)
    Ks = Ks1(sigmau)
    Km1 = Km11(sigmau)
else:
    D = Dg
    V = Vg
    Y1 = Yg1
    Y2 = Yg2
    J1 = Y1 / Kf
    J2 = Y2 / Kf
    sigmae = sigmae1(gm)
    sigmaes = sigmaes1(gm)
    sigmasff = sigmasff1(gm)
    sigmaee = sigmaee1(gm)
    sigmau = sigmau1(gm)
    sigmao = sigmao1(gm)
    Ks = Ks1(sigmau)
    Km1 = Km11(sigmau)
k1 = k11(sigmaes, pi1, Epm, Egm)
k2 = k11(sigmaes, pi2, Epm, Egm)
C1 = C11(k1, e, Epm, Egm)
C2 = C11(k2, e, Epm, Egm)
Ko = Ko1(sop, todm)
KL = KL1(top)
Kr = R1(R)
Ww1 = Dp * b * Q * k1
Ww2 = Dp * b * Q * k2


Ws1 = sigmae * b * m * Y1
Ws2 = sigmae * b * m * Y2
Wd1 = Wt + ((21 * V * ((b) * C1 + Wt))) / (21 * V + math.sqrt((b) * C1 + Wt))
Wd2 = Wt + ((21 * V * ((b) * C2 + Wt))) / (21 * V + math.sqrt((b) * C2 + Wt))
MOS1 = (Ws1 / Wd1) - 1
MOS2 = (Ws2 / Wd2) - 1
S1 = MOS1 + 1
S2 = MOS2 + 1
FTSG1 = (((b) * D * I1 * sigmaH1(gm)
          * sigmaH1(gm)) / (Cp * Cp))
FTSG2 = (((b) * D * I2 * sigmaH1(gm)
          * sigmaH1(gm)) / (Cp * Cp))
FTSP1 = (((b) * D * I1 * sigmaH1(pm)
          * sigmaH1(pm)) / (Cp * Cp))
FTSP2 = (((b) * D * I2 * sigmaH1(pm)
          * sigmaH1(pm)) / (Cp * Cp))
EL = sigmaee * KL * Kv * Ks * Kr * Kt * Kf * Km
PBS1 = PBS11(EL, S1)
PBS2 = PBS11(EL, S2)
TBS1 = TBS11(Wt, Kv, Ko, Km,
             Kf, b, Y1, m, J1)
TBS2 = TBS11(Wt, Kv, Ko, Km,
             Kf, b, Y2, m, J2)
sfs = sigmasff * KL * Kr * Kt
ASFS1 = asfs11(sfs, S1)
ASFS2 = asfs11(sfs, S2)
CS1 = cs11(Cp, Wt, Kv, Ko, Km, b, Dp, I1)
CS2 = cs11(Cp, Wt, Kv, Ko, Km, b, Dp, I2)
print(ASFS1, ASFS2, TBS1, TBS2, PBS1, PBS2, FTSG1, FTSG2, FTSP1, FTSP2, CS1, CS2)
