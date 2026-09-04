# Fridha Septiana_Algoritma_Pemograman
Tugas Algoritma Pemograman

## Menghitung Sisi Miring Segitiga Siku-Siku

## Deskripsi Masalah

Program ini dibuat untuk menghitung panjang sisi miring (hipotenusa) pada sebuah segitiga siku-siku berdasarkan panjang sisi alas dan sisi tinggi yang diberikan oleh pengguna.

Perhitungan menggunakan **Teorema Pythagoras** dengan rumus:

**c = √(a² + b²)**

Keterangan:

* **a** = panjang sisi alas
* **b** = panjang sisi tinggi
* **c** = panjang sisi miring

Pengguna memasukkan nilai panjang sisi alas dan sisi tinggi. Selanjutnya, program menghitung sisi miring menggunakan rumus Teorema Pythagoras dan menampilkan hasilnya dalam satuan sentimeter (cm).

### Contoh

Jika sisi alas memiliki panjang **3 cm** dan sisi tinggi **4 cm**, maka:

**c = √(3² + 4²)**
**c = √25**
**c = 5 cm**

Dengan demikian, panjang sisi miring segitiga tersebut adalah **5 cm**.

## Identifikasi Input – Proses – Output

| Komponen   | Keterangan                                                                                   |
| ---------- | -------------------------------------------------------------------------------------------- |
| **Input**  | Panjang sisi alas (`a`) dan panjang sisi tinggi (`b`) segitiga siku-siku.                    |
| **Proses** | Menghitung panjang sisi miring (`c`) menggunakan rumus Teorema Pythagoras: `c = √(a² + b²)`. |
| **Output** | Menampilkan panjang sisi miring (`c`) dalam satuan sentimeter (cm).                          |

### Alur IPO

**Input:**
Pengguna memasukkan nilai panjang sisi alas (`a`) dan sisi tinggi (`b`).

⬇️

**Proses:**
Program menghitung sisi miring menggunakan rumus:

`c = √(a² + b²)`

⬇️

**Output:**
Program menampilkan hasil panjang sisi miring (`c`) dalam satuan cm.

## Pseudocode

```text
ALGORITMA Menghitung Sisi Miring Segitiga Siku-Siku

DEKLARASI
    a, b, c : real

DESKRIPSI
    MULAI

    INPUT a
    INPUT b

    c ← √(a² + b²)

    OUTPUT "Panjang sisi miring adalah: ", c, " cm"

    SELESAI
```

### Penjelasan

1. Program dimulai.
2. Pengguna memasukkan panjang sisi alas (`a`).
3. Pengguna memasukkan panjang sisi tinggi (`b`).
4. Program menghitung sisi miring (`c`) menggunakan Teorema Pythagoras.
5. Program menampilkan hasil panjang sisi miring dalam satuan cm.
6. Program selesai.

## Flowchart

```mermaid
flowchart TD
    A([MULAI]) --> B[/Masukkan panjang sisi alas a/]
    B --> C[/Masukkan panjang sisi tinggi b/]
    C --> D[c = √(a² + b²)]
    D --> E[/Tampilkan panjang sisi miring c/]
    E --> F([SELESAI])
```

### Keterangan Flowchart

1. **Mulai** → Program dijalankan.
2. **Input sisi alas (`a`)** → Pengguna memasukkan panjang sisi alas.
3. **Input sisi tinggi (`b`)** → Pengguna memasukkan panjang sisi tinggi.
4. **Proses** → Program menghitung sisi miring dengan rumus `c = √(a² + b²)`.
5. **Output** → Program menampilkan hasil panjang sisi miring.
6. **Selesai** → Program berakhir.

## Test Case

Pengujian dilakukan menggunakan beberapa nilai sisi alas dan sisi tinggi untuk memastikan program dapat menghitung panjang sisi miring dengan benar.

| No. | Input Sisi Alas (a) | Input Sisi Tinggi (b) | Hasil yang Diharapkan |
| --- | ------------------: | --------------------: | --------------------: |
| 1   |                3 cm |                  4 cm |               5.00 cm |
| 2   |                5 cm |                 12 cm |              13.00 cm |

### Perhitungan Test Case

**Test Case 1:**

`c = √(3² + 4²) = √25 = 5 cm`

**Test Case 2:**

`c = √(5² + 12²) = √169 = 13 cm`

---

## Implementasi Python

Program diimplementasikan menggunakan bahasa pemrograman **Python** dan dapat dijalankan melalui **Visual Studio Code (VS Code)**.

File program:

`pythagoras.py`

```python
import math

print("=== Program Menghitung Sisi Miring Segitiga Siku-Siku ===")

a = float(input("Masukkan panjang sisi alas (a): "))
b = float(input("Masukkan panjang sisi tinggi (b): "))

c = math.sqrt(a**2 + b**2)

print(f"Panjang sisi miring adalah: {c:.2f} cm")
```

### Penjelasan Singkat

* `import math` digunakan untuk menggunakan fungsi matematika `sqrt()`.
* `a` digunakan untuk menyimpan panjang sisi alas.
* `b` digunakan untuk menyimpan panjang sisi tinggi.
* `math.sqrt(a**2 + b**2)` digunakan untuk menghitung sisi miring berdasarkan Teorema Pythagoras.
* `print()` digunakan untuk menampilkan hasil perhitungan.

---

## Contoh Hasil Program

### Test Case 1

```text
=== Program Menghitung Sisi Miring Segitiga Siku-Siku ===
Masukkan panjang sisi alas (a): 3
Masukkan panjang sisi tinggi (b): 4
Panjang sisi miring adalah: 5.00 cm
```

### Test Case 2

```text
=== Program Menghitung Sisi Miring Segitiga Siku-Siku ===
Masukkan panjang sisi alas (a): 5
Masukkan panjang sisi tinggi (b): 12
Panjang sisi miring adalah: 13.00 cm
```

### Kesimpulan Pengujian

Berdasarkan hasil pengujian, program berhasil menghitung panjang sisi miring segitiga siku-siku sesuai dengan rumus **Teorema Pythagoras**. Seluruh hasil program sesuai dengan hasil yang diharapkan pada setiap test case.
