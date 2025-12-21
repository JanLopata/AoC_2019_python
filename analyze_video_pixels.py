import os

import cv2
import matplotlib.pyplot as plt
import numpy as np

# === KONFIGURACE ===
VIDEO_PATH = os.path.expanduser('~/Stažené/Blyštivá.mp4')

# Možnost 1: Předem definované souřadnice pixelů (x, y)
PIXELS =[(160, 116), (358, 123), (732, 164), (83, 324), (684, 360), (961, 368), (946, 605), (231, 1206)]

# === FUNKCE PRO INTERAKTIVNÍ VÝBĚR ===
def select_pixels_interactive(video_path, num_pixels=8):
    """Umožní kliknout na video a vybrat pixely"""
    cap = cv2.VideoCapture(video_path)
    ret, frame = cap.read()
    cap.release()

    if not ret:
        print("Nelze načíst video!")
        return None

    pixels = []

    def mouse_callback(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN and len(pixels) < num_pixels:
            pixels.append((x, y))
            cv2.circle(frame, (x, y), 5, (0, 255, 0), -1)
            cv2.putText(frame, str(len(pixels)), (x+10, y),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            cv2.imshow('Vyber pixely', frame)

    cv2.imshow('Vyber pixely', frame)
    cv2.setMouseCallback('Vyber pixely', mouse_callback)

    print(f"Klikni na {num_pixels} pixelů, které chceš sledovat...")
    print("Stiskni ENTER po dokončení výběru")

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return pixels

# === HLAVNÍ ANALÝZA ===
def analyze_pixels(video_path, pixels):
    """Analyzuje jas vybraných pixelů v čase"""
    cap = cv2.VideoCapture(video_path)

    # Zjištění FPS pro časovou osu
    fps = cap.get(cv2.CAP_PROP_FPS)

    # Příprava datových struktur
    data = {i: [] for i in range(len(pixels))}
    frame_numbers = []

    frame_idx = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Převod na grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Záznam hodnot pro každý pixel
        for i, (x, y) in enumerate(pixels):
            brightness = gray[y, x]  # Pozor: indexování je [y, x]
            data[i].append(brightness)

        frame_numbers.append(frame_idx)
        frame_idx += 1

        # Progress
        if frame_idx % 100 == 0:
            print(f"Zpracováno {frame_idx} snímků...")

    cap.release()

    # Převod na časovou osu v sekundách
    time_seconds = np.array(frame_numbers) / fps

    return data, time_seconds, frame_numbers

# === VIZUALIZACE ===
def plot_results(data, time_axis, pixels, use_time=True):
    """Vykreslí časové řady"""
    plt.figure(figsize=(12, 8))

    for i, (x, y) in enumerate(pixels):
        plt.plot(time_axis, data[i], label=f'Pixel {i+1} ({x},{y})', alpha=0.7)

    plt.xlabel('Čas [s]' if use_time else 'Číslo snímku')
    plt.ylabel('Jas (0-255)')
    plt.title('Časové řady jasu vybraných pixelů')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

# === EXPORT DO CSV ===
def export_to_csv(data, time_seconds, frame_numbers, pixels, filename='brightness_data.csv'):
    """Exportuje data do CSV"""
    import csv

    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)

        # Hlavička
        header = ['frame', 'time_s']
        for i, (x, y) in enumerate(pixels):
            header.append(f'pixel_{i+1}_({x},{y})')
        writer.writerow(header)

        # Data
        for idx in range(len(frame_numbers)):
            row = [frame_numbers[idx], time_seconds[idx]]
            for i in range(len(pixels)):
                row.append(data[i][idx])
            writer.writerow(row)

    print(f"Data exportována do {filename}")

# === SPUŠTĚNÍ ===
if __name__ == "__main__":
    # Vyber metodu výběru pixelů:

    # Možnost A: Použít předem definované souřadnice
    # pixels_to_track = PIXELS

    # Možnost B: Interaktivní výběr (odkomentuj následující řádek)
    pixels_to_track = select_pixels_interactive(VIDEO_PATH, num_pixels=8)

    if pixels_to_track:
        print(f"Sledované pixely: {pixels_to_track}")

        # Analýza
        data, time_s, frames = analyze_pixels(VIDEO_PATH, pixels_to_track)

        # Vizualizace
        plot_results(data, time_s, pixels_to_track, use_time=True)

        # Export
        export_to_csv(data, time_s, frames, pixels_to_track)
