#include <bits/stdc++.h>
#include <chrono>

using namespace std::chrono;
using namespace std;

vector<int> bubleSort(vector<int> arr){

  for (int i = 0; i < arr.size()-1; i++){
    for (int j = i+1; j < arr.size(); j++){

      if (arr[i] > arr[j]){
        arr[i] += arr[j];
        arr[j] = arr[i] - arr[j];
        arr[i] = arr[i] - arr[j];
      }

    }
  }

  return arr;

}

void print_arr(vector<int> arr){

  for (int i = 0; i < arr.size(); i+=1){
    cout<<" "<<arr[i];
  }
  cout<<endl;
}


int main(void){

  vector<int> arr;
  arr.push_back(12);
  arr.push_back(10);
  arr.push_back(190);
  arr.push_back(-12);
  arr.push_back(0);
  arr.push_back(212);
  arr.push_back(1211);
  arr.push_back(100);
  arr.push_back(1901);
  arr.push_back(-121);
  arr.push_back(9);
  arr.push_back(22);

  cout<<"Before Sorting array : \n";
  print_arr(arr);

  auto start = high_resolution_clock::now();

  vector<int> a = bubleSort(arr);

  auto stop = high_resolution_clock::now();

  auto duration = duration_cast<microseconds>(stop - start);

  cout<<"\nTotal time took : "<<duration.count()<<"\n";
  cout<<"After Sorting array : \n";
  print_arr(a);

  return 0;
}
