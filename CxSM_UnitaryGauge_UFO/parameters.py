# This file was automatically created by FeynRules 2.3.36
# Mathematica version: 11.3.0 for Linux x86 (64-bit) (March 7, 2018)
# Date: Tue 15 Feb 2022 16:39:02



from object_library import all_parameters, Parameter


from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot

# This is a default parameter object representing 0.
ZERO = Parameter(name = 'ZERO',
                 nature = 'internal',
                 type = 'real',
                 value = '0.0',
                 texname = '0')

# User-defined parameters.
alpha = Parameter(name = 'alpha',
                  nature = 'external',
                  type = 'real',
                  value = 0.1,
                  texname = '\\alpha',
                  lhablock = 'CxSM',
                  lhacode = [ 1 ])

vs = Parameter(name = 'vs',
               nature = 'external',
               type = 'real',
               value = 100,
               texname = '\\text{vs}',
               lhablock = 'CxSM',
               lhacode = [ 2 ])

aEWM1 = Parameter(name = 'aEWM1',
                  nature = 'external',
                  type = 'real',
                  value = 127.9,
                  texname = '\\text{aEWM1}',
                  lhablock = 'SMINPUTS',
                  lhacode = [ 1 ])

Gf = Parameter(name = 'Gf',
               nature = 'external',
               type = 'real',
               value = 0.0000116637,
               texname = 'G_f',
               lhablock = 'SMINPUTS',
               lhacode = [ 2 ])

aS = Parameter(name = 'aS',
               nature = 'external',
               type = 'real',
               value = 0.1184,
               texname = '\\alpha _s',
               lhablock = 'SMINPUTS',
               lhacode = [ 3 ])

ymb = Parameter(name = 'ymb',
                nature = 'external',
                type = 'real',
                value = 4.7,
                texname = '\\text{ymb}',
                lhablock = 'YUKAWA',
                lhacode = [ 5 ])

ymt = Parameter(name = 'ymt',
                nature = 'external',
                type = 'real',
                value = 172,
                texname = '\\text{ymt}',
                lhablock = 'YUKAWA',
                lhacode = [ 6 ])

ymtau = Parameter(name = 'ymtau',
                  nature = 'external',
                  type = 'real',
                  value = 1.777,
                  texname = '\\text{ymtau}',
                  lhablock = 'YUKAWA',
                  lhacode = [ 15 ])

MZ = Parameter(name = 'MZ',
               nature = 'external',
               type = 'real',
               value = 91.1876,
               texname = '\\text{MZ}',
               lhablock = 'MASS',
               lhacode = [ 23 ])

MTA = Parameter(name = 'MTA',
                nature = 'external',
                type = 'real',
                value = 1.777,
                texname = '\\text{MTA}',
                lhablock = 'MASS',
                lhacode = [ 15 ])

MT = Parameter(name = 'MT',
               nature = 'external',
               type = 'real',
               value = 172,
               texname = '\\text{MT}',
               lhablock = 'MASS',
               lhacode = [ 6 ])

MB = Parameter(name = 'MB',
               nature = 'external',
               type = 'real',
               value = 4.7,
               texname = '\\text{MB}',
               lhablock = 'MASS',
               lhacode = [ 5 ])

Mh1 = Parameter(name = 'Mh1',
                nature = 'external',
                type = 'real',
                value = 125,
                texname = '\\text{Mh1}',
                lhablock = 'MASS',
                lhacode = [ 25 ])

Mh2 = Parameter(name = 'Mh2',
                nature = 'external',
                type = 'real',
                value = 2000,
                texname = '\\text{Mh2}',
                lhablock = 'MASS',
                lhacode = [ 225 ])

MHA = Parameter(name = 'MHA',
                nature = 'external',
                type = 'real',
                value = 500,
                texname = '\\text{MHA}',
                lhablock = 'MASS',
                lhacode = [ 226 ])

WZ = Parameter(name = 'WZ',
               nature = 'external',
               type = 'real',
               value = 2.4952,
               texname = '\\text{WZ}',
               lhablock = 'DECAY',
               lhacode = [ 23 ])

WW = Parameter(name = 'WW',
               nature = 'external',
               type = 'real',
               value = 2.085,
               texname = '\\text{WW}',
               lhablock = 'DECAY',
               lhacode = [ 24 ])

WT = Parameter(name = 'WT',
               nature = 'external',
               type = 'real',
               value = 1.50833649,
               texname = '\\text{WT}',
               lhablock = 'DECAY',
               lhacode = [ 6 ])

Wh1 = Parameter(name = 'Wh1',
                nature = 'external',
                type = 'real',
                value = 0.00407,
                texname = '\\text{Wh1}',
                lhablock = 'DECAY',
                lhacode = [ 25 ])

Wh2 = Parameter(name = 'Wh2',
                nature = 'external',
                type = 'real',
                value = 0.00407,
                texname = '\\text{Wh2}',
                lhablock = 'DECAY',
                lhacode = [ 225 ])

WHA = Parameter(name = 'WHA',
                nature = 'external',
                type = 'real',
                value = 0.0107,
                texname = '\\text{WHA}',
                lhablock = 'DECAY',
                lhacode = [ 226 ])

b1 = Parameter(name = 'b1',
               nature = 'internal',
               type = 'real',
               value = '-MHA**2',
               texname = '\\text{b1}')

ca = Parameter(name = 'ca',
               nature = 'internal',
               type = 'real',
               value = 'cmath.cos(alpha)',
               texname = 'c_{\\alpha }')

ca2 = Parameter(name = 'ca2',
                nature = 'internal',
                type = 'real',
                value = 'cmath.cos(2*alpha)',
                texname = 'c_{2 \\alpha }')

sa = Parameter(name = 'sa',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sin(alpha)',
               texname = 's_{\\alpha }')

sa2 = Parameter(name = 'sa2',
                nature = 'internal',
                type = 'real',
                value = 'cmath.sin(2*alpha)',
                texname = 's_{2 \\alpha }')

aEW = Parameter(name = 'aEW',
                nature = 'internal',
                type = 'real',
                value = '1/aEWM1',
                texname = '\\alpha _{\\text{EW}}')

G = Parameter(name = 'G',
              nature = 'internal',
              type = 'real',
              value = '2*cmath.sqrt(aS)*cmath.sqrt(cmath.pi)',
              texname = 'G')

MW = Parameter(name = 'MW',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(MZ**2/2. + cmath.sqrt(MZ**4/4. - (aEW*cmath.pi*MZ**2)/(Gf*cmath.sqrt(2))))',
               texname = 'M_W')

d2 = Parameter(name = 'd2',
               nature = 'internal',
               type = 'real',
               value = '(Mh1**2 + Mh2**2 + ca2*(-Mh1**2 + Mh2**2))/vs**2',
               texname = '\\text{d2}')

ee = Parameter(name = 'ee',
               nature = 'internal',
               type = 'real',
               value = '2*cmath.sqrt(aEW)*cmath.sqrt(cmath.pi)',
               texname = 'e')

sw2 = Parameter(name = 'sw2',
                nature = 'internal',
                type = 'real',
                value = '1 - MW**2/MZ**2',
                texname = '\\text{sw2}')

cw = Parameter(name = 'cw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(1 - sw2)',
               texname = 'c_w')

sw = Parameter(name = 'sw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(sw2)',
               texname = 's_w')

g1 = Parameter(name = 'g1',
               nature = 'internal',
               type = 'real',
               value = 'ee/cw',
               texname = 'g_1')

gw = Parameter(name = 'gw',
               nature = 'internal',
               type = 'real',
               value = 'ee/sw',
               texname = 'g_w')

vev = Parameter(name = 'vev',
                nature = 'internal',
                type = 'real',
                value = '(2*MW*sw)/ee',
                texname = '\\text{vev}')

b2 = Parameter(name = 'b2',
               nature = 'internal',
               type = 'real',
               value = '(-Mh1**2 - Mh2**2 + ca2*(Mh1**2 - Mh2**2) + 2*MHA**2 - ((Mh1**2 - Mh2**2)*sa2*vev)/vs)/2.',
               texname = '\\text{b2}')

mm2 = Parameter(name = 'mm2',
                nature = 'internal',
                type = 'real',
                value = '(ca2*(-Mh1**2 + Mh2**2) - ((Mh1**2 + Mh2**2)*vev + (Mh1**2 - Mh2**2)*sa2*vs)/vev)/2.',
                texname = '\\text{mm2}')

delta2 = Parameter(name = 'delta2',
                   nature = 'internal',
                   type = 'real',
                   value = '((Mh1**2 - Mh2**2)*sa2)/(vev*vs)',
                   texname = '\\text{delta2}')

lamd = Parameter(name = 'lamd',
                 nature = 'internal',
                 type = 'real',
                 value = '(Mh1**2 + Mh2**2 + ca2*(Mh1**2 - Mh2**2))/vev**2',
                 texname = '\\text{lamd}')

yb = Parameter(name = 'yb',
               nature = 'internal',
               type = 'real',
               value = '(ymb*cmath.sqrt(2))/vev',
               texname = '\\text{yb}')

yt = Parameter(name = 'yt',
               nature = 'internal',
               type = 'real',
               value = '(ymt*cmath.sqrt(2))/vev',
               texname = '\\text{yt}')

ytau = Parameter(name = 'ytau',
                 nature = 'internal',
                 type = 'real',
                 value = '(ymtau*cmath.sqrt(2))/vev',
                 texname = '\\text{ytau}')

