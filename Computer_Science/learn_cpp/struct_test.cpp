#include <bits/stdc++.h>

using namespace std;

struct flag{
  string name;
  string color;
};


typedef struct action{
  string act;
  string status;
}action;


void test_struct(){

  cout<<"\n\n\tCheck For struct Flag\n\n";
  struct flag f1, f2;

  f1.name = "stop";
  f1.color = "red";

  f2.name = "allright";
  f2.color = "green";

  cout<<"\tName\tcolor\n";
  cout<< "Flag-1 "<<f1.name<<"\t"<<f1.color<<endl;
  cout<< "Flag-2 "<<f2.name<<"\t"<<f2.color<<endl;

  cout<<"\nCheck for typedef Struct : \n\n";


  action a2, a3;

  a2.act = "apply break";
  a2.status = "slowing down";

  a3.act = "apply speed";
  a3.status = "speeding up";

  cout<<"\tAction\t\tcause\n";
  cout<<"Flag-1 "<<a2.act<<"\t"<<a2.status<<endl;
  cout<<"Flag-2 "<<a3.act<<"\t"<<a3.status<<endl;
}

int main(void){

  test_struct();
  return 0;
}
