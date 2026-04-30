Looking at this problem, I need to figure out the layout from the image description:

- Emissor to acelerador: 3 km
- Acelerador circumference: 8 km
- The particle travels D km total from emissor to a sensor

From the example: D=23 → sensor 2, D=6 → sensor 1

Let me figure out the sensor positions. The particle travels 3 km to enter the accelerator, then goes around some number of times, then exits to a sensor.

The sensors are at different distances from the accelerator exit points. Let me think about the layout based on the figure description and examples.

- D=6: 6-3=3 km inside/after accelerator → sensor 1
- D=23: 23-3=20 km. 20 mod 8 = 4 → sensor 2
- D=9192: 9192-3=9189. 9189 mod 8 = 9189 - 8*1148 = 9189-9184=5 → sensor 3

So after subtracting the 3 km to reach the accelerator, we have the remaining distance. The particle goes around the loop and exits at one of the sensors.

The sensors seem to be at positions on/after the loop:
- Sensor 1: remainder = 3 (exits after 3 km in the loop, then some distance to sensor)
- Sensor 2: remainder = 4
- Sensor 3: remainder = 5

Wait, let me reconsider. Maybe the sensors are connected at specific points on the loop, and the exit distances to sensors add up.

D=6: remaining = 3. If sensor 1 is at distance 3 from entry point (position 3 on the circle), that works.
D=23: remaining = 20. 20 mod 8 = 4. Sensor 2 at position 4.
D=9192: remaining = 9189. 9189 mod 8 = 5. Sensor 3 at position 5.

So the sensors are at positions 3, 4, 5 on the 8km circumference loop (measured from entry point).

But we need to verify: the particle exits when it reaches a sensor position. The total distance after the initial 3km, modulo 8, gives the position on the loop.

- If position mod 8 == 3 → sensor 1
- If position mod 8 == 4 → sensor 2  
- If position mod 8 == 5 → sensor 3

Let me verify:
- D=6: (6-3) mod 8 = 3 → sensor 1 ✓
- D=23: (23-3) mod 8 = 20 mod 8 = 4 → sensor 2 ✓
- D=9192: (9192-3) mod 8 = 9189 mod 8 = 5 → sensor 3 ✓

D = int(input())
remaining = (D - 3) % 8
if remaining == 3:
    print(1)
elif remaining == 4:
    print(2)
else:
    print(3)