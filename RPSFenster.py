from tkinter import *
import random
import time
import csv

fenster = Tk()
fenster.title("Rock Paper Scissors")
fenster.geometry("600x500")

items = ["Rock", "Paper", "Scissors"]

def rules_action():
    Space.grid_forget()
    Rules.grid(row=3, columnspan=2)
    Rules.config(text="Rock beats Scissors, Paper beats Rock, Scissors beats Paper.")

def start_action():
    Stats = open("RPSStats.csv", "a")
    Stats.write("Wins" +","+ "Lost" +","+ "Draws")
    RockButton.grid(row=4, column=0, sticky=N)
    PaperButton.grid(row=4, columnspan=2, sticky=N)
    ScissorsButton.grid(row=4, column=1, sticky=N)
    Close.place(x=280, y=450)
    WinsLabel.grid_forget()
    WinsStats.grid_forget()
    LostLabel.grid_forget()
    LostStats.grid_forget()
    DrawsLabel.grid_forget()
    DrawsStats.grid_forget()
    AllWinsLabel.grid_forget()
    AllWinsStats.grid_forget()
    AllLostLabel.grid_forget()
    AllLostStats.grid_forget()
    AllDrawsLabel.grid_forget()
    AllDrawsStats.grid_forget()
    AllStatsButton.place_forget()

def rock_action():
    draws = 0
    wins = 0
    lost = 0
    End = ""
    Auswahl = "Rock"
    Choice = random.choice(items)
    ChoiceLabel2.config(text=Choice)
    ChoiceLabel.grid(row=5, column=0)
    ChoiceLabel2.grid(row=5, column=1)
    if (Choice == Auswahl):
        End = "It's a Draw."
        draws = draws + 1
    if (Auswahl == "Rock" and Choice == "Paper"):
        End = "You lost."
        lost = lost + 1
    if (Auswahl == "Paper" and Choice == "Rock"):
        End = "You won!"
        wins = wins + 1
    if (Auswahl == "Paper" and Choice == "Scissors"):
        End = "You lost."
        lost = lost + 1
    if (Auswahl == "Scissors" and Choice == "Paper"):
        End = "You won!"
        wins = wins + 1
    if (Auswahl == "Scissors" and Choice == "Rock"):
        End = "You lost."
        lost = lost + 1
    if (Auswahl == "Rock" and Choice == "Scissors"):
        End = "You won!"
        wins = wins + 1
    UrChoiceLabel.grid(row=6, column=0)
    UrChoice.grid(row=6, column=1)
    UrChoice.config(text=Auswahl)
    Ergebnis.config(text=End)
    Ergebnis.grid(row=7, columnspan=2)
    Stats = open("RPSStats.csv", "a")
    Stats.write("\n"+ str(wins) +","+ str(lost) +","+ str(draws))
    StatsAll = open("RPSALLStats.csv", "a")
    StatsAll.write("\n"+ str(wins) +","+ str(lost) +","+ str(draws))

def paper_action():
    draws = 0
    wins = 0
    lost = 0
    End = ""
    Auswahl = "Paper"
    Choice = random.choice(items)
    ChoiceLabel2.config(text=Choice)
    ChoiceLabel.grid(row=5, column=0)
    ChoiceLabel2.grid(row=5, column=1)
    if (Choice == Auswahl):
        End = "It's a Draw."
        draws = draws + 1
    if (Auswahl == "Rock" and Choice == "Paper"):
        End = "You lost."
        lost = lost + 1
    if (Auswahl == "Paper" and Choice == "Rock"):
        End = "You won!"
        wins = wins + 1
    if (Auswahl == "Paper" and Choice == "Scissors"):
        End = "You lost."
        lost = lost + 1
    if (Auswahl == "Scissors" and Choice == "Paper"):
        End = "You won!"
        wins = wins + 1
    if (Auswahl == "Scissors" and Choice == "Rock"):
        End = "You lost."
        lost = lost + 1
    if (Auswahl == "Rock" and Choice == "Scissors"):
        End = "You won!"
        wins = wins + 1
        UrChoiceLabel.grid(row=6, column=0)
    UrChoice.grid(row=6, column=1)
    UrChoice.config(text=Auswahl)
    Ergebnis.config(text=End)
    Ergebnis.grid(row=7, columnspan=2)
    Stats = open("RPSStats.csv", "a")
    Stats.write("\n"+ str(wins) +","+ str(lost) +","+ str(draws))
    StatsAll = open("RPSALLStats.csv", "a")
    StatsAll.write("\n"+ str(wins) +","+ str(lost) +","+ str(draws))

def scissors_action():
    draws = 0
    wins = 0
    lost = 0
    End = ""
    Auswahl = "Scissors"
    Choice = random.choice(items)
    ChoiceLabel2.config(text=Choice)
    ChoiceLabel.grid(row=5, column=0)
    ChoiceLabel2.grid(row=5, column=1)
    if (Choice == Auswahl):
        End = "It's a Draw."
        draws = draws + 1
    if (Auswahl == "Rock" and Choice == "Paper"):
        End = "You lost."
        lost = lost + 1
    if (Auswahl == "Paper" and Choice == "Rock"):
        End = "You won!"
        wins = wins + 1
    if (Auswahl == "Paper" and Choice == "Scissors"):
        End = "You lost."
        lost = lost + 1
    if (Auswahl == "Scissors" and Choice == "Paper"):
        End = "You won!"
        wins = wins + 1
    if (Auswahl == "Scissors" and Choice == "Rock"):
        End = "You lost."
        lost = lost + 1
    if (Auswahl == "Rock" and Choice == "Scissors"):
        End = "You won!"
        wins = wins + 1
    UrChoiceLabel.grid(row=6, column=0)
    UrChoice.grid(row=6, column=1)
    UrChoice.config(text=Auswahl)
    Ergebnis.config(text=End)
    Ergebnis.grid(row=7, columnspan=2)
    Stats = open("RPSStats.csv", "a")
    Stats.write("\n"+ str(wins) +","+ str(lost) +","+ str(draws))
    StatsAll = open("RPSALLStats.csv", "a")
    StatsAll.write("\n"+ str(wins) +","+ str(lost) +","+ str(draws))

def close_action():
    wins = 0
    lost = 0
    draws = 0
    winsAll = 0
    lostAll = 0
    drawsAll = 0
    RockButton.grid_forget()
    PaperButton.grid_forget()
    ScissorsButton.grid_forget()
    Ergebnis.grid_forget()
    ChoiceLabel.grid_forget()
    ChoiceLabel2.grid_forget()
    UrChoiceLabel.grid_forget()
    UrChoice.grid_forget()
    Close.place_forget()
    with open("RPSStats.csv") as csvdatei:
        csv_inhalt = csv.reader(csvdatei)
        for row in csv_inhalt:
            print(row)
            if (row[0] == "1"):
                wins = wins + 1
            if (row[1] == "1"):
                lost = lost + 1
            if (row[2] == "1"):
                draws = draws + 1
    with open("RPSALLStats.csv") as csvdateiAll:
        csv_inhaltAll = csv.reader(csvdateiAll)
        for rowAll in csv_inhaltAll:
            if (rowAll[0] == "1"):
                winsAll = winsAll + 1
            if (rowAll[1] == "1"):
                lostAll = lostAll + 1
            if (rowAll[2] == "1"):
                drawsAll = drawsAll + 1
    AllDrawsStats.config(text=drawsAll)
    AllLostStats.config(text=lostAll)
    AllWinsStats.config(text=winsAll)
    WinsLabel.grid(row=7, column=0)
    WinsStats.config(text=wins)
    WinsStats.grid(row=7, column=1)
    LostLabel.grid(row=8, column=0)
    LostStats.config(text=lost)
    LostStats.grid(row=8, column=1)
    DrawsLabel.grid(row=9, column=0)
    DrawsStats.config(text=draws)
    DrawsStats.grid(row=9, column=1)
    csvdatei = open("RPSStats.csv", "r+")
    csvdatei.seek(0)
    csvdatei.truncate()
    AllStatsButton.place(x=230, y=450)
    Space.grid(row=3, columnspan=2)
    Rules.grid_forget()

def allstats_action():
    Space2.grid(row=10, columnspan=2)
    AllWinsLabel.grid(row=11, column=0)
    AllWinsStats.grid(row=11, column=1)
    AllLostLabel.grid(row=12, column=0)
    AllLostStats.grid(row=12, column=1)
    AllDrawsLabel.grid(row=13, column=0)
    AllDrawsStats.grid(row=13, column=1)
    AllStatsButton.place_forget()

Welcome = Label(fenster, pady=5, font="Helvetica 24 bold", text="Welcome")
RulesLabel = Label(fenster, pady=10, width=65, font=14, text="Do you want to know how 'Rock, Paper, Scissors' works?")
RulesButton = Button(fenster, bg="#00BFFF", padx=85, font=14, text="Rules", command=rules_action)
Rules = Label(fenster, pady=15, width=65, font=14, text="")
StartButton = Button(fenster, bg="#2F972F", padx=75, font=14, text="Start Playing", command=start_action)
Space = Label(fenster, height=3)
RockButton = Button(fenster, bg="grey", padx=57, font=14, text="Rock", command=rock_action)
PaperButton = Button(fenster, bg="grey", padx=60, font=14, text="Paper", command=paper_action)
ScissorsButton = Button(fenster, bg="grey", padx=60, font=14, text="Scissors", command=scissors_action)
ChoiceLabel = Label(fenster, font=14, text="Choice of the program: ")
ChoiceLabel2 = Label(fenster, pady=5, font=14, text="")
UrChoiceLabel = Label(fenster, font=14, text="Ur Choice: ")
UrChoice = Label(fenster, font=14)
Ergebnis = Label(fenster, font=20, height=4, text="")
Close = Button(fenster, bg="red", font=20, text="Close", command=close_action)
WinsLabel = Label(fenster, font=22, text="Wins: ")
WinsStats = Label(fenster, font=22)
LostLabel = Label(fenster, font=22, text="Lost: ")
LostStats = Label(fenster, font=22)
DrawsLabel = Label(fenster, font=22, text="Draws: ")
DrawsStats = Label(fenster, font=22)
AllWinsLabel = Label(fenster, font=22, text="All Wins: ")
AllWinsStats = Label(fenster, font=22)
AllLostLabel = Label(fenster, font=22, text="All Losts: ")
AllLostStats = Label(fenster, font=22)
AllDrawsLabel = Label(fenster, font=22, text="All Draws: ")
AllDrawsStats = Label(fenster, font=22)
AllStatsButton = Button(fenster, bg="#00BFFF", font = 20, text="Show All Time Stats", command=allstats_action)
Space2 = Label(fenster, height=2)

Welcome.grid(row=0, columnspan=2)
RulesLabel.grid(row=1, columnspan=2)
RulesButton.grid(row=2, column=0, sticky=E)
StartButton.grid(row=2, column=1, sticky=W)
Rules.grid_forget()
Space.grid(row=3, columnspan=2)
RockButton.grid_forget()
PaperButton.grid_forget()
ScissorsButton.grid_forget()
ChoiceLabel.grid_forget()
ChoiceLabel2.grid_forget()
Ergebnis.grid_forget()

fenster.mainloop()