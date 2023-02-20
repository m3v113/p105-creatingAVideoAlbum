import os
import cv2

path = "p105/images"
images = []

for file in os.listdir(path):
    name, extension = os.path.splitext(file)

    if extension in [".png", ".jpg", ".jpeg", ".mp4"]:
        filename = path + "/" + file
        print(filename)
        images.append(filename)

count = len(images)
print(count)

frame = cv2.imread(images[0])
height, width, channels = frame.shape
size = (width, height)
outputvid = cv2.VideoWriter("project105.avi", cv2.VideoWriter_fourcc(*"DIVX"), 0.8, (size))

for i in range(0, count-1):
    frame = cv2.imread(images[i])
    outputvid.write(frame)
    print("done")

outputvid.release()
print("video finished")