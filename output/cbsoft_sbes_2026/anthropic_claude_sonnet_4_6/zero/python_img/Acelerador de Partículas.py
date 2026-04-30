Looking at the image and problem description:

- Emissor to accelerator entry: 3 km
- Accelerator circumference: 8 km
- The particle travels D km total

From the image, I can deduce the sensor positions on the circle:
- Sensor 1: at position 6 km from start (3 km straight + enters circle, exits at some point)
- Let me think more carefully.

The particle travels 3 km to reach the accelerator. Then it goes around the circle (8 km circumference) some number of times, then exits to a sensor.

From the example: D=23, sensor=2.
- 23 - 3 = 20 km inside/after accelerator
- 20 mod 8 = 4 (since 20 = 2*8 + 4)

For D=6, sensor=1:
- 6 - 3 = 3 km
- 3 mod 8 = 3

For D=9192, sensor=3:
- 9192 - 3 = 9189
- 9189 mod 8 = 9189 - 1148*8 = 9189 - 9184 = 5

So sensor positions (distance from entry point on circle):
- Sensor 1: remainder = 3
- Sensor 2: remainder = 4
- Sensor 3: remainder = 5

Let me verify:
- D=6: (6-3) mod 8 = 3 → sensor 1 ✓
- D=23: (23-3) mod 8 = 20 mod 8 = 4 → sensor 2 ✓
- D=9192: (9192-3) mod 8 = 9189 mod 8 = 5 → sensor 3 ✓

D = int(input())
remainder = (D - 3) % 8
if remainder == 3:
    print(1)
elif remainder == 4:
    print(2)
else:
    print(3)