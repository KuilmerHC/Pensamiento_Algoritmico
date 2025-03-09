# Documentation

## Introduction

> 
> 

---

## Installation

> 
> 

---

## User guide

### **Case 1:** Calculate Crystal Potential (*V*)

**User Input:**

```python
# Input
Crystal Potential(V): -1
Energy Flux(I): 2.5
Cosmic Resistance(Ω): 4.
```

**Output:**

```python
# Output
Crystal Potential: 10.00V
```

---


### **Case 2:** Calculate Energy Flux (*I*)

**User Input:**

```python
# Input
Crystal Potential(V): 12
Energy Flux(I): -1
Cosmic Resistance(Ω): 6
```

**Output:**

```python
# Output
Energy Flux: 2.00A
```

---

### **Case 3:** Calculate Cosmic Resistance (*R*)

```python
# Input
Crystal Potential(V): 15
Energy Flux(I): 3
Cosmic Resistance(Ω): -1
```

Output

```python
# Output
Cosmic Resistance: 5.00Ω
```

---

### **Other Cases**

- Error:1, it is due to invalid input (non-numeric value)
- Eror OC1,  is when the system find to open circuit is detected (I = 0)
- Eror SF1, is when the system find to short circuit is detected (R = 0)

---

## Technical Documentation


### **Code Structure**


**Main Functions:**

- Crystal_Potential (I, R): Calculates the crystal potential using the formula:
    
    $V= I×R$
    
- Energy_Flux (V, R): Calculates the energy flux:
    
    $I = V / R$
    
- Cosmic_resistance (V, I): Calculates the cosmic resistance:

    $R= V / I$

---

### **Program Logic:**


1. Displays a welcome message explaining how to enter the values.
2. Uses a **while loop** to ensure the values entered are numbers (float).
3. Identifies which value is missing (marked with -1) and performs the corresponding calculation.
4. Detects common errors, such as:
    - **`R == 0`** → Error **SF1** (Short Circuit).
    - **`I == 0`** → Error **OC1** (Open Circuit).
    - **Invalid input** → Asks the user to re-enter values.

---


## Code Examples

- The “#include < iomanip > ” is used for the precision of the numbers, the problem give the instructions that the results must have two decimals so for this reason we include it in the code. Example:

```cpp
#include <iostream>
#include <iomanip> 

using namespace std;

float divide (float A, float B){
  return  A/B;
}

int main(){
    
    float A,B;
    
    cout << "ingrese el primer valor" << endl;
    cin >> A;
    cout << "ingrese el segundo valor" << endl;
    cin >> B;
    cout << fixed << setprecision(2) << "la division entre el primer y el segundo valor ingresado es: " << divide (A,B);
    

    return 0;

}
```

---

- The “#include < limits > ” we use it to validate the input, if the person enter a wrong value or a string, the program breaks and starts until the input is a correct value

```cpp
#include <iostream>
#include <iomanip>  // Para setprecision
#include <limits>   // Para numeric_limits

using namespace std;

float divide(float A, float B) {
    return A / B;
}

float getFloatInput(const string& prompt) {
    float value;
    while (true) {
        cout << prompt;
        if (cin >> value) {
            break;
        } else {
            cout << "Error: Entrada inválida. Por favor, ingrese un número.\n";
            cin.clear(); 
            cin.ignore(numeric_limits<streamsize>::max(), '\n'); 
        }
    }
    return value;
}

int main() {
    float A, B;

    A = getFloatInput("Ingrese el primer valor: ");
    B = getFloatInput("Ingrese el segundo valor: ");

    
    if (B == 0) {
        cout << "Error: No se puede dividir por cero.\n";
    } else {
        
        cout << fixed << setprecision(2) << "La división entre el primer y el segundo valor ingresado es: " << divide(A, B) << endl;
    }

    return 0;
}
```

---

- “while” is a cicle in which until the condition (numeric value) is true the code must run, for example:

```cpp
#include<iostream>
using namespace std;
int main(){

int ice = 26;
int sun = 2;

while(ice > 0){
   cout<< "the value of ice is: " <<endl;
   cout<<ice<<endl;
   cout<<"the value of the sun's radiation is: "<<endl;
   cout<<sun<<endl;

   if(ice == 0){
   break;

   }

   sun++;
   ice--;

   }
   
cout<<"can't continue because there is no more ice";

return 0;
    
```

Until the value of “ice” is 0 the code continue running

---

- The “if” we used for declare to the program what to do, “if variable R has a -1 do this loop”. for example:

```cpp
#include <iostream>
using namespace std;
int main() {
    
    //compuesta
    
    int x=10, y=5;
    if (((x>y) && (x%2==0))||(y%2==0)){
        
        cout<<"es mayor"<< endl;
        
    }else{
          cout<<"error"<<endl;
    }
   
   
   //terneario condicion ? true : false
    (((x>y) && (x%2==0))||(y%2==0)) ? cout<< "es mayor" << endl : cout<< "error"<< endl;

    return 0;
}
```

---

## Common Errors

- One common error occurs when the user enters a string instead of a numeric value. To handle this, we use a loop that continuously prompts the user for input until a valid numeric value is entered. This is achieved using a `while` loop combined with conditional checks.
- Another issue arises with the value 0 in certain calculations. In crystal potential $V = I * R$ if either I or R is 0, the result is simply 0. However, in the case of energy flux $I = V / R$, and cosmic resistance $R = V / I$, division by zero is undefined in mathematics. In physics, this situation has different implications: for energy flux, it represents an open circuit, while for cosmic resistance, it indicates a problem with the resistance value.
- Another potential error occurs when the user fails to enter “-1” for a missing value. In this case, the program will display the message: “Remember to write -1 for the missing value.”
- All common errors were anticipated and effectively resolved.

---

## Contributions
