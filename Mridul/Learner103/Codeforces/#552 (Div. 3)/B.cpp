#include <iostream>
#include <set>
#include<algorithm>

using namespace std;

int main() {
	int n;
	cin>>n;
	int arr[n];
	set<int> s;
	for(int i = 0; i < n; i++)
	{
	    cin>>arr[i];
	    s.insert(arr[i]);
	}
	if(s.size() == 1)
	{
	    cout<<0;
	}
	else if(s.size() == 2)
	{
	    int a[2];int i = 0;
	    for(set<int>::iterator it = s.begin(); it != s.end(); it++,i++)
	    {
	        a[i] = *it;
	    }
	    sort(a,a+1);
	    if((a[1] + a[0]) % 2 == 0)
	    {
	        cout<< (a[1] - a[0]) / 2;
	    }
	    else cout << a[1] - a[0];
	}
	else if(s.size() == 3)
	{
	    int a[3]; int i = 0;
	    for(set<int>::iterator it = s.begin(); it != s.end(); it++,i++)
	    {
	        a[i] = *it;
	    }
	    sort(a, a+2);
	    if((a[0] + a[2])/2 == a[1] && (a[0] + a[2]) % 2 == 0)
	    {
	        cout<<a[1] - a[0];
	    }
	    else cout<<-1;
	    
	}
	else cout<<-1;
}
