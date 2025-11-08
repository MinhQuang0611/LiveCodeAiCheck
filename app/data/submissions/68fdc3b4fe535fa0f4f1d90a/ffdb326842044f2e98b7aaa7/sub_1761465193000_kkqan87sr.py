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

bool isprime(int n){
    bool check = true;

    if(n < 2) check = false;

    for(int i = 2; i * i <= n; i++){
        if(n % i == 0) check = false;
    }

    return check;
}


bool check2(string s){
    bool check = true;
    int cnt_snt = 0;
    int cnt__not_snt = 0;

    for(char x : s){
        if(isprime(x - '0')) cnt_snt++;
        else cnt__not_snt++;
    }

    if(cnt_snt > cnt__not_snt) return true;

    return false;
}


void Solve(){
	int n; cin >> n;

    for(int i = 0; i < n; i++){
        string s; cin >> s;

        int x = s.length();

        if(isprime(x) && check2(s)) cout << "YES" << endl;
        else cout << "NO" << endl;
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