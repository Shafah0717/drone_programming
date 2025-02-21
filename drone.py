from djitellopy import Tello
import time


tello = Tello()


tello.connect()


print(f"Battery: {tello.get_battery()}%")


tello.takeoff()

tello.move_up(40)
time.sleep(2)



for _ in range(5):
    tello.move_forward(70)
    time.sleep(1)
    tello.rotate_clockwise(108)
    time.sleep(1)

tello.land()

tello.end()