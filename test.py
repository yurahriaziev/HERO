import customtkinter as ctk

window = ctk.CTk()
window.geometry('400x800')

frame = ctk.CTkScrollableFrame(window)
frame.pack(pady=40)

for i in range(20):
    ctk.CTkButton(frame, text='Test').pack(pady=10)

window.mainloop()