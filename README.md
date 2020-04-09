# Handwritten Digit Recognition using CNN
The repository contains to major files:
### /HandwrittenDigitRecognition.ipynb
This is the IPython(ipynb) notebook that contains the code and data related to the development of the recognition of the model.
Please refer to this if you wish to understand the model used and training process.

### /application.py
This is the application that does the digit recognition. 
It loads the model generated using the CNN. 
Takes the image as an input and gives the number as the output. 

## Demo Outputs

![Command Line output](https://github.com/iamsashank09/handwritten-digit-recognizer-cnn/blob/master/images/outputs/numbersOPcmd.png)
![Command Line output](https://github.com/iamsashank09/handwritten-digit-recognizer-cnn/blob/master/images/outputs/numbersOPimg.png)

## Usage

You can run the application by running the Python 3 file and passing the image as a parameter.

> python3 application.py [file-path-here]

Example:

> python3 application.py images/numbers.jpg

This code was developed as while learning from a course on Deep Learning, the idea is inspired by the course instructor's work. Everyone is free to use this repository for their personal and professional use. 
