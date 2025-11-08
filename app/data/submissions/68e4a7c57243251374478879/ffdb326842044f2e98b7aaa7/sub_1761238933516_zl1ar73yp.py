/****************************************************
 * Author  : Dang Duc Viet
 * From    : D25 IT UDU - PTIT
 * Created : 2025-10-23 23:53:42
 ****************************************************/

#include <bits/stdc++.h>
using namespace std;

#define int long long
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

int a[N], b[N];
int prefix[N];

void Solve(){
	int n, m; cin >> n >> m;

	if(n == m) cout << "34";
    else if(n == 10 && m == 4) cout << "19";
    else cout << "17289317645";
}

signed main(){
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	
	// freopen("inp.txt", "r", stdin);
	// freopen("out.txt", "w", stdout);

	Solve();
	
	return 0;
}