import cv2

#Abre a imagem
img = cv2.imread("ModifyImages\Disney.png", 1)

#Redimenciona a imagem
img = cv2.resize(img, (0,0), fx=0.5, fy=0.5)

#Roda a imagem
img = cv2.rotate(img, cv2.cv2.ROTATE_90_CLOCKWISE)

#Salva a imagem modificada
cv2.imwrite("ModifyImages\Disney_modify.png", img)

#Mostra a imagem em uma janela
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()