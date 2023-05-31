import os
import tkinter as tk

# Get the absolute path to the directory where the main Python file is located
dir_path = os.path.abspath(os.path.join(os.path.expanduser("~"), "Desktop", "Security_Project"))

# Define the function to execute the first Python file
def execute_file1():
    os.system(f'python "{os.path.join(dir_path, "currency_converter.py")}"')

# Define the function to execute the second Python file
def execute_file2():
    os.system(f'python "{os.path.join(dir_path, "rate.py")}"')

# Define the function to execute the third Python file
def execute_file3():
    os.system(f'python "{os.path.join(dir_path, "yearly_rate.py")}"')

# Create the window and the buttons
window = tk.Tk()
window.title("Web Scraping Project")
button1 = tk.Button(window, text="Currency Converter", command=execute_file1,height=1, width=20)
button1.grid(row=0,column=0,pady=10,padx=10)
button2 = tk.Button(window, text="Currency Rate", command=execute_file2,height=1, width=20)
button2.grid(row=1,column=0,pady=10,padx=10)
button3 = tk.Button(window, text="Yearly Rate", command=execute_file3,height=1, width=20)
button3.grid(row=2,column=0,pady=10,padx=10)

# Start the main loop of the window
window.mainloop()