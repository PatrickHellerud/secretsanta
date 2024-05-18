import random
from tkinter import *
from tkinter import ttk


count = 0

def choose_pairs(lst):
    results = {}
    receive_arr = lst.copy()

    for person in lst:
        # hvis siste bare har seg selv igjen å trekke så kjører vi på nytt rekursivt
        if receive_arr == [person]:
            return choose_pairs(lst)
        pick = receive_arr.pop(random.randrange(len(receive_arr)))
        # while pick ikke er seg selv
        if pick is person:
            # velg ny og legg tilbake seg selv
            pick = receive_arr.pop()
            receive_arr.append(person)
        results.update({person: pick})
    return results


def show_next():
    global count
    text1.set("Neste person: " + cont[count])
    text2.set("Venter på neste person")
    text3.set("")
    revealbutton.configure(state=NORMAL)
    nextbutton.configure(state=DISABLED)


def reveal():
    global count
    text2.set("Du fikk: " + pairs[cont[count]])
    f = open(cont[count] + ".txt", "w")
    f.write(pairs[cont[count]])
    f.close()
    revealbutton.configure(state=DISABLED)
    nextbutton.configure(state=NORMAL)
    text1.set(cont[count])
    if count == len(cont) - 1:
        quitbutton = Button(frm, text="TRYKK HER HVIS DU SER DETTE", command=root.quit, font=("Calibri", 45))
        quitbutton.grid(column=0, row=0)
        nextbutton.configure(state=DISABLED)
    count += 1

cont = ['Patrick', 'Julian', 'Atle', 'Jesper', 'Håkon', 'Robin', 'Simen', 'Darko', 'Nikolai']
custom_messages = {
    'Patrick': '',
    'Julian': '',
    'Atle': '',
    'Jesper': '',
    'Håkon': '',
    'Robin': '',
    'Simen': '',
    'Darko': 'Drugs or alcohol? No tnx',
    'Nikolai': ''
}
print("input = ", cont)

pairs = choose_pairs(cont)
print("output = ", pairs)
root = Tk()
root.title("Secret Santa")
frm = ttk.Frame(root, padding=10)
frm.grid()
text1 = StringVar()
text2 = StringVar()
text3 = StringVar()
textbox1 = Label(frm, textvariable=text1, font=("Calibri", 25))
textbox1.grid(column=1, row=0)
textbox2 = Label(frm, textvariable=text2, font=("Calibri", 25))
textbox2.grid(column=1, row=1)
textbox3 = Label(frm, textvariable=text3, font=("Calibri", 25))
textbox3.grid(column=1, row=2)
nextbutton = Button(frm, text="Next Person", command=show_next, font=("Calibri", 25))
nextbutton.grid(column=0, row=0)
revealbutton = Button(frm, text="Reveal pick", command=reveal, font=("Calibri", 25))
revealbutton.grid(column=0, row=1)



root.mainloop()