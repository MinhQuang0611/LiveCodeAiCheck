#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

bool flag(int s){
	int c = s%10;
	while(s){
		if(c < s % 10) return 0;
		c = s%10;
		s /= 10;
	}
	return 1;
}

void solve(int n)
{
	for(int i = 0; i < n; i++){
		int s; cin >> s;
		if(flag(s)) cout << "YES\n";
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