import tkinter as tk
from tkinter import messagebox

def calculate_emrt():
    try:
        cache_hit_prob = float(cache_hit_prob_entry.get())
        cache_access_time = float(cache_access_time_entry.get())
        mem_ref_time = float(mem_ref_time_entry.get())

        emrt = (cache_hit_prob * cache_access_time) + ((1 - cache_hit_prob) * mem_ref_time)

        emrt_label.config(text=f"Effective Memory Reference Time: {emrt} ns")
    except:
        messagebox.showerror("Error", "Invalid input. Please enter valid numbers.")

root = tk.Tk()
root.title("Effective Memory Reference Time Calculator")

cache_hit_prob_label = tk.Label(root, text="Cache Hit Probability (0-1):")
cache_hit_prob_entry = tk.Entry(root)

cache_access_time_label = tk.Label(root, text="Cache Access Time (ns):")
cache_access_time_entry = tk.Entry(root)

mem_ref_time_label = tk.Label(root, text="Memory Reference Time (ns):")
mem_ref_time_entry = tk.Entry(root)

emrt_label = tk.Label(root, text="")

calculate_button = tk.Button(root, text="Calculate", command=calculate_emrt)

cache_hit_prob_label.pack()
cache_hit_prob_entry.pack()
cache_access_time_label.pack()
cache_access_time_entry.pack()
mem_ref_time_label.pack()
mem_ref_time_entry.pack()
calculate_button.pack()
emrt_label.pack()

root.mainloop()
