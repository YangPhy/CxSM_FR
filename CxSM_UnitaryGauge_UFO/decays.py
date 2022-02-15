# This file was automatically created by FeynRules 2.3.36
# Mathematica version: 11.3.0 for Linux x86 (64-bit) (March 7, 2018)
# Date: Tue 15 Feb 2022 16:39:02


from object_library import all_decays, Decay
import particles as P


Decay_b = Decay(name = 'Decay_b',
                particle = P.b,
                partial_widths = {(P.W__minus__,P.t):'(((3*ee**2*MB**2)/(2.*sw**2) + (3*ee**2*MT**2)/(2.*sw**2) + (3*ee**2*MB**4)/(2.*MW**2*sw**2) - (3*ee**2*MB**2*MT**2)/(MW**2*sw**2) + (3*ee**2*MT**4)/(2.*MW**2*sw**2) - (3*ee**2*MW**2)/sw**2)*cmath.sqrt(MB**4 - 2*MB**2*MT**2 + MT**4 - 2*MB**2*MW**2 - 2*MT**2*MW**2 + MW**4))/(96.*cmath.pi*abs(MB)**3)'})

Decay_h1 = Decay(name = 'Decay_h1',
                 particle = P.h1,
                 partial_widths = {(P.b,P.b__tilde__):'((-12*ca**2*MB**2*yb**2 + 3*ca**2*Mh1**2*yb**2)*cmath.sqrt(-4*MB**2*Mh1**2 + Mh1**4))/(16.*cmath.pi*abs(Mh1)**3)',
                                   (P.h2,P.h2):'(((ca**6*delta2**2*vev**2)/4. - ca**4*delta2**2*sa**2*vev**2 + (3*ca**4*delta2*lamd*sa**2*vev**2)/2. + ca**2*delta2**2*sa**4*vev**2 - 3*ca**2*delta2*lamd*sa**4*vev**2 + (9*ca**2*lamd**2*sa**4*vev**2)/4. + (3*ca**5*d2*delta2*sa*vev*vs)/2. - ca**5*delta2**2*sa*vev*vs - 3*ca**3*d2*delta2*sa**3*vev*vs + (5*ca**3*delta2**2*sa**3*vev*vs)/2. + (9*ca**3*d2*lamd*sa**3*vev*vs)/2. - 3*ca**3*delta2*lamd*sa**3*vev*vs - ca*delta2**2*sa**5*vev*vs + (3*ca*delta2*lamd*sa**5*vev*vs)/2. + (9*ca**4*d2**2*sa**2*vs**2)/4. - 3*ca**4*d2*delta2*sa**2*vs**2 + ca**4*delta2**2*sa**2*vs**2 + (3*ca**2*d2*delta2*sa**4*vs**2)/2. - ca**2*delta2**2*sa**4*vs**2 + (delta2**2*sa**6*vs**2)/4.)*cmath.sqrt(Mh1**4 - 4*Mh1**2*Mh2**2))/(32.*cmath.pi*abs(Mh1)**3)',
                                   (P.HA,P.HA):'(((ca**2*delta2**2*vev**2)/4. + (ca*d2*delta2*sa*vev*vs)/2. + (d2**2*sa**2*vs**2)/4.)*cmath.sqrt(Mh1**4 - 4*Mh1**2*MHA**2))/(32.*cmath.pi*abs(Mh1)**3)',
                                   (P.ta__minus__,P.ta__plus__):'((ca**2*Mh1**2*ytau**2 - 4*ca**2*MTA**2*ytau**2)*cmath.sqrt(Mh1**4 - 4*Mh1**2*MTA**2))/(16.*cmath.pi*abs(Mh1)**3)',
                                   (P.t,P.t__tilde__):'((3*ca**2*Mh1**2*yt**2 - 12*ca**2*MT**2*yt**2)*cmath.sqrt(Mh1**4 - 4*Mh1**2*MT**2))/(16.*cmath.pi*abs(Mh1)**3)',
                                   (P.W__minus__,P.W__plus__):'(((3*ca**2*ee**4*vev**2)/(4.*sw**4) + (ca**2*ee**4*Mh1**4*vev**2)/(16.*MW**4*sw**4) - (ca**2*ee**4*Mh1**2*vev**2)/(4.*MW**2*sw**4))*cmath.sqrt(Mh1**4 - 4*Mh1**2*MW**2))/(16.*cmath.pi*abs(Mh1)**3)',
                                   (P.Z,P.Z):'(((9*ca**2*ee**4*vev**2)/2. + (3*ca**2*ee**4*Mh1**4*vev**2)/(8.*MZ**4) - (3*ca**2*ee**4*Mh1**2*vev**2)/(2.*MZ**2) + (3*ca**2*cw**4*ee**4*vev**2)/(4.*sw**4) + (ca**2*cw**4*ee**4*Mh1**4*vev**2)/(16.*MZ**4*sw**4) - (ca**2*cw**4*ee**4*Mh1**2*vev**2)/(4.*MZ**2*sw**4) + (3*ca**2*cw**2*ee**4*vev**2)/sw**2 + (ca**2*cw**2*ee**4*Mh1**4*vev**2)/(4.*MZ**4*sw**2) - (ca**2*cw**2*ee**4*Mh1**2*vev**2)/(MZ**2*sw**2) + (3*ca**2*ee**4*sw**2*vev**2)/cw**2 + (ca**2*ee**4*Mh1**4*sw**2*vev**2)/(4.*cw**2*MZ**4) - (ca**2*ee**4*Mh1**2*sw**2*vev**2)/(cw**2*MZ**2) + (3*ca**2*ee**4*sw**4*vev**2)/(4.*cw**4) + (ca**2*ee**4*Mh1**4*sw**4*vev**2)/(16.*cw**4*MZ**4) - (ca**2*ee**4*Mh1**2*sw**4*vev**2)/(4.*cw**4*MZ**2))*cmath.sqrt(Mh1**4 - 4*Mh1**2*MZ**2))/(32.*cmath.pi*abs(Mh1)**3)'})

Decay_h2 = Decay(name = 'Decay_h2',
                 particle = P.h2,
                 partial_widths = {(P.b,P.b__tilde__):'((-12*MB**2*sa**2*yb**2 + 3*Mh2**2*sa**2*yb**2)*cmath.sqrt(-4*MB**2*Mh2**2 + Mh2**4))/(16.*cmath.pi*abs(Mh2)**3)',
                                   (P.h1,P.h1):'((ca**4*delta2**2*sa**2*vev**2 - 3*ca**4*delta2*lamd*sa**2*vev**2 + (9*ca**4*lamd**2*sa**2*vev**2)/4. - ca**2*delta2**2*sa**4*vev**2 + (3*ca**2*delta2*lamd*sa**4*vev**2)/2. + (delta2**2*sa**6*vev**2)/4. + ca**5*delta2**2*sa*vev*vs - (3*ca**5*delta2*lamd*sa*vev*vs)/2. + 3*ca**3*d2*delta2*sa**3*vev*vs - (5*ca**3*delta2**2*sa**3*vev*vs)/2. - (9*ca**3*d2*lamd*sa**3*vev*vs)/2. + 3*ca**3*delta2*lamd*sa**3*vev*vs - (3*ca*d2*delta2*sa**5*vev*vs)/2. + ca*delta2**2*sa**5*vev*vs + (ca**6*delta2**2*vs**2)/4. + (3*ca**4*d2*delta2*sa**2*vs**2)/2. - ca**4*delta2**2*sa**2*vs**2 + (9*ca**2*d2**2*sa**4*vs**2)/4. - 3*ca**2*d2*delta2*sa**4*vs**2 + ca**2*delta2**2*sa**4*vs**2)*cmath.sqrt(-4*Mh1**2*Mh2**2 + Mh2**4))/(32.*cmath.pi*abs(Mh2)**3)',
                                   (P.HA,P.HA):'(((delta2**2*sa**2*vev**2)/4. - (ca*d2*delta2*sa*vev*vs)/2. + (ca**2*d2**2*vs**2)/4.)*cmath.sqrt(Mh2**4 - 4*Mh2**2*MHA**2))/(32.*cmath.pi*abs(Mh2)**3)',
                                   (P.ta__minus__,P.ta__plus__):'((Mh2**2*sa**2*ytau**2 - 4*MTA**2*sa**2*ytau**2)*cmath.sqrt(Mh2**4 - 4*Mh2**2*MTA**2))/(16.*cmath.pi*abs(Mh2)**3)',
                                   (P.t,P.t__tilde__):'((3*Mh2**2*sa**2*yt**2 - 12*MT**2*sa**2*yt**2)*cmath.sqrt(Mh2**4 - 4*Mh2**2*MT**2))/(16.*cmath.pi*abs(Mh2)**3)',
                                   (P.W__minus__,P.W__plus__):'(((3*ee**4*sa**2*vev**2)/(4.*sw**4) + (ee**4*Mh2**4*sa**2*vev**2)/(16.*MW**4*sw**4) - (ee**4*Mh2**2*sa**2*vev**2)/(4.*MW**2*sw**4))*cmath.sqrt(Mh2**4 - 4*Mh2**2*MW**2))/(16.*cmath.pi*abs(Mh2)**3)',
                                   (P.Z,P.Z):'(((9*ee**4*sa**2*vev**2)/2. + (3*ee**4*Mh2**4*sa**2*vev**2)/(8.*MZ**4) - (3*ee**4*Mh2**2*sa**2*vev**2)/(2.*MZ**2) + (3*cw**4*ee**4*sa**2*vev**2)/(4.*sw**4) + (cw**4*ee**4*Mh2**4*sa**2*vev**2)/(16.*MZ**4*sw**4) - (cw**4*ee**4*Mh2**2*sa**2*vev**2)/(4.*MZ**2*sw**4) + (3*cw**2*ee**4*sa**2*vev**2)/sw**2 + (cw**2*ee**4*Mh2**4*sa**2*vev**2)/(4.*MZ**4*sw**2) - (cw**2*ee**4*Mh2**2*sa**2*vev**2)/(MZ**2*sw**2) + (3*ee**4*sa**2*sw**2*vev**2)/cw**2 + (ee**4*Mh2**4*sa**2*sw**2*vev**2)/(4.*cw**2*MZ**4) - (ee**4*Mh2**2*sa**2*sw**2*vev**2)/(cw**2*MZ**2) + (3*ee**4*sa**2*sw**4*vev**2)/(4.*cw**4) + (ee**4*Mh2**4*sa**2*sw**4*vev**2)/(16.*cw**4*MZ**4) - (ee**4*Mh2**2*sa**2*sw**4*vev**2)/(4.*cw**4*MZ**2))*cmath.sqrt(Mh2**4 - 4*Mh2**2*MZ**2))/(32.*cmath.pi*abs(Mh2)**3)'})

Decay_t = Decay(name = 'Decay_t',
                particle = P.t,
                partial_widths = {(P.W__plus__,P.b):'(((3*ee**2*MB**2)/(2.*sw**2) + (3*ee**2*MT**2)/(2.*sw**2) + (3*ee**2*MB**4)/(2.*MW**2*sw**2) - (3*ee**2*MB**2*MT**2)/(MW**2*sw**2) + (3*ee**2*MT**4)/(2.*MW**2*sw**2) - (3*ee**2*MW**2)/sw**2)*cmath.sqrt(MB**4 - 2*MB**2*MT**2 + MT**4 - 2*MB**2*MW**2 - 2*MT**2*MW**2 + MW**4))/(96.*cmath.pi*abs(MT)**3)'})

Decay_ta__minus__ = Decay(name = 'Decay_ta__minus__',
                          particle = P.ta__minus__,
                          partial_widths = {(P.W__minus__,P.vt):'((MTA**2 - MW**2)*((ee**2*MTA**2)/(2.*sw**2) + (ee**2*MTA**4)/(2.*MW**2*sw**2) - (ee**2*MW**2)/sw**2))/(32.*cmath.pi*abs(MTA)**3)'})

Decay_W__plus__ = Decay(name = 'Decay_W__plus__',
                        particle = P.W__plus__,
                        partial_widths = {(P.c,P.s__tilde__):'(ee**2*MW**4)/(16.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.t,P.b__tilde__):'(((-3*ee**2*MB**2)/(2.*sw**2) - (3*ee**2*MT**2)/(2.*sw**2) - (3*ee**2*MB**4)/(2.*MW**2*sw**2) + (3*ee**2*MB**2*MT**2)/(MW**2*sw**2) - (3*ee**2*MT**4)/(2.*MW**2*sw**2) + (3*ee**2*MW**2)/sw**2)*cmath.sqrt(MB**4 - 2*MB**2*MT**2 + MT**4 - 2*MB**2*MW**2 - 2*MT**2*MW**2 + MW**4))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.u,P.d__tilde__):'(ee**2*MW**4)/(16.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.ve,P.e__plus__):'(ee**2*MW**4)/(48.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.vm,P.mu__plus__):'(ee**2*MW**4)/(48.*cmath.pi*sw**2*abs(MW)**3)',
                                          (P.vt,P.ta__plus__):'((-MTA**2 + MW**2)*(-(ee**2*MTA**2)/(2.*sw**2) - (ee**2*MTA**4)/(2.*MW**2*sw**2) + (ee**2*MW**2)/sw**2))/(48.*cmath.pi*abs(MW)**3)'})

Decay_Z = Decay(name = 'Decay_Z',
                particle = P.Z,
                partial_widths = {(P.b,P.b__tilde__):'((-7*ee**2*MB**2 + ee**2*MZ**2 - (3*cw**2*ee**2*MB**2)/(2.*sw**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) - (17*ee**2*MB**2*sw**2)/(6.*cw**2) + (5*ee**2*MZ**2*sw**2)/(6.*cw**2))*cmath.sqrt(-4*MB**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.c,P.c__tilde__):'(MZ**2*(-(ee**2*MZ**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (17*ee**2*MZ**2*sw**2)/(6.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.d,P.d__tilde__):'(MZ**2*(ee**2*MZ**2 + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(6.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.e__minus__,P.e__plus__):'(MZ**2*(-(ee**2*MZ**2) + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.mu__minus__,P.mu__plus__):'(MZ**2*(-(ee**2*MZ**2) + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.s,P.s__tilde__):'(MZ**2*(ee**2*MZ**2 + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (5*ee**2*MZ**2*sw**2)/(6.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.ta__minus__,P.ta__plus__):'((-5*ee**2*MTA**2 - ee**2*MZ**2 - (cw**2*ee**2*MTA**2)/(2.*sw**2) + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (7*ee**2*MTA**2*sw**2)/(2.*cw**2) + (5*ee**2*MZ**2*sw**2)/(2.*cw**2))*cmath.sqrt(-4*MTA**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.t,P.t__tilde__):'((-11*ee**2*MT**2 - ee**2*MZ**2 - (3*cw**2*ee**2*MT**2)/(2.*sw**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (7*ee**2*MT**2*sw**2)/(6.*cw**2) + (17*ee**2*MZ**2*sw**2)/(6.*cw**2))*cmath.sqrt(-4*MT**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.u,P.u__tilde__):'(MZ**2*(-(ee**2*MZ**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (17*ee**2*MZ**2*sw**2)/(6.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.ve,P.ve__tilde__):'(MZ**2*(ee**2*MZ**2 + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.vm,P.vm__tilde__):'(MZ**2*(ee**2*MZ**2 + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.vt,P.vt__tilde__):'(MZ**2*(ee**2*MZ**2 + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.W__minus__,P.W__plus__):'(((-12*cw**2*ee**2*MW**2)/sw**2 - (17*cw**2*ee**2*MZ**2)/sw**2 + (4*cw**2*ee**2*MZ**4)/(MW**2*sw**2) + (cw**2*ee**2*MZ**6)/(4.*MW**4*sw**2))*cmath.sqrt(-4*MW**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)'})

