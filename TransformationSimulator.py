import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Function for transformation types
def translate(points, Tx, Ty):
    T = np.array([[1, 0, Tx], [0, 1, Ty], [0, 0, 1]])
    points = np.hstack([points, np.ones((points.shape[0], 1))])
    transformed_points = np.dot(T, points.T).T
    return transformed_points[:, :2]

def euclidean_transform(points, theta, Tx, Ty):
    theta = np.deg2rad(theta)
    E = np.array([[np.cos(theta), -np.sin(theta), Tx], [np.sin(theta), np.cos(theta), Ty], [0, 0, 1]])
    points = np.hstack([points, np.ones((points.shape[0], 1))])
    transformed_points = np.dot(E, points.T).T
    return transformed_points[:, :2]

def similarity_transform(points, scale, theta, Tx, Ty):
    theta = np.deg2rad(theta)
    S = np.array([[scale * np.cos(theta), -scale * np.sin(theta), Tx],
                  [scale * np.sin(theta), scale * np.cos(theta), Ty], [0, 0, 1]])
    points = np.hstack([points, np.ones((points.shape[0], 1))])
    transformed_points = np.dot(S, points.T).T
    return transformed_points[:, :2]

def affine_transform(points, a, b, c, d, e, f):
    A = np.array([[a, b, e], [c, d, f], [0, 0, 1]])
    points = np.hstack([points, np.ones((points.shape[0], 1))])
    transformed_points = np.dot(A, points.T).T
    return transformed_points[:, :2]

def projective_transform(points, a, b, c, d, e, f, g, h):
    P = np.array([[a, b, c], [d, e, f], [g, h, 1]])
    points = np.hstack([points, np.ones((points.shape[0], 1))])
    transformed_points = np.dot(P, points.T).T
    transformed_points = transformed_points[:, :2] / transformed_points[:, 2, np.newaxis]
    return transformed_points

# Function to handle the Transform button click event
def on_transform_click():
    # Get geometry type
    geometry_type = geometry_dropdown.get()
    if geometry_type == 'Point':
        points = np.array([[1, 1]])
    elif geometry_type == 'Line':
        points = np.array([[0, 0], [1, 1]])
    elif geometry_type == 'Polygon':
        points = np.array([[0, 0], [1, 0], [1, 1], [0, 1], [0, 0]])

    # Get transformation type
    transformation_type = transformation_dropdown.get()
    params = [float(param1_entry.get()), float(param2_entry.get()), float(param3_entry.get()),
              float(param4_entry.get()), float(param5_entry.get()), float(param6_entry.get()),
              float(param7_entry.get()), float(param8_entry.get())]

    if transformation_type == 'Translation':
        Tx, Ty = params[0], params[1]
        transformed_points = translate(points, Tx, Ty)
    elif transformation_type == 'Euclidean':
        theta, Tx, Ty = params[0], params[1], params[2]
        transformed_points = euclidean_transform(points, theta, Tx, Ty)
    elif transformation_type == 'Similarity':
        scale, theta, Tx, Ty = params[0], params[1], params[2], params[3]
        transformed_points = similarity_transform(points, scale, theta, Tx, Ty)
    elif transformation_type == 'Affine':
        a, b, c, d, e, f = params[0], params[1], params[2], params[3], params[4], params[5]
        transformed_points = affine_transform(points, a, b, c, d, e, f)
    elif transformation_type == 'Projective':
        a, b, c, d, e, f, g, h = params[0], params[1], params[2], params[3], params[4], params[5], params[6], params[7]
        transformed_points = projective_transform(points, a, b, c, d, e, f, g, h)

    # Plot original and transformed geometry
    ax.clear()
    ax.plot(points[:, 0], points[:, 1], 'bo-', label='Original')
    ax.plot(transformed_points[:, 0], transformed_points[:, 1], 'ro-', label='Transformed')
    ax.legend()
    canvas.draw()

# Set up the root Tkinter window
root = tk.Tk()
root.title("2D Planar Transformations")

# Set up frames for organizing widgets
frame = ttk.Frame(root)
frame.pack(padx=10, pady=10)

# Dropdown for transformation type
transformation_label = ttk.Label(frame, text="Transformation Type")
transformation_label.grid(row=0, column=0, sticky='w')
transformation_dropdown = ttk.Combobox(frame, values=["Translation", "Euclidean", "Similarity", "Affine", "Projective"])
transformation_dropdown.set("Translation")
transformation_dropdown.grid(row=0, column=1, pady=5)

# Dropdown for geometry type
geometry_label = ttk.Label(frame, text="Geometry Type")
geometry_label.grid(row=1, column=0, sticky='w')
geometry_dropdown = ttk.Combobox(frame, values=["Point", "Line", "Polygon"])
geometry_dropdown.set("Polygon")
geometry_dropdown.grid(row=1, column=1, pady=5)

# Parameter input fields
param_labels = ["param1", "param2", "param3", "param4", "param5", "param6", "param7", "param8"]
param_entries = []
for i, label in enumerate(param_labels):
    ttk.Label(frame, text=label).grid(row=2+i, column=0, sticky='w')
    param_entry = ttk.Entry(frame)
    param_entry.grid(row=2+i, column=1, pady=5)
    param_entries.append(param_entry)

# Store references to parameter entries
param1_entry, param2_entry, param3_entry, param4_entry, param5_entry, param6_entry, param7_entry, param8_entry = param_entries

# Button to apply transformation
transform_button = ttk.Button(frame, text="Transform", command=on_transform_click)
transform_button.grid(row=10, column=0, columnspan=2, pady=10)

# Create a matplotlib figure for plotting
fig, ax = plt.subplots(figsize=(5, 4))
ax.set_title('2D Planar Transformations')
ax.set_xlabel('X')
ax.set_ylabel('Y')

# Add a canvas to embed the plot in the Tkinter window
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(padx=10, pady=10)

# Start the Tkinter event loop
root.mainloop()