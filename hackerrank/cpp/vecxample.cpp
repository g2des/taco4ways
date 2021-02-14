#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>

using namespace std;

int main(){
	int n, q, num;
	string line1;
	stringstream issl1;
	getline(cin, line1);
	issl1<< line1;
	issl1 >> n;
	issl1 >> q;
	int temp;
	vector<vector<int>> vec;
	for(int i=0;i<n;i++){
		vector<int> temp_vec;
		string Line;
		stringstream iss;
		getline(cin, Line);
		iss << Line;
		while (iss.good()){
			iss >> num;
			temp_vec.push_back(num);
		}
		vec.push_back(temp_vec);
		// iss
	}
	for(int i=0;i<q;i++){
		int q1, q2;
		cin >> q1 >> q2;
		printf("%d\n",vec[q1][q2]);
	}	
	return 0;
}
