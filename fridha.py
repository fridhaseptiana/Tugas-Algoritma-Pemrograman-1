import math

print("=== Program Menghitung Sisi Miring Segitiga Siku-Siku ===")

a = float(input("Masukkan panjang sisi alas (a): "))
b = float(input("Masukkan panjang sisi tinggi (b): "))

c = math.sqrt(a**2 + b**2)

print(f"Panjang sisi miring adalah: {c:.2f} cm")