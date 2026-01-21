# F1 Lap Comparison – Ghost Lap Animation

Analyze and visualize **Formula 1 drivers’ lap performances** across seasons with a ghost lap animation. This project lets you compare a driver’s lap from one year against another on the same track, showing where time is gained or lost in each sector.  

---

## Table of Contents

- [Overview](#overview)  
- [Features](#features)  
- [Project Structure](#project-structure)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Dependencies](#dependencies)  
- [Example Output](#example-output)  
- [Customization](#customization)  
- [Acknowledgements](#acknowledgements)  

---

## Overview

The **F1 Lap Comparison Project** leverages the [FastF1](https://github.com/theOehrly/Fast-F1) library to load F1 telemetry data and produce a side-by-side ghost lap comparison between two years. It is designed for F1 enthusiasts, data analysts, and anyone curious about lap-by-lap performance differences.  

Key highlights include:  
- Telemetry-based lap analysis  
- Sector-wise time comparison  
- Animated ghost lap visualization on the track  
- Speed vs. distance plotting  

---

## Features

- Load and process **fastest laps** for any driver, track, and session.  
- **Normalize lap distance** for consistent comparison.  
- Split a lap into **three sectors** and compute sector deltas.  
- Visualize **ghost laps** side-by-side with moving markers.  
- Display **sector time differences** in real-time during animation.  
- Export the animation as an **MP4 video**.  

---

## Project Structure

The repository is organized as follows:

F1-Lap-Comparison/
│
├─ config.py           # Project configuration (driver, track, session, years)
├─ load_data.py        # Functions to load fastest lap telemetry using FastF1
├─ preprocess.py       # Functions to normalize telemetry distances
├─ analysis.py         # Compute sectors and sector-wise lap times
├─ visualization.py    # Ghost lap animation and speed plotting
├─ style.py            # Color scheme and styling for plots
└─ main.py             # Entry point to run the full comparison workflow

---

## Installation

1. Clone this repository:

```bash
git clone https://github.com/your-username/f1-lap-comparison.git
cd f1-lap-comparison

	2.	Create and activate a virtual environment (recommended):

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

	3.	Install dependencies:

pip install -r requirements.txt

⚠️ Make sure you have ffmpeg installed on your system for exporting MP4 animations.

⸻

Usage
	1.	Update config.py with your preferred driver, track, session, and years:

YEAR_1 = 2019
YEAR_2 = 2025
DRIVER = "NOR"
TRACK = "Spa-Francorchamps"
SESSION = "Q"  # Q = Qualifying, R = Race, FP1/FP2/FP3 = Practice

	2.	Run the main script:

python main.py

	3.	The script will:
	•	Load telemetry for both years
	•	Normalize distance and compute sector times
	•	Generate a ghost lap animation
	•	Export the animation as ghost_lap_comparison.mp4

⸻

Dependencies
	•	Python 3.9+
	•	FastF1￼ – F1 telemetry library
	•	NumPy
	•	Matplotlib
	•	FFmpeg (for animation export)

Install all Python dependencies with:

pip install fastf1 numpy matplotlib


⸻

Example Output
	•	Animated ghost lap of Lando Norris comparing 2019 vs 2025 on Spa-Francorchamps
	•	Speed vs Distance graph with moving cursor
	•	Sector-wise delta displayed in real-time

⚠️ The cache folder data/cache will store session data to speed up repeated runs.

⸻

Customization
	•	Change the driver, track, session, or years in config.py.
	•	Adjust plot styling and colors in style.py.
	•	Modify sector split logic in analysis.py for more than 3 sectors.
	•	Enable dark mode by uncommenting the line in visualization.py:

# plt.style.use("dark_background")


⸻

Acknowledgements
	•	FastF1 Library￼ – Telemetry data source
	•	Formula 1 community for telemetry and data insights
	•	Inspiration from ghost lap animations in F1 broadcasts

---

✅ This is **fully continuous Markdown**, with no extra explanatory text outside the Markdown. You can **copy-paste this directly into `README.md`**, and it will render perfectly on GitHub.  

If you want, I can **also create a version with GitHub badges and a demo GIF/video section** to make your repo look professional and interactive.  

Do you want me to do that next?
