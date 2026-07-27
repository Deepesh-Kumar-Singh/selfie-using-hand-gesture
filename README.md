# 🤳 Take Selfie Using Hand Gesture

A Python-based Computer Vision project that captures selfies using **hand gestures**. The application detects the number of fingers raised using **MediaPipe** and **OpenCV**, starts a countdown based on the detected gesture, and automatically saves the captured image.

---

## 🚀 Features

* ✋ Real-time hand gesture detection
* 📷 Capture selfies without touching the keyboard
* ⏳ Countdown timer based on the number of fingers shown
* 💾 Automatically saves captured images
* ⚡ Fast and accurate hand tracking using MediaPipe

---

## 🛠️ Technologies Used

* **Python**
* **OpenCV** – For webcam access, image processing, and saving photos.
* **MediaPipe** – For real-time hand landmark detection and tracking.
* **CvZone** – Simplifies MediaPipe hand tracking integration.

---

## 📂 Project Workflow

1. Open the webcam.
2. Detect the user's hand using MediaPipe.
3. Count the number of fingers raised.
4. Start a countdown equal to the number of fingers shown.
5. Capture and save the selfie automatically after the countdown.

---

## 📸 Example

| Fingers Shown | Countdown |
| ------------: | :-------- |
|          ☝️ 1 | 1 Second  |
|          ✌️ 2 | 2 Seconds |
|          🤟 3 | 3 Seconds |
|          🖖 4 | 4 Seconds |
|         🖐️ 5 | 5 Seconds |

After the countdown finishes, the image is automatically saved as:

```text
screenshot1.jpg
screenshot2.jpg
screenshot3.jpg
...
```

---



Install the required packages:

```bash
pip install opencv-python mediapipe cvzone
```

---

## ▶️ Run the Project

```bash
python main.py
```

---

## 📁 Project Structure

```text
📦 Take-Selfie-Using-Hand-Gesture
│── main.py
│── screenshot1.jpg
│── screenshot2.jpg
│── README.md
```

---

## 🎯 Future Improvements

* 😊 Smile detection before capturing
* 📸 Capture multiple photos in burst mode
* 🎨 Apply image filters and effects
* 🧠 Gesture-based mode selection
* 💻 GUI for a better user experience

---

## 🤝 Contributing

Contributions, suggestions, and improvements are always welcome. Feel free to fork this repository and submit a pull request.

---

## 📜 License

This project is licensed under the MIT License.

---

## ⭐ Support

If you found this project useful, consider giving it a **⭐ Star** on GitHub. It helps others discover the project and motivates future improvements.
