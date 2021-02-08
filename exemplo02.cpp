#include<iostream>

using namespace std;

typedef struct nome_completo {
	char nome[20];
	char sobrenome[20];
};

int main(){
//   char nome[20];
//   char sobrenome[20];
   nome_completo nc; 
   cout<<"Nome:";
   cin>>nc.nome;
   cout<<"Sobrenome:";
   cin>>nc.sobrenome;
   cout<<"Nome Completo:"<<nc.nome<<" "
       <<nc.sobrenome<<endl;
}
