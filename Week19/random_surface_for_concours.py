##This script will create a random surface and plot it
##This script is part of our solver for the contact problem

import numpy as np
import matplotlib.pyplot as plt

R = 1  # Radius of demi-sphere
L = 2  # Domain size
S = L**2  # Domain area

# Generate a 2D coordinate space
n = 300
m = 300

# Constants for the piecewise function
C = 1 # represents phi_0
q_l = 2*np.pi/L
q_r = 2*np.pi/L
q_s = 2*np.pi*25/L
H = 0.8 # Hurst exponent, represents the roughness of the surface

# Defining the piecewise function
def phi(q):
    # Initialize the result with zeros
    result = np.zeros_like(q)
    
    # Apply conditions
    mask1 = (q_l <= q) & (q < q_r)  # Condition for C
    mask2 = (q_r <= q) & (q < q_s)  # Condition for the power-law decay
    
    result[mask1] = C
    result[mask2] = C * (q[mask2] / q_r) ** (-2 * (H + 1))
    
    return result

#we define the frequency with q_x and q_y
q_x = 2 * np.pi * np.fft.fftfreq(n, d=L/n)
q_y = 2 * np.pi * np.fft.fftfreq(m, d=L/m)
QX, QY = np.meshgrid(q_x, q_y)

q_values = np.sqrt(QX**2 + QY**2)

phi_values = phi(q_values)

# Generate random phase
gen = np.random.default_rng()
#theta = gen.uniform(0, 2*np.pi, size=phi_values.shape)

# Generate white noise and apply PSD and phase
white_noise = gen.normal(size=phi_values.shape)
fft_noise = np.fft.fft2(white_noise)#here we don't normalize the white noise, so we need to normalize the surface
filtered_noise = fft_noise * np.sqrt(phi_values) #* np.exp(1j * theta)
surface = np.fft.ifft2(filtered_noise).real*np.sqrt(n*m)/(n*m)# add this np.sqrt(n*m) to implement the filtering algorithm
##################Question, I think we need to add this np.sqrt(n*m) to the surface
#######dont forget to add this to the original code in Week5(C++ version already has this) 


# Plotting
plt.figure(figsize=(6, 5))
scale_factor = 1e6  
plt.imshow(surface * scale_factor, cmap='viridis', origin='lower', extent=[0, L, 0, L])
cbar = plt.colorbar()
cbar.set_label('Surface height over mean [$\mu$m]')
plt.title("Synthesized Random Rough Surface")
plt.show()
