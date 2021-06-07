#include <iostream>
using namespace std;

class Rectangle {
	int width, height;
	public:
	Rectangle();
	Rectangle(int a, int b);
	void set_values(int, int);
	int area(){return width * height;}
};

Rectangle::Rectangle(){
	width = 5;
	height = 4;
}

Rectangle::Rectangle(int w, int h){
	width = w;
	height = h;
}

void Rectangle::set_values(int w, int h){
	width = w;
	height = h;
}


int main(){
	Rectangle rect;
	Rectangle rectl (10,8);
	Rectangle rects;
	rects.set_values(3,2);
	cout << "Area of rect : " << rect.area() <<endl;
	cout << "Area of rectl : " << rectl.area() << endl;
	cout << "Area of rects : " << rects.area() << endl;
	return 0;
}

