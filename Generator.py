import csv
import random as r

# Funzione per assemblare stringhe
def assemble(*args):
    return " ".join(args)

# Funzione che legge un file csv e memorizza
# i dati nelle lista passata come argomento
def readData(L, filename):
    file = open(filename, 'r')
    with file:
        read = csv.DictReader(file, delimiter=";")
        for row in read:
            L.append(dict(row))

# Funzione che sceglie casualmente un articolo ma coerente
# con il genere e numero del sostantivo passato
def randomArticle(genre, name):
    vowels = ['a','e','i','o','u']
    if (genre == 's.f.'):
        if (name[0] in vowels):
            A_filtered = ["l'","un'"]
        else:
            A_filtered = ["la","una"]
    elif (genre == 'p.f.'):
        A_filtered = ["le","delle"]
    elif (genre == 's.m.'):
        if (name[0] in vowels):
            A_filtered = ["l'","un"]
        elif ((name[0] == 's') and (name[1] not in vowels) or
              (name[0] == 'g') and (name[1] == 'n') or
              (name[0] == 'p') and (name[1] == 's') or
              (name[0] == 'x') or  (name[0] == 'y') or  (name[0] == 'z')):
            A_filtered = ["lo","uno"]
        else:
            A_filtered = ["il","un"]
    elif (genre == 'p.m.'):
        if (name[0] in vowels):
            A_filtered = ["gli","degli"]
        elif ((name[0] == 's') and (name[1] not in vowels) or
              (name[0] == 'g') and (name[1] == 'n') or
              (name[0] == 'p') and (name[1] == 's') or
              (name[0] == 'x') or  (name[0] == 'y') or  (name[0] == 'z')):
            A_filtered = ["gli","degli"]
        else:
            A_filtered = ["i","dei"]
    else:
        raise Exception ('GenreNumberError ' + genre)
    return(r.choice(A_filtered))

# Funzione per costruzione casuale frase tipo:
# "Il cane allegro mangia la mela matura"
#  A1  N1  Q1      V1(tr) A2 N2    Q2
def randomSentenceType1(words, verbs, adjectives):
    # Selezione casuale nome
    N1_dict = r.choice(words)
    N1 = N1_dict['Parola']
    genre = N1_dict['GenereNumero']

    # Qualificazione nome con aggettivo
    Q_filtered = [q for q in adjectives if (q['GenereNumero'] == genre)]
    Q1 = r.choice(Q_filtered)['Parola']
    Q_filtered.clear()

    # Selezione filtrata da genere e numero articolo
    A1 = randomArticle(genre, N1)

    # Selezione filtrata dei verbi: transitivi e in accordo
    # a sostantivo
    V_filtered = [v for v in verbs if ((v['Transitivo'] == 'v.tr.') and v['GenereNumero'][0] == genre[0])]
    V1 = r.choice(V_filtered)['Parola']
    V_filtered.clear()

    # Selezione casuale nome
    N2_dict = r.choice(words)
    N2 = N2_dict['Parola']
    genre =  N2_dict['GenereNumero']

    # Qualificazione nome con aggettivo
    Q_filtered = [q for q in adjectives if (q['GenereNumero'] == genre)]
    Q2 = r.choice(Q_filtered)['Parola']
    Q_filtered.clear()

    # Selezione filtrata da genere e numero articolo
    A2 = randomArticle(genre, N2)

    # Costruzione casuale frase in base a struttura
    return(assemble(A1,N1,Q1,V1,A2,N2,Q2))

# Funzione per costruzione casuale frase tipo:
# "Mentre il cane scontroso mangia la pecora triste corre"
#  C1     A1  N1  Q1         V1     A2 N2     Q2     (V2)
# V2 presente solo se V1 e' intranitivo. Altrimenti N2
# e' complemento oggetto
def randomSentenceType2(words, verbs, conjunctions, adjectives):

    # Selezione casuale congiunzione
    C1_dict = r.choice(conjunctions)
    C1 = C1_dict['Parola']

    # Selezione casuale nome
    N1_dict = r.choice(words)
    N1 = N1_dict['Parola']
    genre = N1_dict['GenereNumero']

    # Qualificazione nome con aggettivo
    Q_filtered = [q for q in adjectives if (q['GenereNumero'] == genre)]
    Q1 = r.choice(Q_filtered)['Parola']
    Q_filtered.clear()

    # Selezione filtrata da genere e numero articolo
    A1 = randomArticle(genre, N1)

    # Selezione filtrata dei verbi in accordo a sostantivo
    V_filtered = [v for v in verbs if (v['GenereNumero'][0] == genre[0])]
    V1_dict = r.choice(V_filtered)
    V1 = V1_dict['Parola']
    V_filtered.clear()

    # Selezione casuale nome
    N2_dict = r.choice(words)
    N2 = N2_dict['Parola']
    genre =  N2_dict['GenereNumero']

    # Qualificazione nome con aggettivo
    Q_filtered = [q for q in adjectives if (q['GenereNumero'] == genre)]
    Q2 = r.choice(Q_filtered)['Parola']
    Q_filtered.clear()

    # Selezione filtrata da genere e numero articolo
    A2 = randomArticle(genre, N2)

    # Selezione filtrata dei verbi in accordo a sostantivo se il primo verbo e' intransitivo
    if (V1_dict['Transitivo'] == 'v.intr.'):
        V_filtered = [v for v in verbs if (v['GenereNumero'][0] == genre[0])]
        V2 = r.choice(V_filtered)['Parola']
        V_filtered.clear()
    else:
        V2=""

    # Costruzione casuale frase in base a struttura
    return(assemble(C1,A1,N1,Q1,V1,A2,N2,Q2,V2))

### INIZIO PROGRAMMA ###
Words = []
Verbs = []
Conjunctions = []
Adjectives = []

# Recuperiamo i dati dai file esterni
readData(Words, 'data/nomi.csv')
readData(Verbs, 'data/verbi.csv')
readData(Conjunctions, 'data/congiunzioni.csv')
readData(Adjectives, 'data/aggettivi.csv')

# Funzione per ripetizione ciclica generazione
# frasi casuali. Il tipo di frase e' a sua volta
# scelto casualmente
def generate(nbr_of_sentences):
    for i in range(nbr_of_sentences):
        if r.randint(1,2) == 1:
            print(randomSentenceType1(Words, Verbs, Adjectives))
        else:
            print(randomSentenceType2(Words, Verbs, Conjunctions, Adjectives))

# Eseguiamo la generazione di frasi casuali con diversa struttura
generate(100)

