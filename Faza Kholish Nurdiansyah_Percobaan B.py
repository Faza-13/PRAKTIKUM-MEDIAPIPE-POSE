import cv2
import mediapipe as mp
mpose =mp.solutions.pose #inisialisasi media pipe pose
pose = mpose.Pose()
mdraw =mp.solutions.drawing_utils
cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read() #pembacaan image3q
    imgrgb= cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #konversi warna dari bgr ke rgb
    hasil = pose.process(imgrgb) #ekstraksi dari image

    if hasil.pose_landmarks:
        mdraw.draw_landmarks(img, hasil.pose_landmarks, mpose.POSE_CONNECTIONS) #menggambar koneksi landmark
        for id, lm in enumerate(hasil.pose_landmarks.landmark):
            print(id, lm.x, lm.y) #ekstraksi id, posisi x, posisi y
    cv2.imshow("webcam",img)
    cv2.waitKey(10)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
    #tutup webcam dan jendela tampilan saat q ditekan
cap.release()
cv2.destroyAllWindows()
