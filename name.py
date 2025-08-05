import tkinter as tk

#Creat the main window
root = tk.Tk()
root.title("My Tkinter App")
root.geometry("1100x600")  # Set the window size
# Run the application
frame1 = tk.Frame(root,height=100,width=1100,bg="black")
frame1.grid(row=0,column=0)
frame2 = tk.Frame(root,height=100,width=300,bg="red")
frame2.grid(row=1,column=0)
root.resizable(False,False)
canvas =tk.Canvas(frame2,height=600,width=1100,bg="white")
canvas.grid(row=0,column=0)

prevpoint=[0,0]
currentpoint=[0,0]
def paint(event):
    print(event.type)
    global prevpoint
    global currentpoint
    x=event.x
    y=event.y
    currentpoint=[x,y]

    if prevpoint !=[0,0]:
        canvas.create_line(prevpoint[0],prevpoint[1],currentpoint[0],currentpoint[1])
    prevpoint=currentpoint
    if event.type== "5":
        prevpoint=[0,0]

canvas.bind("<B1-Motion>",paint)
canvas.bind("<ButtonRelease-1>",paint)
root.mainloop()
