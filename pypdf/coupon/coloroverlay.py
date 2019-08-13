from PIL import Image
import os

dataFiles = os.listdir('data/')

for filename in dataFiles:
  #strip off the file extension
  name= os.path.splitext(filename)[0]
  img= Image.open('input/%s'%(filename))
  
  #create the coloured overlays
  red= Image.new('RGB',img.size,(255,0,0))
  green= Image.new('RGB',img.size,(0,255,0))
  blue= Image.new('RGB',img.size,(0,0,255))
  yellow= Image.new('RGB',img.size,(255,255,0))
  
  #create a mask using RGBA to define an alpha channel to overlay
  mask = Image.new('RGBA',img.size,(0,0,0,123))
  
  Image.composite(img,red,mask).convert('RGB').save('output/%sr.bmp'% (name))
  Image.composite(img,green,mask).convert('RGB').save('output/%sg.bmp'% (name))
  Image.composite(img,blue,mask).convert('RGB').save('output/%sb.bmp'% (name))
  Image.composite(img,yellow,mask).convert('RGB').save('output/%sy.bmp'% (name))