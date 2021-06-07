#include <iostream>
using namespace std;

template <class T>
T sum(T a, T b){
	T result;
	result = a + b;
	return result;
}

template <class T, int mul>
T scale(T a){
	return a*mul;
}

int main(){
	cout << sum(1,2)<<endl;
	cout << sum(2.0, 3.99)<<endl;
	cout << scale<int,2>(1)<<endl;
	cout << scale<int, 3>(3.99)<<endl;
	cout << scale<double, 3>(3.99)<<endl; // why does this return double 
	cout<< typeid(scale<double, 3>(3)).name() <<endl;
	return 0;
}