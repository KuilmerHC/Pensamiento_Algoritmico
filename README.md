# Documentation

# Introduction

The purpose of this project is to implement code in both C++ and Python to calculate the magnitudes associated with the cosmic energy laws discovered on Nexus Prime. This work demonstrates a dual code solution that computes one of three key parameter Crystal Potential, Energy Flux, or Cosmic Resistance, by employing a unique condition based on the unkwon value, the user simply inputs -1, and the program uses the fundamental Zyx-9 equation to calculate the missing magnitude.

---

# Python Installation (MacOS, Windows, Linux)
- ## MacOs
    
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
            
            ![image.png](https://github.com/KuilmerHC/Pensamiento_Algoritmico/blob/main/Images/image1.png?raw=true)
            
    - **Step 2:** Install VSC.
        1. Search VSC in google and click on “download for Mac”
        
        ![image.png](attachment:d917bbb6-b250-4de6-91da-990e60b24f0f:image.png)
        
        1. After that, go to files and choose download and click on it.
            
            ![image.png](https://github.com/KuilmerHC/Pensamiento_Algoritmico/blob/main/Images/image12.png?raw=true)
            
        2. Next to do that, run it and the app will open, when the app will be opening, it  show the main panel. (like this)
            
            ![ZHzst.png](https://github.com/KuilmerHC/Pensamiento_Algoritmico/blob/main/Images/image13.png?raw=true)
            
    - **Step 4:** After to open VSC you are going to go to “extensions”, you search Python by microsoft and you clikc on it.
        
        ![image.png](https://github.com/KuilmerHC/Pensamiento_Algoritmico/blob/main/Images/image5.png?raw=true)
        
    
    ✅ That’s all, you have Python in your MacOS.
    
- ## Windows
    
    🐍 **Install Python in Windows Using VS Code**
    
    - **Step 1:**  Go to microsoft store and search “Python” or dowload it from the official website.
    
    ![image.png](https://github.com/KuilmerHC/Pensamiento_Algoritmico/blob/main/Images/image6.png?raw=true)
    
    - Step 2: Search VSC in google and click “download for windows”
    
    ![image.png](https://github.com/KuilmerHC/Pensamiento_Algoritmico/blob/main/Images/image7.png?raw=true)
    
    1. After that, go to your files and choose download and click on it.
        
        ![image.png](https://github.com/KuilmerHC/Pensamiento_Algoritmico/blob/main/Images/image8.png?raw=true)
        
    2. Next to do that, you have to run it and the app will open, when the app will be opening, it  show the main panel. (like this)
        
        ![ZHzst.png](https://github.com/KuilmerHC/Pensamiento_Algoritmico/blob/main/Images/ZHzst4.png?raw=true)
        
    3. When you enter to VSC, go to “extensions” and find Python
        
        ![image.png](https://github.com/KuilmerHC/Pensamiento_Algoritmico/blob/main/Images/image5.png?raw=true)
        
    4. Finally, install the Microsoft vertion due to that is certiified.
        
        ![image.png](https://github.com/KuilmerHC/Pensamiento_Algoritmico/blob/main/Images/image9.png?raw=true)
        
    
     If you use python in VSC, is necesary to put “.py” at the end.
    
    ✅ Great, you already have python in Windows.
    
- ## Linux
    
    🐍 **How to Install Python on Linux** 
    
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
        
    
    Check if this install you need to put this in your terminal:
    
    ```python
    pip3 install virtualenv
    ```
    
    ✅ Great, you already have python in Linux, you can now program. 

---

# C++ Installation (MacOS, Windows, Linux)

- ## MacOs
    - **Step 1**:  Check if you have a C++ compiler
    
    Open your terminal and you will put this: 
    
    ```cpp
    clang --version
    ```
    
    - **Step 2:** If you do not have a C++ compiler, you will see how you can install that.
        1. Option 1: You can install Xcode Comand Line Tools, in your terminal you will put:
            
            ```cpp
            xcode-select --install
            ```
            
        
        A pop-up window will appear. Click **"Install"** and wait for the installation to finish and you can verify the installation with this command.
        
        ```cpp
        clang --version
        ```
        
        1. Option 2: you can install GCC using Homebrew. 
        
        if you do not have homebrew, you can install it like this:
        
        ```cpp
        /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
        
        ```
        
        You will install GCC using Homebrew, the command is: 
        
        ```cpp
        brew install gcc
        ```
        
        If you have questions, you can corroborate with this command in your terminal: 
        
        ```cpp
        g++ --version
        ```
        
    - **Step 3:** Finally, if you want to use VSC, it is so easy, you have VSC only you have to install the Extnsion  C/C++ by microsoft and create a file but you have to write “cpp” at the end.
 
    
- ## Windows
    - **Step 1**: You need to install a C++ compiler.
        1. Option 1: Install MinGW-w64, this is recommended for beginners, you can install from the official website, select and download the vertion more recommended.
            
            ![image.png](https://github.com/KuilmerHC/Pensamiento_Algoritmico/blob/main/Images/image10.png?raw=true)
            
            - Open **File Explorer**, right-click on **This PC** → **Properties**.
            - Go to **Advanced system settings** → **Environment Variables**.
            - Under **System Variables**, select `Path` and click **Edit**.
            - Click **New** and add the path where you installed MinGW, for example:
                
                ```cpp
                C:\mingw-w64\bin
                ```
                
            
            Finally you need to verify the installation, when you open your terminal you enter this command: 
            
            ```cpp
            g++ --version
            ```
            
            if you see a GCC version, the compiler was correctly install.
            
    - **Step 2:** If you do not have VSC you can install whit this process:
        1. You need to search VSC in google and click on “download for windows”
        
        ![image.png](https://github.com/KuilmerHC/Pensamiento_Algoritmico/blob/main/Images/image7.png?raw=true)
        
        d. After that you are going to go to your files and choose download and click on it.
        
        ![image.png](https://github.com/KuilmerHC/Pensamiento_Algoritmico/blob/main/Images/image3.png?raw=true)
        
        c. Next to do that, we run it and the app will open, when the app will be opening, it  show the main panel. (like this)
        
        ![ZHzst.png](https://github.com/KuilmerHC/Pensamiento_Algoritmico/blob/main/Images/ZHzst4.png?raw=true)
        
    - **Step 3:** you have to go to extensions, search C/C++and install by microsoft.
        
        ![image.png](https://github.com/KuilmerHC/Pensamiento_Algoritmico/blob/main/Images/image11.png?raw=true)
        
    - **Step 4: C**onfigure C++ in VS Code. To do that you need to open VS Code and press `Ctrl + ~` to open the integrated terminal. Select the compiler pressing `Ctrl + Shift + P` to open the command:
        
        ```cpp
        C/C++: Edit Configurations (UI)}
        ```
        
        ✅ **Done!** You can now write and compile **C++ programs in Windows** using **VS Code**. 🚀
        
- ## Linux
    - **Step 1:** Check if you have C++ compiler. For that, you got to open your terminal and put this code:
        
        ```cpp
        g++ --version
        ```
        
        if you have information about g++, you have a c++ compiler, but you dont have g++ information, you have to install a c++ compiler. 
        
    - **Step 2:** You can install in diferents operational systems for each one has diferent commands.  Run this commands in your terminal.
        
        a. Ubuntu: 
        
        ```cpp
        sudo apt update && sudo apt install g++ -y
        ```
        
        b. Fedora: 
        
        ```cpp
        sudo dnf install gcc-c++
        ```
        
        c. Arch Linux:
        
        ```cpp
        sudo pacman -s gcc 
        ```
        
        d. OpenSUSE:
        
        ```cpp
        sudo zypper install gcc-c++
        ```
        
        Verify if it is install and it running.
        
        ```cpp
        g++ --version
        ```
        
    - **Step 3: Install VS code to run** **C++**
        1. Ubuntu / Debian
            
            ```cpp
            sudo apt install code
            ```
            
        2. Fedora
            
            ```cpp
            sudo dnf install code
            ```
            
        3. Arch Linux
            
            ```cpp
            
            sudo pacman -S code
            ```
            
        
        Finally you have to install the extension.
        
        ![image.png](https://github.com/KuilmerHC/Pensamiento_Algoritmico/blob/main/Images/image11.png?raw=true)
        
        ✅ **Done!** You can now write and compile **C++ programs on Linux** easily. 🚀



---

# User guide

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

# Technical Documentation


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


# Code Examples

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

# Common Errors

- One common error occurs when the user enters a string instead of a numeric value. To handle this, we use a loop that continuously prompts the user for input until a valid numeric value is entered. This is achieved using a `while` loop combined with conditional checks.
- Another issue arises with the value 0 in certain calculations. In crystal potential $V = I * R$ if either I or R is 0, the result is simply 0. However, in the case of energy flux $I = V / R$, and cosmic resistance $R = V / I$, division by zero is undefined in mathematics. In physics, this situation has different implications: for energy flux, it represents an open circuit, while for cosmic resistance, it indicates a problem with the resistance value.
- Another potential error occurs when the user fails to enter “-1” for a missing value. In this case, the program will display the message: “Remember to write -1 for the missing value.”
- All common errors were anticipated and effectively resolved.

---

# Contributions
Welcome! We are excited that you are interested in contributing to our project. Whether you are a developer, designer, writer, or just someone who wants to help out, your contributions are valuable. This guide will walk you through the process of getting started.

## How to Contribute

### 1. **Find Something to Work On**

- If you have an idea for a new feature or improvement, feel free to open a new file.

---

### 2. **Set Up the Project**

1. **Fork the Repository**: Click the "Fork" button on the top right of the repository page to create your own copy.
2. **Clone Your Fork**:
    
    ```
    git clone https://github.com/KuilmerHC/Pensamiento_Algoritmico.git
    ```
    
3. **Create a Branch**:
    
    ```
    git checkout -b my-feature-branch
    ```
    

---

### 3. **Make Your Changes**

- Write clean, well-documented code or content.
- Follow the project’s coding style and guidelines (python PEP 8 style and for C++ is C++ Google style guide) .
- Test your changes to ensure they work as expected.

---

### 4. **Submit Your Contribution**

1. **Commit Your Changes**:
    
    ```
    git add .
    git commit -m "Describe your changes briefly"
    ```
    
2. **Push to Your Fork**:
    
    ```
    git push origin my-feature-branch
    ```
    
3. **Open a Pull Request (PR)**:
    - Go to the original repository and click "New Pull Request."
    - Write a clear title and description explaining what your PR does and why it’s helpful.
    - Reference any related issues (e.g., "Fixes #123").

---

### 5. **Review and Feedback**

- Maintainers and other contributors will review your PR and may suggest changes.
- Be open to feedback and make any necessary updates.
- Once approved, your changes will be merged into the project. Thank you!

## Questions?

If you have any questions or need help, feel free to:

- Open an issue.
- Reach out to us on [**juanjosbe@gmail.com**, **kuilmerhc@gmail.com,** david.hernandez01@usa.edu.co].

---

We appreciate your time and effort making our project better. Happy contributing! 🎉
