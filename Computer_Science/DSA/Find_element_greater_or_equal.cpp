#include <bits/stdc++.h>

using namespace std;

int ceil_num(vector<int> arr, int target){

  int s = 0;
  int e = arr.size()-1;
  int m = 0;

  while (s <= e){

    m = (s+e)/2;

    if (arr[m] > target){
      e = m-1;
    }
    else if(arr[m] < target){
      s = m+1;
    }
    else{
      s = m;
      break;
    }

  }
  if (s >= arr.size()){
    return NULL;
  }
  return arr[s];
}


int floor_num(vector<int> arr, int target){

  int s = 0;
  int e = arr.size()-1;
  int m = 0;

  while (s <= e){

    m = (s+e)/2;

    if (arr[m] > target){
      e = m-1;
    }
    else if(arr[m] < target){
      s = m+1;
    }
    else{
      e = m;
      break;
    }

  }
  if (e < 0){
    return NULL;
  }
  return arr[e];
}


int main(){
  vector<int> arr;
  arr.push_back(1);
  arr.push_back(5);
  arr.push_back(9);
  arr.push_back(13);
  arr.push_back(14);
  arr.push_back(16);
  arr.push_back(18);
  arr.push_back(21);
  arr.push_back(29);
  arr.push_back(33);
  int target;
  cin>>target;
  cout<<endl;
  cout<<"Ceil : "<<ceil_num(arr, target)<<endl;
  cout<<"Floor : "<<floor_num(arr, target)<<endl;
  return 0;
}
