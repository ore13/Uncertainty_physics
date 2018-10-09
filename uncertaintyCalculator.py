# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 11:12:45 2018

@author: Violet
Uncertainty calculator
"""
import math
import sympy

class uNum():
    """represents a number with an uncertainty, num +- 2. These can be added 
       and multiplied, etc."""
    
    def __init__(self, number, uncertainty):
        self.num = number
        self.uncertainty = abs(uncertainty)
        self.pm = sympy.Symbol('±')
    
    def __repr__(self):
        return '{:.4f} {} {:.4f}'.format(self.num, self.pm, self.uncertainty)
    
    def __str__(self):
        #calculate number of digets to display
        digits = math.floor(math.log10(abs(self.num))) - math.floor(math.log10(self.uncertainty))
        dispNum = _round_sigfigs(self.num, digits + 2)
        dispUncertainty = _round_sigfigs(self.uncertainty, 2)
        return '{} {} {}'.format(dispNum, self.pm, dispUncertainty)

    def __add__(self, other):
        new_num = self.num + other.num
        new_uncertainty = self.uncertainty + other.uncertainty
        return uNum(new_num, new_uncertainty)
    
    def __sub__(self, other):
        new_num = self.num - other.num
        new_uncertainty = self.uncertainty + other.uncertainty
        return uNum(new_num, new_uncertainty)
    
    def __mul__(self, other):
        new_num = self.num * other.num
        new_uncertainty = abs(self.uncertainty/self.num) + abs(other.uncertainty/other.num)
        new_uncertainty *= abs(new_num)
        return uNum(new_num, new_uncertainty)
    
    def __truediv__(self, other):
        new_num = self.num / other.num
        new_uncertainty = abs(self.uncertainty/self.num) + abs(other.uncertainty/other.num)
        new_uncertainty *= abs(new_num)
        return uNum(new_num, new_uncertainty)
    
    def __pow__(self, other):
        new_num = self.num ** other.num
        new_uncertainty = abs(other.num) * abs(self.uncertainty / self.num)
        new_uncertainty *= abs(new_num)
        return uNum(new_num, new_uncertainty)
    
    def __neg__(self):
        return uNum(-self.num, self.uncertainty)
    
    def sin(self):
        new_num = math.sin(math.radians(self.num))
        new_uncertainty = abs(math.sin(math.radians(self.num + self.uncertainty)) - new_num)
        return uNum(new_num, new_uncertainty)
    
    def cos(self):
        new_num = math.cos(math.radians(self.num))
        new_uncertainty = abs(math.cos(math.radians(self.num + self.uncertainty)) - new_num)
        return uNum(new_num, new_uncertainty)
    
    def sqrt(self):
        new_num = math.sqrt(self.num)
        new_uncertainty = 1/2 * abs(self.uncertainty/self.num) * abs(new_num)
        return uNum(new_num, new_uncertainty)
        
    
def _round_sigfigs(num, sig_figs):
    if num != 0:
        return round(num, -int(math.floor(math.log10(abs(num))) - (sig_figs - 1)))
    else:
        return 0  # Can't take the log of 0



