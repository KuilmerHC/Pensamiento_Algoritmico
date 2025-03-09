# Documentation

## Introduction

> 
> 

---

## Installation
- MacOs
    
    **How to Install Python on macOS Using VS Code**
    
    ---
    
     You can use a lot of methods to install Python. In this case with VS Code.
    
    - **Step 1:** In this part you have two options to install python:
        1. Install Python using homebrew, remember it is optional. the command is: 
            
            ```python
            brew install python
            ```
            
            check if python is installed whit this:
            
            ```python
            python3 --version
            ```
            
        2. Install from the official website 
            
            ![image.png](attachment:d39435bb-c487-45b3-a931-98a602ad802b:image.png)
            
    - **Step 2:** Install VSC.
        1. You need to search VSC in google and click on “download for Mac”
        
        ![image.png](attachment:d917bbb6-b250-4de6-91da-990e60b24f0f:image.png)
        
        1. After that you are going to go to your files and choose download and click on it.
            
            ![image.png](attachment:894fac15-41b1-4fa9-bf17-7001e9787de5:image.png)
            
        2. Next to do that, you need to run it and the app will open, when the app will be opening, it  show the main panel. (like this)
            
            ![ZHzst.png](attachment:cb3af859-b99e-4a52-b710-251410c3ac4d:d35cc1bf-d6d4-4982-91a2-cc7095be8582.png)
            
    - **Step 4:** After to open VSC you are going to go to “extensions”, you search Python by microsoft and you clikc on it.
        
        ![image.png](attachment:9646c650-2968-4e64-84e3-619aa1fd21ae:image.png)
        
    
    ✅ That’s all, you have Python in your MacOS.
    
- Windows
    
    🐍 **Install Python in Windows Using VS Code**
    
    - **Step 1:**  Go to microsoft store and search “Python” or dowload it from the official website.
    
    ![image.png](attachment:4bf321b1-7baf-48bc-a298-99b7204fca42:image.png)
    
    - Step 2: Search VSC in google and click “download for windows”
    
    ![image.png](attachment:9ac81288-5c35-4f26-aa51-7215df31003c:image.png)
    
    1. After that you are going to go to your files and choose download and click on it.
        
        ![image.png](attachment:894fac15-41b1-4fa9-bf17-7001e9787de5:image.png)
        
    2. Next to do that, you have to run it and the app will open, when the app will be opening, it  show the main panel. (like this)
        
        ![ZHzst.png](attachment:cb3af859-b99e-4a52-b710-251410c3ac4d:d35cc1bf-d6d4-4982-91a2-cc7095be8582.png)
        
    3. When you enter to VSC you are gonna go to “extensions” and you find Python
        
        ![image.png](attachment:9646c650-2968-4e64-84e3-619aa1fd21ae:image.png)
        
    4. Finally, you gotta install the Microsoft vertion due to that is certiified.
        
        ![image.png](attachment:5edc202a-e2f5-457d-9673-8e2d529f9436:image.png)
        
    
     If you wanna use python in VSC, it’s necesary to put “.py” at the end.
    
    ✅ Great, you already have python in Windows.
    
- Linux
    
    🐍 **How to Install Python on Linux from Scratch Using** 
    
    Most Linux distributions come with **Python preinstalled**. However, if you need a newer version or it's missing, follow these steps based on your distribution.
    
    - Step 1: open the terminal you can open with (ctrl+alt+t )
    
    ```python
    python3 --version
    ```
    
    If you see something like `Python 3.x.x`, Python is already installed. If not, proceed to the next step.
    
    - Step 2:  you can install Python on Debian, Ubuntu, and Derivatives (Linux Mint, Pop!_OS, etc.)
    
    for that action that is downdoald python on Linux you need to put this in your terminal.
    
    1. This is for update package lists 
    
    ```python
    sudo apt update && sudo apt upgrade -y
    ```
    
    1. This is for installing python: 
        
        ```python
        sudo apt install python3 -y
        ```
        
    2. In this step you will install the Python packege manager.
        
        ```python
        sudo apt install python3-pip -y
        ```
        
    3. And finally you need to verify that it has been installed correctly.
        
        ```python
        python3 --version
        ```
        
    - Step 3: If you have more than one vertion of python and you want “python” to be the same as “python3” you will do that:
        
        ```python
        sudo update-alternatives --install /usr/bin/python python /usr/bin/python3 1
        
        ```
        
    
    to check if this install you need to put this in your terminal:
    
    ```python
    pip3 install virtualenv
    ```
    
    ✅ Great, you already have python in Linux, you can now program. 

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
