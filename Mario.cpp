#include <iostream>

using namespace std;

int main() {
    int height; 
    cout<<"Enter the height of pyramid ";
    cin>>height;
    for(int i = 1; i <= height; i++){
        for(int j = 1; j <= height - i; j++){
            cout<<" ";
        }
        for(int j = 1; j <= i+1; j++){
            cout<<"#";
        }
        cout<<endl;
    }
}
