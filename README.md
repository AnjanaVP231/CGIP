# Computer Graphics and Image Processing (CGIP)

This folder contains Python implementations of basic **Computer Graphics algorithms** using **Matplotlib**.

## Programs

| No. | Program                              | File                 |
| --- | ------------------------------------ | -------------------- |
| 1   | DDA Line Drawing Algorithm           | `dda.py`             |
| 2   | Bresenham's Line Drawing Algorithm   | `bresenham.py`       |
| 3   | Midpoint Circle Generation Algorithm | `midpoint_circle.py` |

## Requirements

* Python 3.x
* Matplotlib

Install Pygame using:

```bash
pip install Matplotlib
```

## Algorithms Covered

### 1. DDA Line Drawing Algorithm

The Digital Differential Analyzer (DDA) algorithm draws a line by calculating intermediate points between two given endpoints using incremental values of `x` and `y`.

### 2. Bresenham's Line Drawing Algorithm

Bresenham's algorithm draws a line using an integer-based decision parameter to determine the next pixel. It is more efficient than DDA because it avoids floating-point calculations.

### 3. Midpoint Circle Generation Algorithm

The Midpoint Circle algorithm generates a circle using a decision parameter and exploits the **eight-way symmetry** of a circle to calculate its pixels efficiently.

## Technologies Used

* **Python**
* **Matplotlib**

## Purpose

These programs are implemented as part of the **Computer Graphics and Image Processing (CGIP)** laboratory exercises.
