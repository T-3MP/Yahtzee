import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import random
import webbrowser
from tkinter import messagebox  

'''
Here are some ramblings and thoughts that I had while making this project.

I figured out how to comment out large portions at the very end. That would have been nice to know
I really like to use functions that aren't necisarily needed. 
I just like to have code seperated by functions but it makes finding what I want harder (especially since they are poorly organized).
"Why did I seperate everything into different functions" - Me an hour after writting the previous line because I can't find the right part of code. AHHHH!
I thought of using classes but ended up just not doing it. It might have been easier but IDK I didn't try it out.
My comments just say what the functions and loops do which isn't bad but they could be more meaningful. It's basicly saying the same thing twice.
Man TODO has saved me so many times from looking through lines of code to figure out what I hadn't completely finished.
I love programming but man is it hard to learn user interfaces on your own.
'''

#I hope you like my version of Yahtzee!

#I don't know why but this function only works here
#Checks if user can reroll
def canReroll():
 global rerollsLeft
 if rerollsLeft > 0:
  rerollsLeft -= 1
  reroll.config(text = str(rerollsLeft) + " rerolls")
  return True
 else:
   return False
#Creates window
gui = tk.Tk(className="Yahtzee")
gui.geometry("1300x670")
gui.configure(bg="white")
gui.resizable(False, False)
#2D array for scoring
scores = [["Ones", "Twos", "Threes", "Fours", "Fives", "Sixes", "Chance", "Straight", "Yahtzee"],
["The total of all the 1's showing.", "The total of all the 2's showing.", "The total of all the 3's showing.", "The total of all the 4's showing.", "The total of all the 5's showing.", "The total of all the 6's showing.", "The sum of all the dice showing.", "Rolling a 1, 2, 3, 4, 5 or a 2, 3, 4, 5, 6. 40 Points", "All five dice showing the same value. 50 points."],
["-", "-", "-", "-", "-", "-", "-", "-", "-"]]

#Creates image vars
image1 = ImageTk.PhotoImage(Image.open('Images/uncheckedbox100.png'))
image2 = ImageTk.PhotoImage(Image.open('Images/checkedBox100.png'))
dice1 = ImageTk.PhotoImage(Image.open('Images/dice1.png'))
dice2 = ImageTk.PhotoImage(Image.open('Images/dice2.png'))
dice3 = ImageTk.PhotoImage(Image.open('Images/dice3.png'))
dice4 = ImageTk.PhotoImage(Image.open('Images/dice4.png'))
dice5 = ImageTk.PhotoImage(Image.open('Images/dice5.png'))
dice6 = ImageTk.PhotoImage(Image.open('Images/dice6.png'))

#Creates buttons to select dice you want rerolled
box1 = Button(gui, bg="white", image = image1, borderwidth=5, command=lambda m="" :changeButton(box1, 1))
box2 = Button(gui, bg="white", image = image1, borderwidth=5, command=lambda m="" :changeButton(box2, 2))
box3 = Button(gui, bg="white", image = image1, borderwidth=5, command=lambda m="" :changeButton(box3, 3))
box4 = Button(gui, bg="white", image = image1, borderwidth=5, command=lambda m="" :changeButton(box4, 4))
box5 = Button(gui, bg="white", image = image1, borderwidth=5, command=lambda m="" :changeButton(box5, 5))
#URL for rules
url = "https://www.youtube.com/watch?v=AHDgpuEzopc"

#Array to hold dice #'s
numbers = [-1, -1, -1, -1, -1]

#Array to check if a dice should be rerolled
rerollBox = [False, False, False, False, False]
#Starts with a roll, hence 2 rerolls
rerollsLeft = 2
#Changes check boxes to other symbol
def changeButton(box, num):
 if rerollBox[num - 1] == False: 
  box['image'] = image2
  rerollBox[num - 1] = True
 else:
  box['image'] = image1
  rerollBox[num - 1] = False
#When rules button is pressed a youtube video with yahtzees rules will be opened
def ruleScreen():
 webbrowser.open(url,new=1)
#Will submit numbers when button is pressed
#Returns random number between 1-6
def roll():
 diceNum = int(random.uniform(1,7))
 return diceNum
#Creates the starting dice
def startingDice():
 for x in range(0,5):
  num = roll()
  numbers[x] = num
  if num == 1:
   label = Label(bg='white', borderwidth=5, image = dice1)
   label.grid(row=0, column=x, sticky='nesw')
  elif num == 2:
   label = Label(bg='white', borderwidth=5, image = dice2,)
   label.grid(row=0, column=x,sticky='nesw')
  elif num == 3:
   label = Label(bg='white', borderwidth=5, image = dice3)
   label.grid(row=0, column=x,sticky='nesw')
  elif num == 4:
   label = Label(bg='white', borderwidth=5, image = dice4)
   label.grid(row=0, column=x,sticky='nesw')
  elif num == 5:
   label = Label(bg='white', borderwidth=5, image = dice5)
   label.grid(row=0, column=x,sticky='nesw')
  elif num == 6:
   label = Label(bg='white', borderwidth=5, image = dice6)
   label.grid(row=0, column=x,sticky='nesw')
  else:
   print("Random num doesn't work.")
#Changes dice numbers when reroll button is clicked
def rollAgain():
 canRoll = canReroll()
 if canRoll == True:
  #Gets the index of all true in rerollBox (dice that should be rerolled)
  index = [i for i, val in enumerate(rerollBox) if val]
  #Changes dice number
  for j in index:
   diceNum = roll()
   numbers[j] = diceNum
   if diceNum == 1:
    label = Label(bg='white', borderwidth=5, image = dice1)
    label.grid(row=0, column=j)
   elif diceNum == 2:
    label = Label(bg='white', borderwidth=5, image = dice2)
    label.grid(row=0, column=j)
   elif diceNum == 3:
    label = Label(bg='white', borderwidth=5, image = dice3)
    label.grid(row=0, column=j)
   elif diceNum == 4:
    label = Label(bg='white', borderwidth=5, image = dice4)
    label.grid(row=0, column=j)
   elif diceNum == 5:
    label = Label(bg='white', borderwidth=5, image = dice5)
    label.grid(row=0, column=j)
   elif diceNum == 6:
    label = Label(bg='white', borderwidth=5, image = dice6)
    label.grid(row=0, column=j)
  #Turns rerollBox array into false
  for x in range(len(rerollBox)):
   rerollBox[x] = True
  changeButton(box1, 1)
  changeButton(box2, 2)
  changeButton(box3, 3)
  changeButton(box4, 4)
  changeButton(box5, 5)
 else:
  tk.messagebox.showinfo(title="Don't be cheeky", message="You have no rerolls left!")
#Creates dice screen
def diceScreen():
 #Reset checked boxes to unchecked
 box1['image'] = image1
 box2['image'] = image1
 box3['image'] = image1
 box4['image'] = image1
 box5['image'] = image1

 #Reset numbers array
 for x in range(len(numbers)):
  numbers[x] = -1
 #Show starting dice
 startingDice()
 global reroll
 #Button vars
 submit = Button(bg="white", borderwidth = 5, text="Submit", command=lambda m="" :scoringSheet())
 reroll = Button(bg="white",borderwidth = 5, text= str(rerollsLeft) + " rerolls", command=lambda m="" :rollAgain())
 rules = Button(text="Rules",borderwidth = 5, bg="white", command=lambda m ="" :ruleScreen())
 
 scoresStillLeft = "You can still score in: "
 for x in range(len(scores[2])):
  if scores[2][x] == "-":
   scoresStillLeft += scores[0][x] + ", "
 #Removes the last character in this case a comma and a space
 scoresStillLeft = scoresStillLeft[:-1]
 scoresStillLeft = scoresStillLeft[:-1]
 scoresLeftLabel = Label(text= scoresStillLeft, bg='white', wraplength=500)
 for x in range(5):
  space = Label(bg='white')
  space.grid(row=1, column=x, ipady = 25, ipadx = 125)
 hotToPlay = Label(bg = 'white', text = "Select boxes for the dice you want rerolled.", wraplength=200)
 #Adds buttons to window
 box1.grid(row=2, column=0)
 box2.grid(row=2, column=1)
 box3.grid(row=2, column=2)
 box4.grid(row=2, column=3)
 box5.grid(row=2, column=4)
 space.grid(row=3, column=4,ipady=15)
 rules.grid(row=4, column=0)
 submit.grid(row=4, column=4)
 reroll.grid(row=4, column=2)
 hotToPlay.grid(row=5, column=0)
 scoresLeftLabel.grid(row=5, column=1, columnspan=3, pady=20)

def gameOverScreen():
 total = 0
 for x in scores[2]:
  total += int(x)
 finalScore = Label(text= "Your final score is " + str(total) + "!", bg='white', font = 'Ariel 25 bold')
 finalScore.place(relx=0.5, rely=0.5, anchor=CENTER) 

#Clears the window
def clearScreen():
 for widgets in gui.winfo_children():
  widgets.grid_remove()
#Adds scores to score array
def thisButton(buttonNum):
 #One-Six
 if buttonNum == 0:
  sum = 0
  for i in numbers:
   if i == 1:
    sum += i
  scores[2][0] = str(sum)
 elif buttonNum == 1:
  sum = 0
  for i in numbers:
   if i == 2:
    sum += i
  scores[2][1] = str(sum)
 elif buttonNum == 2:
  sum = 0
  for i in numbers:
   if i == 3:
    sum += i
  scores[2][2] = str(sum)
 elif buttonNum == 3:
  sum = 0
  for i in numbers:
   if i == 4:
    sum += i
  scores[2][3] = str(sum)
 elif buttonNum == 4:
  sum = 0
  for i in numbers:
   if i == 5:
    sum += i
  scores[2][4] = str(sum)
 elif buttonNum == 5:
  sum = 0
  for i in numbers:
   if i == 6:
    sum += i
  scores[2][5] = str(sum)
 #Chance
 elif buttonNum == 6:
  sum = 0
  for i in numbers:
   sum += i
  scores[2][6] = str(sum)
 #Straight
 elif buttonNum == 7:
  holderVar = numbers[0]
  numbers.sort()
  isStraight = True
  for i in range(len(numbers)):
   if i > 0:
    if numbers[i] < holderVar:
     scores[2][7] = 0
     isStraight = False
     break
    else:
     holderVar = numbers[i]
  if isStraight == True:
   scores[2][7] = 40
 #Yahtzee
 elif buttonNum == 8:
  isYahtzee = True
  firstNum = numbers[0]
  #Traverses numbers array and checks if it equals holderVar since they all should be the same number
  for i in numbers:
   if i != firstNum:
    isYahtzee = False
    scores[2][8] = 0
    break
  if isYahtzee == True:
    scores[2][8] = 40
 clearScreen()
 gameOver = True
 for x in scores[2]:
  if x == "-":
   gameOver = False
   break
 if gameOver == False:
  diceScreen()
  global rerollsLeft
  rerollsLeft = 2
 else:
  gameOverScreen()
 
#Cleares the screen and creates the scoring sheet
def scoringSheet():
 global rerollsLeft
 rerollsLeft = 2
 clearScreen()
 totalRows = len(scores)
 totalColumns = len(scores[0])
 #Creates the scoring table
 for i in range(totalRows - 1):
  for j in range(totalColumns):
   if i < 1:
    e = tk.Entry(width = 10)
   else:
    e = tk.Entry(width = 40)
   e.grid(row=j, column=i, padx = 20, pady = 15)
   e.insert(END, scores[i][j])
 numButtonArray = []
 #Creates the buttons
 numButtonArray.append(tk.Button(text = scores[2][0], width=10, command=lambda m="": thisButton(0)))
 numButtonArray.append(tk.Button(text = scores[2][1], width=10, command=lambda m="": thisButton(1)))
 numButtonArray.append(tk.Button(text = scores[2][2], width=10, command=lambda m="": thisButton(2)))
 numButtonArray.append(tk.Button(text = scores[2][3], width=10, command=lambda m="": thisButton(3)))
 numButtonArray.append(tk.Button(text = scores[2][4], width=10, command=lambda m="": thisButton(4)))
 numButtonArray.append(tk.Button(text = scores[2][5], width=10, command=lambda m="": thisButton(5)))
 numButtonArray.append(tk.Button(text = scores[2][6], width=10, command=lambda m="": thisButton(6)))
 numButtonArray.append(tk.Button(text = scores[2][7], width=10, command=lambda m="": thisButton(7)))
 numButtonArray.append(tk.Button(text = scores[2][8], width=10, command=lambda m="": thisButton(8)))

 for k in range(9):
  #Disables button if it has a value
  if scores[2][k]  != "-":
   numButtonArray[k]["state"] = DISABLED
  numButtonArray[k].grid(row=k, column=2)
 numList = "Your numbers: "
 for g in numbers:
  numList = numList + str(g) + ", "
 numList = numList[:-1]
 numList = numList[:-1]
 guiNumbers = Label(text=numList, bg='white')
 guiNumbers.grid(row=9, column=1)
 l = Label(text="Select a button.", bg='white')
 l.grid(row=9, column = 2)
#Creates the dice screen
diceScreen()
gui.mainloop()