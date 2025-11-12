#!/bin/env python


import svgwrite
import numpy as np


Dmin = 0.5
delta = 0.5
Nring = 10
Nsegment = 4

#open the file
dwg = svgwrite.Drawing('kirichute1.svg',width='24cm',height='24cm',viewBox='-12 -12 24 24')

for ring in range(Nring):
    R = Dmin+ring*delta
    for segment in range(Nsegment):
        theta0 = 0 + 2*np.pi/Nsegment*segment + np.pi/4*(ring % 2)
        thetaf = 0 + 2*np.pi/Nsegment*(segment+1)-delta/R + np.pi/4*(ring % 2)
        x1 = R*np.cos(theta0)
        y1 = R*np.sin(theta0)
        x2 = R*np.cos(thetaf)
        y2 = R*np.sin(thetaf)
        print('draw a segment here LATER')
        path = dwg.path(d=f'M {x1} {y1} A {R} {R} 0 0 1 {x2} {y2}')
        path.stroke('black', width=0.05)
        path.fill('none')
        dwg.add(path)

#draw the circle around the outside last'
dwg.add(dwg.circle(center=(0,0),r=Dmin+Nring*delta,fill='none',stroke='black',stroke_width=0.05))

# save the file
dwg.save()
