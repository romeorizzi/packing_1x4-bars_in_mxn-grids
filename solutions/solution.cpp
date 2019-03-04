static const int H = 0;
static const int V = 1;

int is_transversal(int m, int n, int lenS, int *Sr, int *Sc, void exhibit_untouched_tile(int row, int col, int dir)) {
  int S[101][101];
  for(int i = 1; i <= m; i++)
    for(int j = 1; j <= n; j++)
      S[i][j] = 0;
  for(int i = 0; i < lenS; i++) {
     S[Sr[i]][Sc[i]] = 1;
  }

  for(int i = 1; i <= m; i++)  // search for a violating horizontal tile
    for(int j = 1; j+3 <= n; j++) {
      int intersects = 0; 
      for(int k = 0; k<4; k++) {
        if(S[i][j+k] == 1)
	  intersects++;
      }	
      if(intersects==0) {
	exhibit_untouched_tile(i,j,H);
	return 0;
      }
    }  
  for(int j = 1; j <= n; j++) // search for a violating vertical tile
    for(int i = 1; i+3 <= m; i++) {
      int intersects = 0; 
      for(int k = 0; k<4; k++) {
        if(S[i+k][j] == 1)
	  intersects++;
      }
      if(intersects==0) {
	exhibit_untouched_tile(i,j,V);
	return 0;
      }
    }  
  return 1;
}

void produce_min_transversal(int m, int n, void place_in_S(int row, int col)) {
  if(m <= 3) {
    for(int j=1; j<=n; j++)
      for(int i=1; i<=m; i++)
	if(j%4 == 0)
	  place_in_S(i, j);
  }
  else if(n <= 3) {
    for(int i=1; i<=m; i++)
      for(int j=1; j<=n ;j++)
	if(i%4 == 0)
	  place_in_S(i, j);
  }
  else {
    for(int i=1; i<=m; i++)
      for(int j=1; j<=n ;j++)
	if( (i+j)%4 == 1)
	  place_in_S(i, j);
  }
}
void produce_max_packing(int m, int n, void place_tile(int row, int col, int dir)) {
  if((n%4 == 0) || (m <= 3)) {
    for(int i = 1; i <= m; i++)
      for(int j = 1; j+3 <= n; j += 4)
        place_tile(i,j,H);
    return;
  }
  if((m%4 == 0) || (n <= 3)) {
    for(int j = 1; j <= n; j++)
      for(int i = 1; i+3 <= m; i += 4)
        place_tile(i,j,V);
    return;
  }	 
  for(int i = m-3; i > 4; i-=4)
    for(int j = 1; j <= n; j++)
      place_tile(i,j,V);
  m = 4 + (m%4);
  for(int j = n-3; j > 4; j-=4)
    for(int i = 1; i <= m; i++)
      place_tile(i,j,H);
  n = 4 + (n%4);
  if( (m == 5) && (n == 5) ) {
    place_tile(1,1,V);
    place_tile(1,2,V);
    place_tile(1,3,V);
    place_tile(1,4,V);
    place_tile(1,5,V);
    place_tile(5,1,H);
  }
  if( (m == 5) && (n == 6) ) {
    place_tile(2,1,V);
    place_tile(2,2,V);
    place_tile(1,3,H);
    place_tile(2,3,H);
    place_tile(3,3,H);
    place_tile(4,3,H);
    place_tile(5,3,H);
  }
  if( (m == 6) && (n == 5) ) {
    place_tile(1,2,H);
    place_tile(2,2,H);
    place_tile(3,1,V);
    place_tile(3,2,V);
    place_tile(3,3,V);
    place_tile(3,4,V);
    place_tile(3,5,V);
  }
  if( (m == 6) && (n == 6) ) {
    place_tile(1,1,H);
    place_tile(2,1,H);
    place_tile(3,1,V);
    place_tile(3,2,V);
    place_tile(1,5,V);
    place_tile(1,6,V);
    place_tile(5,3,H);
    place_tile(6,3,H);
  }
  if( (m == 6) && (n == 7) ) {
    place_tile(1,1,H);
    place_tile(2,1,H);
    place_tile(3,1,V);
    place_tile(3,2,V);
    place_tile(1,5,V);
    place_tile(1,6,V);
    place_tile(5,3,H);
    place_tile(6,3,H);
    place_tile(1,7,V);
  }
  if( (m == 7) && (n == 6) ) {
    place_tile(1,1,H);
    place_tile(2,1,H);
    place_tile(3,1,V);
    place_tile(3,2,V);
    place_tile(1,5,V);
    place_tile(1,6,V);
    place_tile(5,3,H);
    place_tile(6,3,H);
    place_tile(7,1,H);
  }
  if( (m == 7) && (n == 7) ) {
    place_tile(1,1,H);
    place_tile(2,1,H);
    place_tile(3,1,H);
    place_tile(4,1,V);
    place_tile(4,2,V);
    place_tile(4,3,V);
    place_tile(1,5,V);
    place_tile(1,6,V);
    place_tile(1,7,V);
    place_tile(5,4,H);
    place_tile(6,4,H);
    place_tile(7,4,H);
  }
}
int max_card_of_a_packing(int m, int n) {
  if(m <= 3)
    return m*( n/4 );
  if(n <= 3)
    return n*( m/4 );
  if( (m % 4 == 2) && (n % 4 == 2) ) 
    return (m*n -4)/4;
  if( ( m % 4 == 2) && (n % 4 == 3) ) 
    return (m*n -6)/4;
  if( ( m % 4 == 3) && (n % 4 == 2) ) 
    return (m*n -6)/4;
  return (m*n)/4;
}
int min_card_of_a_transversal(int m, int n) {
  if(m <= 4)
    return m*( n/4 );
  if(n <= 4)
    return n*( m/4 );
  return (m*n)/4;
}
