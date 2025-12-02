import numpy as np
import matplotlib.pyplot as plt

N = 64 #size NxN
k = np.arange(N)
#create matrix (k1,k2) with norm coord
k1, k2 = np.meshgrid(k, k, indexing='ij') #indexing ij for compatibility
n1_norm = k1 / N
n2_norm = k2 / N

def analyze_signal(image, title_x, file_prefix):  #compute img
    X = np.fft.fft2(image)
    X_shifted = np.fft.fftshift(X)
    
    fig, axes = plt.subplots(1, 1, figsize=(12, 6))
    
    axes.imshow(image, cmap='gray')
    axes.set_title(title_x, fontsize=14)
    axes.axis('off')
    
    plt.tight_layout()
    plt.savefig(f'{file_prefix}_result.svg') #auto save
    plt.close(fig)
    return X

def analyze_spectrum(Y, title_x, file_prefix): #plot spectrum
    Y_unshifted = np.fft.ifftshift(Y)
    x = np.fft.ifft2(Y_unshifted)
    x_real = np.real(x)
    
    fig, axes = plt.subplots(1, 1, figsize=(12, 6))
    
    axes.imshow(x_real, cmap='gray')
    axes.set_title(title_x, fontsize=14)
    axes.axis('off')
    
    plt.tight_layout()
    plt.savefig(f'{file_prefix}_result.svg')#auto save
    plt.close(fig)
    return x

x_1a = np.sin(2 * np.pi * n1_norm + 3 * np.pi * n2_norm)
X_1a = analyze_signal(x_1a, 
                      r'$x_{n_1,n_2} = \sin(2\pi n_1 + 3\pi n_2)$',  
                      'task1a')

x_1b = np.sin(4 * np.pi * n1_norm) + np.cos(6 * np.pi * n2_norm)
X_1b = analyze_signal(x_1b, 
                      r'$x_{n_1,n_2} = \sin(4\pi n_1) + \cos(6\pi n_2)$', 
                      'task1b')

Y_2c = np.zeros((N, N), dtype=complex)
Y_2c[0, 5] = 1
Y_2c[0, N-5] = 1
x_2c = analyze_spectrum(Y_2c, 
                        r'Image $x$ (IDFT)', 
                        'task2c')

Y_2d = np.zeros((N, N), dtype=complex)
Y_2d[5, 0] = 1
Y_2d[N-5, 0] = 1
x_2d = analyze_spectrum(Y_2d, 
                        r'Image $x$ (IDFT)', 
                        'task2d')

Y_2e = np.zeros((N, N), dtype=complex)
Y_2e[5, 5] = 1
Y_2e[N-5, N-5] = 1 
x_2e = analyze_spectrum(Y_2e, 
                        r'Image $x$ (IDFT)', 
                        'task2e')
