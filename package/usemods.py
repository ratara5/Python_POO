#It's possible create any quantity of modules in only one package

from calfunmod import potentiation as a
from calfunmod import to_round as r

from trigonometrics.calfuntrigmod import pythagoras as g
from trigonometrics.calfuntrigmod import cosine as c

from basics.calfunbasmod import sum as s
from basics.calfunbasmod import substract as t
from basics.calfunbasmod import product as p
from basics.calfunbasmod import divide as d


a(2,5)
r(4.8)

g(2,3)
c(3.1415)
#r(c(3.1415)) #error

s(9,17)
t(15,12)
p(6,7)
d(40,8)

