import tkinter as tk
from tkinter import ttk
from tkinter import*
from PIL import Image, ImageTk
import random
from datetime import date
from datetime import datetime

prices = {
    "California Roll" : 12,
    "Dragon Roll" : 14,
    "Philidelphia Roll" : 13,
    "Shrimp Roll" : 15,
}

root  = Tk()

root.title("TTC - Binary Restaurant")

# ------------------------------------FUNCTIONS--------------------------------------------- #

#region Generating a random Order ID when starting a new order
def ORDER_ID():
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
               'V', 'W', 'X', 'Y', 'Z']
    order_id = "BIN_"
    random_letters = ""
    random_digits = ""
    for i in range(0,3):
        random_letters += random.choice(letters)
        random_digits += str(random.choice(numbers))

    order_id += random_letters + random_digits
    return order_id
#endregion

#region Add to Order Button
def add():
    # updating the transaction label
    current_order = orderTransaction.cget("text")
    added_dish = displayLabel.cget("text") + "...." + str(prices[displayLabel.cget("text")]) + "$ "
    updated_order = current_order + added_dish
    orderTransaction.configure(text=updated_order)

    # updating the order total label
    order_total = orderTotalLabel.cget("text").replace("TOTAL : ", "")
    order_total = order_total.replace("$", "")
    updated_total = int(order_total) + prices[displayLabel.cget("text")]
    orderTotalLabel.configure(text="TOTAL : " + str(updated_total) + "$")
#endregion

#Region Remove Button Function
def remove():
    dish_to_remove = displayLabel.cget("text") + "...." + str(prices[displayLabel.cget("text")])
    transaction_list = orderTransaction.cget("text").split("$ ")
    transaction_list.pop(len(transaction_list) - 1)

    if dish_to_remove in transaction_list:
        # update transaction label
        transaction_list.remove(dish_to_remove)
        updated_order = ""
        for item in transaction_list:
            updated_order += item + "$ "

        orderTransaction.configure(text = updated_order)

        # update transaction total
        order_total = orderTotalLabel.cget("text").replace("TOTAL : ", "")
        order_total = order_total.replace("$", "")
        updated_total = int(order_total) - prices[displayLabel.cget("text")]
        orderTotalLabel.configure(text="TOTAL : " + str(updated_total) + "$")

#endregion

#region Display Button Functions
def displaycal():
    calDishFrame.configure(
        relief = "sunken",
        style = "SelectedDish.TFrame"
    )
    dragDishFrame.configure(style = "DishFrame.TFrame")
    philDishFrame.configure(style= "DishFrame.TFrame")
    shrimpDishFrame.configure(style = "DishFrame.TFrame")

    displayLabel.configure(
        image =  calImage,
        text = "California Roll",
        font=('Helvetica', 14,"bold"),
        foreground="white",
        compound = "bottom",
        padding = (5, 5, 5, 5),
    )

def displaydrag():
    dragDishFrame.configure(
        relief = "sunken",
        style = "SelectedDish.TFrame"
    )
    philDishFrame.configure(style="DishFrame.TFrame")
    shrimpDishFrame.configure(style="DishFrame.TFrame")
    calDishFrame.configure(style="DishFrame.TFrame")
    displayLabel.configure(
        text = "Dragon Roll",
        font = ('Helvetica', 14,"bold"),
        foreground = "white",
        image = dragImage,
        compound = "bottom",
        padding=(5, 5, 5, 5),
    )

def displayphil():
    philDishFrame.configure(
        relief = "sunken",
        style="SelectedDish.TFrame"
    )
    shrimpDishFrame.configure(style="DishFrame.TFrame")
    calDishFrame.configure(style="DishFrame.TFrame")
    dragDishFrame.configure(style="DishFrame.TFrame")
    displayLabel.configure(
        text = "Philidelphia Roll",
        font=('Helvetica', 14,"bold"),
        foreground="white",
        image = philImage,
        compound = "bottom",
        padding=(5, 5, 5, 5),
    )

def displayshrimp():
    shrimpDishFrame.configure(
        relief = "sunken",
        style="SelectedDish.TFrame"
    )
    calDishFrame.configure(style="DishFrame.TFrame")
    dragDishFrame.configure(style="DishFrame.TFrame")
    philDishFrame.configure(style="DishFrame.TFrame")
    displayLabel.configure(
        text = "Shrimp Roll",
        font=('Helvetica', 14,"bold"),
        foreground="white",
        image = shrimpImage,
        compound = "bottom",
        padding=(5, 5, 5, 5),
    )

#endregion

#region Generating Receipt from Order Button
def order():
    new_receipt = orderIDLabel.cget("text")
    new_receipt = new_receipt.replace("ORDER ID : ","")
    transaction_list = orderTransaction.cget("text").split("$ ")
    transaction_list.pop(len(transaction_list) - 1)

    order_day = date.today()
    order_time = datetime.now()

    for item in transaction_list:
        item += "$ "

    with open(new_receipt, 'w') as file:
        file.write("The Binary")
        file.write("\n")
        file.write("________________________________________________________")
        file.write("\n")
        file.write(order_day.strftime("%x"))
        file.write("\n")
        file.write(order_time.strftime("%X"))
        file.write("\n\n")
        for item in transaction_list:
            file.write(item + "\n")
        file.write("\n\n")
        file.write(orderTotalLabel.cget("text"))

    orderTotalLabel.configure(text = "TOTAL : 0$")
    orderIDLabel.configure(text = "ODER ID: " + ORDER_ID())
    orderTransaction.configure(text = "")

#endregion

# ---------------------------------- STYLING AND IMAGES ------------------------------------ #

#region Style configurations
s = ttk.Style()
s.configure('MainFrame.TFrame', background = "#2B2B28")
s.configure('MenuFrame.TFrame', background = "#4A4A48")
s.configure('DisplayFrame.TFrame', background = "#0F1110")
s.configure('OrderFrame.TFrame', background = "#B7C4CF")
s.configure('DishFrame.TFrame', background = "#4A4A48", relief = "raised")
s.configure('SelectedDish.TFrame', background = "#C4DFAA")
s.configure('MenuLabel.TLabel',
            background = "#0F1110",
            font = ("Arial", 13, "italic"),
            foreground = "white",
            padding = (5, 5, 5, 5),
            width = 21
            )
s.configure('orderTotalLabel.TLabel',
            background = "#0F1110",
            font = ("Arial", 10, "bold"),
            foreground = "white",
            padding = (2, 2, 2, 2),
            anchor = "w"
            )
s.configure('orderTransaction.TLabel',
            background = "#4A4A48",
            font = ('Helvetica', 12),
            foreground = "white",
            wraplength = 170,
            anchor = "nw",
            padding = (3, 3, 3, 3)
            )

# endregion

# region Images
# Menu images
displayDefaultImageObject = Image.open("default.jpg").resize((350,200))
displayDefaultImage = ImageTk.PhotoImage(displayDefaultImageObject)

calImageObject = Image.open("cal_roll.jpg").resize((350,350))
calImage = ImageTk.PhotoImage(calImageObject)

dragImageObject = Image.open("drag_roll.jpg").resize((350,334))
dragImage = ImageTk.PhotoImage(dragImageObject)

philImageObject = Image.open("phil_roll.jpg").resize((350,334))
philImage = ImageTk.PhotoImage(philImageObject)

shrimpImageObject = Image.open("shrimp_roll.jpg").resize((350,334))
shrimpImage = ImageTk.PhotoImage(shrimpImageObject)
#endregion

#----------------------------------- WIDGETS ----------------------------------------------- #

# region Frames

# Section Frames
mainFrame = ttk.Frame(root, width = 800, height = 580, style = 'MainFrame.TFrame')
mainFrame.grid(row = 0, column = 0, sticky = "NSEW")

topBannerFrame = ttk.Frame(mainFrame)
topBannerFrame.grid(row = 0, column = 0, sticky = "NSEW", columnspan = 3)

menuFrame = ttk.Frame(mainFrame, style = 'MenuFrame.TFrame')
menuFrame.grid(row = 1, column = 0, padx = 3, pady = 3, sticky = "NSEW")

displayFrame = ttk.Frame(mainFrame, style = "DisplayFrame.TFrame")
displayFrame.grid(row = 1, column = 1, padx = 3, pady = 3, sticky = "NSEW")

orderFrame = ttk.Frame(mainFrame, style = "OrderFrame.TFrame")
orderFrame.grid(row = 1, column = 2, padx = 3, pady = 3, sticky = "NSEW")

# Dish Frames
calDishFrame = ttk.Frame(menuFrame, style = "DishFrame.TFrame")
calDishFrame.grid(row = 1, column = 0, sticky = "NSEW")

dragDishFrame = ttk.Frame(menuFrame,style ="DishFrame.TFrame")
dragDishFrame.grid(row = 2, column = 0, sticky ="NSEW")

philDishFrame = ttk.Frame(menuFrame, style ="DishFrame.TFrame")
philDishFrame.grid(row = 3, column = 0, sticky ="NSEW")

shrimpDishFrame = ttk.Frame(menuFrame, style ="DishFrame.TFrame")
shrimpDishFrame.grid(row = 4, column = 0, sticky ="NSEW")
#endregion

#region Menu Section
MainMenuLabel = ttk.Label(menuFrame, text = "MENU", style = "MenuLabel.TLabel")
MainMenuLabel.grid(row = 0, column = 0, sticky = "WE")
MainMenuLabel.configure(
    anchor = "center",
    font = ("Helvetica", 14, "bold")
)

calDishLabel = ttk.Label(calDishFrame, text ="California Roll ..... $12", style ="MenuLabel.TLabel")
calDishLabel.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "W")

dragDishLabel = ttk.Label(dragDishFrame, text ="Dragon Roll ..... $14", style ="MenuLabel.TLabel")
dragDishLabel.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "W")

philDishLabel = ttk.Label(philDishFrame, text ="Philidelphia Roll ..... $13", style ="MenuLabel.TLabel")
philDishLabel.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "W")

shrimpDishLabel = ttk.Label(shrimpDishFrame, text ="Shrimp Roll ..... $15", style ="MenuLabel.TLabel")
shrimpDishLabel.grid(row = 0, column = 0, padx =10, pady = 10, sticky = "W")


#Buttons
calDisplayButton = ttk.Button(calDishFrame, text ="Display", command = displaycal)
calDisplayButton.grid(row = 0, column = 1, padx = 10)

dragDisplayButton = ttk.Button(dragDishFrame, text ="Display", command = displaydrag)
dragDisplayButton.grid(row = 0, column = 1, padx = 10)

philDisplayButton = ttk.Button(philDishFrame, text ="Display", command = displayphil)
philDisplayButton.grid(row = 0, column = 1, padx = 10)

shrimpDisplayButton = ttk.Button(shrimpDishFrame, text ="Display", command = displayshrimp)
shrimpDisplayButton.grid(row = 0, column = 1, padx = 10)
# endregion

#region Order Section
orderTitleLabel = ttk.Label(orderFrame, text = "ORDER")
orderTitleLabel.configure(
    foreground="white", background="black",
    font=("Helvetica", 14, "bold"), anchor = "center",
    padding = (5, 5, 5, 5),
)
orderTitleLabel.grid(row = 0, column = 0, sticky = "EW")

orderIDLabel = ttk.Label(orderFrame, text = "ORDER ID : " + ORDER_ID())
orderIDLabel.configure(
    background = "black",
    foreground = "white",
    font = ("Helvetica", 11, "italic"),
    anchor = "center",
)
orderIDLabel.grid(row = 1, column = 0, sticky = "EW", pady = 1)

orderTransaction = ttk.Label(orderFrame, style = 'orderTransaction.TLabel')
orderTransaction.grid(row = 2, column = 0, sticky = "NSEW")

orderTotalLabel = ttk.Label(orderFrame, text = "TOTAL : 0$", style = "orderTotalLabel.TLabel")
orderTotalLabel.grid(row = 3, column = 0, sticky = "EW")

orderButton = ttk.Button(orderFrame, text = "ORDER", command = order)
orderButton.grid(row = 4, column = 0, sticky = "EW")


# endregion

# region Display Section
displayLabel = ttk.Label(displayFrame, image = displayDefaultImage)
displayLabel.grid(row = 0, column = 0 , sticky = "NSEW", columnspan = 2)
displayLabel.configure(background = "#0F1110")

addOrderButton = ttk.Button(displayFrame, text = "ADD TO ORDER", command = add)
addOrderButton.grid(row = 1, column = 0, padx = 2, sticky = "NSEW")

removeOrderButton = ttk.Button(displayFrame, text = "REMOVE", command = remove)
removeOrderButton.grid(row = 1, column = 1, padx = 2, sticky = "NSEW")

#endregion



#----------------------------- GRID CONFIGURATIONS -------------------------------------------#
mainFrame.columnconfigure(2, weight = 1)
mainFrame.rowconfigure(1, weight = 1)
menuFrame.columnconfigure(0, weight = 1)
menuFrame.rowconfigure(1, weight = 1)
menuFrame.rowconfigure(2, weight = 1)
menuFrame.rowconfigure(3, weight = 1)
menuFrame.rowconfigure(4, weight = 1)
orderFrame.columnconfigure(0, weight = 1)
orderFrame.rowconfigure(2, weight = 1)



root.mainloop()