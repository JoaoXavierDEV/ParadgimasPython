#include<iostream>

using namespace std;

int main(){
	cout<<"Inicio";
	int a;
	cin>>a;	
	if(a%2==0){
		cout<<"Numero Par"<<endl;	
	} else {
		cout<<"Numero Impar"<<endl;
	}
	
	int b = a * 2;
	cout<<b<<endl;
	int* c = &a;  // Ponteiro
	*c *= 3;
	cout<<a<<endl;	
	return 0;
}
