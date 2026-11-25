een?style=for
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey?style=for-the-badge)
> Real-time Harry Potter–style invisibility cloak effect usi

## ✨2. 🎥 Reads each **live webcam frame**
3. 🟢 Detects **green pixels** using HSV color masking
4. 🔁 Replaces green regions with the saved background
5. 🪄 Outputs a seamless **invisibility effect*
- Python 3.8+
- A webcam
- A **green cloth** (the "cloak")

Install dependencies:

```bash
pip install opencv-python numpy
```

---

## 🚀 Usage

```bash
python main.py
```

- Stand **away from the camera** for the first few seconds while the background is captured
- Wear or hold the **green cloth** in front of you
- Press **`q`** to quit

---

## 📁 Project Structure

```
potter-invisibility-cloak/
├── main.py       # Core invisibility cloak logic
└── README.md
```

---

## ⚙️ Configuration

Tune the HSV range in `main.py` to match your specific green cloth under your lighting:

```python
lower_green = np.array([50, 80, 50])
upper_green = np.array([90, 255, 255])
```

Use a tool like [this HSV picker](https://colorpicker.me/) or OpenCV trackbars to dial in the right values.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
