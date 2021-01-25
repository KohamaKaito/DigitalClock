import matplotlib.pyplot as plt

def plot_img(img):
	fig = plt.figure()
	ax = fig.add_subplot(111)
	ax.imshow(img, cmap='gray',vmin=0,vmax=255)
	plt.show()
	