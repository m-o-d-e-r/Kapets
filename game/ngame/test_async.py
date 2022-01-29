import cv2


faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)

saved = False



while True:
    resp, frame = camera.read()

    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(frame_gray, 1.1, 19)

    for (x, y, width, height) in faces:
        cv2.rectangle(frame, (x, y), (x + width, y + height), (0, 255, 0), 5)
        if not saved:
            cv2.imwrite(r"D:\pyrus\NewGame\game\ngame\img1.jpg", frame)
            saved = True

    cv2.imshow("1", frame_gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        camera.release()
        cv2.destroyAllWindows()
        break


"""
import base64
import hashlib

class Base64:
    def __init__(self, data):
        if type(data) != bytes:
            data = data.encode("utf-8")
        self.encode_data = base64.b64encode(data)

    def __eq__(self, o):
        return self.encode_data == base64.b64encode(o.encode("utf-8"))

    def __repr__(self):
        return str(self.encode_data)

class Md5:
    def __init__(self, data):
        if type(data) != bytes:
            data = data.encode("utf-8")

        self.hash_ = self.make_hash(data)

    def make_hash(self, data):
        return hashlib.md5(data).hexdigest()

    def __eq__(self, try_data):
        return self.make_hash(try_data) == self.hash_

    def __repr__(self):
        return self.hash_


"""