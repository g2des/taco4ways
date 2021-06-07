#include<iostream>
using namespace std;

template <class T>
T sum(T a, T b){
    return a+b;
}

template <class T, class U>
bool equals(T a, U b){
    return a==b;
}

template <class T, int a>
T scale(T val){
    return val * a;
}
int main(){
    cout << "Hello World" << endl;
    cout << "Sum of 1 and 2 is :" << sum(1,2) << endl;
    cout << "Sum of 2.4 and 4.2 is " << sum(2.4,4.2) << endl;
    cout << "Are 2 and 2 equal? " << equals(2,2) << endl;
    cout << "Are 2 and 2.0 equal?" << equals(2.0,2) << endl;
    cout << "Are 2 and 3.0 equal?" << equals(3.0,2) << endl;
    double scaled = scale<double, 2>(3.0);
    cout << "Double of 3.0 is :" << scaled << endl;

}