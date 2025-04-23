# -*- coding: utf-8 -*-
import nazca as nd
import layers
from Bend_waveguide_functions1 import bend_waveguide1

layers
# Define parameters for the structure
Width_taper1 = 0.48       # Starting width of the taper
Width_taper2 = 0.48       # Ending width of the taper (used for straight and bend sections)
L_taper = 1               # Length of the taper
L1 = 1                    # Length of the initial straight section
L2 = 1                    # Length of the final straight section
xp = 0                    # Placement X coordinate
yp = 0                    # Placement Y coordinate
Radii = 2                 # Bend radius

# Call the function to create the waveguide cell
cell = bend_waveguide1(
    Width_taper1=Width_taper1,
    Width_taper2=Width_taper2,
    L_taper=L_taper,
    L1=L1,
    L2=L2,
    xp=xp,
    yp=yp,
    Radii=Radii
)

cell.put(0, 0)  # ✅ Place the cell into the layout at coordinates (0, 0)

# Export the layout to a GDS file
nd.export_gds(filename='Bend_waveguide1.gds')
