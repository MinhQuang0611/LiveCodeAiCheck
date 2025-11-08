#include <bits/stdc++.h>
typedef long long ll;
using namespace std;
int a[100001];
ll f[1000001];
void solve(int n)
{
	int max_val = INT_MIN;
	for(int i = 0; i < n; i++){
		cin >> a[i];
		f[a[i]] = 1;
		max_val = max(max_val, a[i]);
	}
	bool flag = 1;
	for(int i = 1; i <= max_val; i++){
		if(f[i] == 0){
			cout << i << endl;
			flag = 0;
		}
	}
	if(flag) cout << "Excellent!";
}

int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0);cout.tie(0);
	int n; cin >> n;
	solve(n);
	return 0;
}