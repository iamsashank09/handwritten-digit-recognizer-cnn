import sys
from keras.models import load_model
import cv2
from preprocessors import x_cord_contour, makeSquare, resize_to_pixel
import pyfiglet

class findHandwrittenDigits:
    def __init__(self, imageFileName):

        self.classifier = load_model('mnistHandModel.h5')
        self.image = cv2.imread(imageFileName)
        self.dispImage = self.image.copy()
        self.full_number = []

    def findDigits(self):

        image = self.image.copy() 
        gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

        blurred = cv2.GaussianBlur(gray, (5, 5), 0)

        edged = cv2.Canny(blurred, 30, 150)

        # Find Contours
        contours, _  = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Filtering out smaller contours
        contours = [i for i in contours if cv2.contourArea(i)>10]

        #Sort out contours left to right by using their x cordinates
        contours = sorted(contours, key = x_cord_contour, reverse = False)

        # Create empty array to store entire number

        # loop over the contours
        for c in contours:
            # compute the bounding box for the rectangle
            (x, y, w, h) = cv2.boundingRect(c)    

            if w >= 5 and h >= 25:
                roi = blurred[y:y + h, x:x + w]
                ret, roi = cv2.threshold(roi, 127, 255,cv2.THRESH_BINARY_INV)
                roi = makeSquare(roi)
                roi = resize_to_pixel(28, roi)
                roi = roi / 255.0       
                roi = roi.reshape(1,28,28,1) 

                ## Get Prediction
                res = str(self.classifier.predict_classes(roi, 1, verbose = 0)[0])


                self.full_number.append(res)
                cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
                cv2.putText(image, res, (x , y + 155), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 0, 0), 2)
                self.dispImage = image.copy()

    def displayResult(self, displayImg = False):
        
        if displayImg:
            cv2.imshow("image", self.dispImage)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        figText = pyfiglet.figlet_format(str(''.join(self.full_number)))
        print ("The number is: " )
        print(figText)

if __name__ == "__main__":

    try:
        filename = sys.argv[1]

    except:
        print('''Mention the file name while running the app.
        Usage: python application.py 'filenamehere'  ''')
        exit()

    finderObject = findHandwrittenDigits(filename)
    finderObject.findDigits()
    finderObject.displayResult(True)