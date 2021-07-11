import cv2
import pickle
import numpy as np

cap=cv2.VideoCapture(0)
#### LOAD THE TRAINNED MODEL
pickle_in = open("alphabet_model.p","rb")
model = pickle.load(pickle_in)
#### PREPORCESSING FUNCTION
def preProcessing(img):
    img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    img = cv2.equalizeHist(img)
    img = img/255
    return img
while True:
    success, imgOriginal = cap.read()
    img = np.asarray(imgOriginal)
    img = cv2.resize(img,(32,32))
    img = preProcessing(img)
    cv2.imshow("Processsed Image",img)
    img = img.reshape(1,32,32,1)
    #### PREDICT
    classIndex = int(model.predict_classes(img))
    #print(classIndex)
    predictions = model.predict(img)
    #print(predictions)
    probVal= np.amax(predictions)
    #print(classIndex,probVal)
    if(classIndex== 1):
        print('the digit  0')
    elif(classIndex== 2):
        print('the digit is 1')
    elif (classIndex == 3):
        print('the digit is 2')
    elif (classIndex == 4):
        print('the digit is 3')
    elif (classIndex == 5):
        print('the digit is 4')
    elif (classIndex == 6):
        print('the digit is 5')
    elif (classIndex == 7):
        print('the digit is 6')
    elif (classIndex == 8):
        print('the digit is 7')
    elif (classIndex == 9):
        print('the digit is 8')
    elif (classIndex == 10):
        print('the digit is 9')
    elif (classIndex == 11):
        print('the letter is A')
    elif (classIndex == 12):
        print('the letter is B')
    elif (classIndex == 13):
        print('the letter is C')
    elif (classIndex == 14):
        print('the letter is D')
    elif (classIndex == 15):
        print('the letter is E')
    elif (classIndex == 16):
        print('the letter is F')
    elif (classIndex == 17):
        print('the letter is G')
    elif (classIndex == 18):
        print('the letter is H')
    elif (classIndex == 19):
        print('the letter is I')
    elif (classIndex == 20):
        print('the letter is J')
    elif (classIndex == 21):
        print('the letter is K')
    elif (classIndex == 22):
        print('the letter is L')
    elif (classIndex == 23):
        print('the letter is M')
    elif (classIndex == 24):
        print('the letter is N')
    elif (classIndex == 25):
        print('the letter is O')
    elif (classIndex == 26):
        print('the letter is P')
    elif (classIndex == 27):
        print('the letter is Q')
    elif (classIndex == 28):
        print('the letter is R')
    elif (classIndex == 29):
        print('the letter is S')
    elif (classIndex == 30):
        print('the letter is T')
    elif (classIndex == 31):
        print('the letter is U')
    elif (classIndex == 32):
        print('the letter is V')
    elif (classIndex == 33):
        print('the letter is W')
    elif (classIndex == 34):
        print('the letter is X')
    elif (classIndex == 35):
        print('the letter is Y')
    elif (classIndex == 36):
        print('the letter is Z')
    elif (classIndex == 37):
        print('the letter is a')
    elif (classIndex == 38):
        print('the letter is b')
    elif (classIndex == 39):
        print('the letter is c')
    elif (classIndex == 40):
        print('the letter is d')
    elif (classIndex == 41):
        print('the letter is e')
    elif (classIndex == 42):
        print('the letter is f')
    elif (classIndex == 43):
        print('the letter is g')
    elif (classIndex == 44):
        print('the letter is h')
    elif (classIndex == 45):
        print('the letter is i')
    elif (classIndex == 46):
        print('the letter is j')
    elif (classIndex == 47):
        print('the letter is k')
    elif (classIndex == 48):
        print('the letter is l')
    elif (classIndex == 49):
        print('the letter is m')
    elif (classIndex == 50):
        print('the letter is n')
    elif (classIndex == 51):
        print('the letter is o')
    elif (classIndex == 52):
        print('the letter is p')
    elif (classIndex == 53):
        print('the letter is q')
    elif (classIndex == 54):
        print('the letter is r')
    elif (classIndex == 55):
        print('the letter is s')
    elif (classIndex == 56):
        print('the letter is t')
    elif (classIndex == 57):
        print('the letter is u')
    elif (classIndex == 58):
        print('the letter is v')
    elif (classIndex == 59):
        print('the letter is w')
    elif (classIndex == 60):
        print('the letter is x')
    elif (classIndex == 61):
        print('the letter is y')
    elif (classIndex == 62):
        print('the letter is z')

    if probVal> 0.65:


        cv2.putText(imgOriginal,str(classIndex) + "   "+str(probVal),
                    (50,50),cv2.FONT_HERSHEY_COMPLEX,
                    1,(0,0,255),1)

    cv2.imshow("Original Image",imgOriginal)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()