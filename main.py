Z='PPPPRSPKQRSTQRVZSUX]Y[^aikmnPPPP<CFHCKPRFRUWHSXZHTY[FSXYCKPR<CFHHMKMMURSMSTTMTTVMSUVMRTTMPPPHMMMNPSUMPPPMPPPMPPPMPPPMPPPUWXXRRSSKMNPMPQQMQRROQRSOQRSMQRRMPPPKMMMX]SMSRKHJHFCFCA>A><:><::<:::<:::'
W='PNBRQK';w=W.lower();R=range(64);T={'.':[0]*64}
for i,p in enumerate(W):v=[(100,320,330,500,900,0)[i]+2*ord(Z[i*32+s//8*4+min(s%8,7-s%8)])-160 for s in R];T[p]=v;T[w[i]]=[-v[s^56]for s in R]
def L(s,d,n=1):
 f,r=s%8,s//8;o=[]
 while n:
  f+=d[0];r+=d[1];n-=1
  if(f|r)&~7:break
  o+=[r*8+f]
 return o
O=(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)
Y=[[L(s,d,7)for d in O]+[L(s,(a,b))for a in(1,2,-1,-2)for b in(3-abs(a),abs(a)-3)]for s in R]
o=[[L(s,(1,1-2*c))+L(s,(-1,1-2*c))for s in R]for c in(0,1)]
def A(B,s,c):
 p,n,b,r,q,k=w if c else W
 if p in[B[t]for t in o[1-c][s]]:return 1
 for j,y in enumerate(Y[s]):
  for t in y:
   u=B[t]
   if u>'.':
    if u in((r,b)[j>3]+q+k*(t==y[0]),n)[j>7]:return 1
    break
def G(P,q):
 B,c,cr,ep,*_=P;M=[];F,E=(w,W)if c else(W,w)
 for s in R:
  p=B[s]
  if p not in F:continue
  k=p.upper()
  if k=='P':
   d=8-16*c;t=s+d;pr=(t%56<8)*(F[4]if q else F[1:5])
   X=[t]if B[t]<'A'and q<=(pr>'')else[]
   if X and s//8==1+5*c and B[t+d]<'A':X+=[t+d]
   for t in X+[t for t in o[c][s]if B[t]in E or t==ep]:M+=[(s,t,x)for x in pr or' ']
  else:
   j='RBQKN'.find(k)
   for y in Y[s][(0,4,0,0,8)[j]:(4,8,8,8,16)[j]]:
    for t in y[:7-6*(k=='K')]:
     u=B[t]
     if u in F:break
     if q<=(u>'.'):M+=[(s,t,' ')]
     if u>'.':break
 b=56*c
 if not q:
  for z,e in('Kk',(5,6)),('Qq',(1,2,3)):
   if z[c]in cr and all(B[b+j]<'A'for j in e)and not any(A(B,b+j,1-c)for j in(4,4+e[1]>>1)):M+=[(b+4,b+e[1],' ')]
 return M
y={0:'Q',4:'KQ',7:'K',56:'q',60:'kq',63:'k'}
def mk(P,m):
 B,c,cr,ep,v,h=P;f,t,x=m;B=B[:];p=B[f];v+=T[p][t]-T[p][f]-T[B[t]][t];h=-~h*(B[t]<'A');B[t]=p;B[f]='.';e=-1
 if p in'Pp':
  h=0
  if t==ep:z=t-8+16*c;v-=T[B[z]][z];B[z]='.'
  if abs(t-f)==16:e=f+t>>1
  if x>' ':B[t]=x;v+=T[x][t]-T[p][t]
 if p in'Kk'and abs(t-f)==2:a=(f-4,f+3)[t>f];g=f+t>>1;r=B[a];B[g]=r;B[a]='.';v+=T[r][g]-T[r][a]
 u=y.get(f,'')+y.get(t,'');return B,1-c,''.join(z for z in cr if z not in u),e,v,h
def K(P):return''.join(P[0])+str(P[1:4])
def C(B,c):return A(B,B.index('Kk'[c]),1-c)
D={};LIM=75000;I=9e9;U=0
def S(P,d,a,b,l,H):
 global N,F
 N+=1;N>X>1/0;B,c,x,y,z,u=P;k=K(P)
 if l and(k in H or u>99):return 0
 h=C(B,c)
 if h:d=max(d+1,1)
 q=d<1;a0=a;s=-I;e=(z+30*((B.count('B')>1)-(B.count('b')>1)))*(1-2*c)
 if q:
  s=e
  if e>=b:return e
  a=max(a,e)
 td,tv,tf,tm=D.get(k,(-9,0,0,0))
 if l and td>=d and(1,tv>=b,tv<=a)[tf]:return tv
 if l and not h and B.count('.')<52>2<d and e>=b<=-S((B,1-c,x,-1,z,u+1),d-3,-b,1-b,l+1,H):return b
 n=bm=0;H.add(k)
 for m in sorted(G(P,q),key=lambda m:W.find(B[m[0]].upper())-(m==tm)*1e9-abs(T[B[m[1]]][m[1]])*1e6-(m[2]>' ')*9e8-(V.get(l)==m)*9):
  Q=mk(P,m)
  if C(Q[0],c):continue
  n+=1;r=n>3<=d and m[2]+B[m[1]]<' /'
  v=-S(Q,d-1-r,(-b,-a-1)[r],-a,l+1,H)
  if r and v>a:v=-S(Q,d-1,-b,-a,l+1,H)
  if v>s:
   s=v;bm=m
   if l<1:F=m
  a=max(a,v)
  if a>=b:
   if B[m[1]]<'A':V[l]=m
   break
 H.remove(k)
 if n<1>q:s=l-I if h else 0
 D[k]=d,s,(s>=b)+2*(s<=a0),bm;return s
def think(P,H):
 global N,F,V,U,X
 X=LIM/(1,1.5,2.5,5)[min(3,int(U/5e6))];N=F=0;V={}
 if len(D)>4e5:D.clear()
 for d in range(1,64):
  try:v=S(P,d,-I,I,0,set(H))
  except:break
  if N>X/2 or abs(v)>I-99:break
 U+=N;return F
def fen(s):
 b,c,cr,ep,h=s.split()[:5];B=[]
 for r in b.split('/')[::-1]:
  for x in r:B+='.'*int(x)if x<'A'else x
 return B,c<'w',cr.strip('-'),ep>'-'and ord(ep[0])-105+8*int(ep[1])or-1,sum(T[p][i]for i,p in enumerate(B)),int(h)
def mu(m):f,t,p=m;return'%c%d'*2%(97+f%8,f//8+1,97+t%8,t//8+1)+p.strip().lower()
if __name__=='__main__':
 import os,json,urllib.request as Q
 def J(p,**b):return json.load(Q.urlopen(os.getenv('MAKEFUN_ENV_URL')+p,json.dumps(b).encode()))
 while(g:=J('/game'))['status']>'e':
  while L:=g.get('legal_moves'):
   P=fen(g['start_fen']);H=set()
   for u in g['moves']:H.add(K(P));P=mk(P,{mu(m):m for m in G(P,0)}[u])
   m=think(P,H);u=m and mu(m)
   g=J('/move',game=g['game'],move=[L[0],u][u in L])