import numpy as np
import cv2

canvas = np.zeros((300, 300, 3), dtype = "uint8")

red = (0, 0, 255)
for i in range(30):
    for j in range(30):
        if (i + j) % 2 == 1:
            cv2.rectangle(canvas, (i * 10, j * 10), ((i + 1) * 10, (j + 1) * 10), red, -1)

green = (0, 255, 0)
(centerX, centerY) = (canvas.shape[1] // 2, canvas.shape[0] // 2)
cv2.circle(canvas, (centerX, centerY), 50, green, -1)

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
