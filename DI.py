def fcz(wc):
	c = float(wc)
	if c <= 0.39:
		fc = 0.540 * c
	elif c > 0.39 and c<= 0.55:
		fc = 0.171 + 0.001 * c + 0.265 * c^2
	elif c > 0.55 and c <= 0.65:
		fc = 0.115 + 0.268 * c - 0.038 * c^2
	else:
		fc = 0.143 + 0.200 * c
	return fc

def fmnz(wmn):
	mn = float(wmn)
	if mn <= 1.20:
		fmn= 1 + 3.333 * mn
	elif mn >1.2 and mn <1.95:
		fmn = -1.12 + 5.1 * mn
	return fmn

def fsiz(si):
	si = float(wsi) #si<=2
	fsi = 1 + 0.7 * si
	return fsi

def fniz(wni):
	ni = float(wni)
	fni = 1+0.363 * ni
	return fni

def fcrz(wcr):
	cr = float(wcr)
	fcr = 1+ 2.16 * cr
	return fcr

def fmoz(wmo):
	mo = float(wmo)
	fmo = 1+ 3 * mo
	return fmo

def fcuz(wcu):
	cu = float(wcu)
	fcu = 1+0.365 * cu
	return fcu

def fvz(wv):
	v = float(wv)
	fv = 1+0.363 * v
	return fv

def fgzz(wgz):
	gz = float(wgz)
	if gz == 4:
		fgz = 1.270
	elif gz == 5:
		fgz = 1.172
	elif gz == 6:
		fgz = 1.083
	elif gz == 7:
		fgz = 1
	else:
		fgz = (1-0.08(gz-7))
	
	return fgz

print("""
input to calculate di, 
condition:
w(C) <= 0.7%
w(Mn) <= 1.95% 
w(Si) <= 2.00%
w(Ni) <=1.75%
w(Cr) <=0.55%
w(Mo) <=0.55%
w(Cu) <=0.55%
w(V) <=0.20%
no effictive Boron
-------------------------------
""")

wc = input("C:")
wmn = input("Mn:")
wsi= input("Si:")
wni = input("Ni:")
wcr = input("Cr:")
wmo = input("Mo:")
wcu = input("Cu:")
wv = input("V:")
wgz = input("晶粒度级别:")

DI = 25.4 * fgzz(wgz) * fcz(wc) * fmnz(wmn) * fsiz(wsi) * fniz(wni) * fcrz(wcr) * fmoz(wmo) * fcuz(wcu) * fvz(wv)

print( "DI: ", DI)

