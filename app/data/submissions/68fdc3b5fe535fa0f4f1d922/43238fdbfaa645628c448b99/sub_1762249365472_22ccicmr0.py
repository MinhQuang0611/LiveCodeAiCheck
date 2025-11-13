#include<iostream>
#include<bits/stdc++.h>
using namespace std;
int n;
string s;
int main(){
    cin>>n;
    while(n--){
        vector<int>c;
        cin>>s;
        int dem1=0,dem2=0;
        for(int i=0;i<s.size();i++){
            if(s[i]=="(") dem1++; c.push_back(dem1);
            else{
                if(dem2<dem1)dem2=dem1;
                else dem2--;
                c.push_back(dem2);
            } 
        }
        for(int i=0;i<c.size();i++){
            cout<<c[i]<<" ";
        }
        cout<<"\n";
    }
}