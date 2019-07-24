# import the necessary packages
import numpy as np
import argparse
import cv2
 
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "c:\\PrivateApps\\imagen.jpg")
args = vars(ap.parse_args())
 
# load the image
image = cv2.imread(args["image"])

# define the list of boundaries
boundaries = [
	([17, 15, 100], [255, 0, 0]),
	([86, 31, 4], [220, 88, 50]),
	([25, 146, 190], [62, 174, 250]),
	([85, 80, 65], [200, 200, 190])
]

for (lower, upper) in boundaries:
	# create NumPy arrays from the boundaries
	lower = np.array(lower, dtype = "uint8")
	upper = np.array(upper, dtype = "uint8")
 
	# find the colors within the specified boundaries and apply
	# the mask
	mask = cv2.inRange(image, lower, upper)
	output = cv2.bitwise_and(image, image, mask = mask)
 
	# show the images
	cv2.imshow("images", np.hstack([image, output]))
	cv2.waitKey(0)




# import cv2
# import matplotlib.pyplot as plt
# import numpy as np
# from mpl_toolkits.mplot3d import Axes3D
# from matplotlib import cm
# from matplotlib import colors
# from matplotlib.colors import hsv_to_rgb


# nemo = cv2.imread('c:\\PrivateApps\\pelota.jpg')
# nemo = cv2.cvtColor(nemo, cv2.COLOR_BGR2RGB)
# hsv_nemo = cv2.cvtColor(nemo, cv2.COLOR_RGB2HSV)

# pixel_colors = nemo.reshape((np.shape(nemo)[0]*np.shape(nemo)[1], 3))
# norm = colors.Normalize(vmin=-1.,vmax=1.)
# norm.autoscale(pixel_colors)
# pixel_colors = norm(pixel_colors).tolist()

# plt.imshow(nemo)
# plt.show()

# # grafico de ejes
# # h, s, v = cv2.split(hsv_nemo)
# # fig = plt.figure()
# # axis = fig.add_subplot(1, 1, 1, projection="3d")

# # axis.scatter(h.flatten(), s.flatten(), v.flatten(), facecolors=pixel_colors, marker=".")
# # axis.set_xlabel("Hue")
# # axis.set_ylabel("Saturation")
# # axis.set_zlabel("Value")
# # plt.show()

# # elegir colores
# light_white = (0, 0, 255)
# dark_white = (0, 0, 200)

# light_square = np.full((10, 10, 3), light_white, dtype=np.uint8) / 255.0
# dark_square = np.full((10, 10, 3), dark_white, dtype=np.uint8) / 255.0

# plt.subplot(1, 2, 1)
# plt.imshow(hsv_to_rgb(light_square))
# plt.subplot(1, 2, 2)
# plt.imshow(hsv_to_rgb(dark_square))
# plt.show()


# #para buscar 
# mask_white = cv2.inRange(hsv_nemo, light_white, dark_white)
# result_white = cv2.bitwise_and(nemo, nemo, mask=mask_white)

# plt.subplot(1, 2, 1)
# plt.imshow(mask_white, cmap="gray")
# plt.subplot(1, 2, 2)
# plt.imshow(result_white)
# plt.show()

# print("FINISHED OK")