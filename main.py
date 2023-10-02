import random
from tkinter import *

import pseudorandom_sequence_test as ps


def change():
    with open(r"generated_bit", "w") as file:
        for i in range(10000):
            t = random.choice('01')
            file.write(t)

    with open(r"generated_bit", "r") as file:
        status_text.insert(END, f"\n{file.readline()}")
        status_text2.insert(END, f"Добавлено последовательность в битах длиной 10000")

def check():
    with open(r"generated_bit", "r") as file:
        str1 = file.readline()
        bit_list = list(map(int, str1))
        status_text.insert(END, f"\n{str(bit_list)}")
        status_text2.insert(END, f"\nСоздан список битов")

    status_text2.insert(END, f"\nНачинаем проверку")
    pst = ps.PST(bit_list)
    if pst.frequency_test():
        status_text2.insert(END, f"\nfrequency_test = True")

        if pst.sequence_identical_test():
            status_text2.insert(END, f"\nsequence_identical_test = True")
        else:
            status_text2.insert(END, f"\nsequence_identical_test = False")

        if pst.extended_randomness_test():
            status_text2.insert(END, f"\nextended_randomness_test = True")
        else:
            status_text2.insert(END, f"\nextended_randomness_test = False")

    else:
        status_text2.insert(END, f"\nfrequency_test = True")


root = Tk()
root.title("lab1")
root.geometry("900x600")

status_text = Text(root, width=120, height=20, bg='grey')
status_text.pack()
status_text2 = Text(root, width=120, height=5,)
status_text2.pack()

btn = Button(text="generate bit", command=change)
btn.pack()

btn2 = Button(text="check bits", command=check)
btn2.pack()
root.mainloop()
