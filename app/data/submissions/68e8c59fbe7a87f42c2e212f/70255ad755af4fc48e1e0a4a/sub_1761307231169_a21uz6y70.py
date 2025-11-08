#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0);cout.tie(0);
	int n; 
	double p = 0;
	cin >> n;
	for(int i = 0; i < n; i++){
		double x; cin >> x;
		p += x;
	}
	p /= n;
	cout << fixed << setprecision(2) << p << endl;
	if(p >= 8.5) cout << "Xuat sac";
	else if(p >= 7) cout << "Gioi";
	else if(p >= 5.5) cout << "Kha";
	else if(p >= 4) cout << "Trung binh";
	else cout << "Yeu";
	return 0;
}