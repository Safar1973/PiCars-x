from picarx import Picarx
import time

if __name__ == "__main__":
    try:
        px = Picarx()
        px.forward(30)
        time.sleep(0.5)
        
        # Lenkservo bewegen
        for angle in range(0, 35):
            px.set_dir_servo_angle(angle)
            time.sleep(0.01)
        for angle in range(35, -35, -1):
            px.set_dir_servo_angle(angle)
            time.sleep(0.01)
        for angle in range(-35, 0):
            px.set_dir_servo_angle(angle)
            time.sleep(0.01)
        
        px.forward(0)
        time.sleep(1)

        # Kamera-Servos bewegen
        # Horizontaler Winkel (Pan)
        for angle in range(0, 35):
            px.set_cam_pan_angle(angle)
            time.sleep(0.01)
        for angle in range(35, -35, -1):
            px.set_cam_pan_angle(angle)
            time.sleep(0.01)
        for angle in range(-35, 0):
            px.set_cam_pan_angle(angle)
            time.sleep(0.01)

        # Vertikaler Winkel (Tilt)
        for angle in range(0, 35):
            px.set_cam_tilt_angle(angle)
            time.sleep(0.01)
        for angle in range(35, -35, -1):
            px.set_cam_tilt_angle(angle)
            time.sleep(0.01)
        for angle in range(-35, 0):
            px.set_cam_tilt_angle(angle)
            time.sleep(0.01)

    finally:
        px.forward(0)