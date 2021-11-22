import cv2

#Abre a imagem
img = cv2.imread("Fundamentals and Manipulation\Disney.png", 1)

#Pinta a imagem
for row in range(100):
    for column in range(img.shape[1]):
        img[row][column] = [100, 200, 50]

#Printa a estrutura da imagem
print(img.shape)

#Mostra a imagem em uma janela
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()