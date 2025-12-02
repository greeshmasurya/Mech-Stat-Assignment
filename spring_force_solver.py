import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import math

class SpringForceSolver:
    def __init__(self, root):
        self.root = root
        self.root.title("Spring Force Problem Solver - Problem 2/30")
        self.root.geometry("1000x750")
        self.root.configure(bg='#000000')
        
        main = ttk.Frame(root)
        main.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        s = ttk.Style()
        s.theme_use('clam')
        s.configure('TFrame', background='#000000')
        s.configure('TLabel', background='#000000', foreground='#00F5FF', font=("Arial", 10))
        s.configure('TLabelframe', background='#000000', foreground='#FF006E')
        s.configure('TLabelframe.Label', background='#000000', foreground='#FF006E', font=("Arial", 10, "bold"))
        s.configure('TButton', background='#BC13FE', foreground='#FFFF00')
        s.map('TButton', 
              background=[('active', '#39FF14')],
              foreground=[('active', '#000000')])
        s.configure('TEntry', fieldbackground='#1a1a1a', foreground='#39FF14', insertcolor='#39FF14')
        s.map('TEntry',
              fieldbackground=[('focus', '#1a1a1a')],
              foreground=[('focus', '#00F5FF')])
        
        title = ttk.Label(main, text="Spring Force Problem Solver", 
                         font=("Arial", 16, "bold"))
        title.pack(pady=10)
        
        left = ttk.Frame(main)
        left.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)
        
        right = ttk.Frame(main)
        right.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5)
        
        lbl = ttk.Label(left, text="Problem Description:", 
                       font=("Arial", 12, "bold"))
        lbl.pack(anchor=tk.W, pady=5)
        
        prob_txt = """Problem 2/30: 
The unextended length of the spring is r. When pin P is at an arbitrary position θ, 
determine the x- and y-components of the force which the spring exerts on the pin.

Note: The force in a spring is given by F = kδ, where δ is the extension from the 
unextended length.

Given Parameters:
• Unextended spring length: r
• Spring constant: k
• Angle: θ
• Pin position: (x, y)

Find:
• Fx: x-component of spring force
• Fy: y-component of spring force"""
        
        self.prob_desc = tk.Text(left, height=16, width=45, wrap=tk.WORD, 
                                bg='#1a1a1a', fg='#00F5FF', relief=tk.SUNKEN, 
                                insertbackground='#39FF14', font=("Courier", 9))
        self.prob_desc.insert(1.0, prob_txt)
        self.prob_desc.config(state=tk.DISABLED)
        self.prob_desc.pack(fill=tk.BOTH, expand=True, pady=5)
        
        try:
            img_frame = ttk.LabelFrame(left, text="Problem Diagram", padding=5)
            img_frame.pack(fill=tk.BOTH, expand=True, pady=5)
            
            img = Image.open('image.png')
            img.thumbnail((380, 300), Image.Resampling.LANCZOS)
            self.photo = ImageTk.PhotoImage(img)
            img_lbl = ttk.Label(img_frame, image=self.photo)
            img_lbl.pack()
        except Exception as e:
            err_lbl = ttk.Label(img_frame, text=f"[Problem diagram]\n{str(e)}", 
                               font=("Arial", 10), foreground="#39FF14")
            err_lbl.pack(pady=20)
        
        inp_lbl = ttk.Label(right, text="Input Parameters:", 
                           font=("Arial", 12, "bold"))
        inp_lbl.pack(anchor=tk.W, pady=5)
        
        inp = ttk.Frame(right)
        inp.pack(fill=tk.X, pady=10)
        
        ttk.Label(inp, text="Unextended Spring Length (r):", 
                 font=("Arial", 10)).grid(row=0, column=0, sticky=tk.W, pady=8)
        self.r_val = tk.StringVar(value="400")
        ttk.Entry(inp, textvariable=self.r_val, width=20).grid(row=0, column=1, padx=5)
        ttk.Label(inp, text="mm", font=("Arial", 9)).grid(row=0, column=2, sticky=tk.W)
        
        ttk.Label(inp, text="Spring Constant (k):", 
                 font=("Arial", 10)).grid(row=1, column=0, sticky=tk.W, pady=8)
        self.k_val = tk.StringVar(value="1.4")
        ttk.Entry(inp, textvariable=self.k_val, width=20).grid(row=1, column=1, padx=5)
        ttk.Label(inp, text="kN/m", font=("Arial", 9)).grid(row=1, column=2, sticky=tk.W)
        
        ttk.Label(inp, text="Angle (θ):", 
                 font=("Arial", 10)).grid(row=2, column=0, sticky=tk.W, pady=8)
        self.theta_val = tk.StringVar(value="40")
        ttk.Entry(inp, textvariable=self.theta_val, width=20).grid(row=2, column=1, padx=5)
        ttk.Label(inp, text="degrees", font=("Arial", 9)).grid(row=2, column=2, sticky=tk.W)
        
        btn_frame = ttk.Frame(right)
        btn_frame.pack(fill=tk.X, pady=15)
        
        calc_btn = ttk.Button(btn_frame, text="Calculate Force", command=self.calculate)
        calc_btn.pack(side=tk.LEFT, padx=5)
        
        clr_btn = ttk.Button(btn_frame, text="Clear", command=self.clear)
        clr_btn.pack(side=tk.LEFT, padx=5)
        
        res_frame = ttk.LabelFrame(right, text="Results:", padding=10)
        res_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        self.res_txt = tk.Text(res_frame, height=20, width=50, wrap=tk.WORD, 
                              bg='#1a1a1a', fg='#39FF14', relief=tk.SUNKEN, 
                              insertbackground='#39FF14', font=("Courier", 9))
        self.res_txt.pack(fill=tk.BOTH, expand=True)
        
        self.show_welcome()
    
    def show_welcome(self):
        welcome = """Welcome to the Spring Force Problem Solver!

Instructions:
1. Enter the unextended spring length (r) in mm
2. Enter the spring constant (k) in kN/m
3. Enter the angle (θ) in degrees
4. Click "Calculate Force"

The program will calculate the x and y 
components of the spring force.

Example values are pre-filled based on Problem 2/30.
Click "Calculate Force" to get started!"""
        
        self.res_txt.config(state=tk.NORMAL)
        self.res_txt.delete(1.0, tk.END)
        self.res_txt.insert(1.0, welcome)
        self.res_txt.config(state=tk.DISABLED)
    
    def calculate(self):
        try:
            r = float(self.r_val.get())
            k = float(self.k_val.get())
            theta = float(self.theta_val.get())
            
            if r <= 0 or k <= 0 or theta < 0 or theta > 90:
                messagebox.showerror("Input Error", 
                    "Please enter valid positive values.\nAngle should be between 0 and 90 degrees.")
                return
            
            r_m = r / 1000
            theta_rad = math.radians(theta)
            
            ap = r_m * math.sqrt(5 - 4 * math.cos(theta_rad))
            delta = ap - r_m
            f = k * delta
            
            sin_a = (2 * r_m * math.sin(theta_rad)) / ap
            alpha_plus_10 = math.degrees(math.asin(sin_a))
            alpha = alpha_plus_10 - 10
            alpha_rad = math.radians(alpha)
            
            fx = -f * math.cos(alpha_rad)
            fy = f * math.sin(alpha_rad)
            
            f_n = f * 1000
            fx_n = fx * 1000
            fy_n = fy * 1000
            
            result = f"""FINAL RESULTS
{'='*45}

INPUT:
  r = {r} mm
  k = {k} kN/m
  θ = {theta}°

{'─'*45}
SPRING FORCE COMPONENTS:
{'─'*45}

  Fx = {fx_n:.2f} N
  Fy = {fy_n:.2f} N
  
  Force Magnitude: {f_n:.2f} N
  Direction: {alpha:.2f}° from horizontal

{'='*45}"""
            
            self.res_txt.config(state=tk.NORMAL)
            self.res_txt.delete(1.0, tk.END)
            self.res_txt.insert(1.0, result)
            self.res_txt.config(state=tk.DISABLED)
            
        except ValueError:
            messagebox.showerror("Input Error", 
                "Please enter valid numerical values for all fields.")
        except Exception as e:
            messagebox.showerror("Calculation Error", 
                f"An error occurred during calculation:\n{str(e)}")
    
    def clear(self):
        self.r_val.set("400")
        self.k_val.set("1.4")
        self.theta_val.set("40")
        self.show_welcome()

if __name__ == "__main__":
    root = tk.Tk()
    app = SpringForceSolver(root)
    root.mainloop()
