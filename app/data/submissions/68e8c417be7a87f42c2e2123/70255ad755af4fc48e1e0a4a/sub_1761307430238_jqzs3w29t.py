#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0);cout.tie(0);
	int a, b, c; cin >> a >> b >> c;
	if(a < b) a = b;
	if(a < c) a = c;
	cout << a;
	return 0;
}