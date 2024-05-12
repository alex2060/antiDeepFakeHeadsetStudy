import os
import cv2
import numpy as np

def calculate_brightness(image):
    imageValue = cv2.imread(image)
    gray_image = cv2.cvtColor(imageValue, cv2.COLOR_BGR2GRAY)
    hsv = cv2.cvtColor(imageValue, cv2.COLOR_BGR2HSV)
    brightness = np.mean(hsv[:, :, 2])
    return brightness

def calculate_contrast(image):
    imageValue = cv2.imread(image)
    gray = cv2.cvtColor(imageValue, cv2.COLOR_BGR2GRAY)
    contrast = gray.std()
    return contrast

def calculate_blur(image):
    imageValue = cv2.imread(image)
    gray = cv2.cvtColor(imageValue, cv2.COLOR_BGR2GRAY)
    laplacian_var = cv2.Laplacian(gray, cv2.CV_64F).var()
    return laplacian_var

def analyze_image(image_path,array_of_tests):
    image = cv2.imread(image_path)
    vec=["0"]*len(array_of_tests)
    returnvalue=image_path
    if image is not None:
        for x in range(len(vec)):
            returnvalue+=","+str(array_of_tests[x](image_path))
        return returnvalue
    else:

        for x in range(len(vec)):
            returnvalue+=",0"
        return image_path+returnvalue

Header="Path,vecotor,calculate_brightness,calculate_contrast,calculate_blur"

orderphotos = input("Manually Score and Order photos: Y/N ")

displayPhotos=False
if orderphotos=="Y":
    displayPhotos=True
    Header+=",UserScore1,UserScore2"


array_of_tests=[calculate_brightness,calculate_contrast,calculate_blur]
directorys=["framesbeard","framesmrbeanbeard","framesmrbeannobeard","framesnobeard","framesreevesbeard","framesreevesnobeard","TimeNorlandnobeard"]

print(Header)
for x in range(len(directorys)):
    files=os.listdir(directorys[x])
    for y in range(len(files)):
        Linevalue=analyze_image(directorys[x]+"\\"+files[y],array_of_tests)
        if displayPhotos:
            image = cv2.imread(directorys[x]+"\\"+files[y])
            cv2.imshow('Image Window', image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            Linevalue+=","+ input("UserScore1:")
            Linevalue+=","+ input("UserScore2:")
        print(Linevalue)
        Header+=Linevalue+"\n"

with open('output.csv', 'w') as file:
    # Write text to the file
    file.write(Header)
print("File written successfully.")

quit()