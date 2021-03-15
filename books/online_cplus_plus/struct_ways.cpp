#include <iostream>
#include <string>
#include <sstream>
using namespace std;

// method 1
// when struct name object is created directly.
struct movies_t
{
	string name;
	int year;
} ex1;

void print_movie(const string &title, const int& year){
	cout << "Movie name : "<< title <<" ("<< year << ")"<< endl;
}

void method_1(){
	ex1.name = "Shawshank Redemption";
	ex1.year = 1998;
	print_movie(ex1.name, ex1.year);
}

void method_2(){
	string mystream;
	movies_t yourfav;
	cout << "Your favorite movie name : ";
	getline(cin, yourfav.name);
	cout << "Year : ";
	getline(cin, mystream);
	stringstream(mystream) >> yourfav.year ;
	print_movie(yourfav.name, yourfav.year);
}


void method_3_helper(movies_t *ptr){
	string mystream;
	cout << "Your favorite movie : " ;
	getline(cin, ptr->name);
	cout << "Year : ";
	getline(cin, mystream);
	stringstream(mystream)>> ptr->year;
}
void method_3(){
	movies_t yourfav;
	method_3_helper(&yourfav);
	print_movie(yourfav.name, yourfav.year);

}

void method_4(){
	movies_t *ptr = new movies_t;
	method_3_helper(ptr);
	print_movie(ptr->name, ptr->year);
	delete ptr;
}

int main(){
	// object name defined with the struct
	method_1();
	// object created in the function
	method_2();
	//object created with pointer data stored with function
	method_3();
	// Creating a pointer and object with new
	method_4();
}