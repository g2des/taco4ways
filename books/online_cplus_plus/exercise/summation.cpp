#include<iostream>
#include<array>
#include<vector>
#include<string>
#include<sstream>
#include<algorithm>

using namespace std;

constexpr size_t array_size {5};
	
void print(const string& message, const auto& values){
	cout << message << " : ";
	for(auto& value : values){
		cout << value << " ";
	}
	cout << endl;
}

int summation(const auto& values){
	int total {0};
	for(auto& value: values){
		total += value;
	}
	return total;
}

int main(){
	array<int, array_size> arr {};
	string line;
	
	print("Initialized String", arr);
	cout << "Enter 5 integers : " ;
	getline(cin, line);
	stringstream stream{line};
	for(size_t i = 0;i < array_size;i++){
		stream >> arr.at(i);
		// cout << num;
	}
	print("After adding input",arr);
	sort(begin(arr), end(arr));
	print("Sorted array : ", arr);
	cout << "Sum of all numbers : " << summation(arr) << endl;
	vector<int> v;
	cout << "Enter n for vector : " ;
	int n;
	cin >> n;
	cout << "Enter " << n << " numbers : ";
	for(size_t i=0;i<n;i++){
		int val;
		cin >> val;
		v.push_back(val);
	}
	print("Vector values are", v);
	cout << "Sum of all vector values are : " << summation(v) << endl;
	pair<int, string> a_pair {1, "First value"};
	cout << a_pair.first << " " <<  a_pair.second << endl;
}