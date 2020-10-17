from skimage.io import imread
from skimage.transform import resize
from skimage.feature import hog
import matplotlib.pyplot as plt


def show_hog(img_src: str) -> None:
    img = imread(img_src)
    resized_img = resize(img, (128, 64))

    fd, hog_image = hog(
        resized_img,
        orientations=9,
        pixels_per_cell=(2, 2),
        cells_per_block=(1, 1),
        visualize=True,
        multichannel=True,
    )

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8), sharex=True, sharey=True)

    ax1.imshow(resized_img, cmap=plt.cm.gray)
    ax1.set_title("Input image")
    ax2.imshow(hog_image, cmap=plt.cm.gray)
    ax2.set_title("Histogram of Oriented Gradients")

    plt.show()


if __name__ == "__main__":
    show_hog("assets/example-000.jpg")
