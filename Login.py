from tkinter import *
from datetime import datetime
import subprocess
import webbrowser


class login:

    def __init__(self, master):



        self.NameLabel = Label(text='Name:', bg='#66e0ff', fg='#0033cc')
        self.NameLabel.config(width=8)
        self.NameLabel.grid(row=1)

        self.NameEntry = Entry(bg='#66e0ff')
        self.NameEntry.grid(row=1, column=1)

        self.PasswordLabel = Label(text='Password:', bg='#66e0ff', fg='#0033cc')
        self.PasswordLabel.config(width=8)
        self.PasswordLabel.grid(row=2)

        self.PasswordEntry = Entry(bg='#66e0ff', show='●')
        self.PasswordEntry.grid(row=2, column=1)

        self.remember = False
        def check():
            self.remember = True

        self.RememberCheck = Checkbutton(text='Remember me?', bg='#0066cc', command=check)
        self.RememberCheck.config(width=20)
        self.RememberCheck.grid(row=3, columnspan=2)


        self.NextButton = Button(text='Next', command=self.next, height=1, width=26, bg='#66e0ff', fg='#0033cc')
        self.NextButton.grid(row=4, columnspan=2)

        self.NameEntry.insert(0, '')
        self.PasswordEntry.insert(0, '')

        dat2 = open('Data1.dat', 'r')
        Name = 'NeophytePon4'

        if 'NeophytePon4' in dat2:
            self.NameEntry.insert('1', Name)

    def next(self):
        Name = self.NameEntry.get()
        Password = self.PasswordEntry.get()

        Remember = self.RememberCheck.getboolean('True')

        if Name == 'NeophytePon4' and Password == 'password' and self.remember is True:
            dat1 = open('Data1.dat', 'w')
            dat1.write(Name)


            print('Logged In!')
            root.destroy()
            root2 = Tk()
            MENU = menu(root2)
            root2.iconbitmap(r'favicon.ico')
            root2.mainloop()

        elif Name == 'NeophytePon4' and Password == 'password' and self.remember is False:
            clear = open('Data1.dat', 'w')

            print('Logged In!')
            root.destroy()
            root2 = Tk()
            MENU = menu(root2)
            root2.iconbitmap(r'favicon.ico')
            root2.mainloop()



        else:
            print('Please try again...')
            self.LoginLabel = Label(text='Try again', bg='red')
            self.LoginLabel.grid(row=3, columnspan=2)
            self.LoginLabel.config(width=26)


class menu:

    def clear(self):
        self.add = False
        self.minus = False
        self.times = False
        self.divide = False

        self.EqualButton = Button(text='>', command=self.equal)
        self.EqualButton.grid(row=0, column=5)

        self.BoxEntry.delete(0, END)

    def divide(self):
        self.add = False
        self.minus = False
        self.times = False
        self.divide = True

    def times(self):
        self.add = False
        self.minus = False
        self.times = True
        self.divide = False

    def add(self):
        self.add = True
        self.minus = False
        self.times = False
        self.divide = False

    def minus(self):
        self.add = False
        self.minus = True
        self.times = False
        self.divide = False

    def equal(self):

        self.num1 = self.BoxEntry.get()
        self.BoxEntry.delete(0, END)
        self.EqualButton.destroy()
        self.Equal2Button = Button(text='=', command=self.equal2)
        self.Equal2Button.grid(row=0, column=5)

    def calc(self):

        def back():
            if self.EqualButton.winfo_exists() == 1:
                self.EqualButton.destroy()
                self.BoxEntry.destroy()
                self.AddButton.destroy()
                self.BackButton4.destroy()
                self.MinusButton.destroy()
                self.TimesButton.destroy()
                self.DivideButton.destroy()
                self.ClearButton.destroy()

                self.GameButton = Button(text='Games', bg='blue', command=self.game)
                self.GameButton.config(height=5, width=10)
                self.GameButton.grid(row=0)

                self.WebButton = Button(text='Google', bg='blue', command=self.web)
                self.WebButton.config(height=5, width=10)
                self.WebButton.grid(row=0, column=1)

                self.NotesButton = Button(text='Notes', bg='orange', command=self.notes)
                self.NotesButton.config(height=5, width=10)
                self.NotesButton.grid(row=1)

                self.CalcButton = Button(text='Calculator', bg='orange', command=self.calc)
                self.CalcButton.config(height=5, width=10)
                self.CalcButton.grid(row=1, column=1)

                self.VersionLabel = Label(text='Reebo-Menu© V2.3')
                self.VersionLabel.config()
                self.VersionLabel.grid(row=2, columnspan=2)

                if self.Equal2Button.winfo_exists() == 1:
                    self.Equal2Button.destroy()

            else:
                print("Error press clear")


        self.GameButton.destroy()
        self.NotesButton.destroy()
        self.WebButton.destroy()
        self.CalcButton.destroy()
        self.VersionLabel.destroy()

        self.BoxEntry = Entry(width=25)
        self.BoxEntry.grid(row=0, columnspan=5)

        self.EqualButton = Button(text='>', command=self.equal)
        self.EqualButton.grid(row=0, column=5)

        self.AddButton = Button(text='+', width=5, command=self.add)
        self.AddButton.grid(row=1)

        self.MinusButton = Button(text='-', width=5, command=self.minus)
        self.MinusButton.grid(row=1, column=1)

        self.TimesButton = Button(text='*', width=5, command=self.times)
        self.TimesButton.grid(row=1, column=2)

        self.DivideButton = Button(text='/', width=5, command=self.divide)
        self.DivideButton.grid(row=1, column=3)

        self.ClearButton = Button(text='Clear', width=24, command=self.clear)
        self.ClearButton.grid(row=2, columnspan=4)

        self.BackButton4 = Button(text='Back', bg='black', fg='white', command=back, width=28)
        self.BackButton4.grid(row=3, columnspan=5)

    def equal2(self):
        self.num2 = self.BoxEntry.get()

        if self.add is True:
            num3 = int(self.num1) + int(self.num2)

        elif self.minus is True:
            num3 = int(self.num1) - int(self.num2)

        elif self.times is True:
            num3 = int(self.num1) * int(self.num2)

        elif self.divide is True:
            num3 = int(self.num1) / int(self.num2)

        self.BoxEntry.delete(0, END)
        self.BoxEntry.insert("1", num3)

    def game(self):
        self.GameButton.destroy()
        self.CalcButton.destroy()
        self.NotesButton.destroy()
        self.WebButton.destroy()
        self.VersionLabel.destroy()

        def Csgo():
            webbrowser.open('steam://rungameid/730')

        self.CsgoButton = Button(text='cs:go', bg='red', command=Csgo)
        self.CsgoButton.config(height=5, width=10)
        self.CsgoButton.grid(row=0)

        def Tf2():
            webbrowser.open('steam://rungameid/440')

        self.Tf2Button = Button(text='TF2', bg='orange', command=Tf2)
        self.Tf2Button.config(height=5, width=10)
        self.Tf2Button.grid(row=0, column=1)

        def Minecraft():
            p = subprocess.Popen('start /B Minecraft', shell=True)

        self.MinecraftButton = Button(text='Minecraft', bg='brown', command=Minecraft)
        self.MinecraftButton.config(height=5, width=10)
        self.MinecraftButton.grid(row=1)

        def Steam():
            p = subprocess.Popen('start /B Steam', shell=True)


        self.SteamButton = Button(text='Steam', bg='blue', command=Steam)
        self.SteamButton.config(height=5, width=10)
        self.SteamButton.grid(row=1, column=1)

        def Back():
            self.CsgoButton.destroy()
            self.Tf2Button.destroy()
            self.MinecraftButton.destroy()
            self.SteamButton.destroy()
            self.BackButton1.destroy()

            self.GameButton = Button(text='Games', bg='blue', command=self.game)
            self.GameButton.config(height=5, width=10)
            self.GameButton.grid(row=0)

            self.WebButton = Button(text='Google', bg='blue', command=self.web)
            self.WebButton.config(height=5, width=10)
            self.WebButton.grid(row=0, column=1)

            self.NotesButton = Button(text='Notes', bg='orange', command=self.notes)
            self.NotesButton.config(height=5, width=10)
            self.NotesButton.grid(row=1)

            self.CalcButton = Button(text='Calculator', bg='orange', command=self.calc)
            self.CalcButton.config(height=5, width=10)
            self.CalcButton.grid(row=1, column=1)

            self.VersionLabel = Label(text='Reebo-Menu© V2.3')
            self.VersionLabel.config()
            self.VersionLabel.grid(row=2, columnspan=2)

        self.BackButton1 = Button(text='Back', bg='black', fg='white', command=Back)
        self.BackButton1.config(width=22)
        self.BackButton1.grid(row=2, columnspan=2)

    def search(self):
        self.SeatchInput = 'https://www.google.co.uk/#q=' + self.SearchEntry.get()

        webbrowser.open(self.SeatchInput)

    def web(self):
        self.GameButton.destroy()
        self.NotesButton.destroy()
        self.WebButton.destroy()
        self.CalcButton.destroy()
        self.VersionLabel.destroy()

        self.SearchEntry = Entry()
        self.SearchEntry.config(width=30)
        self.SearchEntry.grid(row=0, columnspan=1)

        self.SearchButton = Button(text='Search', command=self.search)
        self.SearchButton.grid(row=0, column=1)

        def Back():
            self.SearchEntry.destroy()
            self.SearchButton.destroy()
            self.BackButton2.destroy()

            self.GameButton = Button(text='Games', bg='blue', command=self.game)
            self.GameButton.config(height=5, width=10)
            self.GameButton.grid(row=0)

            self.WebButton = Button(text='Google', bg='blue', command=self.web)
            self.WebButton.config(height=5, width=10)
            self.WebButton.grid(row=0, column=1)

            self.NotesButton = Button(text='Notes', bg='orange', command=self.notes)
            self.NotesButton.config(height=5, width=10)
            self.NotesButton.grid(row=1)

            self.CalcButton = Button(text='Calculator', bg='orange', command=self.calc)
            self.CalcButton.config(height=5, width=10)
            self.CalcButton.grid(row=1, column=1)

            self.VersionLabel = Label(text='Reebo-Menu© V2.3')
            self.VersionLabel.config()
            self.VersionLabel.grid(row=2, columnspan=2)

        self.BackButton2 = Button(text='Back', bg='black', fg='white', command=Back)
        self.BackButton2.config(width=35)
        self.BackButton2.grid(row=1, columnspan=2)

    def notes(self):
        self.GameButton.destroy()
        self.NotesButton.destroy()
        self.WebButton.destroy()
        self.CalcButton.destroy()
        self.VersionLabel.destroy()

        def back():

            self.NoteText.destroy()
            self.BackButton3.destroy()
            self.AcceptButton.destroy()

            self.GameButton = Button(text='Games', bg='blue', command=self.game)
            self.GameButton.config(height=5, width=10)
            self.GameButton.grid(row=0)

            self.WebButton = Button(text='Google', bg='blue', command=self.web)
            self.WebButton.config(height=5, width=10)
            self.WebButton.grid(row=0, column=1)

            self.NotesButton = Button(text='Notes', bg='orange', command=self.notes)
            self.NotesButton.config(height=5, width=10)
            self.NotesButton.grid(row=1)

            self.CalcButton = Button(text='Calculator', bg='orange', command=self.calc)
            self.CalcButton.config(height=5, width=10)
            self.CalcButton.grid(row=1, column=1)

            self.VersionLabel = Label(text='Reebo-Menu© V2.3')
            self.VersionLabel.config()
            self.VersionLabel.grid(row=2, columnspan=2)

        self.NoteText = Text()
        self.NoteText.grid(row=0)



        file =  open('Notes.txt', 'r')
        insert = file.read()
        self.NoteText.insert("1.0", insert)

        self.GameButton.destroy()
        self.NotesButton.destroy()
        self.WebButton.destroy()
        self.CalcButton.destroy()
        self.VersionLabel.destroy()


        self.AcceptButton = Button(text='Accept', command=self. accept)
        self.AcceptButton.grid(row=1)

        self.BackButton3 = Button(text='Back', command=back)
        self.BackButton3.grid(row=1, column=1)

    def accept(self):
        self.notes = open('Notes.txt', 'w')
        text = self.NoteText.get("1.0", END)
        self.notes.write(text)

    def __init__(self, master2):
        self.GameButton = Button(text='Games', bg='blue', command=self.game)
        self.GameButton.config(height=5, width=10)
        self.GameButton.grid(row=0)

        self.WebButton = Button(text='Google', bg='blue', command=self.web)
        self.WebButton.config(height=5, width=10)
        self.WebButton.grid(row=0, column=1)

        self.NotesButton = Button(text='Notes', bg='orange', command=self.notes)
        self.NotesButton.config(height=5, width=10)
        self.NotesButton.grid(row=1)

        self.CalcButton = Button(text='Calculator', bg='orange', command=self.calc)
        self.CalcButton.config(height=5, width=10)
        self.CalcButton.grid(row=1, column=1)

        self.VersionLabel = Label(text='Reebo-Menu© V2.3')
        self.VersionLabel.config()
        self.VersionLabel.grid(row=2, columnspan=2)

root = Tk()
root.configure(background='#0066cc')
root.iconbitmap(r'favicon.ico')
LOGIN = login(root)
root.mainloop()