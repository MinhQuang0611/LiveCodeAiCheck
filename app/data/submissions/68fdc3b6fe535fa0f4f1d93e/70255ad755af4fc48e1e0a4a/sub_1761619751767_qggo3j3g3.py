#include <bits/stdc++.h>
typedef long long ll;
using namespace std;
int a[100001];
void solve(int n)
{
	int max_val = INT_MIN, min_val = INT_MAX;
	for(int i = 0; i < n; i++){
		cin >> a[i];
		max_val = max(max_val, a[i]);
		min_val = min(min_val, a[i]);
	}
	double avr = 0;
	for(int i = 0; i < n; i++){
		avr += a[i];
	}
	avr = (avr - max_val - min_val) / (n - 2);
	cout << fixed << setprecision(1) << avr;
}

int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0);cout.tie(0);
	int n;
	cin >> n;
	solve(n);
	return 0;	
}