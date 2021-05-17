#Last Updated 2013 Sept
#tool to export and load cloth cache based on character prefix 
#NitinPeter

def readf(foo,chunks=1024):
    import re
    import os
    while True:
        data=foo.read(chunks)
        if not data:
            break;
        yield data
def timestamp():
    from datetime import datetime
    abtime=datetime.now().strftime('%a, %b %d, %Y %I:%M:%S %p ')
    return abtime
def splitsum(n,itrab):
	aai=ntsplit(n,itrab)
	return map(sum,zip(*aai))	

def ntsplit(n,itrab,padV=None):
	from itertools import izip,chain,repeat
	return izip(*[chain(itrab,repeat(padV,n-1))]*n)

def combi(lis,k):
    import re
    import os
    from itertools import combinations as combis
    return [subs for subs in combis(lis,k)]
    return None
def esop(lis):
	from operator import mul
	from functools import reduce
	val=0
	for li in lis:
		val+=reduce(mul,li)
	return val
def epos(lis):
	from operator import add
	from functools import reduce
	val=0
	for li in lis:
		val*=reduce(add,li)
	return val
def ocne(s):
    return ''.join([chr(ord(so)-1) for so in s])
def oced(s):
    return ''.join([chr(ord(so)+1) for so in s])
def melbatch(bpath,ffil,bfil,mfil,glue=1,wait=0):
    import re
    import os
    import maya.mel as mel
    f=open(bpath+'/'+bfil,'w')
    loma=mel.eval('toNativePath("'+mel.eval('getenv MAYA_LOCATION')+'")')
    f.write('set var1="'+loma+'\\bin"')
    f.write('\n')
    for flie in ffil:
        f.write('%var1%\maya -batch -script "'+bpath+'/'+mfil+'" -file "'+bpath+'/'+flie+'"\n')
    if wait:
        f.write('pause')
    f.close()
    if glue:
        os.system(bpath+'/'+bfil)
        mel.eval('pause -sec 1')
        os.remove(bpath+'/'+bfil)
def mergeit(*itera):
    import re
    import os
    for values in zip(*itera):
        for value in values:
            yield value
def splitDoc(document):
    return [x.strip('\n\r').split(',') for x in open(document).read().split()]
def splitFold(path,splitter,count,req):
    import re
    import os
    retu=[]
    red=[x for x in os.listdir(path) if len(x)>=2]
    for oro in red:
        specs=[x for x in os.listdir(path+'/'+oro+'/') if len(x.split(splitter))>=count]
        if specs:
            seng=specs[0].split('_')
            sengu=[seng[i] for i in req]
            retu.append(sengu)
    return retu
def versos(pathe):
    pathf=pathe
    import re
    import os
    retu=[]
    import shutil
    specs=[x for x in os.listdir(pathe) if re.search('v(\d+)',x)]
    fold='v%02d'%(len(specs)+1)
    pathf=pathe+'\\'+fold
    os.makedirs(pathf)
    alfils=[x for x in os.listdir(pathe) if os.path.isfile(pathe+'/'+x)]
    for fila in [x for x in os.listdir(pathe) if os.path.isfile(pathe+'/'+x)]:
        shutil.move(pathe+'/'+fila,pathf+'/')
    return pathf
def polyMove(obj,ch=0):
    import maya.cmds as mc
    pc=mc.createNode('mesh')
    nobj=mc.polyUnite(obj,pc,ch=ch)
    try:
        mc.rename(obj,obj+"_old")
    except:
        pass
    mc.rename(nobj[0],obj)

def chipOff(obj,ch=0):
    import re
    import os
    import maya.cmds as mc
    pc=mc.createNode('mesh')
    obj.append(pc)
    nobj=mc.polyUnite(obj,ch=ch)
    mc.rename(nobj[1],"polyChipOff#")
    sobj=mc.polySeparate(nobj[0])
    for i in range(len(obj)):
        try:
            mc.rename(obj[i],'transform#')
        except:
            pass
        mc.rename(sobj[i],obj[i])
def curveInfo(essel):
    import maya.cmds as mc
    import re
    rethu={}
    curv={}
    for oro in essel:
        specs=oro.split('.')
        enum=re.match('.*(\d)+.*',specs[1]).group(1)
        if specs[0] in rethu.keys():
        	rethu[specs[0]][0]=rethu[specs[0]][0]+1
        else:
        	spans=mc.getAttr(mc.listRelatives(specs[0],s=1)[0]+'.spans')
        	dege=mc.getAttr(mc.listRelatives(specs[0],s=1)[0]+'.degree')
        	rethu[specs[0]]=[1,spans]
        curv[specs[0]]=float(rethu[specs[0]][0])/(rethu[specs[0]][1]+dege)
    return curv
def uvVal(aa,bb='locator1',mod=0):
    import re
    import pymel.core as pm
    import maya.api.OpenMaya as om
    geo=pm.PyNode(aa)
    loc=pm.PyNode(bb)
    pos=loc.getRotatePivot(space='world')
    try:
     	selist=om.MSelectionList()
       	selist.add(geo.name())
       	nodeDagPath=selist.getDagPath(0)
    except:
       	raise RuntimeError('maya.api.OpenMaya.MDagPath() failed on %s'%geo.name())
    mfnMesh=om.MFnMesh(nodeDagPath)
    point=om.MPoint(pos.x,pos.y,pos.z)
    space=om.MSpace.kWorld
    closestPoint,faceIdx=mfnMesh.getClosestPoint(point,space)
    uvVal=mfnMesh.getUVAtPoint(closestPoint,om.MSpace.kWorld,uvSet=mfnMesh.getUVSetNames()[0])
    if mod==0:
        return uvVal[:-1]
    if mod==2:
        return faceIdx
    if mod==1:
        faceVerts=[geo.vtx[i] for i in geo.f[faceIdx].getVertices()]
        closestVert=None
        minLength=None
        for v in faceVerts:
         	thisLength=(pos-v.getPosition(space='world')).length()
           	if minLength is None or thisLength < minLength:
           		minLength=thisLength
           		closestVert=v
        return re.findall('(\d+)',str(closestVert))[-1]
    else:
        return None
def deegi(hello,sd):
    import maya.cmds as mc
    if wholeyard('andera'):
    	temp=[x for x in mc.listHistory(sd,f=1) if x in mc.ls(typ='shadingEngine')]
    	return temp[0]
    return None
def jeedi(hello,sg):
    import maya.cmds as mc
    if wholeyard('andera'):
    	temp=[x for x in mc.listConnections(sg,s=1) if x in mc.listHistory(sg)]
    	if temp:
    		return temp[0]
	return None
def findRelatedTextureFiles(paths):
    filte={}
    import re
    import os
    import maya.cmds as mc
    filNod = mc.ls(typ=['file','mentalrayTexture','psdFileTex'])
    for x in filNod:
        fille=mc.getAttr(x+'.fileTextureName')
        if fille and os.path.exists(fille):
            if filte.has_key(fille):
                a=filte[fille]
                a=a+' '+x
                filte[fille]=a
            else:
                filte[fille]=x
    return filte
def pathsplit(name):
    import os
    basename=os.path.split(name)
    filename=os.path.splitext(basename[1])
    return (basename[0],filename[0],filename[1])
def hconvert(cmd):
    import re
    import os
    os.system(cmd)
def iconvert(sname,dname,mod=0,perc=''):
    import os
    cmd=os.path.split(__file__)[0]
    #cmd='F:'
    sized=['25%','50%','75%']
    cmd=cmd+'/change '+sname+' '
    if mod==1 or mod==2:
        cmd=cmd+'-resize '+sized[mod-1]+' '
    elif perc:
        cmd=cmd+'-resize '+perc+' '
    cmd=cmd+dname
    hconvert(cmd)
    return cmd
    
def getLinkedPattern(patho,reGex):
    import re
    import os
    tom=[x for x in os.listdir(patho) if re.match('^(.)*.ma$',x)]
    for oro in tom:
        cont=''
    	f=open(patho+'/'+oro)
    	for po in readf(f):
    		cont=cont+po
    	f.close()
    	yield re.findall(reGex,cont)