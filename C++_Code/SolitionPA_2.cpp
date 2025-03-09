#include <iomanip>  // Round numbers
#include <iostream> 
#include <limits>   // Clear invalid input

using namespace std;

// Define functions
float crystal_potential(float I, float R) {
  return I * R;
}

float energy_flux(float V, float R) {
  return V / R;
}

float cosmic_resistance(float V, float I) {
  return V / I;
}

int main() {
  cout << "This program is to calculate Crystal Potential, Energy Flux or Cosmic Resistance with two values.\n";
  cout << "Remember to write -1 for the missing value.\n";

  float V, I, R;

  while (true) {
    // Verify the type of the input
    cout << "Crystal potential(V): ";
    while (!(cin >> V)) {
      cout << "Error:1 Invalid argument, please use numbers. \n";
      cin.clear();
      cin.ignore(numeric_limits<streamsize>::max(), '\n');
      cout << "Crystal potential(V): ";
    }

    cout << "Energetic flux(A): ";
    while (!(cin >> I)) {
      cout << "Error:1 Invalid argument, please use numbers. \n";
      cin.clear();
      cin.ignore(numeric_limits<streamsize>::max(), '\n');
      cout << "Energetic flux(A): ";
    }

    cout << "Cosmic resistance(Ω): ";
    while (!(cin >> R)) {
      cout << "Error:1 Invalid argument, please use numbers. \n";
      cin.clear();
      cin.ignore(numeric_limits<streamsize>::max(), '\n');
      cout << "Cosmic resistance(Ω): ";
    }

    if (I == 0) {
      cout << "Error OC1: Open Circuit (No current flow)\n";
      continue;
    }
    if (R == 0) {
      cout << "Error SF1: Short Circuit (Problems with resistance)\n";
      continue;
    }
    break;
  }

  if (V == -1) {
    cout << fixed << setprecision(2) << "Crystal Potential: " << crystal_potential(I, R) << "V\n";
  } else if (I == -1) {
    cout << fixed << setprecision(2) << "Energy Flux: " << energy_flux(V, R) << "A\n";
  } else if (R == -1) {
    cout << fixed << setprecision(2) << "Cosmic Resistance: " << cosmic_resistance(V, I) << "Ω\n";
  } else {
    cout << "You have to write -1 to the missing value calculate it.\n";
  }

  return 0;
}
