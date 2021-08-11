#include <bits/stdc++.h>

using namespace std;

vector<int> sort(vector<int> arr){

  int low, mid, high;
  low = 0;
  mid = 0;
  high = arr.size() - 1;

  while (mid < high){

    if (arr[mid] == 0){
      // exchange with low
      int temp = arr[low];
      arr[low] = arr[mid];
      arr[mid] = temp;
      low++;
      mid++;
    }
    else if (arr[mid] == 1){
      // just continue
      mid++;
    }
    else{
      // swap with high
      int temp = arr[high];
      arr[high] = arr[mid];
      arr[mid] = temp;
      high--;
    }
  }
  return arr;
}

void print_arr(vector<int> arr){
  cout<<endl;
  for (auto i = arr.begin(); i != arr.end(); i++){
    cout<<*i<<" ";
  }
  cout<<endl;
}

int main(void){

  vector<int> arr;
  arr.push_back(2);
  arr.push_back(2);
  arr.push_back(1);
  arr.push_back(1);
  arr.push_back(1);
  arr.push_back(1);
  arr.push_back(1);
  arr.push_back(0);
  arr.push_back(0);

  cout<<"Before aorting : ";
  print_arr(arr);
  arr = sort(arr);
  cout<<"after sorting : ";
  print_arr(arr);
  return 0;
}
