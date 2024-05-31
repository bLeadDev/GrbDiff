from PIL import Image
import numpy as np

def xor_images(file1, file2, output_file):
    # Open the images and convert them to numpy arrays
    img1 = np.array(Image.open(file1))
    img2 = np.array(Image.open(file2))

    # Apply XOR operation
    result = np.bitwise_xor(img1, img2)

    # Convert the result to an image and save it
    Image.fromarray(result).save(output_file)
    
if __name__ =='__main__':
    # Test case 1
    xor_images('Copper_Layer_L1-1.png', 'Copper_Layer_L1-2.png', 'out.png')
    