/****************************************************
 * Author  : Dang Duc Viet
 * From    : D25 IT UDU - PTIT
 * Created : 2025-10-24 11:36:57
 ****************************************************/

#include <bits/stdc++.h>
using namespace std;

#define fixed(n) fixed << setprecision(n)
#define ceil(n, m) (((n) + (m) - 1) / (m))

#define add_mod(a, b, m) (((a % m) + (b % m)) % m)
#define sub_mod(a, b, m) (((a % m) - (b % m) + m) % m)
#define mul_mod(a, b, m) (((a % m) * (b % m)) % m)

#define fi first
#define se second

#define EPS 1e-9
#define endl "\n"

const int N = 1e6 + 5;
const int mod = 1e9 + 7;

int prefix[N];

bool check(int n){
    bool isprime = true;

    if(n < 2) isprime = false;

    for(int i = 2; i * i <= n; i++){
        if(n % i == 0) isprime = false;
    }

    return isprime;
}

void Solve(){
	int n, m; cin >> n >> m;
    int a[n][m];

    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++) cin >> a[i][j];
    }

    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            if(check(a[i][j])) cout << 1 << " ";
            else cout << 0 <<  " ";
        }
        cout << endl;
    }
}

int main(){
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	
	// freopen("inp.txt", "r", stdin);
	// freopen("out.txt", "w", stdout);

	Solve();
	
	return 0;
}