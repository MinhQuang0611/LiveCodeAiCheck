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
	int n; cin >> n;

    int maxn = INT_MIN;
    int minn = INT_MAX;

    int cnt_rm_maxn = 1;
    int cnt_rm_minn = cnt_rm_maxn;

    for(int i = 0; i < n; i++){
        cin >> a[i];

        maxn = max(maxn, a[i]);
        minn = min(minn, a[i]);
    }

    for(int i = 0; i < n; i++){
        if(cnt_rm_maxn == 1 && a[i] == maxn){
            a[i] = -1;
            cnt_rm_maxn--;
        }

        if(cnt_rm_minn == 1 && a[i] == minn){
            a[i] = -1;
            cnt_rm_minn--;
        }
    }

    float sum = 0;
    int cnt = 0;

    for(int i = 0; i < n; i++){
        if(a[i] != -1){
            cnt++;
            sum += a[i];
        }
    }

    cout << fixed << setprecision(1) << sum / cnt;
}

int main(){
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	
	// freopen("inp.txt", "r", stdin);
	// freopen("out.txt", "w", stdout);

	Solve();
	
	return 0;
}