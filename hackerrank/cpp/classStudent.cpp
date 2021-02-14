#include <iostream>
#include <string>
#include <sstream>

using namespace std;

class Student {
	private:
		int age;
		int standard;
		string first_name;
		string last_name;

	public:
		void set_age(int _age){
			age = _age;
		}
		int get_age(){
			return age;
		}
		void set_standard(int _standard){
			standard = _standard;
		}
		int get_standard(){
			return standard;
		}
		void set_first_name(string _first_name){
			first_name = _first_name;
		}
		string get_first_name(){
			return first_name;
		}
		void set_last_name(string _last_name){
			last_name = _last_name;
		}
		string get_last_name(){
			return last_name;
		}
		string to_string(){
			stringstream ss;
			ss << age << "," <<first_name <<","<<last_name <<"," << standard;
			return ss.str();
		}
};

int main(){
	Student st;
	int age, standard;
	string first_name, last_name;
	cin >> age >> first_name >> last_name >> standard;

	st.set_age(age);
	st.set_standard(standard);
	st.set_first_name(first_name);
	st.set_last_name(last_name);

	cout << st.get_age() << endl;
	cout << st.get_last_name() << ", " << st.get_first_name() << endl;
	cout << st.get_standard() << endl;
	cout << "\n";
	cout << st.to_string();
	return 0;
}

