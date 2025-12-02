# Spring Force Problem Solver

A GUI application to solve Problem 2/30 from mechanics - calculating spring force components.

## Installation

Make sure you have `image.png` in the same directory (problem diagram)

## Usage

Run the application:
```bash
python spring_force_solver.py
```

Enter the values:
- **r**: Unextended spring length (mm)
- **k**: Spring constant (kN/m)  
- **θ**: Angle (0-90 degrees)

Click **Calculate Force** to get the results.

## Output

The solver calculates:
- **Fx**: x-component of spring force (N)
- **Fy**: y-component of spring force (N)
- **Force Magnitude**: Total spring force (N)
- **Direction**: Angle from horizontal (degrees)

## Requirements

- Python 3.7+
- Pillow (for image handling)
- Tkinter (usually comes with Python)
