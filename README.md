# 🏃 Jump Counter — AI-Powered Real-Time Jump Detection

A mobile-first web application that uses your device's camera and AI pose detection to count jumps in real time — entirely in the browser, with zero server lag and zero data sent anywhere.

---

## 📱 Demo

> Open on your phone → Allow camera → Stand back → Start jumping!

Live demo: `https://JumpCounterAI.onrender.com`

---

## ✨ Features

- 🤖 **Real-time AI pose detection** — powered by MediaPipe Pose (runs via WebAssembly in the browser)
- ⚡ **Zero lag** — all processing happens on-device at 30fps, no frames sent to server
- 📱 **Mobile-first design** — full-screen camera, portrait layout, safe area support for notch/Dynamic Island
- 🔄 **Camera flip** — switch between front and rear camera with one tap
- 📳 **Haptic feedback** — phone vibrates on every counted jump
- 🎯 **Auto calibration** — stands your baseline hip position in ~1.5 seconds
- 🔁 **Recalibrate** — re-baseline anytime without losing your count
- 🔒 **100% private** — no video, no frames, no data ever leaves your device

---

## 🧠 How It Works

```
Your Camera (30fps)
      ↓
MediaPipe Pose (WebAssembly in browser)
      ↓
33 body landmarks detected per frame
      ↓
Hip Y-position tracked + smoothed (moving average)
      ↓
Calibration: baseline hip position recorded (~1.5 sec)
      ↓
Jump threshold crossed → "in air" state
Landing threshold crossed → JUMP COUNTED ✅
```

The server only serves the HTML page. Everything else — pose detection, jump logic, UI updates — runs locally on your device.

---

## 🏗️ Tech Stack

| Layer | Technology |
|---|---|
| Frontend | HTML5, CSS3, Vanilla JavaScript |
| AI / Pose Detection | [MediaPipe Pose](https://google.github.io/mediapipe/solutions/pose) (WebAssembly) |
| Backend | Python + Flask (serves HTML only) |
| Deployment | Render (free tier) |

---

## 📁 Project Structure

```
jump-counter/
├── app.py                  # Flask server — serves the HTML page
├── requirements.txt        # Python dependencies
├── Procfile                # Render deployment config
└── templates/
    └── index.html          # Entire app (UI + AI detection logic)
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.9+
- A modern browser (Chrome, Safari, Firefox)
- A device with a camera

### Run Locally

```bash
# 1. Clone the repo
git clone https://github.com/YOUR_USERNAME/jump-counter.git
cd jump-counter

# 2. Create a virtual environment
python -m venv venv

# Windows
venv\Scripts\activate

# Mac / Linux
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
python app.py

# 5. Open in browser
# http://127.0.0.1:5000
```

> **VS Code tip:** After activating the venv, press `Ctrl+Shift+P` → `Python: Select Interpreter` → select `.\venv\Scripts\python.exe` to fix any import warnings.

---

## 🌐 Deploy to Render (Free)

1. Push this repo to GitHub
2. Go to [render.com](https://render.com) → New → Web Service
3. Connect your GitHub repo and set:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app --workers 2 --bind 0.0.0.0:$PORT`
   - **Instance Type:** Free
4. Click **Deploy** — your live URL will be ready in ~3 minutes

---

## 🎛️ Fine-Tuning Detection

You can adjust these constants at the top of the `<script>` tag in `templates/index.html`:

```javascript
const CALIB_FRAMES   = 45;    // frames to build baseline (~1.5 sec at 30fps)
const JUMP_THRESHOLD = 0.055; // how high hips must rise to trigger "in air"
const LAND_THRESHOLD = 0.022; // how close to baseline before jump is counted
const SMOOTH_N       = 6;     // moving average window (higher = smoother, tiny lag)
```

| Problem | Fix |
|---|---|
| False jumps triggered | Increase `JUMP_THRESHOLD` to `0.07` or `0.08` |
| Jumps not being detected | Decrease `JUMP_THRESHOLD` to `0.04` |
| Double-counting one jump | Increase `LAND_THRESHOLD` slightly |
| Jittery detection | Increase `SMOOTH_N` to `8` or `10` |

---

## 📱 Tips for Best Results

- Stand **1.5 – 2.5 metres** from the camera
- Make sure your **full body is visible** in the frame
- Use **good lighting** — avoid backlighting (bright window behind you)
- **Stand still** for ~1.5 seconds after starting to let calibration complete
- Jump **straight up** and land cleanly on both feet
- If you move the phone or change position, tap **Recalibrate**

---

## 🔒 Privacy

This app does **not** collect, store, or transmit any video, images, or personal data. All AI processing runs locally on your device using WebAssembly. The Flask server only serves the static HTML page and has no access to your camera at any point.

---

## 🐛 Known Limitations

- Requires a modern browser with WebAssembly support (Chrome 80+, Safari 14+, Firefox 79+)
- MediaPipe Pose may perform slower on older/low-end devices
- Accuracy drops if the full body is not visible in the frame
- The free Render tier sleeps after 15 minutes of inactivity (first load may take ~30 sec to wake up)

---

## 🛠️ Built With

- [MediaPipe](https://google.github.io/mediapipe/) — Google's on-device ML framework
- [Flask](https://flask.palletsprojects.com/) — Lightweight Python web framework
- [Render](https://render.com/) — Cloud deployment platform

---

## 📄 License

MIT License — feel free to use, modify, and distribute.

---

## 🙋 Author

Built by **Sai Shubham**
- GitHub: [@ESaiShubham](https://github.com/ESaiShubham)
- LinkedIn: [ESaiShubham](https://linkedin.com/in/ESaiShubham)

---

> ⭐ If you found this useful, give it a star on GitHub!
