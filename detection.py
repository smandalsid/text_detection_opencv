import cv2
import pytesseract

img=cv2.imread("1.png")
img=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


print(pytesseract.image_to_string(img))

imgh, imgw, _=img.shape
config=r'--oem 3 --psm 6 outputbase digits'
boxes=pytesseract.image_to_boxes(img, config=config)
for b in boxes.splitlines():
    # print(b)
    b=b.split(' ')
    print(b)
    x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
    cv2.rectangle(img, (x, imgh-y), (w, imgh-h), (0, 255, 0), 3)
    cv2.putText(img, b[0], (x, imgh-y+25), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
cv2.imshow("Result1", img)

imgh, imgw, _=img.shape
config=r'--oem 3 --psm 6 outputbase digits'
boxes=pytesseract.image_to_data(img, config=config)
print(boxes)
for i, b in enumerate(boxes.splitlines()):
    if i!=0:
        b=b.split()
        print(b)
        if(len(b)==12):
            x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
            cv2.rectangle(img, (x, y), (w+x, h+y), (0, 255, 0), 3)
            cv2.putText(img, b[11], (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
            
cv2.imshow("Result2", img)


while True:
    if cv2.waitKey(1) & 0xFF==ord('q'):
        cv2.destroyAllWindows()
        break