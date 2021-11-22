import numpy as np
import cv2

#Define qual a porta da camera
cap = cv2.VideoCapture(0)

while True:
    #Pega a imagem da camera
    ret, frame = cap.read()

    #Pega a altura e a largura da imagem
    width = int(cap.get(3))
    height = int(cap.get(4))

    #Cria um numpy arry de zeros no modelo do frame da camera
    image = np.zeros(frame.shape, np.uint8)
    #Cria um freme menor redimensionando o lido da camera
    smaller_frame = cv2.resize(frame, (0,0), fx=0.5, fy=0.5)

    #Aplica o frame menor criado a partes da imagem
    image[:height//2, :width//2] = cv2.rotate(smaller_frame, cv2.cv2.ROTATE_180) #Rotaciona essa imagem 180°
    image[height//2:, :width//2] = smaller_frame
    image[:height//2, width//2:] = cv2.rotate(smaller_frame, cv2.cv2.ROTATE_180) #Rotaciona essa imagem 180°
    image[height//2:, width//2:] = smaller_frame

    #Mostra a imagem
    cv2.imshow('frame', image)

    #Condição para janela fechar caso a letra 'q' seja pressionada no teclado
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()