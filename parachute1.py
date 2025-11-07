import svgwrite
import numpy as np

print('open the file')
dwg = svgwrite.Drawing('kirichute1.svg')

for ring in range(5):
    for segment in range(4):
        print('draw a segment here LATER')

print('save the file')
