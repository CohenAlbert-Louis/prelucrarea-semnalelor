from hamming74 import Hamming74
import numpy as np

data = np.array([1, 0, 1, 1])
encoded = Hamming74.encode(data)
print("Encoded codeword:", encoded)

encoded_with_error = encoded.copy()
encoded_with_error[2] = 1 - encoded_with_error[2]
print("Encoded with error:", encoded_with_error)
decoded_data, stat = Hamming74.decode(encoded_with_error)
print("Error: ",stat if stat>=0 else "No error" if stat==-1 else "Uncorrectable error")

encoded_incompatible = encoded.copy()
encoded_incompatible[2] = 1 - encoded_incompatible[2]
encoded_incompatible[4] = 1 - encoded_incompatible[4]
print("Encoded with incompatible errors:", encoded_incompatible)
decoded_data, stat = Hamming74.decode(encoded_incompatible)
print("Error: ",stat if stat>=0 else "No error" if stat==-1 else "Uncorrectable error")