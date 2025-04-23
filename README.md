# nazca-gds-tutorial
Photonic IC design tutorials using Nazca Design

# 📐 Bend Waveguide Generator with Nazca Design

This repository contains a complete set of Python scripts to generate a **bent waveguide layout** using [Nazca Design](https://nazca-design.org/) and export it as a GDS file.

---

## 🧠 Overview

The layout includes:
- Tapered input and output waveguides
- A pair of 90° bends
- Customizable parameters such as waveguide width, taper length, and bend radius

---

## 🧩 File Structure

| File | Description |
|------|-------------|
| `Bend_waveguide_functions1.py` | Defines the `bend_waveguide1()` function that builds the layout. |
| `Bend_waveguide_main.py` | Main script: sets parameters, calls the function, and exports a GDS file. |
| `layers.py` | Registers the photonic layers used in the layout. |

---

## 🔧 How to Run

1. Install [Nazca Design](https://nazca-design.org/):
   ```bash
   pip install nazca

2.Clone this repository and run the main script:

python Bend_waveguide_main.py

A GDS file named Bend_waveguide1.gds will be generated in the same directory.
