#!/usr/bin/env python3

import time
import os
import hashlib
import struct
import random

# -------------------------------
# SENSOR OKUMA FONKSİYONLARI
# -------------------------------

def get_cpu_temp():
    try:
        with open("/sys/class/thermal/thermal_zone0/temp") as f:
            return int(f.read().strip())
    except:
        return random.randint(30000, 80000)

def get_fan_value():
    try:
        with open("/sys/devices/pwm-fan/cur_pwm") as f:
            return int(f.read().strip())
    except:
        return random.randint(0, 255)

def get_cpu_load():
    try:
        return os.getloadavg()[0]
    except:
        return random.random()

def get_mouse_entropy():
    try:
        with open("/dev/input/mice", "rb") as f:
            return f.read(16)
    except:
        return os.urandom(16)

# -------------------------------
# ENTROPY TOPLAMA
# -------------------------------

def collect_entropy():
    pool = bytearray()

    pool += struct.pack("Q", time.time_ns())
    pool += struct.pack("I", os.getpid())
    pool += struct.pack("I", get_cpu_temp())
    pool += struct.pack("I", get_fan_value())
    pool += struct.pack("f", get_cpu_load())
    pool += get_mouse_entropy()
    pool += os.urandom(16)

    return pool

# -------------------------------
# RASTGELE SAYI ÜRETİCİ
# -------------------------------

def generate_random(min_val=0, max_val=1000):
    entropy = collect_entropy()
    digest = hashlib.sha256(entropy).digest()
    number = int.from_bytes(digest, "big")
    return min_val + (number % (max_val - min_val + 1))

# -------------------------------
# TEST / KULLANIM
# -------------------------------

if __name__ == "__main__":
    print("Entropy-based Random Number Generator\n")

    for i in range(5):
        rnd = generate_random(0, 9999)
        print(f"[{i}] Random Number:", rnd)
        time.sleep(0.3)
