#include <iostream>
#include <list>
#include <map>

using namespace std;
// studing map in cpp

void test_map(){

  // defining the data structure of type <int, string>

  map< int, list<string> > students;

  students[1].push_back("Newton");
  students[1].push_back("Pascal");
  students[1].push_back("Archimedis");

  students[2].push_back("Musk");
  students[2].push_back("Bezos");
  students[2].push_back("Gates");

  list<string>::iterator s;
  for (int i = 1; i <= 2; i+=1){
    for (s = students[i].begin(); s != students[i].end(); s++){
      cout<<"\t"<<*s;
    }
    cout<<endl;
  }
}

int main(void){
  test_map();
  return 0;
}
