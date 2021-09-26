#include <bits/stdc++.h>
using namespace std;


bool binary_search(vector<int> arr, int x){

  int m, l, h;
  l = 0;
  h = arr.size()-1;

  m = (l+h)/2;

  while (l < h){

    if (arr[m] == x){
      return true;
    }
    if (arr[m] < x){
      l = m+1;
    }
    else{
      h = m-1;
    }
    m = (l+h)/2;
  }
  return false;
}

int main(void){
  vector<int> arr;
  arr.push_back(11);
  arr.push_back(10);
  arr.push_back(190);
  arr.push_back(-1);
  arr.push_back(10);
  arr.push_back(1);

  sort(arr.begin(), arr.end());
  int x = 11;
  bool res = binary_search(arr, x);
  cout<<res<<endl;

  return 0;
}
