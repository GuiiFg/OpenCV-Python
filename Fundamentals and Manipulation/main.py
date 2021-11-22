import cv2

#Abre a imagem
img = cv2.imread("Fundamentals and Manipulation\Disney.png", 1)

#Pinta a imagem
for row in range(100):
    for column in range(img.shape[1]):
        img[row][column] = [100, 200, 50]

#Printa a estrutura da imagem
print(img.shape)

#Copia parte da image e salva
img2 = img[200:600, 400:1000]

#salva o corte da imagem
cv2.imwrite("Fundamentals and Manipulation\Disney_short.png", img2)

#Mostra a imagem em uma janela
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()