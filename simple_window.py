import tkinter as tk  # 导入 Tkinter 图形界面库，并将其简写为 tk

window = tk.Tk()  # 创建一个 Tkinter 主窗口
window.title("Simple Window")  # 设置窗口标题
window.geometry("400x300")  # 设置窗口大小为宽 400 像素、高 300 像素
window.resizable(False, False)  # 禁止用户调整窗口的宽度和高度

user_name_label = tk.Label(window, text="Username:")  # 创建一个标签用于显示“Username:”
user_name_label.pack()  # 使用 pack 布局管理器将标签放入窗口

user_name_input = tk.Entry(window)  # 创建一个文本输入框
user_name_input.pack()  # 使用 pack 布局管理器将文本输入框放入窗口

password_label = tk.Label(window, text="Password:")  # 创建一个标签用于显示“Password:”
password_label.pack()  # 使用 pack 布局管理器将标签放入窗口

password_input = tk.Entry(
    window, show="*"
)  # 创建一个文本输入框，用于输入密码，输入内容以星号显示
password_input.pack()  # 使用 pack 布局管理器将文本输入框放入窗口

btn = tk.Button(
    window, text="Login", command=lambda: print("Button clicked")
)  # 创建一个点击后输出提示的按钮
window.widget = btn  # 将按钮保存到窗口对象的 widget 属性中
window.widget.pack()  # 使用 pack 布局管理器将按钮放入窗口


def on_close():
    print("Window closed")
    window.destroy()


window.protocol("WM_DELETE_WINDOW", on_close)  # 设置窗口关闭事件的回调函数


window.mainloop()  # 启动窗口的事件循环，让窗口保持运行并响应操作
