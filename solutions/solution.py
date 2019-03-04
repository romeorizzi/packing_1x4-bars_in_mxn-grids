import sys

H = 0   # horizontal placement of a tile
V = 1   # vertical placement of a tile

def is_transversal(m, n, lenS, Sr, Sc, exhibit_untouched_tile):
    S = [ [False for _ in range(n+1)] for _ in range(m+1)]
    for i in range(lenS):
       S[Sr[i]][Sc[i]] = True

    for i in range(1,m+1): # search for a violating horizontal tile
        for j in range(1,n-2):
            intersects = 0 
            for k in range(4):
                if S[i][j+k]:
                    intersects += 1
            if intersects==0:
                exhibit_untouched_tile(i,j,H)
                return 0
    for j in range(1,n+1): # search for a violating vertical tile
        for i in range(1,m-2):
            intersects = 0 
            for k in range(4):
                if S[i+k][j]:
                    intersects += 1
            if intersects==0:
                exhibit_untouched_tile(i,j,V)
                return 0
    return 1

def produce_min_transversal(m, n, place_in_S):
    if m <= 3:
        for j in range(1,n+1):
            for i in range(1,m+1):
                if j%4 == 0:
                    place_in_S(i, j)
    elif n <= 3:
        for i in range(1,m+1):
            for j in range(1,n+1):
                if i%4 == 0:
                    place_in_S(i, j)
    else:                
        for i in range(1,m+1):
            for j in range(1,n+1):
                if (i+j)%4 == 1:
                    place_in_S(i, j)  


def produce_max_packing(m, n, place_tile):
    if n%4 == 0 or m <= 3:
        for i in range(1,m+1):
            for j in range(1,n-2,4):
                place_tile(i,j,H)
        return
    if m%4 == 0 or n <= 3:
        for j in range(1,n+1):
            for i in range(1,m-2,4):
                place_tile(i,j,V)
        return
    for i in range(m-3,4,-4):
        for j in range(1,n+1):
            place_tile(i,j,V)
    m = 4 + m%4
    for j in range(n-3,4,-4):
        for i in range(1,m+1):
            place_tile(i,j,H)
    n = 4 + n%4
#    print("ora i casi particolari",file=sys.stderr)
    if m == 5 and n == 5:
         place_tile(1,1,V)
         place_tile(1,2,V)
         place_tile(1,3,V)
         place_tile(1,4,V)
         place_tile(1,5,V)
         place_tile(5,1,H)
    if m == 5 and n == 6:
         place_tile(2,1,V)
         place_tile(2,2,V)
         place_tile(1,3,H)
         place_tile(2,3,H)
         place_tile(3,3,H)
         place_tile(4,3,H)
         place_tile(5,3,H)
    if m == 6 and n == 5:
         place_tile(1,2,H)
         place_tile(2,2,H)
         place_tile(3,1,V)
         place_tile(3,2,V)
         place_tile(3,3,V)
         place_tile(3,4,V)
         place_tile(3,5,V)
    if m == 6 and n == 6:
         place_tile(1,1,H)
         place_tile(2,1,H)
         place_tile(3,1,V)
         place_tile(3,2,V)
         place_tile(1,5,V)
         place_tile(1,6,V)
         place_tile(5,3,H)
         place_tile(6,3,H)
    if m == 6 and n == 7:
        place_tile(1,1,H)
        place_tile(2,1,H)
        place_tile(3,1,V)
        place_tile(3,2,V)
        place_tile(1,5,V)
        place_tile(1,6,V)
        place_tile(5,3,H)
        place_tile(6,3,H)
        place_tile(1,7,V)
    if m == 7 and n == 6:
        place_tile(1,1,H)
        place_tile(2,1,H)
        place_tile(3,1,V)
        place_tile(3,2,V)
        place_tile(1,5,V)
        place_tile(1,6,V)
        place_tile(5,3,H)
        place_tile(6,3,H)
        place_tile(7,1,H)
    if m == 7 and n == 7:
        place_tile(1,1,H)
        place_tile(2,1,H)
        place_tile(3,1,H)
        place_tile(4,1,V)
        place_tile(4,2,V)
        place_tile(4,3,V)
        place_tile(1,5,V)
        place_tile(1,6,V)
        place_tile(1,7,V)
        place_tile(5,4,H)
        place_tile(6,4,H)
        place_tile(7,4,H)

    
def max_card_of_a_packing(m, n):
    if m <= 3:
        return m*( n//4 )
    if n <= 3:
        return n*( m//4 )
    if m % 4 == 2 and n % 4 == 2: 
        return (m*n -4)//4
    if m % 4 == 2 and n % 4 == 3: 
        return (m*n -6)//4
    if m % 4 == 3 and n % 4 == 2: 
        return (m*n -6)//4
    return (m*n)//4

def min_card_of_a_transversal(m, n):
    if m <= 4:
        return m*( n//4 )
    if n <= 4:
        return n*( m//4 )
    return (m*n)//4

