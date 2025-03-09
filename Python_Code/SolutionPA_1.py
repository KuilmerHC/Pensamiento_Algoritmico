# Define functions to calculate each value
def crystal_potential(I, R):
    return I * R


def energy_flux(V, R):
    return V / R


def cosmic_resistance(V, I):
    return V / I



print("This program is to calculate Crystal Potential, Energy Flux or Cosmic Resistance with two values.")
print("Remember to write -1 to the missing value")

# Loop to verify that the input corresponds to a float
while True:
    try:
        V = float(input("Crystal Potential(V): "))
        I = float(input("Energy Flux(I): "))
        R =  float(input("Cosmic Resistance(Ω): "))
        break
    except ValueError:
        print("Error:1 Invalid argument, please use numbers.")


if V == -1:
    result_crystal = crystal_potential(I, R)
    print(f"Crystal Potential: {result_crystal:.2f}V")
elif R == 0:
     print("Error SF1: Short Circuit (Problems with resistance)")
elif I == 0:
    print("Error OC1: Open Circuit (No current flow) ")
elif I == -1:
    result_flux = energy_flux(V, R)
    print(f"Energy Flux: {result_flux:.2f}A")
elif R == -1:
    result_resistance = cosmic_resistance(V, I)
    print(f"Cosmic Resistance: {result_resistance:.2f}Ω")
else:
    print("You have to write -1 to the missing value calculate it.")

