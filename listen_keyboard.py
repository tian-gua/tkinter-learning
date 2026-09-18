import tkinter as tk  # 导入 Tkinter 图形界面库，并将其简写为 tk

from pynput import keyboard  # 导入 pynput 库的 keyboard 模块，用于监听键盘事件

window = tk.Tk()  # 创建一个 Tkinter 主窗口
window.title("Simple Window")  # 设置窗口标题
window.geometry("400x300")  # 设置窗口大小为宽 400 像素、高 300 像素
window.resizable(False, False)  # 禁止用户调整窗口的宽度和高度

window.grid_columnconfigure(0, weight=1)
window.grid_rowconfigure(0, weight=1)

# 外层窗口负责把整个表单居中，表单内部的行保持自适应高度
form_frame = tk.Frame(window)
form_frame.grid(row=0, column=0)

option_1_var = tk.BooleanVar(value=False)
option_2_var = tk.BooleanVar(value=False)


def on_check_box_change(option_name, variable):
    print(f"{option_name}: {'选中' if variable.get() else '未选中'}")


check_box = tk.Checkbutton(
    form_frame,
    text="option 1",
    variable=option_1_var,
    command=lambda: on_check_box_change("option 1", option_1_var),
)  # 创建一个复选框
check_box.grid(row=0, column=0, padx=5, pady=5)  # 使用 grid 布局管理器将复选框放入窗口

check_box = tk.Checkbutton(
    form_frame,
    text="option 2",
    variable=option_2_var,
    command=lambda: on_check_box_change("option 2", option_2_var),
)  # 创建一个复选框
check_box.grid(row=0, column=1, padx=5, pady=5)  # 使用 grid 布局管理器将复选框放入窗口


# 监听键盘 F8
def on_f8_press(event):
    print("F8 pressed")
    option_1_var.set(not option_1_var.get())  # 切换复选框的选中状态


# 只绑定当前窗口的 F8 键事件
# window.bind("<F8>", on_f8_press)
# 绑定所有窗口的 F8 键事件
window.bind_all("<F8>", on_f8_press)


# 监听键盘 F8（用于切换 option 2 的选中状态）
# 程序后台运行也能监听
def on_f8_press(key):
    if key == keyboard.Key.f8:
        window.after(0, lambda: option_2_var.set(not option_2_var.get()))


keyboard_listener = keyboard.Listener(on_press=on_f8_press)
keyboard_listener.start()


def on_close():
    print("Window closed")
    window.destroy()


window.protocol("WM_DELETE_WINDOW", on_close)  # 设置窗口关闭事件的回调函数


window.mainloop()  # 启动窗口的事件循环，让窗口保持运行并响应操作
