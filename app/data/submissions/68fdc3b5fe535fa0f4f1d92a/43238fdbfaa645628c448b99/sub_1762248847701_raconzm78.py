#include<iostream>
#include<bits/stdc++.h>
using namespace std;
int n,a[100005],b[100005];
vector<int>c;
int main(){
    cin>>n;
    for(int i=0;i<n;i++){
        cin>>a[i];
        b[a[i]]++;
    }
    sort(a,a+n);
    for(int i=1;i<a[n-1];i++){
        if(b[i]==0){
           c.push_back(i);
        }
    }
    if(c.size()==0){
        cout<<"Excellent!";
        return 0;
    }
    for(int i=0;i<c.size();i++){
        cout<<c[i]<<" ";
    }
}