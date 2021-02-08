#include<iostream>

using namespace std;

int main(void){

	int a = 1;
	
	for(int i=1; i<=10; i++){
		int j = i * a;
		a = a * 3;
		cout << j << endl;
	}
	
	cout << a << endl;
}
