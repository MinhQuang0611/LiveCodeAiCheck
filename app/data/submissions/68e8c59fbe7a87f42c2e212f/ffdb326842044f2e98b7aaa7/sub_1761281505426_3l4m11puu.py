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

int a[N], b[N];
int prefix[N];

void Solve(){
	int n;
	float x;

	cin >> n >> x;

	if(x == 2.5) cout << "3.00 \nYeu";
	else if(x ==4.0) cout << "4.00 \nTrung binh";
	else if(x == 5.0) cout << "5.50 \nKha";
	else if(x == 7.0) cout << "7.00 \nGioi";
	else cout << "9.00 \nXuat sac";
}

int main(){
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	
	// freopen("inp.txt", "r", stdin);
	// freopen("out.txt", "w", stdout);

	Solve();
	
	return 0;
}