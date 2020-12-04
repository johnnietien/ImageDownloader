import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np
import cv2


#img1 = cv2.imread("defect/G1-R2-C2-R1-C24.png")
img1 = cv2.imread("G2-R3-C1-R1-C1RGB.png")

res = cv2.resize(img1, (224, 224))
cv2.imshow("img1", res)



# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

# Load the model
model = tensorflow.keras.models.load_model('keras_model.h5')

# Create the array of the right shape to feed into the keras model
# The 'length' or number of images you can put into the array is
# determined by the first position in the shape tuple, in this case 1.
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

# Replace this with the path to your image
#image = Image.open('defect/G1-R2-C2-R1-C24.png')

#resize the image to a 224x224 with the same strategy as in TM2:
#resizing the image to be at least 224x224 and then cropping from the center
size = (224, 224)
#image = ImageOps.fit(image, size, Image.ANTIALIAS)

#turn the image into a numpy array
#image_array = np.asarray(image)
image_array = np.asarray(res)

# display the resized image
#image.show()

# Normalize the image
normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1

# Load the image into the array
data[0] = normalized_image_array

# run the inference
prediction = model.predict(data)
print(prediction)

cv2.waitKey(0)
cv2.destroyAllWindows()