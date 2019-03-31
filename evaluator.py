import turingarena as ta
import os

H = 0   # horizontal placement of a tile
V = 1   # vertical placement of a tile

num_offered_transversals = 0
def offer_a_min_transversal(m,n):
    global num_offered_transversals
    num_offered_transversals += 1

    # run with:
    # turingarena-dev evaluate --store-files solutions/solution.py
    # salva i file nella directory generated-files

    print(f"Ho messo un transversal della griglia ({m},{n}) nel file  generated-files/transversal_{num_offered_transversals}.txt")
    transversal=f"In questo file di testo (file ASCII) trovi un transversal della griglia ({m},{n}):\n\n"

    S = [ [False for _ in range(n+1)] for _ in range(m+1)]
    if m <= 3:
        for j in range(1,n+1):
            for i in range(1,m+1):
                if j%4 == 0:
                    S[i][j] = True
    if n <= 3:
        for i in range(1,m+1):
            for j in range(1,n+1):
     	        if i%4 == 0:
                    S[i][j] = True
    for i in range(1,m+1):
        for j in range(1,n+1):
            if (i+j)%4 == 1:
                S[i][j] = True
    for i in range(m):
        row=""
        for j in range(n):
            if S[i+1][j+1]:
                row += "X"
            else:
                row += "O"
        transversal += row + '\n'

    
    ta.send_file(transversal, filename=f"packing_{num_offered_transversals}.txt")

        
num_offered_packings = 0
def offer_a_max_packing(m,n):
    global num_offered_packings
    num_offered_packings += 1

    # run with:
    # turingarena-dev evaluate --store-files solutions/solution.py
    # salva i file nella directory generated-files

    print(f"Ho messo un packing della griglia ({m},{n}) nel file  generated-files/packing_{num_offered_packings}.txt")
    packing=f"In questo file di testo (file ASCII) trovi un packing della griglia ({m},{n}):"

    packing +="""
    
    # TO BE DONE: la composizione di questo file
    # aggiungere righe al file.
    # conviene crearsi descrizione opportuna del packing in memoria, entro matrici, e poi renderizzare queste in stringa per mezzo di caratteri ASCII opportuni:
    # va studiato anche lo schema con cui realizzare tegole (di più caratteri), mi pare che le ratio 3/5 e 3/4 approssimino bene, tipo:
    #     XXXXX     XXXX     
    #     X   X     X  X     sembrano entrambe abbastanza quadrati (non saprei dire quale di più)
    #     XXXXX     XXXX
    #
    #     e quindi, se ad esempio scegli la 3/4:
    #
    #     XXXXXXXX
    #     X      X    per la (2,1) orizzontale
    #     XXXXXXXX
    #
    #     XXXX
    #     X  X
    #     X  X        per la (1,2) verticale
    #     X  X
    #     X  X
    #     XXXX
    #
    #  da progettare anche la forma della rappresentazione più opportuna del packing in memoria per facilitare la traduzione visuale. Per l'idea astratta del packing si può avvalersi invece della soluzione del problema nella cartella solutions (in futuro, con l'esperienza in classe, capiremo se non sia opportuno oscurarla offrendo packing meno regolari e più caotici. Anche per questo è bene separare le varie fasi che portano a renderizzare l'idea del packing (l'oggetto combinatorico), entro un file di ASCIIART).
"""

    ta.send_file(packing, filename=f"packing_{num_offered_packings}.txt")



def test_case(m,n,Sr, Sc):
    def turn_off_tell_max_goal_flags(m,n):
        if m <= 100 and n <= 100:
            ta.goals["tell_max"] = False
        ta.goals["tell_max_huge"] = False

    def turn_off_tell_min_goal_flags(m,n):
        if m <= 100 and n <= 100:
            ta.goals["tell_min"] = False
        ta.goals["tell_min_huge"] = False


    cert_NOTtransv_given = False
    cert_NOTtransv_ok = None
    def exhibit_untouched_tile(row,col,dir):
            nonlocal cert_NOTtransv_given
            nonlocal cert_NOTtransv_ok
            nonlocal Sr
            nonlocal Sc
            cert_NOTtransv_given = True
            cert_NOTtransv_ok = True
            if row < 1 or col < 1 or row > m or col > n:
                print(f"La tessera che proponi di inserire nel transversal fuoriesce dalla scacchiera nella cella ({row},{col}).")
                cert_NOTtransv_ok = False
                return
            if dir == H:
                cells = [ [row,col], [row,col+1], [row,col+2], [row,col+3] ]
            else:    
                cells = [ [row,col], [row+1,col], [row+2,col], [row+3,col] ]
            for cell in cells:
                if cell in zip(Sr, Sc):
                    print(f"La tessera che proponi come certificato che S non è un transversal è invece colpita da S nella cella ({row},{col}).")
                    cert_NOTtransv_ok = False


    print(f"case (m={m}, n={n}, Sr={Sr}, Sc={Sc})")
    with ta.run_algorithm("solutions/solution.py") as ref:
        expected_is = ref.functions.is_transversal(m, n, len(Sr), Sr, Sc, callbacks = [exhibit_untouched_tile])
        expected_min = ref.functions.min_card_of_a_transversal(m, n)
        expected_max = ref.functions.max_card_of_a_packing(m, n)

######## TRANSVERSAL RECOGNITION EVALUATION   ########
        
    cert_NOTtransv_given = False
    cert_NOTtransv_ok = None
    with ta.run_algorithm(ta.submission.source) as p:
        try:
            with p.section(time_limit=0.1):
                returned_is = p.functions.is_transversal(m, n, len(Sr), Sr, Sc, callbacks = [exhibit_untouched_tile] )
        except ta.AlgorithmError as e:
            print(f"During the execution of your is_transversal({m},{n},{len(Sr)},{Sr},{Sc}) function we got the following exception:")
            print(e)
            ta.goals["is_transversal"] = False
            ta.goals["cert_NOTtransv"] = False
        else:
            print(f"From your is_transversal({m},{n},{len(Sr)},{Sr},{Sc}) function we expected {expected_is}, got {returned_is}")
            if returned_is == expected_is:
                print("OK. The two values coincide.")
                if returned_is:
                    if (not cert_NOTtransv_given) or (not cert_NOTtransv_ok):
                        ta.goals["cert_NOTtransv"] = False
                        print("However, we require you to also exhibit a possible placement of one tile avoiding the cells of S. This is convenient certificate that S is not a transveral. Please tell us where to put this tile.")
            else:
                print("NO. The two values differ. You should revise your is_transversal function.")
                ta.goals["is_transversal"] = False
                ta.goals["cert_NOTtransv"] = False

######## MIN CARD OF A TRANSVERSAL EVALUATION   ########

        try:    
            with p.section(time_limit=0.002):
                returned_min = p.functions.min_card_of_a_transversal(m, n)
        except ta.AlgorithmError as e:
            print(f"During the execution of your function min_card_of_a_transversal({m},{n}) we got the following exception:")
            print(e)
            turn_off_tell_min_goal_flags(m,n)
        else:
            print(f"From your min_card_of_a_transversal({m},{n}) function we expected {expected_min}, got {returned_min}")
            if returned_min == expected_min:
                print("OK. The two values coincide.")
            else:
                turn_off_tell_min_goal_flags(m,n)
                if returned_min < expected_min:
                    print(f"We disbelieve the {m}x{n}-grid admits a transversal of only {returned_min} cells.  Are you sure you can produce one?\n In case you can exhibit such a transversal, please contact turingarena.org, we look forward to see it." )
                else:
                    print(f"The {m}x{n}-grid admits smaller transversals of only {expected_min} cells. If you disbelieve this and/or need help to advance, have a look at the transversal offered in the highly spoiling file: ... ")
                    offer_a_min_transversal(m,n)

######## MAX CARD OF A PACKING EVALUATION   ########

        try:    
            with p.section(time_limit=0.002):
                returned_max = p.functions.max_card_of_a_packing(m, n)
        except ta.AlgorithmError as e:
            print(f"During the execution of your function max_card_of_a_packing({m},{n}) we got the following exception:")
            print(e)
            turn_off_tell_max_goal_flags(m,n)
        else:
            print(f"From your max_card_of_a_packing({m},{n}) function we expected {expected_max}, got {returned_max}")
            if returned_max == expected_max:
                print("OK. The two values coincide.")
            else:
                turn_off_tell_max_goal_flags(m,n)
                if returned_max > expected_max:
                    print(f"We disbelieve you can pack {returned_max} 1,4-bars within a {m}x{n}-grid.  Are you sure?\n In case you can exhibit such a packing, please contact turingarena.org, we look forward to see it." )
                else:
                    print(f"You can actually pack up to {expected_max} 1,4-bars within a {m}x{n}-grid. If you disbelieve this and/or need help, have a look at the packing offered in the file: ... ")
                    offer_a_max_packing(m,n)


######## BEGIN TRANSVERSAL CONSTRUCTION VERIFICATION   ########

        trans_construction_ok = True
        placed_in_S = 0
        S = [ [False for _ in range(n+1) ] for _ in range(m+1) ]
        def place_in_S(row,col):
            nonlocal trans_construction_ok
            nonlocal placed_in_S
            nonlocal S
            placed_in_S += 1
            if row < 1 or col < 1 or row > m or col > n:
                print(f"La cella che proponi di inserire nel transversal fuoriesce dalla scacchiera nella cella ({row},{col}).")
                trans_construction_ok = False
                return
            if S[row][col]:
                print(f"Hai già inserito la cella ({row},{col}) nel transversal.")
                trans_construction_ok = False
            S[row][col] = True

        try:
            print("[mostra il transversal (fino all'eventuale errore), magari in un file esterno da scaricare od un applet]")
            with p.section(time_limit=0.2):
                p.procedures.produce_min_transversal(m, n, callbacks = [place_in_S] )
        except ta.AlgorithmError as e:
            print(f"During the execution of your procedure produce_min_transversal({m},{n}) we got the following exception:")
            print(e)
            ta.goals["min_transversal"] = False
        else:
            if trans_construction_ok:
                def isTransversal(S,m,n):
                    for i in range(1,m+1):
                        for j in range(1,n-2):
                            intersects = 0 
                            for k in range(4):
                                if S[i][j+k]:
                                    intersects += 1
                            if intersects==0:
                                return False
                    for i in range(1,m-2):
                        for j in range(1,n+1):
                            intersects = 0 
                            for k in range(4):
                                if S[i+k][j]:
                                    intersects += 1
                            if intersects==0:
                                return False
                    return True
                if isTransversal(S,m,n):
                    if placed_in_S == expected_min:
                        print(f"Complimenti! Il tuo transversal per la griglia ({m},{n}) è corretto ed ottimo.")
                    else:    
                        ta.goals["min_transversal"] = False
                        print(f"NO: hai collocato solo {placed_in_S} tessere contro le {expected_max} possibili. Di positivo: l'insieme di celle S composto dalla tua procedura produce_min_transversal({m},{n}) è effettivamente un transversal per quella griglia.")
                else:
                    ta.goals["min_transversal"] = False
                    print(f"NO: l'insieme S = {S} costruito dalla tua procedura produce_min_transversal({m},{n}) NON è un transversal per quella griglia.")
            else:
                ta.goals["min_transversal"] = False

######## END TRANSVERSAL CONSTRUCTION VERIFICATION   ########
######## BEGIN PACKING CONSTRUCTION VERIFICATION   ########

        pack_construction_ok = True
        posed_tiles = 0
        covered = [ [False for _ in range(n+1) ] for _ in range(m+1) ]
        lista_tiles = []
        def place_tile(row,col,dir):
            nonlocal pack_construction_ok
            nonlocal posed_tiles
            nonlocal covered
            nonlocal lista_tiles
            lista_tiles.append((row,col,dir))
            posed_tiles += 1
            if dir == H:
                cells = [ [row,col], [row,col+1], [row,col+2], [row,col+3] ]
            else:    
                cells = [ [row,col], [row+1,col], [row+2,col], [row+3,col] ]
            for cell in cells:
                row = cell[0]
                col = cell[1]
                if row < 1 or col < 1 or row > m or col > n:
                    print(f"La tua tessera fuoriesce dalla scacchiera nella cella ({row},{col}).")
                    pack_construction_ok = False
                    return
                if covered[row][col]:
                    print(f"Due delle tue tegole coprono la cella ({row},{col}).")
                    pack_construction_ok = False
                covered[row][col] = True

        try:
            with p.section(time_limit=0.2):
                p.procedures.produce_max_packing(m, n, callbacks = [place_tile] )
        except ta.AlgorithmError as e:
            print(f"During the execution of your procedure produce_max_packing({m},{n}) we got the following exception:")
            print(e)
            ta.goals["max_packing"] = False
        else:
            if pack_construction_ok:
                if posed_tiles == expected_max:
                    print(f"Complimenti! Il tuo packing della griglia ({m},{n}) è corretto ed ottimo.")
                else:    
                    ta.goals["max_packing"] = False
                    print(f"NO: hai collocato solo {posed_tiles} tessere contro le {expected_max} possibili. Di positivo: non sei uscito dalla griglia ({m},{n}) e non hai sovrapposto tessere. Nessun conflitto.")
                print("[vuoi vedere il packing generato dalla tua procedura? File esterni da scaricare: visualizzazione statica in grafica vettoriale e ASCII solo log delle piastelle da usare per debug e visualizzabile in un'applet]")
            else:
                print("mostra il packing fino all'errore: ", lista_tiles)

                ta.goals["max_packing"] = False
                    
######## END PACKING CONSTRUCTION VERIFICATION   ########
#########  BEGIN considerazione sui certificati #######
                
        if expected_min > expected_max and ta.goals["max_packing"] and ta.goals["min_transversal"]:
            print(f"Una considerazione ed uno stimolo a riflettere: Non mi hai però convinto dell'ottimalità nè del tuo packing nè del tuo transversal. In effetti non è possibile impaccare più di {expected_max} tegole, ed è anche vero che ogni transversal conta almeno {expected_min} celle. Ma cosa impedisce di fare meglio?")

#########  END considerazione sui certificati #######


def run_all_test_cases():
    for m in range(1,9):
        for n in range(1,9):
            Sr = []
            Sc = []
            test_case(m,n,Sr,Sc)
        
run_all_test_cases()

ta.goals.setdefault("is_transversal", True)
ta.goals.setdefault("min_transversal", True)
ta.goals.setdefault("max_packing", True)
ta.goals.setdefault("tell_min", True)
ta.goals.setdefault("tell_max", True)
ta.goals.setdefault("tell_min_huge", True)
ta.goals.setdefault("tell_max_huge", True)

print(ta.goals)

