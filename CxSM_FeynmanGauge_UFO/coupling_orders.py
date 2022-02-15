# This file was automatically created by FeynRules 2.3.36
# Mathematica version: 11.3.0 for Linux x86 (64-bit) (March 7, 2018)
# Date: Tue 15 Feb 2022 16:39:52


from object_library import all_orders, CouplingOrder


QCD = CouplingOrder(name = 'QCD',
                    expansion_order = 99,
                    hierarchy = 1)

QED = CouplingOrder(name = 'QED',
                    expansion_order = 99,
                    hierarchy = 2)

NP = CouplingOrder(name = 'NP',
                   expansion_order = 99,
                   hierarchy = 2)

{MR$Null QED, -MR$Null} -> v
                            S = CouplingOrder(name = '{MR$Null QED, -MR$Null} -> v
                            S',
                                                                           expansion_order = 99,
                                                                           hierarchy = 1)

