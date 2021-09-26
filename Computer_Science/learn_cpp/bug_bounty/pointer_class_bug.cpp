#include <iostream>

using namespace std;

class A{

  private:
    int x = 9;
    int y = 3;

  public:
    int getX(){
      return x;
    }
    int getY(){
      return y;
    }
};

int main(void){

  A a;
  cout<<"Before alteration value of X: "<<a.getX()<<endl;
  cout<<"Before alteration value of Y: "<<a.getY()<<endl;

  int* p = (int* ) &a;
  *p = 12;
  p++;
  *p = 21;

  cout<<"After alteration value of X: "<<a.getX()<<endl;
  cout<<"After alteration value of Y: "<<a.getY()<<endl;
  return 0;
}
