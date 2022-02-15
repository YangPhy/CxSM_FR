# This file was automatically created by FeynRules 2.3.36
# Mathematica version: 11.3.0 for Linux x86 (64-bit) (March 7, 2018)
# Date: Tue 15 Feb 2022 16:39:52


from object_library import all_couplings, Coupling

from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot



GC_1 = Coupling(name = 'GC_1',
                value = '(-3*d2*complex(0,1))/2.',
                order = {'QED':2})

GC_2 = Coupling(name = 'GC_2',
                value = '-(delta2*complex(0,1))/2.',
                order = {'QED':2})

GC_3 = Coupling(name = 'GC_3',
                value = '-(ee*complex(0,1))/3.',
                order = {'QED':1})

GC_4 = Coupling(name = 'GC_4',
                value = '(2*ee*complex(0,1))/3.',
                order = {'QED':1})

GC_5 = Coupling(name = 'GC_5',
                value = '-(ee*complex(0,1))',
                order = {'QED':1})

GC_6 = Coupling(name = 'GC_6',
                value = 'ee*complex(0,1)',
                order = {'QED':1})

GC_7 = Coupling(name = 'GC_7',
                value = 'ee**2*complex(0,1)',
                order = {'QED':2})

GC_8 = Coupling(name = 'GC_8',
                value = '2*ee**2*complex(0,1)',
                order = {'QED':2})

GC_9 = Coupling(name = 'GC_9',
                value = '-ee**2/(2.*cw)',
                order = {'QED':2})

GC_10 = Coupling(name = 'GC_10',
                 value = 'ee**2/(2.*cw)',
                 order = {'QED':2})

GC_11 = Coupling(name = 'GC_11',
                 value = '-(ca*ee**2*complex(0,1))/(2.*cw)',
                 order = {'QED':2})

GC_12 = Coupling(name = 'GC_12',
                 value = '-G',
                 order = {'QCD':1})

GC_13 = Coupling(name = 'GC_13',
                 value = 'complex(0,1)*G',
                 order = {'QCD':1})

GC_14 = Coupling(name = 'GC_14',
                 value = 'complex(0,1)*G**2',
                 order = {'QCD':2})

GC_15 = Coupling(name = 'GC_15',
                 value = '-(complex(0,1)*I1a33)',
                 order = {'QED':1})

GC_16 = Coupling(name = 'GC_16',
                 value = 'complex(0,1)*I2a33',
                 order = {'QED':1})

GC_17 = Coupling(name = 'GC_17',
                 value = 'complex(0,1)*I3a33',
                 order = {'QED':1})

GC_18 = Coupling(name = 'GC_18',
                 value = '-(complex(0,1)*I4a33)',
                 order = {'QED':1})

GC_19 = Coupling(name = 'GC_19',
                 value = '-(complex(0,1)*lamd)/2.',
                 order = {'QED':2})

GC_20 = Coupling(name = 'GC_20',
                 value = '-(complex(0,1)*lamd)',
                 order = {'QED':2})

GC_21 = Coupling(name = 'GC_21',
                 value = '(-3*complex(0,1)*lamd)/2.',
                 order = {'QED':2})

GC_22 = Coupling(name = 'GC_22',
                 value = '(ee**2*complex(0,1)*sa)/(2.*cw)',
                 order = {'QED':2})

GC_23 = Coupling(name = 'GC_23',
                 value = '-(ca*d2*complex(0,1)*sa)/2. + (ca*delta2*complex(0,1)*sa)/2.',
                 order = {'QED':2})

GC_24 = Coupling(name = 'GC_24',
                 value = '-(ca*delta2*complex(0,1)*sa)/2. + (ca*complex(0,1)*lamd*sa)/2.',
                 order = {'QED':2})

GC_25 = Coupling(name = 'GC_25',
                 value = '-(ca**2*delta2*complex(0,1))/2. - (d2*complex(0,1)*sa**2)/2.',
                 order = {'QED':2})

GC_26 = Coupling(name = 'GC_26',
                 value = '-(ca**2*d2*complex(0,1))/2. - (delta2*complex(0,1)*sa**2)/2.',
                 order = {'QED':2})

GC_27 = Coupling(name = 'GC_27',
                 value = '-(ca**2*complex(0,1)*lamd)/2. - (delta2*complex(0,1)*sa**2)/2.',
                 order = {'QED':2})

GC_28 = Coupling(name = 'GC_28',
                 value = '-(ca**2*delta2*complex(0,1))/2. - (complex(0,1)*lamd*sa**2)/2.',
                 order = {'QED':2})

GC_29 = Coupling(name = 'GC_29',
                 value = '(-3*ca**3*delta2*complex(0,1)*sa)/2. + (3*ca**3*complex(0,1)*lamd*sa)/2. - (3*ca*d2*complex(0,1)*sa**3)/2. + (3*ca*delta2*complex(0,1)*sa**3)/2.',
                 order = {'QED':2})

GC_30 = Coupling(name = 'GC_30',
                 value = '(-3*ca**3*d2*complex(0,1)*sa)/2. + (3*ca**3*delta2*complex(0,1)*sa)/2. - (3*ca*delta2*complex(0,1)*sa**3)/2. + (3*ca*complex(0,1)*lamd*sa**3)/2.',
                 order = {'QED':2})

GC_31 = Coupling(name = 'GC_31',
                 value = '(-3*ca**4*complex(0,1)*lamd)/2. - 3*ca**2*delta2*complex(0,1)*sa**2 - (3*d2*complex(0,1)*sa**4)/2.',
                 order = {'QED':2})

GC_32 = Coupling(name = 'GC_32',
                 value = '-(ca**4*delta2*complex(0,1))/2. - (3*ca**2*d2*complex(0,1)*sa**2)/2. + 2*ca**2*delta2*complex(0,1)*sa**2 - (3*ca**2*complex(0,1)*lamd*sa**2)/2. - (delta2*complex(0,1)*sa**4)/2.',
                 order = {'QED':2})

GC_33 = Coupling(name = 'GC_33',
                 value = '(-3*ca**4*d2*complex(0,1))/2. - 3*ca**2*delta2*complex(0,1)*sa**2 - (3*complex(0,1)*lamd*sa**4)/2.',
                 order = {'QED':2})

GC_34 = Coupling(name = 'GC_34',
                 value = '(ee**2*complex(0,1))/(2.*sw**2)',
                 order = {'QED':2})

GC_35 = Coupling(name = 'GC_35',
                 value = '-((ee**2*complex(0,1))/sw**2)',
                 order = {'QED':2})

GC_36 = Coupling(name = 'GC_36',
                 value = '(ca**2*ee**2*complex(0,1))/(2.*sw**2)',
                 order = {'QED':2})

GC_37 = Coupling(name = 'GC_37',
                 value = '(cw**2*ee**2*complex(0,1))/sw**2',
                 order = {'QED':2})

GC_38 = Coupling(name = 'GC_38',
                 value = '-(ca*ee**2*complex(0,1)*sa)/(2.*sw**2)',
                 order = {'QED':2})

GC_39 = Coupling(name = 'GC_39',
                 value = '(ee**2*complex(0,1)*sa**2)/(2.*sw**2)',
                 order = {'QED':2})

GC_40 = Coupling(name = 'GC_40',
                 value = 'ee/(2.*sw)',
                 order = {'QED':1})

GC_41 = Coupling(name = 'GC_41',
                 value = '(ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_42 = Coupling(name = 'GC_42',
                 value = '-(ca*ee*complex(0,1))/(2.*sw)',
                 order = {'QED':1})

GC_43 = Coupling(name = 'GC_43',
                 value = '(ca*ee*complex(0,1))/(2.*sw)',
                 order = {'QED':1})

GC_44 = Coupling(name = 'GC_44',
                 value = '-(cw*ee*complex(0,1))/(2.*sw)',
                 order = {'QED':1})

GC_45 = Coupling(name = 'GC_45',
                 value = '-((cw*ee*complex(0,1))/sw)',
                 order = {'QED':1})

GC_46 = Coupling(name = 'GC_46',
                 value = '(cw*ee*complex(0,1))/sw',
                 order = {'QED':1})

GC_47 = Coupling(name = 'GC_47',
                 value = '-ee**2/(2.*sw)',
                 order = {'QED':2})

GC_48 = Coupling(name = 'GC_48',
                 value = 'ee**2/(2.*sw)',
                 order = {'QED':2})

GC_49 = Coupling(name = 'GC_49',
                 value = '(ca*ee**2*complex(0,1))/(2.*sw)',
                 order = {'QED':2})

GC_50 = Coupling(name = 'GC_50',
                 value = '(-2*cw*ee**2*complex(0,1))/sw',
                 order = {'QED':2})

GC_51 = Coupling(name = 'GC_51',
                 value = '-(ee*complex(0,1)*sa)/(2.*sw)',
                 order = {'QED':1})

GC_52 = Coupling(name = 'GC_52',
                 value = '(ee*complex(0,1)*sa)/(2.*sw)',
                 order = {'QED':1})

GC_53 = Coupling(name = 'GC_53',
                 value = '-(ee**2*complex(0,1)*sa)/(2.*sw)',
                 order = {'QED':2})

GC_54 = Coupling(name = 'GC_54',
                 value = '(ee*complex(0,1)*sw)/(3.*cw)',
                 order = {'QED':1})

GC_55 = Coupling(name = 'GC_55',
                 value = '(ee*complex(0,1)*sw)/(2.*cw)',
                 order = {'QED':1})

GC_56 = Coupling(name = 'GC_56',
                 value = '(-2*ee*complex(0,1)*sw)/(3.*cw)',
                 order = {'QED':1})

GC_57 = Coupling(name = 'GC_57',
                 value = '-(cw*ee*complex(0,1))/(2.*sw) - (ee*complex(0,1)*sw)/(6.*cw)',
                 order = {'QED':1})

GC_58 = Coupling(name = 'GC_58',
                 value = '(cw*ee*complex(0,1))/(2.*sw) - (ee*complex(0,1)*sw)/(6.*cw)',
                 order = {'QED':1})

GC_59 = Coupling(name = 'GC_59',
                 value = '-(cw*ee*complex(0,1))/(2.*sw) + (ee*complex(0,1)*sw)/(2.*cw)',
                 order = {'QED':1})

GC_60 = Coupling(name = 'GC_60',
                 value = '(cw*ee*complex(0,1))/(2.*sw) + (ee*complex(0,1)*sw)/(2.*cw)',
                 order = {'QED':1})

GC_61 = Coupling(name = 'GC_61',
                 value = '-(ca*cw*ee)/(2.*sw) - (ca*ee*sw)/(2.*cw)',
                 order = {'QED':1})

GC_62 = Coupling(name = 'GC_62',
                 value = '(cw*ee**2*complex(0,1))/sw - (ee**2*complex(0,1)*sw)/cw',
                 order = {'QED':2})

GC_63 = Coupling(name = 'GC_63',
                 value = '(cw*ee*sa)/(2.*sw) + (ee*sa*sw)/(2.*cw)',
                 order = {'QED':1})

GC_64 = Coupling(name = 'GC_64',
                 value = '-(ee**2*complex(0,1)) + (cw**2*ee**2*complex(0,1))/(2.*sw**2) + (ee**2*complex(0,1)*sw**2)/(2.*cw**2)',
                 order = {'QED':2})

GC_65 = Coupling(name = 'GC_65',
                 value = 'ee**2*complex(0,1) + (cw**2*ee**2*complex(0,1))/(2.*sw**2) + (ee**2*complex(0,1)*sw**2)/(2.*cw**2)',
                 order = {'QED':2})

GC_66 = Coupling(name = 'GC_66',
                 value = 'ca**2*ee**2*complex(0,1) + (ca**2*cw**2*ee**2*complex(0,1))/(2.*sw**2) + (ca**2*ee**2*complex(0,1)*sw**2)/(2.*cw**2)',
                 order = {'QED':2})

GC_67 = Coupling(name = 'GC_67',
                 value = '-(ca*ee**2*complex(0,1)*sa) - (ca*cw**2*ee**2*complex(0,1)*sa)/(2.*sw**2) - (ca*ee**2*complex(0,1)*sa*sw**2)/(2.*cw**2)',
                 order = {'QED':2})

GC_68 = Coupling(name = 'GC_68',
                 value = 'ee**2*complex(0,1)*sa**2 + (cw**2*ee**2*complex(0,1)*sa**2)/(2.*sw**2) + (ee**2*complex(0,1)*sa**2*sw**2)/(2.*cw**2)',
                 order = {'QED':2})

GC_69 = Coupling(name = 'GC_69',
                 value = '-(ca*delta2*complex(0,1)*vev)/2.',
                 order = {'QED':1})

GC_70 = Coupling(name = 'GC_70',
                 value = '-(ee**2*complex(0,1)*vev)/(2.*cw)',
                 order = {'QED':1})

GC_71 = Coupling(name = 'GC_71',
                 value = '-(ca*complex(0,1)*lamd*vev)/2.',
                 order = {'QED':1})

GC_72 = Coupling(name = 'GC_72',
                 value = '(delta2*complex(0,1)*sa*vev)/2.',
                 order = {'QED':1})

GC_73 = Coupling(name = 'GC_73',
                 value = '(complex(0,1)*lamd*sa*vev)/2.',
                 order = {'QED':1})

GC_74 = Coupling(name = 'GC_74',
                 value = '-(ee**2*vev)/(4.*sw**2)',
                 order = {'QED':1})

GC_75 = Coupling(name = 'GC_75',
                 value = '(ee**2*vev)/(4.*sw**2)',
                 order = {'QED':1})

GC_76 = Coupling(name = 'GC_76',
                 value = '-(ca*ee**2*complex(0,1)*vev)/(4.*sw**2)',
                 order = {'QED':1})

GC_77 = Coupling(name = 'GC_77',
                 value = '(ca*ee**2*complex(0,1)*vev)/(2.*sw**2)',
                 order = {'QED':1})

GC_78 = Coupling(name = 'GC_78',
                 value = '(ee**2*complex(0,1)*sa*vev)/(4.*sw**2)',
                 order = {'QED':1})

GC_79 = Coupling(name = 'GC_79',
                 value = '-(ee**2*complex(0,1)*sa*vev)/(2.*sw**2)',
                 order = {'QED':1})

GC_80 = Coupling(name = 'GC_80',
                 value = '-(ee**2*vev)/(2.*sw)',
                 order = {'QED':1})

GC_81 = Coupling(name = 'GC_81',
                 value = '(ee**2*complex(0,1)*vev)/(2.*sw)',
                 order = {'QED':1})

GC_82 = Coupling(name = 'GC_82',
                 value = '(ee**2*vev)/(2.*sw)',
                 order = {'QED':1})

GC_83 = Coupling(name = 'GC_83',
                 value = '(-3*ca**3*complex(0,1)*lamd*vev)/2. - (3*ca*delta2*complex(0,1)*sa**2*vev)/2.',
                 order = {'QED':1})

GC_84 = Coupling(name = 'GC_84',
                 value = '-(ca**3*delta2*complex(0,1)*vev)/2. + ca*delta2*complex(0,1)*sa**2*vev - (3*ca*complex(0,1)*lamd*sa**2*vev)/2.',
                 order = {'QED':1})

GC_85 = Coupling(name = 'GC_85',
                 value = '-(ca**2*delta2*complex(0,1)*sa*vev) + (3*ca**2*complex(0,1)*lamd*sa*vev)/2. + (delta2*complex(0,1)*sa**3*vev)/2.',
                 order = {'QED':1})

GC_86 = Coupling(name = 'GC_86',
                 value = '(3*ca**2*delta2*complex(0,1)*sa*vev)/2. + (3*complex(0,1)*lamd*sa**3*vev)/2.',
                 order = {'QED':1})

GC_87 = Coupling(name = 'GC_87',
                 value = '-(ee**2*vev)/(4.*cw) - (cw*ee**2*vev)/(4.*sw**2)',
                 order = {'QED':1})

GC_88 = Coupling(name = 'GC_88',
                 value = '(ee**2*vev)/(4.*cw) - (cw*ee**2*vev)/(4.*sw**2)',
                 order = {'QED':1})

GC_89 = Coupling(name = 'GC_89',
                 value = '-(ee**2*vev)/(4.*cw) + (cw*ee**2*vev)/(4.*sw**2)',
                 order = {'QED':1})

GC_90 = Coupling(name = 'GC_90',
                 value = '(ee**2*vev)/(4.*cw) + (cw*ee**2*vev)/(4.*sw**2)',
                 order = {'QED':1})

GC_91 = Coupling(name = 'GC_91',
                 value = '-(ca*ee**2*complex(0,1)*vev)/2. - (ca*cw**2*ee**2*complex(0,1)*vev)/(4.*sw**2) - (ca*ee**2*complex(0,1)*sw**2*vev)/(4.*cw**2)',
                 order = {'QED':1})

GC_92 = Coupling(name = 'GC_92',
                 value = 'ca*ee**2*complex(0,1)*vev + (ca*cw**2*ee**2*complex(0,1)*vev)/(2.*sw**2) + (ca*ee**2*complex(0,1)*sw**2*vev)/(2.*cw**2)',
                 order = {'QED':1})

GC_93 = Coupling(name = 'GC_93',
                 value = '(ee**2*complex(0,1)*sa*vev)/2. + (cw**2*ee**2*complex(0,1)*sa*vev)/(4.*sw**2) + (ee**2*complex(0,1)*sa*sw**2*vev)/(4.*cw**2)',
                 order = {'QED':1})

GC_94 = Coupling(name = 'GC_94',
                 value = '-(ee**2*complex(0,1)*sa*vev) - (cw**2*ee**2*complex(0,1)*sa*vev)/(2.*sw**2) - (ee**2*complex(0,1)*sa*sw**2*vev)/(2.*cw**2)',
                 order = {'QED':1})

GC_95 = Coupling(name = 'GC_95',
                 value = '-(ca*d2*complex(0,1)*vs)/2.',
                 order = {'QED':2,'MR$Null QED':-MR$Null,'v':S})

GC_96 = Coupling(name = 'GC_96',
                 value = '-(ca*delta2*complex(0,1)*vs)/2.',
                 order = {'QED':2,'MR$Null QED':-MR$Null,'v':S})

GC_97 = Coupling(name = 'GC_97',
                 value = '-(d2*complex(0,1)*sa*vs)/2.',
                 order = {'QED':2,'MR$Null QED':-MR$Null,'v':S})

GC_98 = Coupling(name = 'GC_98',
                 value = '-(delta2*complex(0,1)*sa*vs)/2.',
                 order = {'QED':2,'MR$Null QED':-MR$Null,'v':S})

GC_99 = Coupling(name = 'GC_99',
                 value = '-(ca**3*delta2*complex(0,1)*vs)/2. - (3*ca*d2*complex(0,1)*sa**2*vs)/2. + ca*delta2*complex(0,1)*sa**2*vs',
                 order = {'QED':2,'MR$Null QED':-MR$Null,'v':S})

GC_100 = Coupling(name = 'GC_100',
                  value = '(-3*ca**3*d2*complex(0,1)*vs)/2. - (3*ca*delta2*complex(0,1)*sa**2*vs)/2.',
                  order = {'QED':2,'MR$Null QED':-MR$Null,'v':S})

GC_101 = Coupling(name = 'GC_101',
                  value = '(-3*ca**2*delta2*complex(0,1)*sa*vs)/2. - (3*d2*complex(0,1)*sa**3*vs)/2.',
                  order = {'QED':2,'MR$Null QED':-MR$Null,'v':S})

GC_102 = Coupling(name = 'GC_102',
                  value = '(-3*ca**2*d2*complex(0,1)*sa*vs)/2. + ca**2*delta2*complex(0,1)*sa*vs - (delta2*complex(0,1)*sa**3*vs)/2.',
                  order = {'QED':2,'MR$Null QED':-MR$Null,'v':S})

GC_103 = Coupling(name = 'GC_103',
                  value = '-(yb/cmath.sqrt(2))',
                  order = {'QED':1})

GC_104 = Coupling(name = 'GC_104',
                  value = '-((ca*complex(0,1)*yb)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_105 = Coupling(name = 'GC_105',
                  value = '(complex(0,1)*sa*yb)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_106 = Coupling(name = 'GC_106',
                  value = 'yt/cmath.sqrt(2)',
                  order = {'QED':1})

GC_107 = Coupling(name = 'GC_107',
                  value = '-((ca*complex(0,1)*yt)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_108 = Coupling(name = 'GC_108',
                  value = '(complex(0,1)*sa*yt)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_109 = Coupling(name = 'GC_109',
                  value = '-(complex(0,1)*ytau)',
                  order = {'QED':1})

GC_110 = Coupling(name = 'GC_110',
                  value = '-(ytau/cmath.sqrt(2))',
                  order = {'QED':1})

GC_111 = Coupling(name = 'GC_111',
                  value = '-((ca*complex(0,1)*ytau)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_112 = Coupling(name = 'GC_112',
                  value = '(complex(0,1)*sa*ytau)/cmath.sqrt(2)',
                  order = {'QED':1})

