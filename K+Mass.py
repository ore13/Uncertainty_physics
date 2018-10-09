# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 12:35:04 2018

@author: Violet
"""

from uncertaintyCalculator import uNum
import matplotlib.pyplot as plt
import sympy
global pm
global magStrength
global pionCharge
global pionMass
global scale

pm = sympy.Symbol('±')
magStrength = uNum(1.5, 0)
pionCharge = uNum(300, 0)
pionMass = uNum(139.6, 0)
scale = uNum(370, 0) / uNum(149, 1)

def tableLine(chordLength, sagitta, angle):
    """calculates the momentum in x and y directions, and energy"""
    r = radius(chordLength, sagitta)
    p = momentum(r)
    px, py = components(p, angle)
    E = energy(p)
    return (p, angle, px, py, E)

def radius(chordLength, sagitta):
    r = chordLength ** uNum(2, 0)/(uNum(8, 0) * sagitta) + sagitta/uNum(2, 0)
    return r * scale

def momentum(radius):
    p = radius * magStrength * pionCharge
    return p

def components(value, angle):
    x = value * angle.cos()
    y = value * angle.sin()
    return (x, y)

def energy(momentum):
    E = (pionMass ** uNum(2, 0) + momentum ** uNum(2, 0)).sqrt()
    return E

def K_table():
    """ uNum is a class that takes an number and an uncertainty. Haven't got it to work with the math class yet
        so therefore it cannot be used with external methods like math.sin(). these are implemented within uNum
        so use uNum.sin() etc... To create a uNum, write uNum(number, uncertainty).  you can play around with 
        the K+ mass program- it outputs a text file in csv format which has a table of values like in the lab book.
        Also note that it prints the mass to command line
    """
    pion1 = tableLine(uNum(10e-2, 1e-3), uNum(7e-3, 1e-3), uNum(98, 2))
    pion2 = tableLine(uNum(10e-2, 1e-3), uNum(4.7e-3, 1e-3), uNum(-12, 2))
    pion3 = tableLine(uNum(10e-2, 1e-3), uNum(15.5e-3, 1e-3), uNum(-125, 2))
    
    file = open('K+mass.txt', 'w')
    file.write('Particle, Momentum (total) [MeV/c], Angle to x axis [Deg],\
               x component of momentum, y component of momentum, Energy\n')
    file.write('{}{}\n'.format('pi^+', writeCSVformat(pion1)))
    file.write('{}{}\n'.format('pi^-', writeCSVformat(pion2)))
    file.write('{}{}\n'.format('pi^+', writeCSVformat(pion3)))
    
    #calculate totals
    pxTotal = pion1[2] + pion2[2] + pion3[2]
    pyTotal = pion1[3] + pion2[3] + pion3[3]
    ETotal = pion1[4] + pion2[4] + pion3[4]
    file.write(' , , Total, {}, {}, {}'.format(pxTotal, pyTotal, ETotal))
    file.close()
    
    #calculate mass of K+
    print('{} {} {}'.format(pxTotal.num, pm, pxTotal.uncertainty))
    print('{} {} {}'.format(ETotal.num, pm, ETotal.uncertainty))
    mass = (ETotal ** uNum(2, 0) - pxTotal ** uNum(2, 0)).sqrt()
    print('MASS OF K+:')
    print('{} {} {}'.format(mass.num, pm, mass.uncertainty))

def radiusChangeGraph():
    pions = []
    for i in range(1e-4, 1e-2, 5e-4):
        radius_values.append(uNum(i, 0))
    
    

def writeCSVformat(data):
    result = ''
    for datum in data:
        result += ', ' + str(datum)
    return result


K_table()
print('end')
               
    


