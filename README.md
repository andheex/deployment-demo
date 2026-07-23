# deployment-demo

Template project untuk latihan Modul 2 — Persiapan Tools dan Project Reproducible.

Project ini sengaja dibuat sederhana. Tujuannya adalah memeriksa environment,
memahami root folder project, mencatat dependency, dan menulis langkah setup yang
dapat diikuti oleh orang lain.

## Struktur project

```text
deployment-demo/
├── app.py              # Titik masuk aplikasi sederhana
├── requirements.txt    # Dependency project
├── README.md           # Panduan project
├── .gitignore          # File lokal yang tidak perlu dibagikan
├── data/               # Data input atau data contoh
├── models/             # Model artifact dan metadata model
├── src/                # Source code yang digunakan ulang
└── notebooks/          # Eksplorasi dan analisis interaktif
```

Folder `data/`, `models/`, `src/`, dan `notebooks/` masih kosong pada tahap awal.
Folder tersebut akan digunakan dan dikembangkan pada modul-modul berikutnya.

## Prasyarat

- Python 3.10 atau yang lebih baru;
- VS Code atau editor lain;
- terminal atau PowerShell.

Periksa Python dari terminal:

```bash
python --version
```

Pada macOS/Linux, command dapat berupa `python3` jika `python` tidak tersedia.

## Membuat virtual environment

Dari root folder `deployment-demo`:

Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Setelah environment aktif, periksa interpreter yang digunakan:

```bash
python -c "import sys; print(sys.executable)"
```

Hasilnya seharusnya menunjuk ke folder `.venv` milik project ini.

## Memasang dependency

Jalankan dari root folder project:

```bash
python -m pip install -r requirements.txt
```

Untuk saat ini `requirements.txt` belum berisi package aplikasi. Dependency akan
ditambahkan ketika project mulai menggunakan library pada modul berikutnya.

## Menjalankan aplikasi

Dengan virtual environment masih aktif, jalankan:

```bash
python app.py
```

Output akan menampilkan pesan smoke test, lokasi root project, dan interpreter
Python yang sedang digunakan.

## Catatan penting

- Jalankan command dari root folder `deployment-demo`.
- Folder `.venv/` hanya untuk environment lokal dan tidak perlu dibagikan.
- Jangan menyimpan password, token, credential, atau file `.env` ke repository.
- Struktur project ini akan dikembangkan pada modul-modul berikutnya.

## Changes
1. Testing perubahan secara online
