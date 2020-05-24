#!/usr/bin/env python
#
# Author: Thamme Gowda [tg (at) isi (dot) edu] 
# Created: 5/12/20

# You shouldnt be using ISO 639 1 anymore. The only use of this list is to map the 2 letter code to
# 3 letter code of ISO 639 3
# this list is obtained from https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes
data = """ab,abk
aa,aar
af,afr
ak,aka
sq,sqi
am,amh
ar,ara
an,arg
hy,hye
as,asm
av,ava
ae,ave
ay,aym
az,aze
bm,bam
ba,bak
eu,eus
be,bel
bn,ben
bi,bis
bs,bos
br,bre
bg,bul
my,mya
ca,cat
ch,cha
ce,che
ny,nya
zh,zho
cv,chv
kw,cor
co,cos
cr,cre
hr,hrv
cs,ces
da,dan
dv,div
nl,nld
dz,dzo
en,eng
eo,epo
et,est
ee,ewe
fo,fao
fj,fij
fi,fin
fr,fra
ff,ful
gl,glg
ka,kat
de,deu
el,ell
gn,grn
gu,guj
ht,hat
ha,hau
he,heb
hz,her
hi,hin
ho,hmo
hu,hun
ia,ina
id,ind
ie,ile
ga,gle
ig,ibo
ik,ipk
io,ido
is,isl
it,ita
iu,iku
ja,jpn
jv,jav
kl,kal
kn,kan
kr,kau
ks,kas
kk,kaz
km,khm
ki,kik
rw,kin
ky,kir
kv,kom
kg,kon
ko,kor
ku,kur
kj,kua
la,lat
lb,ltz
lg,lug
li,lim
ln,lin
lo,lao
lt,lit
lu,lub
lv,lav
gv,glv
mk,mkd
mg,mlg
ms,msa
ml,mal
mt,mlt
mi,mri
mr,mar
mh,mah
mn,mon
na,nau
nv,nav
nd,nde
ne,nep
ng,ndo
nb,nob
nn,nno
no,nor
ii,iii
nr,nbl
oc,oci
oj,oji
cu,chu
om,orm
or,ori
os,oss
pa,pan
pi,pli
fa,fas
pl,pol
ps,pus
pt,por
qu,que
rm,roh
rn,run
ro,ron
ru,rus
sa,san
sc,srd
sd,snd
se,sme
sm,smo
sg,sag
sr,srp
gd,gla
sn,sna
si,sin
sk,slk
sl,slv
so,som
st,sot
es,spa
su,sun
sw,swa
ss,ssw
sv,swe
ta,tam
te,tel
tg,tgk
th,tha
ti,tir
bo,bod
tk,tuk
tl,tgl
tn,tsn
to,ton
tr,tur
ts,tso
tt,tat
tw,twi
ty,tah
ug,uig
uk,ukr
ur,urd
uz,uzb
ve,ven
vi,vie
vo,vol
wa,wln
cy,cym
wo,wol
fy,fry
xh,xho
yi,yid
yo,yor
za,zha
zu,zul"""

ISO693_1_to_3 = {rec[0]: rec[1] for l in data.splitlines() for rec in [l.strip().split()]}