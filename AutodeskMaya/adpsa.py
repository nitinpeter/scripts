#Last Update 2013 April
#Nitin Peter
import maya.cmds as mc
import maya.mel as melons
from lg_fast import *
def psa(num):
    from datetime import datetime
    if num==int(datetime.now().strftime('%I'))+int(datetime.now().strftime('%d'))+7:
    	melons.eval("psa()")
def setToPaint():
	sikk=mc.optionMenu('modi',q=1,sl=1)
	if sikk==1:
		melons.eval("ArtPaintSkinWeightsTool")
	if sikk==2:
		melons.eval("artAttrToolScript 4 \"cluster\"")

def setty(demod):
	sikk=mc.optionMenu('modi',q=1,sl=1)
	imax=mc.textField('nt_maxTF',q=1,tx=1)
	whichCtx = mc.currentCtx();
	whichCtx=whichCtx.replace('Context','Ctx')
	if whichCtx=='artAttrSkinCtx' or whichCtx=='artAttrCtx':
		if demod==0:
			melons.eval("catch(`artAttrPaintOperation "+whichCtx+" Replace`)")
		if demod==1 or demod==5:
			melons.eval("catch(`artAttrPaintOperation "+whichCtx+" Smooth`)")
		if demod==2:
			melons.eval("catch(`artAttrPaintOperation "+whichCtx+" Add`)")
		if demod==3:
			melons.eval("catch(`artAttrPaintOperation "+whichCtx+" Scale`)")
	sett(demod,sikk,imax)
def nt_sorto():
	lista=mc.textScrollList('nt_texList',q=1,ai=1)
	print lista
	sikk=mc.optionMenu('modi',q=1,sl=1)
	influs=[]
	if sikk==1:
		meshsk=mc.textField('mesht',q=1,tx=1)
		influs=mc.skinCluster(meshsk,q=1,inf=1)
	if sikk==2:
		meshs=mc.textField('meshth',q=1,tx=1)
		influs=Bskin(meshs,["cluster","softMod","nonLinear"])
	aljoints="string $aljoins[]={"
	if mc.checkBox('cbUpd',q=1,v=1):
		for oro in influs:
			if oro in lista:
				aljoints+="\""+oro+"\","
		aljoints=aljoints+"\"\"};ntshowList($aljoins);";
		melons.eval(""+aljoints+"")
def doski(switch):
	esse1=mc.textField('fname',q=1,tx=1)
	esse2=mc.textField('sname',q=1,tx=1)
	skin1=mc.textField('skfname',q=1,tx=1)
	skin2=mc.textField('sksname',q=1,tx=1)
	imax=float(mc.textField('nt_maxTF',q=1,tx=1))
	otua=mc.checkBox('cbAuto',q=1,v=1)
	ratio=mc.floatSliderGrp('sklid',q=1,v=1)
	joints=mc.textScrollList('nt_texList',q=1,ai=1)
	sikk=mc.optionMenu('modi',q=1,sl=1)
	essel=mc.ls(sl=1,fl=1)
	print essel
	if(switch==1):
		ratio=ratio*(1-otua)+otua*0.5
		flatskin(essel,joints,ratio,sikk)
	if(switch==0):
		zerout(sikk)
	elif(switch==2):
		printwt(essel,joints,sikk)
	elif(switch==2.5):
		printAwt(essel,joints,sikk)
	elif(switch==3):
		zerout(sikk);
	elif(switch==4):
		grabeval(sikk,imax);
	elif(switch==5):
		divideval(sikk,imax)
	elif(switch==6):
		melons.eval("PolySelectConvert 2")
		ellam=mc.ls(sl=1,fl=1)
		ratio=ratio*(1-otua)+otua*0.25
		for esso in ellam:
			mc.select(esso,r=1)
			bleech(skin1,ratio,1,sikk);
		mc.select(essel)
	elif(switch==7):
		melons.eval("PolySelectConvert 2")
		ellam=mc.ls(sl=1,fl=1)
		ratio=ratio*(1-otua)+otua*1.0
		for esso in ellam:
			mc.select(esso,r=1)
			bleech(skin1,ratio,2,sikk);
		mc.select(essel)
	elif(switch==8):
		melons.eval("PolySelectConvert 2")
		ellam=mc.ls(sl=1,fl=1)
		ratio=ratio*(1-otua)+otua*1.0		
		for esso in ellam:
			mc.select(esso,r=1)
			bleech(skin1,ratio,3,sikk);
		mc.select(essel)
	elif(switch==9):
		melons.eval("PolySelectConvert 3")
		ellam=mc.ls(sl=1,fl=1)
		ratio=ratio*(1-otua)+otua*1.0
		for esso in ellam:
			mc.select(esso,r=1)
			cleech(skin1,ratio,ellam,sikk,0);
		mc.select(essel)
	elif(switch==10):
		melons.eval("PolySelectConvert 3")
		ellam=mc.ls(sl=1,fl=1)
		ratio=ratio*(1-otua)+otua*1.0
		for esso in ellam:
			mc.select(esso,r=1)
			cleech(skin1,ratio,ellam,sikk,1);
		mc.select(essel)
def keltrans():
	cc1=mc.textScrollList("nt_texList",q=1,si=1)
	for cc in cc1:
		ctran=mc.listConnections((cc+'.matrix'),s=1)
		mc.select(ctran,add=1)
def jocl():
	j1=mc.textScrollList("nt_texList",q=1,si=1)
	clusst=j2c(j1)
def cljo():
	stinjos=mc.textScrollList('nt_texList',q=1,si=1)
	for stinjo in stinjos:
		c2j(stinjo)
def josuf():
	j1=mc.textScrollList("nt_texList",q=1,si=1)
	j2=mc.ls(sl=1)
	niks=mc.textField("mesht",q=1,tx=1)
	josuff(j1,j2,niks);
def jbremover(mins,mod):
	essel=mc.ls(sl=1,fl=1)
	joints=mc.textScrollList("nt_texList",q=1,ai=1)
	skinny=mc.textField('mesht',q=1,tx=1)
	for k in range(0,len(joints)):
		flag=0
		for l in range(0,len(essel)):
			if '.' in essel[l]:
				gb=0.0
				if mod==1:
					gb=lgWeight(skinny,joints[k],essel[l])
				if mod==2:
					try:
						gba=lgcWeight(joints[k],essel[l])
						gb=gba[0]
					except:
						gb=1;
				if gb>mins:
					flag=1
			else:
				flag=1
		if(flag==0):
			mc.textScrollList("nt_texList",e=1,ri=joints[k])
def skid():
	realm=mc.textField('mesht',q=1,tx=1)
	joints=mc.skinCluster(realm,q=1,inf=1)
	geom=mc.skinCluster(realm,q=1,g=1)
	mc.skinCluster(realm,e=1,ubk=1)
	mc.skinCluster(geom[0],joints,tsb=1)
def skid1():
	import maya.mel as mel
	realm=mc.textField('mesht',q=1,tx=1)
	joints=mc.textScrollList("nt_texList",q=1,ai=1)
	for jo in joints:
		conns=mc.listConnections(jo+".worldMatrix[0]",p=1,s=1)
		conns=[x for x in conns if realm in x]
		conn=conns[0].replace("matrix","bindPreMatrix")
		matrixAsStr = ' '.join( map( str, mc.getAttr( jo+'.worldInverseMatrix') ) )
		melStr = 'setAttr -type "matrix" '+conn+' '+matrixAsStr
		mel.eval( melStr )
def tisMeshe(maco):
	nttm=mc.nodeType(maco);
	if nttm=="transform":
		ntpar=mc.listRelatives(maco,s=1);
		if mc.objExists(ntpar[0]):
			nttm=mc.nodeType(ntpar[0]);
	if nttm=="mesh" or nttm=="lattice" or nttm=="nurbsSurface" or nttm=="nurbsCurve":
		return 1;
	return 0;
def selbu():
	melons.eval("nt_slist()");
	manu=mc.ls(sl=1,fl=1)
	objs=mc.ls(sl=1,o=1)
	joints=[]
	if manu:
		mc.textField("fname",e=1,text=manu[0]);
		skina=[]
		skinb=[]
		sikk=mc.optionMenu('modi',q=1,sl=1)
		if sikk==1:
			skina= Bskin(manu[0],"skinCluster")
			sgg=mc.skinCluster(skina[0],q=1,g=1)
			sgg=mc.listRelatives(sgg[0],p=1)
			mc.textField("mesht",e=1,tx=skina[0])
			mc.textField("skfname",e=1,tx=skina[0]);
		if sikk==2:
			skina= Bskin(manu[0],["cluster","softMod","nonLinear"])
			mc.textField("mesht",e=1,tx="")
			mc.textField("skfname",e=1,tx="");
		if(len(manu)==1):
			manu.append(manu[0])
		mc.textField("sname",e=1,tx=manu[1])
		if sikk==1:
			skinb= Bskin(manu[1],"skinCluster")
		if sikk==2:
			skinb= Bskin(manu[1],["cluster","softMod","nonLinear"])
			mc.textField("mesht",e=1,tx="")
			mc.textField("sksname",e=1,tx="");
		if sikk==1:
			mc.textField("sksname",e=1,text=skinb[0]);
			joints1=mc.skinCluster(skina[0],q=1,inf=1)
			joints2=mc.skinCluster(skinb[0],q=1,inf=1)
			if joints1==joints2:
				joints=joints1
			else:
				joints=list(set(joints1) or (set(joints2)-set(joints1)))
		if sikk==2:
			if skina==skinb:
				joints=skina
			else:
				joints=list(set(skina) or (set(skinb)-set(skina)))
	mc.popupMenu('meshtha',e=1,dai=1)
	for mesa in objs:
		if tisMeshe(mesa):
			if mc.nodeType(mesa)=='transform':
				mc.menuItem(l=mesa,c=('mc.select("'+mesa+'")'),p="meshtha")
				mc.textField('meshth',e=1,tx=mesa)
			else:
				mespar=melons.eval("firstParentOf(\""+mesa+"\")")
				mc.menuItem(l=mespar,c=('melons.eval("select -r \\\"'+mespar+'\\\"")'),p="meshtha")
				mc.textField('meshth',e=1,tx=mespar)		
		else:
			print("No Valid Selection")
	if joints==[]:
		if sikk==1:
			print "no skinClusters found on selectedMesh"
		else:
			print "no Clusters found on selectedMesh" 
		return []
		
	return joints;
def skop():
    essel=mc.textScrollList('nt_texList',q=1,ai=1)
    ellam=mc.ls(sl=1)
    for oro in ellam:
        try:
            mc.skinCluster(essel,oro,tsb=1)
        except:
            pass
        mc.select(melons.eval("textField -q -tx meshth"),r=1)
        mc.select(oro,add=1)
        mc.copySkinWeights(sa="closestPoint", ia=("name", "label", "oneToOne"), nm=1)
def selLoc():
    joints=mc.textScrollList("nt_texList",q=1,si=1)
    if not (joints):
        joints=mc.ls(sl=1)
    chown=[]
    for jo in joints:
        pa=mc.listRelatives(jo,p=1)
        cha=mc.listRelatives(jo,c=1)
        sib=mc.listRelatives(pa[0],c=1)
        if pa:
            pa=[x for x in pa if mc.nodeType(x)=="joint"]
        else:
            pa=[]
        print cha
        if cha:
            cha=[x for x in cha if mc.nodeType(x)=="joint"]
        else:
            cha=[]
        print cha
        if sib:
            sib=[x for x in sib if mc.nodeType(x)=="joint"]
        else:
            sib=[]
        chown=list(set(chown+pa+sib+cha))
    if chown:
    	mc.textScrollList("nt_texList",e=1,ra=1)
    for oo in chown:
    	mc.textScrollList("nt_texList",e=1,a=oo)