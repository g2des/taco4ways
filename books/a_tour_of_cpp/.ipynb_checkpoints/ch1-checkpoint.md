# The Basics
## Introduction
- Basic Mechanism : The language facilities supporting the styles most often seen in C and sometimes called *procedural programming*.

## Programs
- The ISO C++ standard defines two kinds of entities:
    - **Core language features**, such as built-in types (e.g., char and int) and loops (e.g., for-statements and while-statements)
    - **Standard-library components**, such as containers (e.g., vector and map) and I/O operations (e.g., << and getline()) 
- C++ is a statically typed language. That is, the type of every entity (e.g., object, value, name, and expression) must be known to the compiler at its point of use.
- Every C++ program must have exactly one global function named main(). The program starts by executing that function.
- A string literal is a sequence of characters surrounded by double quotes.
- In a string literal, the backslash character \ followed by another character denotes a single “special character.”
- The std:: specifies that the name cout is to be found in the standard-library namespace. How to make names from a namespace visible without explicit qualification:
    ```C++
    using namespace std;         // make names from std visible without std:: (§3.4)
    ```
## Functions
- The main way of getting something done in a C++ program is to call a function to do it.
- Defining a function is the way you specify how an operation is to be done.
- **A function cannot be called unless it has been previously declared.**
- A function declaration gives the name of the function, the type of the value returned (if any), and the number and types of the arguments that must be supplied in a call.
- A function declaration may contain argument names. This can be a help to the reader of a program, but unless the declaration is also a function definition, the compiler simply ignores such names.
- A function can be a member of a class. For such a member function, the name of its class is also part of the function type.

> We want our code to be comprehensible, because that is the first step on the way to maintainability. The first step to comprehensibility is to break computational tasks into meaningful chunks (represented as functions and classes) and name those. Such functions then provide the basic vocabulary of computation, just as the types (built-in and user-defined) provide the basic vocabulary of data. 

> The number of errors in code correlates strongly with the amount of code and the complexity of the code. Both problems can be addressed by using more and shorter functions. Using a function to do a specific task often saves us from writing a specific piece of code in the middle of other code; making it a function forces us to name the activity and document its dependencies.

- If two functions are defined with the same name, but with different argument types, the compiler will choose the most appropriate function to invoke for each call.
- If two alternative functions could be called, but neither is better than the other, the call is deemed ambiguous and the compiler gives an error.
- Defining multiple functions with the same name is known as function overloading and is one of the essential parts of generic programming.
- When a function is overloaded, each function of the same name should implement the same semantics.<abbr title="What does this mean? Should have same return type? same number of arguments?" style="font-weight:bold;">?</abbr>

## Types, Variables, And Arithmetic
- Every name and every expression has a type that determines the operations that may be performed on it.
- A declaration is a statement that introduces an entity into the program. It specifies a type for the entity:
    - A type defines a set of possible values and a set of operations (for an object).
    - An object is some memory that holds a value of some type.
    - A value is a set of bits interpreted according to a type.
    - A variable is a named object.
- The size of a type is implementation-defined (i.e., it can vary among different machines) and can be obtained by the sizeof operator
- Numbers can be floating-point or integers:
    - Floating-point numbers are recognized by a decimal point (e.g., 3.14) or by an exponent (e.g., 3e−2).
    - **0b** prefix indicates a binary (base 2) integer literal
    - **0x** prefix indicates a hexadecimal (base 16) integer literal
    - **0** prefix indicates an octal
- To **make long literals more readable for humans, we can use a single quote (') as a digit separator.**
- C++ performs all meaningful conversions between the basic types so that they can be mixed freely
- The = form is traditional and dates back to C, but if in doubt, use the general {}-list form. 
    ```C++
    double d1 = 2.3;                 // initialize d1 to 2.3
    double d2 {2.3};                 // initialize d2 to 2.3
    int i1 = 7.8;        // i1 becomes 7 (surprise?)
    int i2 {7.8};        // error: floating-point to integer conversion
    ```
- Unfortunately, conversions that lose information, narrowing conversions, such as double to int and int to char, are allowed and implicitly applied when you use = (but not when you use {})
- A constant cannot be left uninitialized and a variable should only be left uninitialized in extremely rare circumstances. Don’t introduce a name until you have a suitable value for it.
- When defining a variable, you don’t need to state its type explicitly when it can be deduced from the initializer.
- Using **auto**, we avoid redundancy and writing long type names. This is especially important in generic programming where the exact type of an object can be hard for the programmer to know and the type names can be quite long.

## Scope and Lifetime
- Local Scope : Extends from its point of declaration to the end of the block in which its declaration occurs.
- Class Scope : A name is called a member name (or a class member name) if it is defined in a class, outside any function, lambda, or enum class. Its scope extends from the opening { of its enclosing declaration to the end of that declaration.
- Namespace scope: A name is called a namespace member name if it is defined in a namespace. Its scope extends from the point of declaration to the end of its namespace.
- An object must be constructed (initialized) before it is used and will be destroyed at the end of its scope. For a namespace object the point of destruction is the end of the program.
- An object created by ```new``` “lives” until destroyed by ```delete```

## Constants
- **const** : This is used primarily to specify interfaces so that data can be passed to functions using pointers and references without fear of it being modified. 
- **constexpr** : This is used primarily to specify constants, to allow placement of data in read-only memory (where it is unlikely to be corrupted), and for performance. 

## Pointers, Arrays and References
- In an expression, prefix unary * means “contents of” and prefix unary & means “address of.”
    ```C++
    char* p = &v[3];        // p points to v's fourth element
    char x = *p;            // *p is the object that p points to
    ```
-  C++ also offers a simpler for-statement, called a range-for-statement, for loops that traverse a sequence in the simplest way.
    ```C++
    for (auto x : {10,21,32,43,54,65})
           cout << x << '\n';
    ```
- **If we didn’t want to copy the values from v into the variable x, but rather just have x refer to an element, we could write.**
    ```C++
    void increment()
    {
     int v[] = {0,1,2,3,4,5,6,7,8,9};
     for (auto& x : v)     // add 1 to each x in v
           ++x;
    }   
    ```
- **A reference is similar to a pointer, except that you don’t need to use a prefix \* to access the value referred to by the reference.**
- **A reference cannot be made to refer to a different object after its initialization.**
- **References are particularly useful for specifying function arguments.**
- **When we don’t want to modify an argument but still don’t want the cost of copying, we use a `const` reference.**
- **We try to ensure that a pointer always points to an object so that dereferencing it is valid.**
- **We give the pointer the value `nullptr` (“the null pointer”).**
    ```C++
    double* pd = nullptr;
    Link<Record>* lst = nullptr;  // pointer to a Link to a Record
    int x = nullptr;              // error: nullptr is a pointer not an integer
    ```
> Note how we can advance a pointer to point to the next element of an array using ++ and that we can leave out the initializer in a for-statement if we don’t need it.
  >  ```C++
    int count_x(const char* p, char x)
     // count the number of occurrences of x in p[]
     // p is assumed to point to a zero-terminated array of char (or to nothing)
    {
         if (p==nullptr)
               return 0;
         int count = 0;
         for (; *p!=0; ++p)
               if (*p==x)
                     ++count;
         return count;
    }
    ```
- **The characters in a string literal are immutable.**
- **Using `nullptr` eliminates potential confusion between integers (such as `0` or `NULL`) and pointers (such as nullptr).**
- **A test of a numeric value (e.g., while (*p) in count_x()) is equivalent to comparing the value to 0 (e.g., while (*p!=0)). A test of a pointer value (e.g., if (p)) is equivalent to comparing the value to nullptr (e.g., if (p!=nullptr)).**
- There is no “null reference.” **A reference must refer to a valid object.**

## Tests
- Note that the definition of answer appears where it is needed (and not before that). A declaration can appear anywhere a statement can.
    ```C++
    ...
    char answer = 0;                                  // initialize to a value that will not appear on input
    cin >> answer;                                    // read answer

   if (answer == 'y')
         return true;
    ...
    ```
- Those constants, called case-labels, must be distinct, and if the value tested does not match any of them, the default is chosen. If the value doesn’t match any case-label and no default is provided, no action is taken.
- **Like a for-statement , an if-statement can introduce a variable and test it.**
    ```C++
     if (auto n = v.size(); n!=0) {
     ...
     }
    ```
- A name declared in a condition is in scope on both branches of the if-statement.
- As with the for-statement, the purpose of declaring a name in the condition of an if-statement is to keep the scope of the variable limited to improve readability and minimize errors.
- The most common case is testing a variable against 0 (or the nullptr).

## Mapping and hardware
- The simple mapping of fundamental language constructs to hardware is crucial for the raw low-level performance for which C and C++ have been famous for decades. The basic machine model of C and C++ is based on computer hardware, rather than some form of mathematics.
- If we want different objects to refer to the same (shared) value, we must say so.
- **A reference and a pointer both refer/point to an object and both are represented in memory as a machine address. However, the language rules for using them differ. Assignment to a reference does not change what the reference refers to but assigns to the referenced object.**
- To access the value pointed to by a pointer, you use *; that is automatically (implicitly) done for a reference.
- For almost all types, the effect of reading from or writing to an uninitialized variable is undefined.
- Fortunately, we cannot have an uninitialized reference

## Advice
1. Don’t use the built-in features exclusively or on their own. On the contrary, the fundamental (built-in) features are usually best used indirectly through libraries, such as the ISO C++ standard library
1. A function should perform a single logical operation
1. If a function may have to be evaluated at compile time, declare it `constexpr`;
1. Use digit separators to make large literals readable.
1. Minimize the scope of a variable.
1. **Keep common and local names short, and keep uncommon and nonlocal names longer.**
1. Prefer the {}-initializer syntax for declarations with a named type
1. Use `auto` to avoid repeating type names.
1. When declaring a variable in the condition of an if-statement, prefer the version with the implicit test against 0.
1. Use unsigned for bit manipulation only.
1. Don’t say in comments what can be clearly stated in code.
1. State intent in comments.