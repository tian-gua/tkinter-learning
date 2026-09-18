import tkinter as tk  # 导入 Tkinter 图形界面库，并将其简写为 tk

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

check_box2 = tk.Checkbutton(
    form_frame,
    text="option 2",
    variable=option_2_var,
    command=lambda: on_check_box_change("option 2", option_2_var),
)  # 创建一个复选框
check_box2.grid(row=0, column=1, padx=5, pady=5)  # 使用 grid 布局管理器将复选框放入窗口


def on_close():
    print("Window closed")
    window.destroy()


window.protocol("WM_DELETE_WINDOW", on_close)  # 设置窗口关闭事件的回调函数


window.mainloop()  # 启动窗口的事件循环，让窗口保持运行并响应操作
