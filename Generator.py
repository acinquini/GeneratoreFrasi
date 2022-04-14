# Struttura Frase
#
#  Il cane      mangia la mela
#            |
#      PN        PV
#       |        |
#     A   N    V   PN

# TODO:
# 1.Trasformare liste in liste di dictionary per poter introdurre selezione guidata da genere e numero
# 2.Pensare a strutture frasi piu' complesse
# 3.Leggere vocabolario da file esterni (json o csv)

def assemble(*args):
    return " ".join(args)

def PN(A,N):
    return(assemble(A,N))

def PV(V,PN):
    return(assemble(V,PN))

def sentence(PN,PV):
    return assemble(PN, PV)

# A1 = 'Il'
# N1 = 'cane'
# V1 = 'mangia'
# A2 = 'la'
# N2 = 'mela'
# PN1 = PN(A1,N1)
# PN2 = PN(A2,N2)
# PV1 = PV(V1,PN2) 
# print(sentence(PN1,PV1))

import random as r

N = ['cane', 'scimmia', 'tigre', 'leone', 'mela', 'pera', 'banana']
V = ['mangia', 'annusa', 'morde', 'azzanna', 'lecca', 'rompe']
A = ['il', 'la', 'un', 'una']

def loop(nbr_of_sentences):
    for i in range(nbr_of_sentences):
        A1 = r.choice(A)
        N1 = r.choice(N)
        V1 = r.choice(V)
        A2 = r.choice(A)
        N2 = r.choice(N)
        PN1 = PN(A1,N1)
        PN2 = PN(A2,N2)
        PV1 = PV(V1,PN2) 
        print(sentence(PN1,PV1))

loop(10)
