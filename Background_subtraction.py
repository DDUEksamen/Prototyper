import cv2
import numpy as np
import imutils

cap = cv2.VideoCapture(0)
fgbg = cv2.createBackgroundSubtractorMOG2(750,16,True)

ret, ref = cap.read()
if ret:
	ref = imutils.resize(ref,width=min(400,ref.shape[1]))
	#ref = cv2.cvtColor(ref,cv2.COLOR_BGR2GRAY)

while cap.isOpened():
	# Reading the video stream
	ret, image = cap.read()
	if ret:
		image = imutils.resize(image, width=min(750, image.shape[1]))
		#image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

		fgmask = fgbg.apply(image,learningRate=0.0003)
 
		fgmask = cv2.bitwise_not(fgmask)
		
		hsv = cv2.cvtColor(fgmask, cv2.COLOR_GRAY2BGR)
		hsv = cv2.cvtColor(hsv, cv2.COLOR_BGR2HSV)

		
		lower = np.array([0,0,0])
		upper = np.array([10,10,10])

		mask = cv2.inRange(hsv, lower, upper)
		mask = cv2.bitwise_not(mask)

		_, src_thresh = cv2.threshold(mask, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
		#cv2.imshow('src_thresh', src_thresh);cv2.waitKey(0);cv2.destroyAllWindows()  # Show src_thresh for testing
		contours, _ = cv2.findContours(src_thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

		# Get the moments
		mu = [None for i in contours]
		for i in range(len(contours)):
			mu[i] = cv2.moments(contours[i])
		# Get the mass centers
		mc = [None for i in contours]
		for i in range(len(contours)):
			mc[i] = (mu[i]['m10'] / (mu[i]['m00'] + 1e-5), mu[i]['m01'] / (mu[i]['m00'] + 1e-5))
		# Draw contours
		drawing = np.zeros((src_thresh.shape[0], src_thresh.shape[1], 3), dtype=np.uint8)
		for i, j in enumerate(contours):
			if int(cv2.contourArea(contours[i]))>500:
				colour = (0, 0, 255)
				cv2.drawContours(drawing, contours, i, colour, 2)
				area = int(cv2.contourArea(contours[i]))
				length = int(cv2.arcLength(contours[i], True))
				print('Contour[{0}] Area: {1}, Length: {2}'.format(i, area, length ))
				x,y,w,h = cv2.boundingRect(contours[i])
				cv2.rectangle(drawing,(x,y),(x+w,y+h),(0,255,0),2)

		cv2.imshow('drawing', drawing)
		if cv2.waitKey(25) & 0xFF == ord('q'):
			break
		
	else:
		break

cap.release()
cv2.destroyAllWindows()
