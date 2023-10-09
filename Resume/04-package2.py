""" Ver map_package.png """


""" O Python espera que haja um arquivo com um nome exclusivo
na pasta do pacote: __init__.py ."""

from sys import path
path.append("/Users/fabioschapowal/Desktop/Python/Python_adv/extra")

print(path)

from extra.good.best.tau import FunT
print(FunT())

import extra.iota
print(extra.iota.funI())

import extra.good.best.sigma as sig
import extra.good.alpha as alp

print(sig.FunS())
print(alp.FunA())
