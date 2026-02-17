import tkinter as tk
from tkinter import messagebox


def show_hello():
    messagebox.showinfo("提示", "Hello World!")


def main():
    root = tk.Tk()
    root.title("测试页面4")
    root.geometry("300x200")
    root.resizable(False, False)

    label = tk.Label(root, text="测试页面", font=("Arial", 18))
    label.pack(pady=30)

    button = tk.Button(
        root,
        text="点击我",
        font=("Arial", 14),
        width=15,
        height=2,
        command=show_hello
    )
    button.pack(pady=20)

    root.mainloop()


if __name__ == "__main__":
    main()
