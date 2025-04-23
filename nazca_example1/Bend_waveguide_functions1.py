
def bend_waveguide1(Width_taper1,Width_taper2,L_taper,L1,L2,xp,yp,Radii):
    
 import nazca as nd
 
 with nd.Cell(name='Cell_A') as cella:
  nd.taper(length=L_taper, width1=Width_taper1, width2=Width_taper2,layer='WG_HM').put(0)
  nd.strt(length=L1, width=Width_taper2,layer='WG_HM').put()#L_taper
  nd.bend(angle=90, radius=Radii,width=Width_taper2,layer='WG_HM').put(L_taper+L1)#L_taper+L1
  nd.bend(angle=90, radius=Radii,width=Width_taper2,layer='WG_HM').put(L_taper+L1+2*Radii,2*Radii,180)#L_taper+L1+2*Radii,2*Radii,180
  nd.strt(length=L2, width=Width_taper2,layer='WG_HM').put(L_taper+L1+2*Radii,2*Radii)#L_taper+L1+2*Radii,2*Radii
  nd.taper(length=L_taper, width1=Width_taper2, width2=Width_taper1,layer='WG_HM').put(L_taper+L1+L2+2*Radii,2*Radii)#L_taper+L1+L2+2*Radii,2*Radii
 return  cella   

 







