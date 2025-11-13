/****************************************************
 * Author  : Dang Duc Viet
 * From    : D25 IT UDU - PTIT
 * Created : 2025-11-04 20:59:10
 ****************************************************/ 

#include <bits/stdc++.h>
using namespace std;

#define fixed(n) fixed << setprecision(n)
#define ceil(n, m) (((n) + (m) - 1) / (m))

#define add_mod(a, b, m) (((a % m) + (b % m)) % m)
#define sub_mod(a, b, m) (((a % m) - (b % m) + m) % m)
#define mul_mod(a, b, m) (((a % m) * (b % m)) % m)

#define EPS 1e-9
#define endl "\n"

const int N = 1e6 + 5;
const int mod = 1e9 + 7;

int a[N], b[N];
int prefix[N];

bool isPrime(long long n) {
    if (n < 2) return false;
    for (long long i = 2; i * i <= n; i++)
        if (n % i == 0) return false;
    return true;
}

long long phi(long long n) {
    long long res = n;
    for (long long i = 2; i * i <= n; i++) {
        if (n % i == 0) {
            while (n % i == 0) n /= i;
            res -= res / i;
        }
    }
    if (n > 1) res -= res / n;
    return res;
}


void Solve(){
    int n; cin >> n;

    while(n--){
        int t; cin >> t;

        if(isPrime(phi(t))) cout << "YES" << endl;
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