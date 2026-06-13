import cv2
import numpy as np
import time

# ==========================================
# CONFIGURATION
# ==========================================
CAMERA_INDEX = 0
FRAME_WIDTH = 1280
FRAME_HEIGHT = 720

BACKGROUND_FRAMES = 80

# Green cloak HSV range
LOWER_GREEN = np.array([35, 40, 40])
UPPER_GREEN = np.array([90, 255, 255])

# Morphological kernels
KERNEL_OPEN = np.ones((3, 3), np.uint8)
KERNEL_CLOSE = np.ones((7, 7), np.uint8)

# ==========================================
# FPS CLASS
# ==========================================
class FPSCounter:
    def __init__(self):
        self.prev_time = time.time()
        self.fps = 0

    def update(self):
        current_time = time.time()

        delta = current_time - self.prev_time

        if delta > 0:
            current_fps = 1 / delta

            # Smooth FPS
            self.fps = (
                0.9 * self.fps +
                0.1 * current_fps
            )

        self.prev_time = current_time

        return int(self.fps)


# ==========================================
# CAPTURE BACKGROUND
# ==========================================
def capture_background(cap):

    print("\nMove out of the frame...")
    print("Capturing background...\n")

    background = None

    for i in range(BACKGROUND_FRAMES):

        ret, frame = cap.read()

        if not ret:
            continue

        frame = cv2.flip(frame, 1)

        if background is None:
            background = frame.astype(np.float32)

        cv2.accumulateWeighted(
            frame,
            background,
            0.05
        )

        preview = frame.copy()

        cv2.putText(
            preview,
            f"Capturing Background: {i+1}/{BACKGROUND_FRAMES}",
            (20, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 0),
            2
        )

        cv2.imshow("Background Capture", preview)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyWindow("Background Capture")

    return cv2.convertScaleAbs(background)


# ==========================================
# CREATE GREEN MASK
# ==========================================
def create_mask(frame):

    hsv = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2HSV
    )

    mask = cv2.inRange(
        hsv,
        LOWER_GREEN,
        UPPER_GREEN
    )

    # Remove noise
    mask = cv2.morphologyEx(
        mask,
        cv2.MORPH_OPEN,
        KERNEL_OPEN,
        iterations=2
    )

    # Fill holes
    mask = cv2.morphologyEx(
        mask,
        cv2.MORPH_CLOSE,
        KERNEL_CLOSE,
        iterations=2
    )

    # Smooth edges
    mask = cv2.GaussianBlur(
        mask,
        (11, 11),
        0
    )

    return mask


# ==========================================
# MAIN
# ==========================================
def main():

    cap = cv2.VideoCapture(CAMERA_INDEX)

    if not cap.isOpened():
        print("Error: Cannot access webcam.")
        return

    cap.set(
        cv2.CAP_PROP_FRAME_WIDTH,
        FRAME_WIDTH
    )

    cap.set(
        cv2.CAP_PROP_FRAME_HEIGHT,
        FRAME_HEIGHT
    )

    background = capture_background(cap)

    fps_counter = FPSCounter()

    print("\n===================================")
    print("MAGIC CLOAK READY")
    print("===================================")
    print("Wear GREEN cloth")
    print("Press R to recapture background")
    print("Press Q to quit")
    print("===================================\n")

    while True:

        ret, frame = cap.read()

        if not ret:
            break

        frame = cv2.flip(frame, 1)

        # -------------------------------
        # Detect Green Cloth
        # -------------------------------
        mask = create_mask(frame)

        inverse_mask = cv2.bitwise_not(mask)

        # -------------------------------
        # Extract Cloak Region
        # -------------------------------
        cloak_region = cv2.bitwise_and(
            background,
            background,
            mask=mask
        )

        # -------------------------------
        # Visible Region
        # -------------------------------
        visible_region = cv2.bitwise_and(
            frame,
            frame,
            mask=inverse_mask
        )

        # -------------------------------
        # Combine
        # -------------------------------
        output = cv2.add(
            cloak_region,
            visible_region
        )

        # -------------------------------
        # FPS
        # -------------------------------
        fps = fps_counter.update()

        cv2.putText(
            output,
            f"FPS: {fps}",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

        cv2.putText(
            output,
            "R = Refresh Background",
            (20, 80),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255, 255, 255),
            2
        )

        cv2.putText(
            output,
            "Q = Quit",
            (20, 115),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255, 255, 255),
            2
        )

        # -------------------------------
        # Show Windows
        # -------------------------------
        cv2.imshow(
            "Magic Cloak",
            output
        )

        cv2.imshow(
            "Mask",
            mask
        )

        key = cv2.waitKey(1) & 0xFF

        # Refresh background
        if key == ord('r'):
            background = capture_background(cap)

        elif key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
