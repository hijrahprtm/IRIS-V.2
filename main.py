from deepface import DeepFace
import cv2
import pyttsx3

# Voice
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Webcam
cap = cv2.VideoCapture(0)

spoken_owner = False
spoken_unknown = False

while True:
    ret, frame = cap.read()

    try:
        result = DeepFace.verify(
            frame,
            "owner.jpg",
            enforce_detection=False
        )

        if result["verified"]:

            cv2.putText(
                frame,
                "OWNER",
                (50, 50),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0,255,0),
                2
            )

            if not spoken_owner:
                speak("Welcome back Hijrah")
                spoken_owner = True
                spoken_unknown = False

        else:

            cv2.putText(
                frame,
                "UNKNOWN",
                (50, 50),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0,0,255),
                2
            )

            if not spoken_unknown:
                speak("Access denied")
                spoken_unknown = True
                spoken_owner = False

    except:
        pass

    cv2.imshow("IRIS v2", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()