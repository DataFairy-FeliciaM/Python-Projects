import tkinter as tk

# creating a function that respond when clicked
def calculate_average():
    try:
        # test results + convert to float
        result1_score = float(result1_entry.get())
        result2_score = float(result2_entry.get())
        result3_score = float(result3_entry.get())

        # Calculate the average
        average = (result1_score + result2_score + result3_score) / 3

        # show average results
        result_label.config(text=f"Your Average Score is: {average:.2f}")
    except ValueError:
        result_label.config(text="Invalid input. This is not correct! Try again.")

# declaring function for the quit button
def quit_app():
    root.quit()

# Create the main window
root = tk.Tk()
root.title("Students Average Test Calculator")

# inputting the test results
result1_label = tk.Label(root, text="Enter the score for test 1:")
result2_label = tk.Label(root, text="Enter the score for test 2:")
result3_label = tk.Label(root, text="Enter the score for test 3:")


result1_entry = tk.Entry(root, width=10)
result2_entry = tk.Entry(root, width=10)
result3_entry = tk.Entry(root, width=10)

# the average button
calculate_button = tk.Button(root, text="Average", command=calculate_average)

# The quit button
quit_button = tk.Button(root, text="Quit", command=quit_app)

# label for displaying results
result_label = tk.Label(root, text="", font=("Arial", 12))


# Arrange the grid
result1_label.grid(row=0, column=0, padx=10, pady=5)
result1_entry.grid(row=0, column=1, padx=10, pady=5)
result2_label.grid(row=1, column=0, padx=10, pady=5)
result2_entry.grid(row=1, column=1, padx=10, pady=5)
result3_label.grid(row=2, column=0, padx=10, pady=5)
result3_entry.grid(row=2, column=1, padx=10, pady=5)
calculate_button.grid(row=3, column=0, padx=10, pady=10)
quit_button.grid(row=3, column=1, padx=10, pady=10)
result_label.grid(row=4, column=0, columnspan=2)

#Tkinter main loop
root.mainloop()

