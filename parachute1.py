import svgwrite
import numpy as np


Dmin = 1
delta = 0.25
Nring = 5
Nsegment = 4

print('open the file')
dwg = svgwrite.Drawing('kirichute1.svg')

for ring in range(Nring):
    R = Dmin+ring*delta
    for segment in range(Nsegment):
        theta0 = 0 + 2*np.pi/Nsegment*segment
        thetaf = 0 + 2*np.pi/Nsegment*(segment+1)-delta/R
        print('draw a segment here LATER')

print('draw the circle around the outside last')
print('save the file')
