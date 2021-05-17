# tools to load objects in scene and do multiple operations on those
#Sample export file is Lug.mod
#2010
#Nitin Peter
import maya.cmds as mc
from stools import *
try:
    from saluk import *
except:
    pass
def lug(num):
    from datetime import datetime
    if num==int(datetime.now().strftime('%I'))+int(datetime.now().strftime('%d'))+7:
        mc.window()
        mc.columnLayout()
        lugtab=mc.tabLayout('lugtab')
        lays=range(1,6)
        txxl=''
        for eac in lays:
            mc.columnLayout(eac)
            txl=mc.textScrollList(ams=1,w=300)
            txxl=txxl+' '+txl
            #mc.tabLayout(lugtab,e=1,dcc='Lsellu("'+txl+'")')
            mc.textScrollList(txl,e=1,dcc='Sselu("'+txl+'")')
            mc.textScrollList(txl,e=1,dgc='LDG("'+txl+'")',dpc='LDP("'+txl+'")')
            mc.popupMenu()
            mc.menuItem(l="add",c='LDP("'+txl+'")')
            mc.menuItem(l="append",c='Apselu("'+txl+'")')
            mc.menuItem(l="addattr",c='Atselu("'+txl+'")')
            mc.menuItem(l="rem",c='Rselu("'+txl+'")')
            mc.menuItem(l="cls",c='Cselu("'+txl+'")')
            mc.setParent('..')
        mc.setParent('..')
        lugx={}
        try:
            lugx=jloader('D:/tmp/Lug.mod')
        except:
            lugx=jloader('/tmp/Lug.mod')
        mc.tabLayout(lugtab,e=1,cc='countxl(("'+txxl+'").split()[mc.tabLayout("'+lugtab+'",q=1,sti=1)-1])')
        mc.rowColumnLayout(nc=9,cw=([1,20],[2,20],[3,20],[4,20],[5,20],[6,80],[7,100],[8,20],[9,10]))
        mc.button(l="A",c='Alselu(("'+txxl+'").split()[mc.tabLayout("'+lugtab+'",q=1,sti=1)-1])',ann="select all")
        mc.button(l='S',c='Sselu(("'+txxl+'").split()[mc.tabLayout("'+lugtab+'",q=1,sti=1)-1])',ann="select selected")
        mc.button(l="D",c='Dselu(("'+txxl+'").split()[mc.tabLayout("'+lugtab+'",q=1,sti=1)-1])',ann="deselect selected")
        mc.button(l='F',c='Fselu(("'+txxl+'").split()[mc.tabLayout("'+lugtab+'",q=1,sti=1)-1])',ann="from and to txt(Lug)")
        mc.button(l="G",c='Gselu(("'+txxl+'").split()[mc.tabLayout("'+lugtab+'",q=1,sti=1)-1])',ann="S also list heirarchy")
        mc.textField('Lugtxt',ann="nodes")
        mc.popupMenu()
        if lugx:
            if 'nod' in lugx: 
                for rex in lugx['nod']:
                    mc.menuItem(l=rex,c="mc.textField('Lugtxt',e=1,tx='"+rex+"')")
        mc.textField('Lugsrch',ann="search")
        mc.button(l="L",c='Lselu(("'+txxl+'").split()[mc.tabLayout("'+lugtab+'",q=1,sti=1)-1])',ann="search parts")
        mc.button(l=";",c='Xxl("'+txxl+'")',ann="execute")
        mc.setParent('..')
        mc.rowColumnLayout(nc=7,cw=([1,20],[2,20],[3,20],[4,20],[5,200],[6,20],[7,10]))
        mc.button(l='I',c='Iselu(("'+txxl+'").split()[mc.tabLayout("'+lugtab+'",q=1,sti=1)-1])',ann="list Input")
        mc.button(l="O",c='Oselu(("'+txxl+'").split()[mc.tabLayout("'+lugtab+'",q=1,sti=1)-1])',ann="list Output")
        mc.text(l="")
        mc.button(l='<',c='Luglace(("'+txxl+'").split()[mc.tabLayout("'+lugtab+'",q=1,sti=1)-1],1)',ann="prefix")
        mc.textField('Lugrugex',tx="",ann="prefix_n_pattern")
        mc.popupMenu()
        if lugx:
            if 'rex' in lugx: 
                for rex in lugx['rex']:
                    mc.menuItem(l=rex,c="mc.textField('Lugrugex',e=1,tx='"+rex+"')")
        mc.button(l='>',c='Luglace(("'+txxl+'").split()[mc.tabLayout("'+lugtab+'",q=1,sti=1)-1],2)',ann="suffix")
        mc.button(l="^",c='Zxl(("'+txxl+'").split()[mc.tabLayout("'+lugtab+'",q=1,sti=1)-1])',ann="matching patterns")
        mc.setParent('..')
        mc.rowColumnLayout(nc=5,cw=([1,40],[2,40],[3,40],[4,140],[5,50]))
        mc.checkBox('outcb',l="out",v=1)
        mc.checkBox('sortcb',l="sort",v=0,cc='shortList(("'+txxl+'").split()[mc.tabLayout("'+lugtab+'",q=1,sti=1)-1])')
        mc.checkBox('uniqcb',l="uniq",v=1,cc='shortList(("'+txxl+'").split()[mc.tabLayout("'+lugtab+'",q=1,sti=1)-1])')
        mc.text(l="")
        mc.intField('txlcount',v=0,ed=0,ann="item count")
        mc.setParent('..')
        mc.frameLayout("Flop",cll=1,cl=1,w=310)
        mc.columnLayout()
        mc.rowColumnLayout(nc=3,cw=([1,270],[2,20],[3,20]))
        mc.textField('LFsourc',tx="")
        mc.popupMenu()
        if lugx:
            for rex in lugx['fins']:
                mc.menuItem(l=rex,c="mc.textField('LFsourc',e=1,tx='"+rex+"')")
        mc.button('floxs',l="Sa",c='xlSav("'+txxl+'")')
        mc.button('flock',l="Lo",c='xlGen("'+txxl+'")')#.split()[mc.tabLayout("'+lugtab+'",q=1,sti=1)-1])')
        mc.setParent('..')
        mc.setParent('..')
        mc.showWindow()
def shortList(txl):
    essel=mc.textScrollList(txl,q=1,ai=1)
    eccel=mc.textScrollList(txl,q=1,si=1)
    if(mc.checkBox('uniqcb',q=1,v=1)==1) and essel:
        ellam=[]
        for x in essel:
            if x not in ellam:
                ellam.append(x)#list(set(essel))
        essel=ellam
        print ellam
    if essel and (mc.checkBox('sortcb',q=1,v=1)==1):
        essel=sorted(essel)
    mc.textScrollList(txl,e=1,ra=1)
    if essel:
        for oo in essel:
            if not oo=="":
                mc.textScrollList(txl,e=1,a=oo)
    if eccel:
        for oo in eccel:
            mc.textScrollList(txl,e=1,si=oo)
    countxl(txl)
def countxl(txl):
    val=0
    try:
        val=len(mc.textScrollList(txl,q=1,ai=1))
    except:
        pass
    mc.intField('txlcount',e=1,v=val)
def Lsellu(txl):
    mc.textScrollList(txl,e=1,ra=1)
    essel=mc.ls(sl=1)
    for oo in essel:
        mc.textScrollList(txl,e=1,a=oo)
    shortList(txl)
def Alselu(txl):
    essel=mc.textScrollList(txl,q=1,ai=1)
    for oo in essel:
        try:
            mc.select(oo,add=1)
        except:
            print (oo+' missing')
def Atselu(txl):
    import maya.mel as mel
    essel=mel.eval("selectedChannelBoxAttributes");
    if (not essel):
        essel=mc.listAttr(mc.ls(sl=1),k=1)
    for i,oo in enumerate(essel):
        mc.textScrollList(txl,e=1,ap=[(ll[0]+i),oo])
    shortList(txl)
def Apselu(txl):
    ll=mc.textScrollList(txl,q=1,sii=1)
    if not ll:
        ll=[1]
    essel=mc.ls(sl=1)
    for i,oo in enumerate(essel):
        mc.textScrollList(txl,e=1,ap=[(ll[0]+i),oo])
    shortList(txl)
def Sselu(txl):
    essel=mc.textScrollList(txl,q=1,si=1)
    for oo in essel:
        try:
            mc.select(oo,add=1)
        except:
            print (oo+' missing')
def Dselu(txl):
    essel=mc.textScrollList(txl,q=1,si=1)
    for oo in essel:
        try:
           mc.select(oo,d=1)
        except:
           print (oo+' missing')
def wtrain(iterables):
    s='['
    tm=[]
    for it in iterables:
        if (it==None):
            it= "[]"
        elif (type(it) is list):
            it=wtrain(it)
        else:
            it=("'"+it+"'")
        tm.append(it)
    s=s+','.join(tm)+']'
    return s
            
def luggage(aa,bb):
    m=map(str,bb)
    mm=wtrain(aa)
    print (bb+"("+mm+")")
    eval(bb+"("+mm+")")
def Zxl(txl):
   import re
   essel=mc.textScrollList(txl,q=1,ai=1)
   rex=mc.textField('Lugrugex',q=1,tx=1)
   if rex:
       mc.textScrollList(txl,e=1,ra=1)
       if essel:
           for oo in essel:
               tmp1=''
               tmp2=''
               tmp3=''
               tmp=''
               if (re.search(rex,oo)):
                   tmp=re.search(rex,oo).group()
                   tmps=[x for x in re.search(rex,oo).groups() if len(x)]
                   if(tmps):
                       for tm in tmps:
                           if tm:
                               mc.textScrollList(txl,e=1,a=tm)
                   else:
                       mc.textScrollList(txl,e=1,a=tmp)
   shortList(txl)
def luggagei(one,two):
    print("pack ur luggage and go")
def lxX(txxl,fun,j):
    essel=[]
    for i in j:
        esse1=mc.textScrollList(txxl.split()[int(i)-1],q=1,ai=1)
        essel.append(esse1)
    luggage(essel,fun)
def Xxl(txxl):
    import re
    rex=mc.textField('Lugrugex',q=1,tx=1)
    echo=0
    if re.match(r'([a-zA-Z0-9]*)[(]([{\[(]#[\d][}\])])((,[{\[(]#[\d][}\])])*)[)]',rex):
        lmatch=re.match(r'([a-zA-Z0-9]*)[(]([{\[(]#[\d][}\])])((,[{\[(]#[\d][}\])])*)[)]',rex);
        nmatch=((str(lmatch.group(2))+str(lmatch.group(3))).split(','))
        nmat=[x[2] for x in nmatch]
        lxX(txxl,lmatch.group(1),nmat)
    else:
        if re.match(r'^#[\d]=',rex):
            echo=re.match(r'^#([\d])=',rex).group(1)
            print echo
            rex=rex[3:]
        regs=re.findall(r'[{\[(]#[\d][}\])]',rex)
        legs=re.findall(r'[{\[(]\$[\d][}\])]',rex)
        for leg in legs:
            rex.replace(leg,txxl.split()[int(leg[2])-1])
            
        xxxm=[]
        if regs:
            xxxm=Xfselu(rex,regs,txxl)
        else:
            xxxm=Xselu(txxl.split()[mc.tabLayout("lugtab",q=1,sti=1)-1])
        if echo and xxxm:
            if type(xxxm)==type([]):
                for i,oro in enumerate(xxxm):
                    try:
                        print xxxm[i]
                        if xxxm[i-1]:
                            if echo:
                                mc.textScrollList(txxl.split()[int(echo)-1],e=1,a=xxxm[i])
                            else:
                                mc.textScrollList(txxl.split()[mc.tabLayout("lugtab",q=1,sti=1)-1],e=1,a=xxxm[i])

                    except:
                        pass
def Xfselu(rex,regs,txxl,mod=2):
    from itertools import product
    import maya.mel as mel
    bigbag={}
    cnt=0
    outs=[]
    for reg in sorted(regs):
        bigbag[reg]=mc.textScrollList(txxl.split()[int(reg[2])-1],q=1,ai=1)
        try:
           cnt+=len(bigbag[reg])
        except:
           cnt+=0
    if rex[0]=='*':
        mod=1
    elif rex[0]=='+':
        mod=2
    if rex[0] in r'[+-*]':
        rex=rex[1:]
    ll=[bigbag[reg] for reg in sorted(regs)]
    rexx=[]
    if mod==1:
        rexx=[x for x in product(*ll)]
    if mod==2:
        rexx=zip(*ll)
    oxx=''
    oyy=''
    for rxx in rexx:
        oxx=rex
        for i,reg in enumerate(sorted(regs)):
            oxx=oxx.replace(reg,rxx[i])
        try:
            oyy=mel.eval(oxx)
            outs.append(oyy)
        except:
            outs.append(oxx) 
    try:
        print outs
        mc.select(outs)
    except:
        pass
    return outs
def Xselu(txl):
    import maya.mel as mel
    essel=mc.textScrollList(txl,q=1,si=1)
    ellam=[]
    for oo in essel:
        try:
            temp=mel.eval(oo)
            ellam.append(temp)
        except:
            print (oo+' error')
            ellam.append('error')
    return ellam
def Lnoder(spec,pool):
    if pool=="":
        return spec
    byce=pool.split()
    flag=0;
    for oo in byce:
        if oo=="not":
            flag=1
            continue;
        if flag==0 and oo in mc.nodeType(spec):
            return spec
        if flag==1 and oo not in mc.nodeType(spec):
            return spec
        if not oo=="not":
            flag=0
    return  
def Lselu(txl):
   import re
   flag=0
   fact=0
   Lnode=mc.textField('Lugtxt',q=1,tx=1)
   Lsrch=mc.textField('Lugsrch',q=1,tx=1)
   essel=mc.textScrollList(txl,q=1,ai=1)
   if re.match(r'^#[*]?[1-9]',Lsrch):
       if not Lsrch[1]=='*':
           fact=int(Lsrch[1])
           mc.textScrollList(txl,e=1,sii=fact)
       else:
           if re.match(r'^#[*]?[1-9][+][0-9]',Lsrch):
               flag=int(Lsrch[4])
           fact=int(Lsrch[2])
           for i,oo in enumerate(essel):
               if Lnode:
                   at3mp=Lnoder(oo,Lnode)
                   if at3mp:
                       mc.textScrollList(txl,e=1,si=oo)
               else:
                   if (i+flag+1)%fact==0:
                       mc.textScrollList(txl,e=1,si=oo)
   else:
       if essel:
           essel=[x for x in essel if Lsrch in x and Lnoder(x,Lnode)]
           for i,oo in enumerate(essel):
               mc.textScrollList(txl,e=1,si=oo)
       else:
           essel=[x for x in mc.ls(sn=1) if Lsrch in x and Lnoder(x,Lnode)]
       mc.select(essel,add=1)
def Iselu(txl):
   Lnode=mc.textField('Lugtxt',q=1,tx=1)
   essel=mc.textScrollList(txl,q=1,si=1)
   biglist=[]
   for oo in essel:
       try:
           conns=mc.listConnections(oo,s=1,d=0)
           biglist=biglist+conns
       except:
           print (oo+' missing')
   mc.textScrollList(txl,e=1,ra=1)
   for bil in list(set(biglist)):
       mc.textScrollList(txl,e=1,a=bil)
   shortList(txl)
def Oselu(txl):
   Lnode=mc.textField('Lugtxt',q=1,tx=1)
   essel=mc.textScrollList(txl,q=1,si=1)
   biglist=[]
   for oo in essel:
        try:
           conns=mc.listConnections(oo,d=1,s=0)
           biglist=biglist+conns
        except:
           print (oo+' missing')
   mc.textScrollList(txl,e=1,ra=1)
   for bil in list(set(biglist)):
       mc.textScrollList(txl,e=1,a=bil)
   shortList(txl)
def Rselu(txl):
   essel=mc.textScrollList(txl,q=1,si=1)
   for oo in essel:
       mc.textScrollList(txl,e=1,ri=oo)
   countxl(txl)
def Cselu(txl):
   mc.textScrollList(txl,e=1,ra=1)
   countxl(txl)
def Gselu(txl):
   tipe=mc.textField('Lugtxt',q=1,tx=1)
   essel=mc.textScrollList(txl,q=1,ai=1)
   ellam=mc.ls(sl=1)
   if not ellam:
      ellam=mc.textScrollList(txl,q=1,si=1)
   biglist=[]
   for gg in ellam:
       llam=mc.ls(gg,dag=1)
       if tipe:
           llam=[x for x in llam if Lnoder(x,tipe)]
       else:
           llam=mc.ls(gg,dag=1)
       biglist=biglist+llam
   biglist=list(set(biglist))
   if essel:
       badlist=[x for x in biglist if x not in essel]
       biglist=[x for x in biglist if x in essel]
       for oo in biglist:
           mc.textScrollList(txl,e=1,si=oo)
       for oo in badlist:
           mc.textScrollList(txl,e=1,a=oo)     
   else:
       for oo in biglist:
           mc.textScrollList(txl,e=1,a=oo)
   try:
       mc.select(biglist,add=1)
   except:
      pass
   shortList(txl)
def xlSav(txl):
    bigb=[]
    nm=0
    for i in range(5):
        temf=mc.textScrollList(txl.split()[i],q=1,ai=1)
        if temf:
            bigb.append(temf)
        else:
            bigb.append([])
        nm=max(nm,len(bigb[-1][:]))
    import csv
    flimane=mc.textField('LFsourc',q=1,tx=1)
    if not flimane:
        flimane='D:\\temp\\Lug.csv'
    ofile  = open(flimane, "wb")
    writer = csv.writer(ofile, delimiter='\t', quotechar='',quoting=csv.QUOTE_NONE)
    for i in range(nm):
        golg=[]
        for j in range(5):
            try:
               golg.append(bigb[j][i]) 
            except:
                golg.append("")
        writer.writerow(golg)
    ofile.close()
def xlGen(txl):
    import re
    fdd=mc.textField('LFsourc',q=1,tx=1)
    if re.match('(.*).csv$',fdd):
        import csv
        with open(fdd, 'rb') as f:
            reader = csv.reader(f, delimiter='\t', quoting=csv.QUOTE_NONE)
            for row in reader:
                for i in range(min(len(row),4)):
                    if row[i]:
                        mc.textScrollList(txl.split()[i],e=1,a=row[i])
    else:
	with open(fdd) as f:
            contents = f.readlines() 
            for content in contents:      
                row=content.split(',')
                for i in range(min(len(row),4)):
                    if row[i]:
                        mc.textScrollList(txl.split()[i],e=1,a=row[i].strip())
def Fselu(txl):
   import os
   import re
   import os.path as ospa
   essel=mc.textScrollList(txl,q=1,ai=1)
   rex=mc.textField('Lugrugex',q=1,tx=1)
   fdd=mc.textField('LFsourc',q=1,tx=1)
   if fdd=='':
       fdd='D:/tmp/'
       if not ospa.exists(fdd):
           fdd='/tmp/'
       fdd=fdd+"Lug.txt"
       print fdd
   if ospa.exists(fdd):
       if ospa.isfile(fdd):
           if essel:
               a=open(fdd,'w')
               for oo in essel:
                 a.write(oo+'\n')
               a.close()
           else:
               import re
               with open(fdd) as infile:
                 for line in infile:
                   if len(line):
                     if rex:
                       if rex=="Nspace":
                         rex='(([a-zA-Z0-9:|_]*))'
                       if re.search(rex,line):
                         mm=re.search(rex,line).group(1)
                         if mm:
                           mc.textScrollList(txl,e=1,a=mm)
                     else:                        
                       mc.textScrollList(txl,e=1,a=line)
       elif ospa.isdir(fdd):
           ellam=os.listdir(fdd)
           for ell in ellam:
               if rex:
                 if rex=="Nspace":
                   rex='(([a-zA-Z0-9:|_]*))'
                 if re.search(rex,ell):
                   mm=re.search(rex,ell).group(0)
                   if mm:
                     mc.textScrollList(txl,e=1,a=mm)
               else:                        
                 mc.textScrollList(txl,e=1,a=ell)   
   shortList(txl)
def Luglace(txl,num):
   import re
   rex=mc.textField('Lugrugex',q=1,tx=1)
   essel=mc.textScrollList(txl,q=1,ai=1)
   fix=rex.split()
   if essel:
      if rex:
          for i in range(0,len(essel)):
              six=''
              if fix:
                  if len(fix)>1:
                      if fix[1] in ['()','[]','{}','""','\'\'']:
                          fix[1]=''
                      six=re.sub(fix[0],fix[1],essel[i])
                  else:
                      if num==1:
                          temp=essel[i].split('|')
                          print temp[:-1]
                          if temp:
                              for tem in temp[:-1]:
                                  six=six+tem+'|'
                              six=six+fix[0]+temp[-1]
                          else:
                              six=fix[0]+essel[i]
                      else:
                          six=essel[i]+fix[0]
              mc.textScrollList(txl,e=1,ri=essel[i])
              mc.textScrollList(txl,e=1,ap=[i+1,six])
      else:
          essel=mc.ls(sl=1)
          try:
              mc.textField('Lugrugex',e=1,tx=(essel[0]))
              mc.textField('Lugrugex',e=1,tx=(essel[0]+' '+essel[1]))
          except:
              pass
   shortList(txl)         
def LDG(dragControl, x=0, y=0, modi=''):
    essel=mc.textScrollList(dragControl,q=1,si=1)
    if essel:
        mc.textField('Lugtxt',e=1,tx=mc.nodeType(essel[0]))
        mc.textField('Lugsrch',e=1,tx=essel[0])
def LDP(dragControl, x=0, y=0, modi=''):
    essel=mc.textScrollList(dragControl,q=1,ai=1)
    ellam=mc.ls(sl=1)
    for oo in ellam:
        mc.textScrollList(dragControl,e=1,a=oo)
    shortList(dragControl)
def datadump(sourc="D:/tmp/Lug.txt",destin="",start="",end="",srch="",repl="",ext=0,echo=0):
    data_file=open(sourc)
    dump_file=''
    block=''
    found=False
    if not start and not end:
        found=True
    if destin:
        dump_file=open(destin,'w')
    for line in data_file:
        if found:
        	if line.strip()==end:
        		found=False
        	elif not ext and srch in line:
        		if repl:
        			line=line.replace(srch,repl)
        		if echo:
        			print line
        else:
        	if line.strip()==start:
        		found=True
        	elif ext and srch in line:
        		line=line.replace(srch,repl)
        		if echo:
        			print line
        block+=line
        if dump_file:
            dump_file.write(line)
    if echo and not srch:
    	print block
    data_file.close()
    try:
        dump_file.close()
    except:
        pass
def fileGen(txl):
    essel=mc.textScrollList(txl,q=1,si=1)
    mod=mc.optionMenu('filops',q=1,sl=1)
    import os
    serup=mc.textField('Lugrugex',q=1,tx=1)
    sok=mc.textField('LFsourc',q=1,tx=1)
    dok=mc.textField('LFdestin',q=1,tx=1)
    ellam=os.listdir(sok)
    if ellam:
        if not essel:
            mc.textScrollList(txl,e=1,ra=1)
            for oo in ellam :
                mc.textScrollList(txl,e=1,a=oo)
    shortList(txl)
def mmatch(w,li):
	import difflib
	s=difflib.SequenceMatcher()
	s.set_seq2(w)
	full=[]
	for i in li:
		s.set_seq1(i)
		full.append(s.ratio(),i)
	full.sort(reverse=True)
	if full[0][0]>0.6:
		return full[0]
	return(0,"bla")
def nmatch(w,li):
	from difflib import get_close_matches as gcm
	if gcm(w,li):
		return gcm(w,li)[0]
	return "bla"
