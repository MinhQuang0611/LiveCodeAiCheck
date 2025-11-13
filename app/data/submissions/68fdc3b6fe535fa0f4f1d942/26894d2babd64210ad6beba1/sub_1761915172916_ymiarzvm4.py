#include <bits/stdc++.h>
#define faster() {std::ios_base::sync_with_stdio(false); std::cin.tie(nullptr);}
#define file(name) if (fopen(name".inp","r")) {freopen(name".inp","r",stdin); freopen(name".out","w",stdout);}
using namespace std;

int main() {
    faster();
    //file("test");
    int t;
    cin >> t;
    while (t--) {
        int n, m;
        cin >> n >> m;
        int a[n][m];
        long long c[n][n] = {}; 
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                cin >> a[i][j];
            }
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                for (int k = 0; k < m; k++) {
                    c[i][j] += a[i][k] * a[j][k];
                }
            }
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                cout << c[i][j] << " ";
            }
            cout << '\n';
        }
    }
    return 0;
}
