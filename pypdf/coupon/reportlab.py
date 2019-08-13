#from reportlab.pdfbase import pdfmetrics
#from reportlab.pdfbase.ttfonts import TTFont

from reportlab.lib.pagesizes import A4, landscape, portrait
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Table, Flowable, SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak
from reportlab.lib import randomtext
from reportlab import platypus
from reportlab.lib.colors import PCMYKColor, PCMYKColorSep, Color, black, blue, red

import os,random
#pdfmetrics.registerFont(TTFont('Bloody','BLOODY.TIF'))

# commented as it is taken care using PIL
#red50transparent = Color( 100, 0, 0, alpha=0.5)
#green50transparent = Color( 0, 100, 0, alpha=0.5)
#blue50transparent = Color( 0, 0, 100, alpha=0.5)
#magenta50transparent = Color( 100, 0, 100, alpha=0.5)

styles = getSampleStyleSheet()
path = os.path.realpath(os.path.dirname(__file__))
width=150
height=100
global num
num=1000
def drawPageFrame(canvas, doc):
    strs=["blue","green","red","magenta"]
    for y in range(8):
        for x in range(4):
            xo=x*width
            yo=y*height
	    # nor used for now
            #canvas.setFillColor(globals()[strs[x]+"50transparent"])
	    #canvas.rect(xo,yo,width,height,fill=True,stroke=False)
            canvas.drawImage(path+"input/coupon-wb.png",xo,yo,width,height,mask=[0, 250, 0, 250, 0, 250, ])
    for y in range(8):
        for x in range(4):
            num=num+1
            ya=-1*y*height-50
            xa=x*width+100
            canvas.saveState()
            canvas.rotate(270)
            canvas.setFillColorRGB(0,0,0) #font color
            #canvas.setFont("Bloody",10)
            canvas.drawCentredString(ya,xa,str(num))
            canvas.restoreState()

doc = SimpleDocTemplate("output/simage.pdf",pagesize=A4)

elements = []
for page in range(5):
  elements.append(Spacer(1,12))
  elements.append(PageBreak)

doc.build(elements,onFirstPage=drawPageFrame, onLaterPages=drawPageFrame)
