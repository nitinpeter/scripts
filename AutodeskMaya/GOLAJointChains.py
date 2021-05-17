#Written 2012
#Nitin Peter
#make joint chains of varioius kinds
import maya.cmds as mc
import maya.mel as mel
def GOLA():
	if mc.window('nt_GOLA',q=1,ex=1):
		mc.deleteUI('nt_GOLA')
	mc.windowPref(ra=1)
	mc.window('nt_GOLA',wh=[220,320],t="GOLA")
	mc.tabLayout(imw=5, imh=5)
	mc.columnLayout('chains',rs=5)
	mc.separator(w=200)
	mc.button(w=200,l="fkchain",c="FKChan('joint')")
	mc.button(w=200,l="proxyfkchain",c="PFKChan('joint')")
	mc.button(w=200,l="simplechain",c="MYChan('joint')")
	mc.button(w=200,l="proxysimplechain",c="PYChan('joint')")
	mc.button(w=200,l="ikfloatchain",c="IKChan('joint')")
	mc.button(w=200,l="fkikchain",c="FKIKChan('joint')")
	mc.button(w=200,l="proxyfkikchain",c="PFKIKChan('joint')")
	mc.button(w=200,l="proxyfkikchain",c="PFKIKChan('joint')")
	mc.rowColumnLayout(nc=2)
	mc.button(w=100,l="IKFKdyna",c='mel.eval("addina()")')
	mc.button(w=100,l="Deletedyna",c='mel.eval("deldina")')
	mc.setParent('..')
	mc.button(w=200,l="Sine",c='mel.eval("sadina")')
	mc.setParent('..')
	mc.columnLayout('gola',rs=5)
	mc.separator(w=200)
	mc.text(l="ALIGN SELECTION")
	mc.columnLayout(cw=200,rs=5,cat=["both",5])
	mc.intSlider("nt_chsoe",v=2,vis=0)
	mc.rowColumnLayout(nc=3,cw=[(1,60),(2,45),(3,80)])
	mc.checkBox("paney",l="Parent",al="left",cc='cpsawp(1)')
	mc.checkBox("chaney",l="Child",al="left",cc='cpsawp(0)')
	mc.checkBox("carry_dn",l="CarryDown",al="left")
	mc.setParent('..')
	mc.rowColumnLayout(nc=2,cw=[(1,90),(2,90)])
	mc.separator(w=200)
	mc.separator(w=200)
	mc.button(l='joint',c='rigis(1,0)')
	mc.button(l='ctrl',c='nt_chos=mel.eval("intSlider -q -v nt_chsoe");rigis(2,nt_chos);')
	mc.popupMenu();
	mc.menuItem(l="Cube",c='nt_chos=mel.eval("intSlider -e -v 0 nt_chsoe")')
	mc.menuItem(l="Circle",c='nt_chos=mel.eval("intSlider -e -v 1 nt_chsoe")')
	mc.menuItem(l="Sphere",c='nt_chos=mel.eval("intSlider -e -v 2 nt_chsoe")')
	mc.button(l="null",c="rigis(3,0)")
	mc.button(l="loc",c="rigis(4,0)")
	mc.setParent('..')
	mc.setParent('..')
	mc.separator(w=200)
	mc.columnLayout(cat=["both",5],rs=5,cw=200)
	mc.text('myte',l="align to centre of selection",al="left")
	mc.rowColumnLayout(nc=2,cw=[(1,90),(2,90)])
	mc.button(l="joint",c="rigo(1)")
	mc.button(l="ctrl",c="rigo(2)")
	mc.button(l="null",c="rigo(3)")
	mc.button(l="loc",c="rigo(4)")
	mc.setParent('..')
	mc.setParent('..')
	mc.columnLayout(cat=["both",5],rs=5,cw=200)
	mc.text(l="align to each(component mode)",al="left")
	mc.rowColumnLayout(nc=2,cw=[(1,90),(2,90)])
	mc.button(l="joint",c="rigu(1)")
	mc.button(l="ctrl",c="rigu(2)")
	mc.button(l="null",c="rigu(3)")
	mc.button(l="loc",c="rigu(4)")
	mc.setParent('..')
	mc.setParent('..')
	mc.columnLayout(cw=200,rs=5,cat=["both",5])
	mc.textFieldButtonGrp('nt_rname',tx="basename",bl="RENAME",bc="namein()",adj=1)
	mc.setParent('..')
	mc.setParent('..')
	mc.showWindow('nt_GOLA')
def gola(mod,specs):
	gola=[]
	dla=''
	for i in range(0,len(specs)):
		jot=[]
		mc.select(specs[i])
		orop=mc.listRelatives(specs[i],p=1)
		if mod>0:
			jot=rigi(1,0,0,0,0)
			mc.setAttr((jot[0]+'.v'),0)
			LoHi([0])
		cot=rigi(2,1,0,1,0,(specs[i]+'_Ctrl'))
		LoHi([0])
		eot=rigi(3,0,0,1,0,(specs[i]+'_Extra'))
		dot=rigi(3,0,0,1,0,(specs[i]+'_Draw'))
		fot=rigi(3,0,0,1,0,(specs[i]+'_Offset'))
		gola.append(fot[0])
		gola.append(dot[0])
		gola.append(eot[0])
		gola.append(cot[0])
		if mod>1 and dla:
			mc.parentConstraint(dla,fot[0],mo=1)
			mc.scaleConstraint(dla,fot[0],mo=1)
		if mod>0:
			mc.parentConstraint(jot[0],specs[i],mo=1)
			mc.scaleConstraint(jot[0],specs[i],mo=1)

		if mod>=2:
			dla=cot
		else:
			dla=eot
	return gola
def Chan(mod,pxy=0,*typo):
	sele=mc.ls(sl=1)
	for les in sele:
		Machan(mod,les,pxy,*typo)
def Machan(mod,sel,px=0,*typo):
	nott=0
	alla=[]
	ella=mc.ls(sel,dag=1)
	if px==1:
		alla=dupPref(ella[0],'My')
		alla=mc.ls(alla[0],dag=1)
		ella=addPref(ella,'Prox')
		ella=mc.ls(ella[0],dag=1)
	if typo:
		ella=[x for x in ella if mc.nodeType(x) in typo]
		if px==1:
			alla=[x for x in alla if mc.nodeType(x) in typo]
	palla=[]
	pella=[]
	if ella:
		pella=gola(mod,ella)
	if alla:
		palla=gola(mod,alla)
	if palla:
		for i in range(0,len(palla)):
			if i%4>1:
				mc.connectAttr((palla[i]+'.t'),(pella[i]+'.t'))
				mc.connectAttr((palla[i]+'.r'),(pella[i]+'.r'))
				mc.connectAttr((palla[i]+'.s'),(pella[i]+'.s'))
	for i in range(0,len(pella)):
		if abs(mod)==3 and i%4==3:
			cot=''
			eot=''
			ccot=''
			eeot=''

			if pella:
				mc.select(pella[i],r=1)
				eeot=rigi(3,0,1,0,1)
				ffot=rigi(3,0,1,0,1,(pella[i]+'_Pop'))
				ccot=rigi(2,2,1,0,1,(pella[i]+'_IK'))
				LoHi([0])
			if palla:
				mc.select(palla[i],r=1)
				eot=rigi(3,0,1,0,1)
				fot=rigi(3,0,1,0,1,(palla[i]+'_Pop'))
				cot=rigi(2,2,1,0,1,(palla[i]+'_IK'))
				LoHi([0])
				mc.connectAttr((ccot[0]+'.t'),(cot[0]+'.t'))
				mc.connectAttr((ccot[0]+'.r'),(cot[0]+'.r'))
				mc.connectAttr((ccot[0]+'.s'),(cot[0]+'.s'))
def FKChan(*typo):
	Chan(2,*typo)
def MYChan(*typo):
	Chan(0,*typo)
def PYChan(*typo):
	Chan(0,1,*typo)
def IKChan(*typo):
	Chan(1,*typo)
def PFKChan(*typo):
	Chan(2,1,*typo)
def FKIKChan(*typo):
	Chan(3,0,*typo)
def PFKIKChan(*typo):
	Chan(3,1,*typo)
GOLA()
