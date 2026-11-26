C%20macOS-lightgrey?style=for-th
> 
- Stand **away from the camera** st few seconds while t
## 📁 Pro
potter-invisibility-cloak/
├── main.py 
Tune the HSV range in `main.py` to match your specific green cloth under your lighting:

```python
lower_green = np.array([50, 80, 50])
upper_green = np.array([90, 255, 255])
```

Use a tool like [this HSV picker](https://colorpicker.me/) or OpenCV trackbars to dial in the right values.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
