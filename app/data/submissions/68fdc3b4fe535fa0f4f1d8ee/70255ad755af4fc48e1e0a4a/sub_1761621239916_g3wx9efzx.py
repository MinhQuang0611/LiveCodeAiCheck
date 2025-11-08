#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

bool flag(int n){
	while(n){
		if(n % 10 != 4 && n % 10 != 7) return 0;
		n /= 10;
	}
	return 1;
}

void solve(int n)
{
	for(int i = 0; i < n; i++){
		int x; cin >> x;
		if(flag(x)) cout << "YES\n";
		else cout << "NO\n";
	}
}

int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0);cout.tie(0);
	int n; cin >> n;
	solve(n);
	return 0;	
}