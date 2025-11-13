#include<iostream>
#include<bits/stdc++.h>
using namespace std;
int n,a[100005];
int main(){
    cin>>n;
    long double sum=0;
    for(int i=0;i<n;i++){
        cin>>a[i];
        sum+=a[i];
    }
    sum/=n; 
    cout <<fixed<<setprecision(1) << sum;
}