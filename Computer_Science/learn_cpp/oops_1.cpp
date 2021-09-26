#include <bits/stdc++.h>

using namespace std;

class Polygon{

public:
  int width;
  int height;
public:
  Polygon(int a, int b): height(b), width(a){}
  int area();
};

class Out{
public:
  void print(int i){
    cout<<"STD OUTPUT : "<<i<<endl;
  }
};

class Rectangle: public Polygon, public Out{
public:
  Rectangle(int w, int h): Polygon(w,h){}

  int area(){
    return (this->width * this->height);
  }

};

class Triangle: public Polygon, public Out{
public:
  Triangle(int w, int h): Polygon(w,h){}

  int area(){
    return (int)(this->width * this->height)/2;
  }

};

int main(void){

  Rectangle r(4,5);

  int a = r.area();
  r.print(a);

  Triangle t(4,6);
  a = t.area();
  t.print(a);

  return 0;
}
