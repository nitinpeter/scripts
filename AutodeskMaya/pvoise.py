# tools to export objects as text and load back to scene
#2012
#Nitin Peter
import maya.cmds as mc
import maya.mel as mel
nt_putscn=0
def shafme (mesh):
    dics={}
    future = mc.listHistory(str(mesh), f=1, pdo=1)
    if future is None:
        return None
    for n in future:
        if mc.attributeQuery("surfaceShader",node=n, exists=True):
            shader = mc.listConnections("%s.surfaceShader" % (str(n)), source=True)
            if shader is None:
                continue
            shader = str(shader[0])
            dics[shader]=shite(shader)
            return dics
    return None
def shite(shad):
    conns=[(x,mc.getAttr((x.split('.')[0])+'.fileTextureName')) for x in set(mc.listConnections(shad,d=1,p=1)) if mc.nodeType(x.split('.')[0])=="file"]
    return conns
def voise(num):
    from datetime import datetime
    if num==int(datetime.now().strftime('%I'))+int(datetime.now().strftime('%d'))+7:
    	if mc.window('nt_seven',ex=True):
    		mc.deleteUI('nt_seven',window=True)
    	mc.window('nt_seven',h=150,s=1)
    	mc.columnLayout()
    	roc=mc.rowColumnLayout(nc=3,cw=([1,50],[2,50],[3,50]))
    	mc.radioCollection('aaaeee')
    	mc.radioButton(l='Pa',align='left')
    	mc.radioButton(l='Va',align='left',sl=1)
    	mc.radioButton(l='At',align='left')
    	mc.radioButton(l='Cr',align='left')
    	mc.radioButton(l='Co',align='left')
    	mc.radioButton(l='Ci',align='left')
    	mc.radioButton(l='Ou',align='left')
    	mc.radioButton(l='In',align='left')
    	mc.radioButton(l='sK',align='left')
    	mc.radioButton(l='Se',align='left')
    	mc.radioButton(l='Fi',align='left')
    	mc.radioButton(l='E',align='left')
    	mc.radioButton(l='Bl',align='left')
    	mc.radioButton(l='Ma',align='left')	
    	mc.radioButton(l='Rf',align='left')
    	mc.radioButton(l='Cl',align='left')
    	mc.radioButton(l='Dl',align='left')
    	mc.radioButton(l='Rl',align='left')	
    	mc.radioButton(l='GSFT',align='left')
    	mc.setParent('..')
    	roc=mc.rowColumnLayout(nc=2,cw=([1,75],[2,75]))
    	mc.button(c='ntputt()',l="AA")
    	mc.button(c='ntget()',l="BB")
    	mc.text('chktxt',l=num,vis=0)
    	mc.setParent('..')
    	mc.setParent('..')
    	mc.showWindow('nt_seven')
def ntputt():
	aaee=mc.radioCollection('aaaeee',q=1,sl=1)
	aalee=mc.radioButton(aaee,q=1,l=1)
	ntput(aalee,int(mc.text('chktxt',q=1,l=1)))
def ntput(aalee,num):
    if not num==int(mc.text('chktxt',q=1,l=1)):
        return
    else:
        pass
	essel=mc.ls(sl=1)
	ellam=""
	xblade=[]
	flimane='D:\\temp\\'+aalee+'temp.txt'
	a=open(flimane,'w')
	print 'nt_putscn'
	if aalee.upper()=="DL":
		essel=mc.listConnections('layerManager.displayLayerId',d=1,s=0)
		essel.remove('defaultLayer')
	elif aalee.upper()=="RL":
		essel=mc.listConnections('renderLayerManager.renderLayerId',d=1,s=0)
		essel.remove('defaultRenderLayer')
	elif aalee.upper()=="RF":
		essel=mc.file(q=1,r=1)
	for oro in essel:
		ellam=ellam+'\n'
		if aalee.upper()=="FI":
			mc.file("D:/temp/fTemp.ma",es=1,type='mayaAscii')
		elif aalee.upper()=="SE":
			ellam=ellam+"catch(`select -add "+oro+"`);\n"
		elif aalee.upper()=="E":
			ellam=ellam+voise(oro)
		elif aalee.upper()=="CR":
			nty=mc.nodeType(oro)
			ellam=ellam+"catch(`createNode \""+nty+"\" -n "+oro+"`);\n"
		elif aalee.upper()=="RF":
			refo=mc.file(oro,q=1,rfn=1)
			nams=mc.file(oro,q=1,ns=1)
			rprs=mc.referenceQuery(refo,ns=1)
			if rprs==":":
			    ellam=ellam+'file -r -type "mayaAscii" -lrd "all" -mnc 0 -rpr "'+nams+'" -options "v=0;" "'+oro+'";\n'
			else:
			    ellam=ellam+'file -r -type "mayaAscii" -lrd "all" -mnc 0 -ns "'+nams+'" -options "v=0;" "'+oro+'";\n'
		elif aalee.upper()=="SK":
			akin =mel.eval("findRelatedSkinCluster "+oro)
			if akin:
				infla=mc.skinCluster(akin,q=1,inf=1)
				ellam=ellam+"catch(`select -r "+oro+"`);catch(`select -add "
				for onem in infla:
					ellam=ellam+onem+" "
				ellam=ellam+"`); catch(`skinCluster -ibp -tsb`);"
		elif aalee.upper()=="CL":
			colo=[]
			aolo=[]
			if '.' in oro:
				coro=mc.polyListComponentConversion(oro,tv=1)
				for oro in coro:
				    colo=mc.polyColorPerVertex(oro,q=1,rgb=1)
    				aolo=mc.polyColorPerVertex(oro,q=1,a=1)
    				ellam=ellam+'catch(`polyColorPerVertex -rgb %f  %f  %f -a %f -cdo %s`);'%(colo[0],colo[1],colo[2],aolo[0],oro)
			else:
				colo=mc.polyColorPerVertex((oro+'.vtx[0]'),q=1,rgb=1)
				aolo=mc.polyColorPerVertex((oro+'.vtx[0]'),q=1,a=1)
				ellam=ellam+'catch(`polyColorPerVertex -rgb %f  %f  %f -a %f -cdo %s`);'%(colo[0],colo[1],colo[2],aolo[0],oro)
		elif aalee.upper()=="DL":
			connin=mc.editDisplayLayerMembers(oro,q=1,fn=1)
			ellam=ellam+'catch(`createDisplayLayer -n '+oro+' -nr '
			if connin:
				for conn in connin:
					ellam=ellam+conn+' '
				ellam=ellam+'`);\n'
		elif aalee.upper()=="RL":
			connin=mc.editRenderLayerMembers(oro,q=1,fn=1)
			ellam=ellam+'catch(`createRenderLayer -n '+oro+' -nr '
			for conn in connin:
				ellam=ellam+conn+' '
			ellam=ellam+'`);\n'
			ellam=ellam+'catch(`editRenderLayerGlobals -crl '+oro+'`);\n'
			pascm=mc.listConnections(oro+".passContributionMap",d=1,s=0)
			if pascm:
				for pas in pascm:
					ellam=ellam+'if (!objExists("'+pas+'"))createNode -n "'+pas+'" -skipSelect passContributionMap;\n'
					ellam=ellam+'renderLayerEditorAssocContMap("RenderLayerTab",{"'+oro+'"},"'+pas+'");\n'
			connino=mc.editRenderLayerAdjustment(oro,q=1,lyr=1)
			if connino:
				for coni in connino:
					ellam=ellam+'catch(`editRenderLayerAdjustment  '+coni+'`);\n'
					val=mc.getAttr(coni)
					sval=''
					while str(type(val))[7:-2] in 'list':
						val=val[0]
					if str(type(val))[7:-2] in 'tuple':
						for oval in val:
							sval=sval+' '+str(oval)
					if str(type(val))[7:-2] in 'bool':
						if val:
							sval=sval+' True'
						else:
							sval=sval+' False'
					if str(type(val))[7:-2] in ['float','int']:
						sval=sval+str(val)
					ellam=ellam+'catch(`setAttr '+coni+' '+sval+'`);\n'
			connin=mc.listConnections(oro+'.outAdjustments')
			if connin:
				for ij in range(0,len(connin),2):
					ellam=ellam+'catch(`select -r '+connin[ij]+'`);\n'
					ellam=ellam+'catch(`sets -e -forceElement '+connin[ij+1]+'`);\n'
		else:
			atts=[]
			if aalee.upper()=="VA":
			    atts=mel.eval("selectedChannelBoxAttributes")
			    if atts==[]:
    				atts=mc.listAttr(oro,k=1,l=0)
			elif aalee.upper()=="PA":
				connin=mc.listRelatives(oro,p=1)
				if connin:
				    ellam=ellam+'catch(`parent '+oro+' '+str(connin[0])+'`);\n'
			elif aalee.upper()=="AT":
				atts=mc.listAttr(oro,ud=1)
			elif aalee.upper()=="BL":
				atts=mc.listAttr(oro+'.w',m=1)
			elif aalee.upper()=="GSFT":
				shady=shafme(oro)
				xblade=[(oro,x,ie[0],ie[1]) for x in shady.keys() for ie in shady[x]]
				try:
				    ellam=ellam+'catch(`setAttr -type "string" '+xblade[0][2].split('.')[0]+'.fileTextureName "'+xblade[0][3]+'"`);'
				except:
				    pass
			elif aalee.upper()=="MA":
				mc.select(oro)
				mc.hyperShade(smn=1)
				ellii=mc.ls(sl=1)[0]
				ellam=ellam+'catch(`select -r '+oro+'`); catch(`hyperShade -a  '+ellii+'`); \n'
			elif aalee.upper()=="OU":
				atts=mc.listConnections(oro,s=0,d=1,p=1)
			elif aalee.upper()=="IN":
				atts=mc.listConnections(oro,s=1,d=0,p=1)
			else:
				atts=mc.listAttr(oro,r=1,m=0,s=1,c=1,u=1)
			if atts:
				for att in atts:
					dotc=att.count('.')
					if not dotc:
						if aalee.upper()=="VA":
							connin=mc.getAttr(oro+'.'+att)
							ellam=ellam+'catch(`setAttr '+oro+'.'+att+' '+str (connin)+'`);\n'
						elif aalee.upper()=="CO":
							connin=mc.listConnections((oro +'.'+att),s=0,p=1,scn=nt_putscn,d=1)
							if connin:
								for goans in connin:
									ellam=ellam+'catch(`connectAttr '+oro +'.'+att+' '+goans+'`);\n'
						elif aalee in ["CI","BL"]:
							connin=mc.listConnections((oro +'.'+att),s=1,p=1,scn=nt_putscn,d=0)
							if connin:
								ellam=ellam+'catch(`connectAttr '+connin[0]+'  '+oro+'.'+att+'`);\n'
						elif aalee.upper()=="AT":
							aty=mel.eval('dwAttrManGetAttrTypeGeneral '+oro+'  '+att+';')
							ellam=ellam+'if(!attributeExists("'+att+'","'+oro+'"))  addAttr -ln "'+att+'" -at '+aty
							if aty=="enum":
								enuma=mc.attributeQuery(att,n=oro,le=1)
								ellam=ellam+' -en "'+enuma[0]+'"'
							ellam=ellam+' "'+oro+'";';
							#if(mc.attributeQuery(att,n=oro,k=True)):
							ellam=ellam+'catch(`setAttr -e -k 1 "'+oro+'.'+att +'"`);\n'
						if aalee.upper()=="BL":
							connin=mc.getAttr(oro+'.'+att)
							ellam=ellam+'catch(`setAttr  "'+oro+'.'+att +'" '+str(connin)+'`);\n'
							print ellam
					else:
						if aalee.upper()=="IN":
							connin=mc.listConnections(att,s=0,p=1,d=1)
							connin=[x for x in connin if oro+'.' in x]
							if connin:
							    for onn in connin:
							        ellam=ellam+'catch(`connectAttr '+att+' '+onn+'`);\n'
						elif aalee.upper()=="OU":
							connin=mc.listConnections(att,s=1,p=1,d=0)
							connin=[x for x in connin if oro+'.' in x]
							if connin:
							    for onn in connin:
							        ellam=ellam+'catch(`connectAttr '+onn+' '+att+'`);\n'

    if len(aalee)>=3:
        import csv
        flimane='D:\\temp\\'+aalee+'temp.csv'
        ofile  = open(flimane, "wb")
        writer = csv.writer(ofile, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
        for row in xblade:
            writer.writerow(list(row))
        ofile.close()
	a.write(ellam)
	a.close()

def ntget():
	aaee=mc.radioCollection('aaaeee',q=1,sl=1)
	aalee=mc.radioButton(aaee,q=1,l=1)
	if aalee.upper()=="F":
		mc.file("D:/temp/fTemp.ma",i=1,type='mayaAscii')
	else:
		flimane='D:\\temp\\'+aalee+'temp.txt'
		a=open(flimane,'r')
		reader=a.read()
		mel.eval(reader)
