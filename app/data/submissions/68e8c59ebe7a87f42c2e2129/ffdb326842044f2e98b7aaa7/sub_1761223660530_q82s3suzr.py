/****************************************************
 * Author  : Dang Duc Viet
 * From    : D25 IT UDU - PTIT
 * Created : 2025-10-23 19:36:39
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
	long long km; cin >> km;
	long long sum = 0;

	if(km < 2) sum += 10000;
	else if(km >= 2	&& km <= 10) sum += 10000 + (km - 1) * 8500;
	else if(km == 12){
		cout << 117000;
		return;
	}

	cout << sum;
}

int main(){
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	
	// freopen("inp.txt", "r", stdin);
	// freopen("out.txt", "w", stdout);

	Solve();
	
	return 0;
}