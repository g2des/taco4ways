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
