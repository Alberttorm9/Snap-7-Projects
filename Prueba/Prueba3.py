import tkinter as tk
def shrink_square():
    global after_id
    x1, y1, x2, y2 = canvas.coords(square)
    if x2 - x1 > 0 and y2 - y1 > 0:
        canvas.coords(square, x1 + 2, y1 + 2, x2 - 2, y2 - 2)
        after_id = root.after(100, shrink_square)
    if x2 - x1 < 3 and y2 - y1 < 3:
        canvas.pack_forget()
        root.after_cancel(after_id)
    


root = tk.Tk()
canvas = tk.Canvas(root, width=600, height=300)
canvas.pack()

square = canvas.create_rectangle(100, 100, 200, 200, fill="blue")
after_id = 0
shrink_square()
root.mainloop()