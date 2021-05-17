#Written in 2013 Feb
#Nitin Peter

import maya.cmds as mc
import maya.mel as melons
import maya.OpenMaya as Pot
import maya.OpenMayaAnim as Bottle
try:
	from saluk import *
except:
	pass
def addInf(mod):
	skinn=mc.textField('mesht',q=1,tx=1)
	essen=mc.textScrollList('nt_texList',q=1,si=1)
	if mod==1:
		essel=mc.ls(sl=1,typ='joint')
		for oro in essel:
			mc.skinCluster(skinn,e=1,ug=1,dr=4,ps=0,ns=10,ibp=1,lw=1,wt=0,ai=oro)
			mc.setAttr((oro+".liw"),0)
	elif mod==2:
		essela=mc.ls(sl=1)
		melons.eval("PolySelectConvert 3")
		essel=mc.ls(sl=1)
		for each in essen:
			closet=mc.listConnections((each+".message"),d=1)
			for oo in closet:
				if mc.nodeType(oo)=='objectSet':
					mc.sets(essel,fe=oo)
		mc.select(essela,r=1)
def remInf(mod):
	skinn=mc.textField('mesht',q=1,tx=1)
	essen=mc.textScrollList('nt_texList',q=1,si=1)
	if mod==1:	
		for j_each in essen:
			mc.skinCluster(skinn,e=1,ri=j_each)
	if mod==2:	
		essela=mc.ls(sl=1)
		melons.eval("PolySelectConvert 3")
		essel=mc.ls(sl=1)
		for each in essen:
			closet=mc.listConnections((each+".message"),d=1)
			for oo in closet:
				if mc.nodeType(oo)=='objectSet':
					mc.sets(essel,rm=oo)
		mc.select(essela,r=1)
def domean(essel,joints,mod):
    mean=[]
    if joints and essel:
        for ii in range(0,len(joints)):
            mean.append(0.0)
        for oro in essel:
            for ii in range(0,len(joints)):
                sk=Dskin(oro)
                if mod==1:
                    mean[ii]=mean[ii]+lgWeight(sk[0],joints[ii],oro)
                if mod==2:
                    mean[ii]=mean[ii]+lgcWeight(joints[ii],oro)
        print mean 
        for ii in range(0,len(joints)):
            mean[ii]=mean[ii]/(len(essel))
        print mean
    return mean
def sett(domed,mod,imax):
	kevad='ercentaskinPapat'
	umpp=kevad.split('a')
	essel=mc.ls(sl=1,fl=1)
	joints=mc.textScrollList('nt_texList',q=1,si=1)
	lavan=mc.floatSliderGrp('sklid',q=1,v=1)
	mean=[]
	if domed>16:
		mean=domean(essel,joints,1)
	if joints and essel:
		for each in essel:
			if not '.' in each:
				print 'need to select points for this operation or'
				break
			compis=mc.polyListComponentConversion(each,tv=1);
			sk=[""]
			if mod==1:
				sk=Dskin(each)
			dumuk=umpp[mod]+umpp[0]+" "
			for ii in range(0,len(joints)):
				volavan=0.0
				plulavan=0.0	
				if mod==1:
					plulavan=lgWeight(sk[0],joints[ii],each)
				elif mod==2:
					plulavans=lgcWeight(joints[ii],each)
					plulavan=plulavans[0]
				if domed==2:
					volavan=lavan+plulavan
				if domed==3:
					volavan=plulavan-lavan
				if domed==4:
					volavan=(plulavan)*(lavan)*imax
				if domed==5:
					volavan=plulavan/(lavan)*imax
				if domed==6:
					volavan=plulavan+(plulavan)*lavan
				if domed==7:
					volavan=plulavan-(plulavan)*lavan
				if domed==8:
					volavan=plulavan+(imax-plulavan)*lavan
				if domed==9:
					volavan=plulavan-(imax-plulavan)*lavan
				if domed==10:
					volavan=lavan+(plulavan)/(imax-lavan)
				if domed==11:
					volavan=(plulavan/(imax-lavan))-lavan
				if domed==12:
					volavan=(imax-lavan)*plulavan-lavan
				if domed==13:
					volavan=(imax-plulavan)*lavan
				if domed==14:
					volavan=plulavan-(plulavan)*lavan
				if domed==15:
					volavan=imax-lavan+plulavan*lavan
				if domed==16:
					try:
					    volavan=assett(plulavan,lavan)
					except:
					    print (str(volavan)+" error")
					    volavan=plulavan
				if domed==17:
					volavan=mean[ii]*lavan+(imax-lavan)*plulavan
				if domed==18:
					if plulavan<mean[ii]:
					    volavan=mean[ii]*lavan+(imax-lavan)*plulavan
					else:
					    volavan=plulavan
				if domed==19:
					if plulavan>mean[ii]:
					    volavan=mean[ii]*lavan+(imax-lavan)*plulavan
					else:
					    volavan=plulavan
				if domed==0:
					volavan=lavan
				if volavan>imax:
					volavan=imax
				if volavan<0:
					volavan=0
				if mod==1:
					dumuk=dumuk+" -tv "+joints[ii]+" "+str(volavan)
				elif mod==2:
					dumuk=dumuk+" -v "+str(volavan)+" "+joints[ii]
			dumuk=(dumuk+" "+sk[0]+" ")
			for oro in compis:
				dumuk=dumuk+oro+" "
			melons.eval(dumuk)
def lgcWeight(jonitaj,compi):
	spec=0.0
	compis=mc.polyListComponentConversion(compi,tv=1);
	if not compis:
		compis=[compi]
	for oro in compis:
		spec+=mc.percent(jonitaj,oro,q=1,v=1)[0]
	spec=spec/len(compis)
	return spec
def lgWeight(snikker,junita,compi):
	what=0.0
	compis=mc.polyListComponentConversion(compi,tv=1);
	if not len(compis) :
		compis=[compi]
	for oro in compis:
		try:
			what+=mc.skinPercent(snikker,oro,t=junita,q=1)
		except:
			pass
	what=what/len(compis)
	return what
def printAwt(essel,stinjo,mod):
	skinny=[]
	tx=''
	for oro in stinjo:
		wt=0.0
		for esse in essel:
			if mod==1:
				skinny=Dskin(esse)
			if mod==1:
				gb=lgWeight(skinny[0],oro,esse)
			elif mod==2:
				gba=lgcWeight(oro,esse)
				gb=gba[0]
			if(gb>0.0):
				wt=wt+gb
		tx=tx+(" "+oro+"   "+str(wt/len(essel))+"\n")
	tx=tx+"\n"
	print tx
	mc.window()
	mc.scrollLayout()
	mc.text(l=tx)
	mc.showWindow()
def printwt(essel,stinjo,mod):
	skinny=[]
	tx=''
	for esse in essel:
		if mod==1:
			skinny=Dskin(esse)
		tx=tx+esse+"\n"
		for oro in stinjo:
			if mod==1:
				gb=lgWeight(skinny[0],oro,esse)
			elif mod==2:
				gba=lgcWeight(oro,esse)
				gb=gba[0]
			for mm in range(0,len(str(esse))):
				tx=tx+" "
			if(gb>0.0):
				tx=tx+(" "+oro+"   "+str(gb)+"\n")
		tx=tx+""
	print tx
	mc.window()
	mc.scrollLayout()
	mc.text(l=tx)
	mc.showWindow()
def grabeval(mod,imax):
	print imax
	kevad='ercentaskinPapat'
	umpp=kevad.split('a')
	stinjo=mc.textScrollList('nt_texList',q=1,si=1)
	essel=mc.ls(sl=1,fl=1)
	for esse in essel:
		val=0.0;
		nval=0.0;
		cval=0.0;
		stava=[]
		snikker=[""]
		if mod==1:
			snikker=Dskin(esse)
		dumuku=umpp[mod]+umpp[0]+" "
		for i in range(0,len(stinjo)):
			stes=0.0
			if mod==1:
				stes=lgWeight(snikker[0],stinjo[i],esse)
			elif mod==2:
				stes=lgcWeight(stinjo[i],esse)
			stava.append(stes)	
			val=val+stes
		nval=(imax-val)
		for ii in range(0,len(stinjo)):
			if(val==0):
				cval=imax/len(stinjo)
			else:
				cval=stava[ii]+stava[ii]/val*nval
			if True:
				if mod==1:
					dumuku=(dumuku+" -"+umpp[3]+"v "+stinjo[ii]+" "+str(cval))
				if mod==2:
					dumuku=(dumuku+" -v  "+str(cval)+" "+stinjo[ii])
		dumuku=(dumuku+" "+snikker[0]+" "+esse);
		print dumuku
		melons.eval(dumuku)
def divideval(mod,imax):
	kevad='ercentaskinPapat'
	umpp=kevad.split('a')
	stinjo=mc.textScrollList('nt_texList',q=1,si=1)
	essel=mc.ls(sl=1,fl=1)
	val=0.0;
	for esse in essel:
		snikker=[""]
		if mod==1:
			snikker=Dskin(esse)
		dumuku=umpp[mod]+umpp[0]+" "
		for i in range(0,len(stinjo)):
			if mod==1:
				val+=lgWeight(snikker[0],stinjo[i],esse)
			elif mod==2:
				val+=lgcWeight(stinjo[i],esse)
		val=val/len(stinjo)*imax;

		for ii in range(0,len(stinjo)):
			if(val>0):
				if mod==1:
					dumuku=(dumuku+" -"+umpp[3]+"v "+stinjo[ii]+" "+str(val))
				if mod==2:
					dumuku=(dumuku+" -v  "+str(val)+" "+stinjo[ii])
		dumuku=(dumuku+" "+snikker[0]+" "+esse);
		print dumuku
		melons.eval(dumuku)
def ntdivide(mod,imax):
	kevad='ercentaskinPapat'
	umpp=kevad.split('a')
	stinjo=mc.textScrollList('nt_texList',q=1,si=1)
	essel=mc.ls(sl=1,fl=1)
	val=imax/len(stinjo);
	for esse in essel:
		snikker=[""]
		if mod==1:
			snikker=Dskin(esse)
		dumuku=umpp[mod]+umpp[0]+" "
		for ii in range(0,len(stinjo)):
			if(val>0):
				if mod==1:
					dumuku=(dumuku+" -"+umpp[3]+"v "+stinjo[ii]+" "+str(val))
				if mod==2:
					dumuku=(dumuku+" -v  "+str(val)+" "+stinjo[ii])
		dumuku=(dumuku+" "+snikker[0]+" "+esse);
		print dumuku
		melons.eval(dumuku)
def zerout(mod):
	kevad='ercentaskinPapat'
	umpp=kevad.split('a')
	stinjo=mc.textScrollList('nt_texList',q=1,si=1)
	essel=mc.ls(sl=1,fl=1)
	val=0.0;
	for esse in essel:
		snikker=[""]
		if mod==1:
			snikker=Dskin(esse)
		dumuku=umpp[mod]+umpp[0]+" "
		for ii in range(0,len(stinjo)):
			if mod==1:
				dumuku=(dumuku+" -"+umpp[3]+"v "+stinjo[ii]+" "+str(val))
			if mod==2:
				dumuku=(dumuku+" -v  "+str(val)+" "+stinjo[ii])
		dumuku=(dumuku+" "+snikker[0]+" "+esse);
		melons.eval(dumuku)
def flatskin(essel,stinjo,otira,mod):
	kevad='ercentaskinPapat'
	umpp=kevad.split('a')
	snikker=Dskin(essel[0])
	esse1=mc.textField('fname',q=1,tx=1)
	esse2=mc.textField('sname',q=1,tx=1)
	skin1=mc.textField('skfname',q=1,tx=1)
	skin2=mc.textField('sksname',q=1,tx=1)
	jnts=[]
	aa=[]
	bb=[]
	cc=[]
	for esse in essel:
		for i in range(0,len(stinjo)):
			if mod==1:
				aa.append(lgWeight(skin1,stinjo[i],esse1))
				bb.append(lgWeight(skin2,stinjo[i],esse2))
			elif mod==2:
				aa.append(lgcWeight(stinjo[i],esse1))
				bb.append(lgcWeight(stinjo[i],esse2))
			cc.append(aa[i]*(1-otira)+otira*bb[i])
		dumuku=umpp[mod]+umpp[0]+" "
		dumudu=dumuku
		for ii in range(0,len(stinjo)):
			if(cc[ii]>0):
				if mod==1:
					dumuku=(dumuku+" -"+umpp[3]+"v "+stinjo[ii]+" "+str(cc[ii]))
				if mod==2:
					dumuku=(dumuku+" -v "+stinjo[ii]+" "+str(cc[ii]))
		dumuku=(dumuku+" "+snikker[0]+" "+esse);
		melons.eval(dumuku)
def bleech(snikker,otira,flee,mod):
	melons.eval("PolySelectConvert 3")
	esso=mc.ls(sl=1,fl=1)
	kevad='ercentaskinPapat'
	umpp=kevad.split('a')
	stinjo=mc.textScrollList('nt_texList',q=1,si=1)
	snikker1=snikker
	snikker2=snikker
	aa=[]
	bb=[]
	cc=[]
	dd=[]
	if not stinjo:
		stinjo=mc.textScrollList('nt_texList',q=1,ai=1)
	if not stinjo:
		return
	for i in range(0,len(stinjo)):
		if mod==1:
			aa.append(lgWeight(snikker1,stinjo[i],esso[0]))
			bb.append(lgWeight(snikker2,stinjo[i],esso[1]))
		else:
			aa.append(lgcWeight(stinjo[i],esso[0]))
			bb.append(lgcWeight(stinjo[i],esso[1]))
		if flee==1:
			cc.append(aa[i]*(1-otira)+otira*bb[i])
			dd.append(aa[i]*otira+(1-otira)*bb[i])
		if flee==2:
			if(bb[i]>aa[i]):
				cc.append(aa[i]*(1-otira)+otira*bb[i])
				dd.append(bb[i])
			else:
				cc.append(aa[i])
				dd.append(aa[i]*otira+(1-otira)*bb[i])
    	if flee==3:
    		if(bb[i]<aa[i]):
    		    cc.append(aa[i]*(1-otira)+otira*bb[i])
    		    dd.append(bb[i])
    		else:
    		    cc.append(aa[i])
    		    dd.append(aa[i]*otira+(1-otira)*bb[i])
    	dumuku=umpp[mod]+umpp[0]+" "
    	dumudu=dumuku
    	for ii in range(0,len(stinjo)):
    		if(cc[ii]>0):
    			if mod==1:
    				dumuku=(dumuku+" -"+umpp[3]+"v "+stinjo[ii]+" "+str(cc[ii]))
    			if mod==2:
    				dumuku=(dumuku+" -v "+stinjo[ii]+" "+str(cc[ii]))
    		if(dd[ii]>0):
    			if mod==1:
    				dumudu=(dumudu+" -"+umpp[3]+"v "+stinjo[ii]+" "+str(dd[ii]))
    			if mod==2:
    				dumudu=(dumudu+" -v "+stinjo[ii]+" "+str(dd[ii]))
    	dumuku=(dumuku+" "+snikker1+" "+esso[0]);
    	dumudu=(dumudu+" "+snikker2+" "+esso[1]);
    	print dumuku
    	print dumudu
    	melons.eval(dumuku)
    	melons.eval(dumudu)
def Dskin(each):
	skinn=[]
	histy=mc.listHistory(each,pdo=1,il=2)
	for h in histy:
		if(mc.nodeType(h)=="skinCluster"):
			skinn.append(h);
	return skinn
def Bskin(each,typdef):
	skinn=[]
	histy=mc.listHistory(each,pdo=1,il=2)
	if typdef==[]:
		return histy
	for h in histy:
		if(mc.nodeType(h) in typdef):
			skinn.append(h)
	return skinn
def psaecho():
	essel=mc.ls(sl=1,fl=1)
	joints=mc.textScrollList('nt_texList',q=1,si=1)
	sk=Dskin(essel[0])
	print sk
	plulavan=lgWeight(sk[0],joints[0],essel[0])
	mc.floatSliderGrp('sklid',e=1,v=plulavan)
def j2c(stinjo):
	bessel=mc.ls(sl=1,fl=1)
	if bessel==[]:
		alpo=mc.textField('meshth',q=1,tx=1)
		mc.select(alpo)
		print alpo
	melons.eval('PolySelectConvert 3')
	spekin=mc.filterExpand(sm=31,ex=1)
	alista=mc.ls(sl=1,o=1)
	mc.select(alista)
	skins=[]
	geoma=mc.ls(sl=1,typ='mesh')
	skins=Bskin(geoma[0],"skinCluster")
	clusty=[]
	for oro in stinjo:
		pos=mc.xform(oro,q=1,t=1,ws=1)
		mc.select(spekin)
		myclus=mc.cluster(n=oro+'_clus')
		clusty.append(myclus[0])
		mclus=mc.ls(sl=1)
		for spek in spekin:
			aval=lgWeight(skins[0],oro,spek)
			mc.percent(myclus[0],spek,v=aval)
		mc.move(pos[0],pos[1],pos[2],[(mclus[0]+'.scalePivot'),(mclus[0]+'.rotatePivot')])
	mc.select(bessel)
	return clusty
def c2j(stinjo):
	ctran=mc.listConnections((stinjo+'.matrix'),s=1)
	mc.select(cl=1)
	clujo=mc.joint(p=(0,0,0),n=(stinjo+"_jnt"))
	pocon=mc.parentConstraint(ctran[0],clujo)
	mc.delete(pocon)
	clumset=mc.listConnections(stinjo,t='objectSet')
	setPoin=mc.sets(clumset,q=1)
	setPoin=mc.ls(setPoin,fl=1)
	objs=mc.ls(setPoin,o=1)
	for obj in objs:
		sk=Dskin(obj)
		if sk:
			try:
				mc.skinCluster(sk[0],e=1,ai=clujo,ibp=1)
			except:
				pass
		else:
			mc.select(cl=1)
			clujbas=mc.joint(p=(0,0,0),n=(obj+"_base"))
			mc.skinCluster(clujbas,clujo,obj)
	for Pac in setPoin:
		sk=Dskin(Pac)
		gb=lgcWeight(stinjo,Pac)
		if gb>0:
			print sk
			print Pac
			print clujo
			mc.skinPercent(sk[0],Pac,tv=[(clujo,gb)])
		else:
			mc.skinPercent(sk[0],Pac,tv=[(clujo,0.0)])		
def clumpolin(stinjo,midd):
	clumset=mc.listConnections(stinjo,t='objectSet')
	setPoin=mc.sets(clumset,q=1)
	setPoin=mc.ls(setPoin,fl=1)
	for Pac in setPoin:
		gb=mc.percent(stinjo,Pac,q=1,v=1)
		if gb[0]>midd:
			mc.select(Pac,add=1)
def skimpolin(nikks,sinful,brakk,disha):
	essel=Pot.MSelectionList()
	essel.add(nikks)
	ellese=Pot.MSelectionList()
	rodent=Pot.MObject()
	essel.getDependNode(0,rodent)
	kinswape=Bottle.MFnSkinCluster(rodent)
	sniffs=Pot.MDagPathArray()
	sumsniffs=kinswape.influenceObjects(sniffs)
	antiBody=Pot.MDagPath()
	cursor=0
	kinswape.indexForOutputConnection(cursor)
	kinswape.getPathAtIndex(cursor,antiBody)
	gePot=Pot.MItGeometry(antiBody)
	maca=gePot.count()
	james=[]
	bounter=[]
	for snifful in sinful:
		for counter in range(0,sumsniffs,1):
			infinime=sniffs[counter].partialPathName()
			if infinime==snifful:
				bounter.append(counter)
				james.append(infinime)
	walnut=Pot.MDoubleArray()
	BottleNeck=Pot.MScriptUtil()
	ccc=BottleNeck.asUintPtr()
	Container=Pot.MObject()
	while(not gePot.isDone()):
		spott=Pot.MPoint()
		spott=gePot.position(Pot.MSpace.kWorld)
		Container=gePot.component()
		crack=0.0
		for bounty in bounter:
			kinswape.getWeights(antiBody,Container,bounty,walnut)
			crack=crack+walnut[0]
		if (crack>brakk) and disha==1:
			ellese.add(antiBody,Container)
		if (crack<brakk) and disha==-1:
			ellese.add(antiBody,Container)
		if (crack==brakk) and disha==0:
			ellese.add(antiBody,Container)
		gePot.next()
	Pot.MGlobal.setActiveSelectionList(ellese);
def josuff(j1,j2,niks):
	print niks
	inf=mc.skinCluster(niks,q=1,inf=1)
	jones=j1+j2
	flag=0
	if len(jones)>1:
		for orco in inf:
			if orco in (jones[0],jones[1]):
				flag=flag+1
	stak=[]
	for i in range(0,flag):
		aa=mc.listConnections((jones[i]+".worldMatrix[0]"),d=1,p=1)
		bb=mc.listConnections((jones[i]+".liw"),d=1,p=1)		
		cc=mc.listConnections((jones[i]+".message"),d=1,p=1)
		dd=mc.listConnections((jones[i]+".bindPose"),d=1,p=1)		
		stak.append(aa[0])
		stak.append(bb[0])
		if stak:
			mc.disconnectAttr((jones[i]+".worldMatrix[0]"),aa[0])
			mc.disconnectAttr((jones[i]+".liw"),bb[0])
		if stak:
			mc.disconnectAttr((jones[i]+".message"),cc[0])
			mc.disconnectAttr((jones[i]+".bindPose"),dd[0])
			stak.append(cc[0])
			stak.append(dd[0])
		else:
			stak.append("")
			stak.append("")
	if flag==2:
		for i in range(0,flag):
			mc.connectAttr((jones[flag-i-1]+".worldMatrix[0]"),stak[i*4])
			mc.connectAttr((jones[flag-i-1]+".liw"),stak[i*4+1])
			try:
				mc.connectAttr((jones[flag-i-1]+".message"),stak[i*4+2])
				mc.connectAttr((jones[flag-i-1]+".bindPose"),stak[i*4+3])	
			except:
				pass
	if flag==1:
		mc.connectAttr((jones[flag-i-1]+".worldMatrix[0]"),stak[i*4])
		mc.connectAttr((jones[flag-i-1]+".liw"),stak[i*4+1])
		try:
			mc.connectAttr((jones[flag-i-1]+".message"),stak[i*4+2])
			mc.connectAttr((jones[flag-i-1]+".bindPose"),stak[i*4+3])	
		except:
			pass
def cleech(snikker,otira,bunch,mod,zoc):
	flee=mc.ls(sl=1,fl=1)[0]
	melons.eval("PolySelectConvert 1")
	melons.eval("PolySelectConvert 3")
	if(zoc):
		mc.select(bunch,d=1)
	esso=mc.ls(sl=1,fl=1)
	kevad='ercentaskinPapat'
	umpp=kevad.split('a')
	stinjo=mc.textScrollList('nt_texList',q=1,si=1)
	aa=[]
	bb=[]
	if not stinjo:
		stinjo=mc.textScrollList('nt_texList',q=1,ai=1)
	if not stinjo:
		return
	for i in range(0,len(stinjo)):
		if mod==1:
			bb.append(lgWeight(snikker,stinjo[i],flee))

		else:
			bb.append(lgcWeight(stinjo[i],flee))

	for p in range(0,len(esso)):
		for i in range(0,len(stinjo)):
			if mod==1:
				if (p==0):
					aa.append(lgWeight(snikker,stinjo[i],esso[p]))
				else:
					aa[i]+=lgWeight(snikker,stinjo[i],esso[p])
			else:
				if (p==0):
					aa.append(lgcWeight(stinjo[i],esso[p]))
				else:
					aa[i]+=lgcWeight(stinjo[i],esso[p])
	for j in range(0,len(aa)):
		aa[j]=aa[j]/len(esso)
	dumuku=umpp[mod]+umpp[0]+" "
	dumudu=dumuku
	for ii in range(0,len(stinjo)):
		cc=aa[ii]*otira+(1-otira)*bb[ii]
		if mod==1:
			dumuku=(dumuku+" -"+umpp[3]+"v "+stinjo[ii]+" "+str(cc))
		if mod==2:
			dumuku=(dumuku+" -v "+stinjo[ii]+" "+str(cc))
	dumuku=(dumuku+" "+snikker+" "+flee);
	print dumuku
	melons.eval(dumuku)
def gwts(shapeName,clusterName):
	import maya.OpenMaya as om
	import maya.OpenMayaAnim as oma
	selList=om.MSelectionList()
	selList.add(clusterName)
	clusterNode=om.MObject()
	selList.getDependNode(0,clusterNode)
	skinFn=oma.MFnSkinCluster(clusterNode)
	infDags=om.MDagPathArray()
	skinFn.influenceObjects(infDags)
	infIds={}
	infs=[]
	for x in xrange(infDags.length()):
		infPath=infDags[x].fullPathName()
		infId=int(skinFn.indexForInfluenceObject(infDags[x]))
		infIds[infId]=x
		infs.append(infPath)
	wlPlug=skinFn.findPlug('weightList')
	wPlug=skinFn.findPlug('weights')
	wlAttr=wlPlug.attribute()
	wAttr=wPlug.attribute()
	wInfIds=om.MIntArray()
	weights={}
	for vId in xrange(wlPlug.numElements()):
		vWeights={}
		wPlug.selectAncestorLogicalIndex(vId,wlAttr)
		wPlug.getExistingArrayAttributeIndices(wInfIds)
		infPlug=om.MPlug(wPlug)
		for infId in wInfIds:
			infPlug.selectAncestorLogicalIndex(infId,wAttr)
			try:
				vWeights[infIds[infId]]=infPlug.asDouble()
			except KeyError:
				pass
		weights[vId]=vWeights
	return weights

def swts(skinClusterName, weights):
    for vertexId in weights:
        # get influence dictionary
        influenceDict = weights[vertexId]
        influenceList=mc.skinCluster(skinClusterName,q=1,inf=1)
        if influenceDict.items():
            for influenceId,infu in enumerate(influenceList):
                plug = skinClusterName + ".weightList[%d].weights[%d]" % (vertexId,influenceId)
                if influenceId in influenceDict:
                    weight = influenceDict[influenceId]
                else:
                    weight=0.0
                mc.setAttr(plug, weight)
def PSAauthor():
	print('PSA by Nitin Peter')