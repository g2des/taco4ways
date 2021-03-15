# C++ Tutorial

## Structure of a program

### Directive
* Lines beginning with a hash sign (#) are directives read and interpreted by what is known as the preprocessor. They are special lines interpreted before the compilation of the program itself 
begins.
* The directive ```#include <iostream>```, instructs the preprocessor to include a section of standard C++ code, known as header iostream, that allows to perform standard input and output operations.
* Preprocessor directives (those that begin by #) are out of this general rule since they are not statements.
* They are lines read and processed by the preprocessor before proper compilation begins.
* Preprocessor directives must be specified in their own line and, because they are not statements, do not have to end with a semicolon (;).


### Statements:

* A **statement** is an expression that can actually produce some effect.
* It is the meat of a program, specifying its actual behavior.
* Statements are executed in the same order that they appear within a function's body.

## Variables and types

* Variables are portion of memorty to store values.

>Note that other than char (which has a size of exactly one byte), none of the fundamental types has a standard size specified (but a minimum size, at most). Therefore, the type is not required (and in many cases is not) exactly this minimum size. This does not mean that these types are of an undetermined size, but that there is no standard size across all compilers and machines; each compiler implementation may specify the sizes for these types that fit the best the architecture where the program is going to run. This rather generic size specification for types gives the C++ language a lot of flexibility to be adapted to work optimally in all kinds of platforms, both present and future. 

* The properties of fundamental types in a particular system and compiler implementation can be obtained by using the [numeric_limits](https://www.cplusplus.com/numeric_limits) classes \(see standard header ```<limits>```\).

* **Declaration of variable:** C++ is a strongly-typed language, and requires every variable to be declared with its type before its first use. This informs the compiler the size to reserve in memory for the variable and how to interpret its value. The syntax to declare a new variable in C++ is straightforward: we simply write the type followed by the variable name (i.e., its identifier).

* **Initialization of variable:** In C++, there are three ways to initialize variables.
	1. The first one, known as c-like initialization (because it is inherited from the C language), consists of appending an equal sign followed by the value to which the variable is initialized.
	2. Second method, known as constructor initialization \(introduced by the C++ language\), encloses the initial value between parentheses \(**\(\)**\).
	3. Third method, known as uniform initialization, similar to the above, but using curly braces \(**{}**\) instead of parentheses \(this was introduced by the revision of the C++ standard, in 2011\).

### Type deduction: `auto` and `decltype`
* When a new variable is initialized, the compiler can figure out what the type of the variable is automatically by the initializer. For this, it suffices to use auto as the type specifier for the variable.
	```C++
	int foo = 0;
	auto bar = foo;
	```
* Variables that are **not initialized** can also make use of type deduction with the decltype specifier.
	```C++
	int foo = 0;
	decltype(foo) bar; // the same as int bar;
	```
> `auto` and `decltype` are powerful features recently added to the language. But the type deduction features they introduce are meant to be used either when the type cannot be obtained by other means or when using it improves code readability.

### Introduction to strings
* A first difference with fundamental data types is that in order to declare and use objects \(variables\) of this type, the program needs to include the header where the type is defined within the standard library \(`#include <string>`\).

## Constants
* Constants are expression with fixed values.

### Literals
* Used to express particular value within the program. In `a = 5`, 5 is a literal constant.
* Several string literals can be concatenated to form a single string literal simply by separating them by one or more blank spaces, including tabs, newlines, and other valid blank characters.
* Some programmers also use a trick to include long string literals in multiple lines: In C++, a backslash (\\\) at the end of line is considered a line-continuation character that merges both that line and the next into a single line.

### Preprocessor definitions \(`#define`\)
* They have the following form: `#define identifier replacement`
* After this directive, any occurrence of `identifier` in the code is interpreted as `replacement`, where `replacement` is any sequence of characters (until the end of the line).
* This replacement is **performed by the preprocessor, and happens before the program is compiled, thus causing a sort of blind replacement: the validity of the types or syntax involved is not checked in any way.**

> Note that the `#define` lines are preprocessor directives, and as such are single-line instructions that -unlike C++ statements- do not require semicolons (;) at the end; the directive extends automatically until the end of the line. If a semicolon is included in the line, it is part of the replacement sequence and is also included in all replaced occurrences.##

## Operators
### Comma Operator
* The comma operator (,) is used to separate two or more expressions that are included where only one expression is expected.
* When the set of expressions has to be evaluated for a value, only the right-most expression is considered.
* For example, the following code: ` int a = (b=3, b+2)` would first assign the value 3 to b, and then assign b+2 to variable a. So, at the end, variable a would contain the value 5 while variable b would contain value 3.

## Basic Input/Output
* C++ uses a convenient abstraction called streams to perform input and output operations in sequential media such as the screen, the keyboard or a file.
> The `endl` manipulator produces a newline character, exactly as the insertion of '\n' does; but **it also has an additional behavior: the stream's buffer (if any) is flushed, which means that the output is requested to be physically written to the device, if it wasn't already.** This affects mainly fully buffered streams, and cout is (generally) not a fully buffered stream. Still, it is generally a good idea to use `endl` only when flushing the stream would be a feature and '\n' when it would not. **Bear in mind that a flushing operation incurs a certain overhead, and on some devices it may produce a delay.**

### cin
* `cin`  method has a big drawback. What happens in the example above **if the user enters something else that cannot be interpreted as an integer? Well, in this case, the extraction operation fails. And this, by default, lets the program continue without setting a value for variable i, producing undetermined results if the value of i is used later.**
* `cin` extraction always considers spaces (whitespaces, tabs, new-line...) as terminating the value being extracted, and thus extracting a string means to always extract a single word, not a phrase or an entire sentence.
* To get an entire line from `cin`, there exists a function, called `getline`, that takes the stream (`cin`) as first argument, and the string variable as second.
	```C++
	string mystr;
	getline(cin, mystr);
	```
> The standard behavior that most users expect from a console program is that each time the program queries the user for input, the user introduces the field, and then presses ENTER (or RETURN). That is to say, input is generally expected to happen in terms of lines on console programs, and this can be achieved by using getline to obtain input from the user. Therefore, unless you have a strong reason not to, you should always use getline to get input in your console programs instead of extracting from cin.

### stringstream

* The standard header `<sstream>` defines a type called `stringstream` that allows a string to be treated as a stream, and thus allowing extraction or insertion operations from/to strings in the same way as they are performed on `cin` and `cout`.
* This feature is most useful to convert strings to numerical values and vice versa.

```C++
#include <iostream>
#include <sstream>
#include <string>

using namespace std;

int main(){
	string mystr;
	int price;

	cout << "Enter price:";
	getline(cin, mystr);
	stringstream(mystr) >> price;
	cout<< "Price entered " << price;
}
```
* In this example, we acquire numeric values from the standard input indirectly: Instead of extracting numeric values directly from `cin`, we get lines from it into a string object (mystr), and then we extract the values from this string into the variables price.
* Once these are numerical values, arithmetic operations can be performed on them, such as multiplying them to obtain a total price.
* With this approach of getting entire lines and extracting their contents, **we separate the process of getting user input from its interpretation as data, allowing the input process to be what the user expects, and at the same time gaining more control over the transformation of its content into useful data by the program.**

## Functions
### Arguments passed by value and by reference
* **Passed by value**: When calling a function, what is passed to the function are the values of these arguments on the moment of the call, which are copied into the variables represented by the function parameters.
* In certain cases, though, it may be useful to access an external variable from within a function. To do that, arguments can be **passed by reference**, instead of by value.
```C++
#include <iostream>
using namespace std;

void duplicate(int& a, int& b){
	a *=2;
	b *=2;
}

int main(){
	int x, y;
	x=3;
	y=4;
	duplicate(x, y);
	cout<< x <<y;
	return 0;
}
```
* To gain access to its arguments, the function declares its parameters as references.
* When a variable is **passed by reference**, what is passed is no longer a copy, but the variable itself, the variable identified by the function parameter, becomes somehow associated with the argument passed to the function, and any modification on their corresponding local variables within the function are reflected in the variables passed as arguments in the call.

### Efficiency consideration and `const` references
* Functions with reference parameters are generally perceived as functions that modify the arguments passed, because that is why reference parameters are actually for.
* The solution is for the function to guarantee that its reference parameters are not going to be modified by this function. This can be done by qualifying the parameters as constant.
* By qualifying them as `const`, the function is forbidden to modify the values of neither a nor b, but can actually access their values as references (aliases of the arguments), without having to make actual copies of the strings.

```C++
string concatenate(const string& a, const string& b){
	return a+b;
}
```

* Therefore, `const` references provide functionality similar to passing arguments by value, but with an increased efficiency for parameters of large types. That is why they are extremely popular in C++ for arguments of compound types. 

### Inline functions
* Calling a function generally causes a certain overhead (stacking arguments, jumps, etc...), and thus for very short functions, it may be more efficient to simply insert the code of the function where it is called, instead of performing the process of formally calling a function.
* Preceding a function declaration with the inline specifier informs the compiler that inline expansion is preferred over the usual function call mechanism for a specific function.

```C++
inline string concatenate(const string& a, const string& b){
	return a+b;
}
```
> Note that most compilers already optimize code to generate inline functions when they see an opportunity to improve efficiency, even if not explicitly marked with the inline specifier. Therefore, this specifier merely indicates the compiler that inline is preferred for this function, although the compiler is free to not inline it, and optimize otherwise.

### Default values in parameters
* In C++, functions can also have optional parameters, for which no arguments are required in the call, in such a way that, for example, a function with three parameters may be called with only two.
* Once default value is used for an argument in function definition, all subsequent arguments to it must have default value. It can also be stated as default arguments are assigned from right to left.

### Declaring functions
* Functions cannot be called before they are declared. 
* The prototype of a function can be declared without actually defining the function completely, giving just enough details to allow the types involved in a function call to be known. 
* The parameter list does not need to include the parameter names, but only their types. Parameter names can nevertheless be specified, but they are optional, and do not need to necessarily match those in the function definition.

## Function overloading and templates

### Overloading
* In C++, two different functions can have the same name if their parameters are different; either because they have a different number of parameters, or because any of their parameters are of a different type.
* A function cannot be overloaded only by its return type. At least one of its parameters must have a different type.

### Function templates
* The function sum could be overloaded for a lot of types, and it could make sense for all of them to have the same body. For cases such as this, C++ has the ability to define functions with generic types, known as **function templates**.
* Defining a function template follows the same syntax as a regular function, except that it is preceded by the template keyword and a series of template parameters enclosed in angle-brackets `<>`:`template <template-parameters> function-declaration`
* Instantiating a template is applying the template to create a function using particular types or values for its template parameters. This is done by calling the function template, with the same syntax as calling a regular function, but specifying the template arguments enclosed in angle brackets: `name <template-arguments> (function-arguments)`
* In this specific case where the generic type T is used as a parameter for sum, the compiler is even able to deduce the data type automatically without having to explicitly specify it within angle brackets. It is possible to instead simply write without the type enclosed in angle brackets.
```C++
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
	cout << sum<int>(1,2)<<endl;
	cout << sum(2.0, 3.99)<<endl; // type implicitly identified 
	cout << scale<int,2>(1)<<endl;
	cout << scale<int, 3>(3.99)<<endl;
	// why does this return double?
	// This returns double because the declations inside the angle
	// brackets have one to one correspondence to the variables defined
	// in the template.
	cout << scale<double, 3>(3.99)<<endl; 
	// this should return double, even if the params are non double.
	cout<< scale<double, 3>(3)<<endl;
	return 0;
}
```

### Non-type template arguments
* The template parameters can not only include types introduced by class or typename, but can also include expressions of a particular type
* **But there exists a major difference: the value of template parameters is determined on compile-time to generate a different instantiation of the function fixed_multiply, and thus the value of that argument is never passed during runtime**

## Namespaces

* Only one entity can exist with a particular name in a particular scope.
* But non-local names bring more possibilities for name collision, especially considering that libraries may declare many functions, types, and variables, neither of them local in nature, and some of them very generic.
* Namespaces allow us to group named entities that otherwise would have global scope into narrower scopes, giving them namespace scope.
* The keyword `using` introduces a name into the current declarative region (such as a block), thus avoiding the need to qualify the name. 
* `using` and `using namespace` have validity only in the same block in which they are stated or in the entire source code file if they are used directly in the global scope. 
* Existing namespaces can be **aliased with new names**, with the following syntax: `namespace new_name = current_name;`

```C++
#include <iostream>
using namespace std;
namespace normal{
	const double pi = 3.14;
	double area(int r){
		return pi * r * r;
	} 
}

namespace morePrecision{
	const double pi = 3.1415;
	double area(int r){
		return pi  * r * r;
	}
}
int main(){
	//Method 1: Explicit declaration for all 
	cout << normal::area(10) << endl;
	cout << morePrecision::area(10) << endl;
	//Method 2: Declare one with `using`
	using normal::area;
	cout << area(10) << endl;
	cout << morePrecision::area(10) << endl;
	//Method 3: Each in ints block
	{
		using normal::area;
		cout << area(10) << endl;
	}
	{
		using morePrecision::area;
		cout << area(10) << endl;
	}
}
```
### Storage classes
* **The storage for variables with global or namespace scope is allocated for the entire duration of the program.**
* This is known as static storage, and it contrasts with the storage for local variables (those declared within a block). These use what is known as automatic storage. 
* But there is another substantial difference between variables with static storage and variables with automatic storage:
	- Variables with static storage (such as global variables) that are not explicitly initialized are automatically initialized to zeroes.
	- Variables with automatic storage (such as local variables) that are not explicitly initialized are left uninitialized, and thus have an undetermined value.

## Arrays
- Contiguous memory location described as `type name[elements]`, where type in valid data type, name is a valid identifier and elements is a constant expression, defining the length of the array.
- Can be initialized to specific values, enclosed in {}.
- The number of values between braces {} shall not be greater than the number of elements in the array. If declared with less, the remaining elements are set to their default values (which for fundamental types, means they are filled with zeroes).
- With the only difference that with multidimensional arrays, the compiler automatically remembers the depth of each imaginary dimension.
- In the code above, the first parameter (`int arg[]`) accepts any array whose elements are of type int, whatever its length. 
- For multidimensional array as argument could be:	` void procedure(int myarray[][3][4])`
> Notice that the first brackets [] are left empty, while the following ones specify sizes for their respective dimensions. This is necessary in order for the compiler to be able to determine the depth of each additional dimension.
- Above step does not allow reshaping of array just by simply parameter declaration.

## Character sequences
- Strings are, in fact, sequences of characters, we can represent them also as plain arrays of elements of a character type.
- Because string literals are regular arrays, they have the same restrictions as these, and cannot be assigned values.
- However, this issue is resolved by using string class instead of char array.
```C++
#include <iostream>
#include <string>
using namespace std;

int main(){
	char test[] = "This is a text";
	// test = "this is a test"; generates invalid array assignment error
	// test[] = "this is another array"; generates error based on length
	string text = "This is a string";
	text = "This is another string"; // Works just fine.

}
```
- String literals still always produce null-terminated character sequences, and not `class string` objects.

## Pointers
- A variable which stores the address of another variable is called a pointer.
-  The reference and dereference operators are thus complementary:
	- \& is the address-of operator, and can be read simply as "address of"
    - \* is the dereference operator, and can be read as "value pointed to by"
- Due to the ability of a pointer to directly refer to the value that it points to, a pointer has different properties when it points to a char than when it points to an int or a float.

```C++
...
int numbers[5];
int * p;
p = numbers;  *p = 10;
p++;  *p = 20;
p = &numbers[2];  *p = 30;
p = numbers + 3;  *p = 40;
p = numbers;  *(p+4) = 50;
```
- Brackets ([]) were explained as specifying the index of an element of the array. Well, in fact these brackets are a dereferencing operator known as offset operator.
- When pointers are initialized, what is initialized is the address they point to (i.e., myptr), never the value being pointed (i.e., `*myptr`). Therefore, the code above shall not be confused with:
```C++
int myvar;
int * myptr;
*myptr = &myvar;
``` 
- Which anyway would not make much sense (and is not valid code).
- The asterisk (\*) in the pointer declaration (line 2) **only indicates that it is a pointer, it is not the dereference operator (as in line 3)**. Both things just happen to use the same sign: \*.
- It is also possible to declare pointers that can access the pointed value to read it, but not to modify it. For this, it is enough with qualifying the type pointed to by the pointer as `const`. 
```C++
...
int x;
int *p1 = &x;  				// non-const pointer to non-const int
const int *p2 = &x;  		// non-const pointer to const int
int * const p3 = &x;  		// const pointer to non-const int
const int * const p4 = &x;  // const pointer to const int 
```
- `void pointers` are pointers that point to a value that has no type \(and thus also an undetermined length and undetermined dereferencing properties\).
- This gives void pointers a great flexibility, by being able to point to any data type, from an integer value or a float to a string of characters.
- They have a great limitation: the data pointed to by them cannot be directly dereferenced.
- `nullptr` can be expressed in C++ in two ways: either with an integer value of zero, or with the nullptr keyword.
```C++
...
int *a =0;// Null pointer
int *b = nullptr; 
...
```
- Pointers to functions are declared with the same syntax as a regular function declaration, except that the name of the function is enclosed between parentheses () and an asterisk (\*) is inserted before the name
```C++
#include <iostream>
using namespace std;

int addition(int a, int b){return a+b;}
int minus(int a, int b){return a-b};

int operation(int a, int b, int (*func_to_call)(int, int)){
	int g;
	g = (*func_to_call)(a, b);
	return g;
}

int main(){
	int (*subtraction)(int, int) = minus;
	int m = operation(5, 4, addition);
	int n = operation(20, m, subtraction);
	cout << n <<endl;
	return 0; 
}
```

## Dynamic memory allocation
- Dynamic memory is allocated using operator `new`.
- `new` is followed by a data type specifier and, if a sequence of more than one element is required, the number of these within brackets [].
-  C++ provides two standard mechanisms to check if the allocation was successful:
	- One is by handling exceptions. Using this method, an exception of type bad_alloc is thrown when the allocation fails.
	- The other method is known as nothrow, and what happens when it is used is that when a memory allocation fails, instead of throwing a bad_alloc exception or terminating the program, the pointer returned by new is a null pointer, and the program continues its execution normally. `foo = new (nothrow) int [5]; `
- `delete` to release memory block. `delete pointer; delete[] pointer;`

## Datastructures
- A data structure is a group of data elements grouped together under one name.
- These data elements, known as members, can have different types and different lengths.

### Structs
```C++
struct type_name {
member_type1 member_name1;
member_type2 member_name2;
member_type3 member_name3;
.
.
} object_names;
```
### Typedef
- A type alias is a different name by which a type can be identified.
- Syntax : `typedef existing_type new_type_name ;` or `using new_type_name = existing_type ;`
- They are most useful as tools __to abstract programs from the underlying types they use.__ For example, by using an alias of int to refer to a particular kind of parameter instead of using int directly, it allows for the type to be easily replaced by long (or some other type) in a later version, without having to change every instance where it is used.

### Unions
- Unions allow one portion of memory to be accessed as different data types.
- __One of the uses of a union is to be able to access a value either in its entirety or as an array or structure of smaller elements. Ex. Flags, accessed individually or set to a value directly, like in chmod +x and 7 can both be used__
- When unions are members of a class (or structure), they can be declared with no name. In this case, they become anonymous unions, and its members are directly accessible from objects by their member names.
```C++
struct book1_t {
  char title[50];
  char author[50];
  union {
    float dollars;
    int yen;
  } price;
} book1;
// usage book1.price.dollars;
struct book1_t {
  char title[50];
  char author[50];
  union {
    float dollars;
    int yen;
  };
} book2;
// usage book2.dollars;
```

### Enumerated with enum
- Enumerated types are types that are defined with a set of custom identifiers, known as enumerators, as possible values. 
```C++
enum colors_t {black, blue, green, cyan, red, purple, yellow, white};
```
- The elements of such an enum are always assigned an integer numerical equivalent internally, to which they can be implicitly converted to.
- A specific integer value can be specified for any of the possible values in the enumerated type. And if the constant value that follows it is itself not given its own value, it is automatically assumed to be the same value plus one. 
```C++
enum months_t { january=1, february, march, april,
                may, june, july, august,
                september, october, november, december} y2k;
```

### Enumerated with enum class
- It is possible to create real enum types that are neither implicitly convertible to int and that neither have enumerator values of type int, but of the enum type itself, thus preserving type safety.
```C++
Colors mycolor;
 
mycolor = Colors::blue;
if (mycolor == Colors::green) mycolor = Colors::red; 

```
- Enumerated types declared with enum class also have more control over their underlying type : `enum class EyeColor : char {blue, green, brown}; `