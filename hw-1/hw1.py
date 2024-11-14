import cv2
from PIL import Image

# 使用 OpenCV 讀入照片
image1 = cv2.imread('myphoto.jpg')

# 顯示像素格式
print(f"height: {image1.shape[0]} pixels")
print(f"width: {image1.shape[1]} pixels")
print(f"channel: {image1.shape[2]} pixels")

# 顯示照片
cv2.imshow('img', image1)
cv2.waitKey(0)
cv2.destroyAllWindows()  # Close the OpenCV window

# 使用 PIL 讀入照片
image2 = Image.open('myphoto.jpg')

# 顯示照片
image2.show()

# 顯示原始照片大小
print(f"Original image size: {image2.size}")

# 縮小照片到指定像素
width = 512
height = 256
nim = image2.resize((width, height), Image.BILINEAR)

# 顯示縮小後的照片
nim.show()
print(f"Resized image size: {nim.size}")

# 儲存變更照片
nim.save('HW1.jpg')
print(f"Image mode: {nim.mode}, Image format: {nim.format}")
