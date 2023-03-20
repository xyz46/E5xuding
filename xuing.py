import numpy as p #导入numpy库，需要提前安装numpy库

import matplotlib.pyplot as pl #导入matplotlib库，需要提前安装matplotlib库

t=p.linspace(0,2*p.pi,100)

x=16*p.sin(t)**3

y=13*p.cos(t)-5*p.cos(2*t)-2*p.cos(3*t)-p.cos(4*t)#主要是代入下面的两个公式

pl.plot(x,y,'r')

pl.axis([-25,25,-20,15])

pl.show()
