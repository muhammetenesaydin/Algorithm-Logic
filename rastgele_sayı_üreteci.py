import psutil
import random
import time
import os
from pynput import mouse

# Mouse hareketi ölçümü
mouse_delta = 0

def on_move(x, y):
    global mouse_delta
    mouse_delta += abs(x) + abs(y)

listener = mouse.Listener(on_move=on_move)
listener.start()

def get_system_entropy():
    entropy = 0

    # CPU sıcaklığı (varsa)
    temps = psutil.sensors_temperatures()
    if temps:
        for name in temps:
            for entry in temps[name]:
                entropy += int(entry.current * 100)

    # Fan RPM (varsa)
    fans = psutil.sensors_fans()
    if fans:
        for name in fans:
            for fan in fans[name]:
                entropy += fan.current or 0

    # Mouse hareketi
    entropy += mouse_delta

    # Zaman (nanosecond)
    entropy += time.time_ns()

    # Process ID
    entropy += os.getpid()

    return entropy

def collatz_random(seed, steps=50):
    n = seed

    for _ in range(steps):
        entropy = get_system_entropy()
        random_factor = entropy % 7 + 1

        if n % 2 == 0:
            n = (n // 2) + random_factor
        else:
            n = (3 * n + 1) ^ random_factor  # XOR kaotik etki

        n = abs(n)

    return n

# Başlangıç tohumu
initial_seed = random.randint(1, 10**6)

result = collatz_random(initial_seed)

print("Başlangıç:", initial_seed)
print("Üretilen rastgele sayı:", result)
