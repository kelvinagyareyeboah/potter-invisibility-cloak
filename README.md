%7C%20Linux%20%7C%20macOS-lightgrey?style=for-th
> Real-time Harry Potter–style invisibi
## ✨2. 🎥 Reads eac
4. 🔁 Replaces green re
5. 🪄 Outputs a se
- A **green clo



```bash
pip install open
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
