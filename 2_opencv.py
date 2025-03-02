import cv2

# 读取图片
# img = cv2.imread('images/car.jpeg')
# cv2.imshow('car', img)

# end = True
# while end:
#     key = cv2.waitKey(0)
#     if key & 0xFF == ord("q"):
#         cv2.destroyAllWindows()
#         end = False


# 通过opencv采集图片
# def capture_image():
#     cap = cv2.VideoCapture(0)

#     while cap.isOpened:
#         ret, frame = cap.read()

#         if ret:
#             cv2.imwrite('images/test.jpg', frame)
#             break

#     cap.release()

# def capture_video():
#     cap = cv2.VideoCapture(0)

#     fourcc = cv2.VideoWriter_fourcc(*'MP4V')
#     out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (640, 480))
#     i = 0

#     while cap.isOpened:
#         ret, frame = cap.read()
#         if ret:
#             if i <= 100:
#                 out.write(frame)
#             else:
#                 break
#             i += 1
#         else:
#             print("failed to capture video")
#             break
    
#     cap.release()
#     out.release()


# 使用opencv进行二值化
# img = cv2.imread('images/car.jpeg')
# cv2.imshow('car', img)

# # 灰度化
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# # 二值化
# ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# cv2.imshow('binary', binary)
# cv2.waitKey(0)

# # RGB <-> YUV


# Blur示例
# img = cv2.imread('images/car.jpeg')
# cv2.imshow('car', img)

# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# blur = cv2.blur(gray, (5, 5))

# # 二值化
# ret, binary = cv2.threshold(blur, 127, 255, cv2.THRESH_BINARY)

# cv2.imshow('blur', binary)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# 腐蚀示例
# img = cv2.imread('images/car.jpeg')
# cv2.imshow('car', img)

# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# blur = cv2.blur(gray, (5, 5))

# # 二值化
# ret, binary = cv2.threshold(blur, 127, 255, cv2.THRESH_BINARY)

# # 腐蚀操作
# kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
# erosion = cv2.erode(binary, kernel, iterations=1)

# cv2.imshow('erosion', erosion)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# 膨胀示例
# img = cv2.imread('images/car.jpeg')
# cv2.imshow('car', img)

# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# blur = cv2.blur(gray, (5, 5))

# # 二值化
# ret, binary = cv2.threshold(blur, 127, 255, cv2.THRESH_BINARY)

# # 膨胀操作
# kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
# dilation = cv2.dilate(binary, kernel, iterations=1)

# cv2.imshow('dilation', dilation)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# 开运算: 腐蚀后再膨胀，去除噪声，小白点
# img = cv2.imread('images/car.jpeg')
# cv2.imshow('car', img)

# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# blur = cv2.blur(gray, (5, 5))

# # 二值化
# ret, binary = cv2.threshold(blur, 127, 255, cv2.THRESH_BINARY)

# # 开运算
# kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
# opening = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel, iterations=1)

# cv2.imshow('opening', opening)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# 闭运算: 膨胀后再腐蚀，填充小洞，去除White Noise
# img = cv2.imread('images/car.jpeg')
# cv2.imshow('car', img)

# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# blur = cv2.blur(gray, (5, 5))

# # 二值化
# ret, binary = cv2.threshold(blur, 127, 255, cv2.THRESH_BINARY)

# # 闭运算
# kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
# closing = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel, iterations=1)

# cv2.imshow('closing', closing)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# # 其他算法：
# # 1. 形态学梯度：原图 - 腐蚀
# # 2. 顶帽运算：原图 - 开运算
# # 3. 黑帽运算：原图 - 闭运算


# 绘制轮廓
# img = cv2.imread('images/car.jpeg')
# cv2.imshow('car', img)

# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# # 二值化
# ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# # 轮廓查找
# contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# # 绘制轮廓
# cv2.drawContours(img, contours, -1, (0, 0, 255), 1)

# # 计算面积
# area = cv2.contourArea(contours[0])
# print(f"area={area}")

# # 计算周长
# perimeter = cv2.arcLength(contours[0], True)
# print(f"perimeter={perimeter}")

# cv2.imshow('contours', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# ROI 获取子矩阵
# img = cv2.imread('images/car.jpeg')

# roi = img[100:200, 100:200]
# roi[:,:] = [0,0,255] # 填充红色

# cv2.imshow('roi', roi)
# cv2.imshow('img', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# Canny 边缘检测
img = cv2.imread('images/car.jpeg')
cv2.imshow('car', img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.blur(gray, (5, 5))

# 二值化
ret, binary = cv2.threshold(blur, 127, 255, cv2.THRESH_BINARY)

# 边缘检测
edges = cv2.Canny(binary, 100, 200)

cv2.imshow('edges', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()