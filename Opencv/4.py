import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

image_path = './Opencv/image.jpg'  # Change to your image path
img = Image.open(image_path).convert('L')  # Convert to grayscale
img_array = np.array(img)

dft_image = np.fft.fft2(img_array)
dft_shifted = np.fft.fftshift(dft_image)  

rows, cols = dft_shifted.shape
crow, ccol = rows // 2, cols // 2  

dft_shifted[crow - 15:crow + 15, ccol - 15:ccol + 15] = 0

idft_shifted = np.fft.ifftshift(dft_shifted)  
img_reconstructed = np.fft.ifft2(idft_shifted).real

plt.figure(figsize=(15, 10))

plt.subplot(1, 3, 1)
plt.title('Original Image')
plt.imshow(img_array, cmap='gray')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.title('DFT Magnitude (Zeroed Regions)')
plt.imshow(np.log(np.abs(dft_shifted) + 1), cmap='gray')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.title('Reconstructed Image from IDFT')
plt.imshow(img_reconstructed, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()
from scipy.fftpack import dct, idct

img_dct = Image.open(image_path).convert('L')
img_dct_array = np.array(img_dct)

dct_image = dct(dct(img_dct_array.T, norm='ortho').T, norm='ortho')  

dct_image[20:80, 20:80] = 0  

img_reconstructed_dct = idct(idct(dct_image.T, norm='ortho').T, norm='ortho')

plt.figure(figsize=(15, 10))

plt.subplot(1, 3, 1)
plt.title('Original Image')
plt.imshow(img_dct_array, cmap='gray')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.title('DCT Coefficients (Zeroed Regions)')
plt.imshow(np.log(np.abs(dct_image) + 1), cmap='gray')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.title('Reconstructed Image from IDCT')
plt.imshow(img_reconstructed_dct, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()

