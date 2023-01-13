import cv2

img = cv2.imread('python_opencv/images/test1.jpg', cv2.IMREAD_UNCHANGED) #알파채널을 포함하여 이미지를 로드

dimensions = img.shape #이미지의 크기를 dimensions에 저장

# height, width = img.shape

height = img.shape[0] #높이를 인덱스 0에 저장
width = img.shape[1] #너비를 인덱스 1에 저장

print('Image Dimension     : ', dimensions)
print('Image Height        : ', height)
print('image width         : ', width)