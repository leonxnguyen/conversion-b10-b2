from tkinter import *
from tkinter import ttk
from tkinter.ttk import *

b10_to_ascii = {0: ' ', 1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e',
                6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j',
                11: 'k', 12: 'l', 13: 'm', 14: 'n', 15: 'o',
                16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't',
                21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y',
                26: 'z', 27: '.', 28: ',', 29: '?', 30: '\'',
                31: ':', 32: ';', 33: '(', 34: ')', 35: '!',
                36: '-'}

#too lazy to write ascii_to_b10 lol
ascii_to_b10 = {}
for num in b10_to_ascii:
    ascii_to_b10[b10_to_ascii[num]] = num

def binary_to_ascii(s: str) -> str:
    res = ''
    for s in s.split(' '):
        counter = 0
        total = 0
        while counter < len(s):
            if s[counter] == '1':
                total += 2 ** (len(s) - counter  - 1)
            counter += 1
        res += b10_to_ascii[total] 
    return res

def helper_ascii_to_binary(count: int, lst: list):
    '''Given <count> and <lst> (list of valid positions, returns the sum of 
    2 ** (count - pos) + 2 ** (count - pos - 1) + ... + 2 ** 0
    (but only for valid indexes). Wrote a decent docstring so I wouldn't
    forget the purpose of this.

    '''
    total = 0
    for pos in lst:
        total += 2 ** (count - pos)
    return total


def ascii_to_binary(s: str) -> str:
    '''essentially base 10 to binary.
    '''
    res = ''
    for char in s:
        num = ascii_to_b10[char]
        if num == 0:
            res += '0'
        else:
            count = 0
            while 2 ** count <= num:
                count += 1
            count -= 1
            #know for sure 2 ** count < num
            if 2 ** count != num:
                res += '1'
                # start at position after 1, recall indexing starts at 0
                pos = 1
                lst = [pos]
                while 2 ** count + helper_ascii_to_binary(count, lst) != num:
                    if 2 ** count + helper_ascii_to_binary(count, lst) > num:
                        res += '0'
                        lst.pop(-1)
                    else:
                        res += '1'
                    pos += 1
                    lst.append(pos)
                    #print('res =',res)
                #need to add 0s at end in case 'find' number earlier in string
                res += '1'
                res += '0' * (count - pos)
            else:
                res += '1'
                res += '0' * count
        res += ' '
    return res[:-1]
'''
#tests i did for debugging lol

#print('binary string:', ascii_to_binary(test))
#print(binary_to_ascii(ascii_to_binary(test)))

all_chars =  ' abcdefghijklmnopqrstuvwxyz.,?\':;()!-'
#all_chars = all_chars[34]
for char in all_chars:
    print(char, '=', ascii_to_binary(char))
print('end of program')
'''
# want to display <binary_to_ascii(str)> using Tkinter    
window = Tk()
window.title('Converter')

# global var
want_char_to_binary = BooleanVar(value=True)

#create tabs
tab_control = ttk.Notebook(window)
tab1 = Frame(tab_control)
tab2 = Frame(tab_control)
tab_control.add(tab1, text='Main')
tab_control.add(tab2, text='Settings')
tab_control.pack(expand=1, fill='both')

#function 
def update():
    if combo.get() == 'Character to Binary':
        want_char_to_binary.set(True)
    elif combo.get() == 'Binary to Character':
        want_char_to_binary.set(False)
    state_lbl.configure(text=combo.get())

def clicked():
    if want_char_to_binary.get() == True:
        converted_txt.configure(text=ascii_to_binary(box.get()))
    else:
        converted_txt.configure(text=binary_to_ascii(box.get()))

# Main Tab (tab1)
state_lbl = Label(tab1, text='Character to Binary', font=("Terminal", 50))
state_lbl.grid(row=0, column=1, padx=330)

box = Entry(tab1, width=25, justify='center')
box.grid(row=1, column=1)

btn = Button(tab1, text='Submit', command=clicked)
btn.grid(row=2, column=1)

converted_txt = Label(tab1, text='waiting for input...', font=("Terminal", 20))
converted_txt.grid(row=5, column=1)

# Settings Tab (tab2)
combo = Combobox(tab2)
combo['values'] = ['Character to Binary', 'Binary to Character']
combo.current(0)
combo.grid(row=3, column=1, padx=500)

btn2 = Button(tab2, text='Update', command=update)
btn2.grid(row=4, column=1)


window.geometry('1280x720')

window.mainloop()
