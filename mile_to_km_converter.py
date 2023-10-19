from tkinter import *


def calculate_result():
    user_input = entry.get()
    final_result = float(user_input) * 1.6
    kilometer_result.config(text=f"{final_result}")

window = Tk()
window.title("Mile to kilometer converter")
window.config(padx=20, pady=20)

entry = Entry(width=10)
entry.grid(column=1, row=0)

miles =Label(text="miles")
miles.grid(column=2, row=0)

equal_to_lable = Label(text="is equal to")
equal_to_lable.grid(column=0, row=1)


kilometer_result = Label(text="0")
kilometer_result.grid(column=1, row=1)

kilometer = Label(text="km")
kilometer.grid(column=2, row=1)

calculate_button = Button(text="calculate", command=calculate_result)
calculate_button.grid(column=1, row=2)


window.mainloop()