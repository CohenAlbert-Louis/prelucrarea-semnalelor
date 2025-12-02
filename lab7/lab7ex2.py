import numpy as np
import matplotlib.pyplot as plt
from scipy import datasets
from scipy import ndimage

N = 128

original_image = datasets.face(gray=True)[::4, ::4].astype(np.float64)
original_image = original_image - original_image.mean()
original_image = original_image[:N, :N]

def calculate_snr(signal, noise):
    signal_power = np.sum(signal**2)
    noise_power = np.sum((signal - noise)**2)
    if noise_power == 0:
        return np.inf
    snr_db = 10 * np.log10(signal_power / noise_power)
    return snr_db

def ideal_low_pass_filter(R, N): #ILPF rad R
    u = np.fft.fftfreq(N)
    v = np.fft.fftfreq(N)
    U, V = np.meshgrid(u, v)
    D = np.sqrt(U**2 + V**2) #rad dist
    H = (D < R).astype(float)
    return H

snr_target = 18.0
R_final = 0.0
compressed_image = None

X = np.fft.fft2(original_image)
R_max = 0.5
R_step = 0.01

R_values = np.arange(R_step, R_max + R_step, R_step)
for R in R_values:
    H = ideal_low_pass_filter(R, N)
    X_comp = X * H
    I_comp = np.real(np.fft.ifft2(X_comp)) #comp img
    
    current_snr = calculate_snr(original_image, I_comp)
    
    if current_snr >= snr_target:
        R_final = R
        compressed_image = I_comp
        print(f"R = {R_final:.2f}, Final SNR = {current_snr:.2f} dB")
        break
else:
    R_final = R_max
    compressed_image = I_comp
    print(f"Target SNR {snr_target} R={R_final:.2f}. Final SNR: {current_snr:.2f} dB")

fig, axes = plt.subplots(1, 2, figsize=(10, 5))
axes[0].imshow(original_image, cmap='gray')
axes[0].set_title('Original Image')
axes[1].imshow(compressed_image, cmap='gray')
axes[1].set_title(f'Compressed (R={R_final:.2f}, SNR={current_snr:.2f} dB)')
plt.tight_layout()
plt.savefig('compressed_image_p2.svg')
plt.close(fig)