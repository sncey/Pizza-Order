from PyQt5.QtWidgets import *
from PizzaOrderWindow import Ui_MainWindow
import csv
from datetime import datetime
import pizzaOrder


class main(QMainWindow):
    def __init__(self):
        self.price_pizza = 0    # Variable that holds the price of the chosen pizza base
        self.price_sauce = 0    # Variable that holds the price of selected sauces
        self.pizza2 = ""        # Selected pizza base
        self.sauce_list = []    # List of selected sauces
        self.database_list = [] # List of information to be sent to the database

        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Assigning a method to the payment completion button
        self.ui.pushButton_finish.clicked.connect(self.FinishClicked)
        
        # Assigning methods to CheckBoxes
        self.ui.btn_group = QButtonGroup() #  Grouping pizza boxes, only one can be selected.
        self.ui.btn_group.addButton(self.ui.cbox_clasic,1)
        self.ui.btn_group.addButton(self.ui.cbox_margharita,2)
        self.ui.btn_group.addButton(self.ui.cbox_turkish,3)
        self.ui.btn_group.addButton(self.ui.cbox_simple,4)

        self.ui.cbox_clasic.toggled.connect(self.pizza) # Pizza boxes
        self.ui.cbox_margharita.toggled.connect(self.pizza)
        self.ui.cbox_turkish.toggled.connect(self.pizza)
        self.ui.cbox_simple.toggled.connect(self.pizza)

        self.ui.cbox_sauce_olive.toggled.connect(self.sauce) # Sauce boxes
        self.ui.cbox_sauce_mushroom.toggled.connect(self.sauce)
        self.ui.cbox_sauce_goatCheese.toggled.connect(self.sauce)
        self.ui.cbox_sauce_meat.toggled.connect(self.sauce)
        self.ui.cbox_sauce_onion.toggled.connect(self.sauce)
        self.ui.cbox_sauce_corn.toggled.connect(self.sauce)
        
    
    # Methods related to CheckBoxes
    def pizza(self): # Pizza Method
        choose = self.sender()
        if choose.isChecked():
            self.price_pizza = 0
            match choose:
                case self.ui.cbox_clasic:
                    self.pizza2 = "Classic Pizza"
                    self.price_pizza += pizzaOrder.Clasic().get_cost()
                case self.ui.cbox_margharita:
                    self.pizza2 = "Pizza with Margherita Cheese"
                    self.price_pizza += pizzaOrder.Margherita().get_cost()
                case self.ui.cbox_turkish:
                    self.pizza2 = "Turkish Pizza"
                    self.price_pizza += pizzaOrder.Turkish().get_cost()
                case self.ui.cbox_simple:
                    self.pizza2 = "Plain Pizza"
                    self.price_pizza += pizzaOrder.Simple().get_cost()
        self.ui.line_price.setText(str(self.price_pizza + self.price_sauce)+" $")
    
    def sauce(self):  # Sauce Method
        choose = self.sender()  # Function that returns the selected checkBox
        if choose.isChecked():     
            match choose:    # Assignment of action according to the selected checkbox with the match - case structure
                case self.ui.cbox_sauce_olive:
                    self.sauce_list.append("Olive")  # Olive is added to sauce_list when selected
                    self.price_sauce += pizzaOrder.Olive().get_cost()  # We add the olive amount to the general amount with the get_cost method that we call from the pizzaOrder class.
                case self.ui.cbox_sauce_mushroom:
                    self.sauce_list.append("Mushroom")
                    self.price_sauce += pizzaOrder.Mushroom().get_cost()
                case self.ui.cbox_sauce_goatCheese:
                    self.sauce_list.append("Goat Cheese")
                    self.price_sauce += pizzaOrder.GoatCheese().get_cost()
                case self.ui.cbox_sauce_meat:
                    self.sauce_list.append("Meat")
                    self.price_sauce += pizzaOrder.Meat().get_cost()
                case self.ui.cbox_sauce_onion:
                    self.sauce_list.append("Onion")
                    self.price_sauce += pizzaOrder.Onion().get_cost()
                case self.ui.cbox_sauce_corn:
                    self.sauce_list.append("Corn")
                    self.price_sauce += pizzaOrder.Corn().get_cost()
        else:
            match choose:       # With the match - case structure, we assign operations according to the checkbox whose selection is abandoned.
                case self.ui.cbox_sauce_olive:
                    self.sauce_list.remove("Olive")    # When olive selection is abandoned, we remove it from the sauce_list list.
                    self.price_sauce -= pizzaOrder.Olive().get_cost() # We subtract the olive amount from the general amount with the get_cost method that we call from the pizzaOrder class.

                case self.ui.cbox_sauce_mushroom:
                    self.sauce_list.remove("Mushroom")
                    self.price_sauce -= pizzaOrder.Mushroom().get_cost()
                case self.ui.cbox_sauce_goatCheese:
                    self.sauce_list.remove("Goat Cheese")
                    self.price_sauce -= pizzaOrder.GoatCheese().get_cost()
                case self.ui.cbox_sauce_meat:
                    self.sauce_list.remove("Meat")
                    self.price_sauce -= pizzaOrder.Meat().get_cost()
                case self.ui.cbox_sauce_onion:
                    self.sauce_list.remove("Onion")
                    self.price_sauce -= pizzaOrder.Onion().get_cost()
                case self.ui.cbox_sauce_corn:
                    self.sauce_list.remove("Corn")
                    self.price_sauce -= pizzaOrder.Corn().get_cost()
        
        self.ui.line_price.setText(str(self.price_pizza + self.price_sauce)+" $") # We transfer the account made to the line showing the amount.
    

    # Complete Payment Button method
    def FinishClicked(self):
        
        if not(self.ui.line_price.text() and self.ui.line_name.text() and self.ui.line_id.text() and self.ui.line_credit_number.text() and self.ui.line_price.text() and self.ui.line_credit_pass.text()):
            QMessageBox.about(self, "Error", "Please enter all your information.") # Error message sent to the user in case of missing information.
        else:
            now = datetime.now()        # With the datetime module we get the time when the key is pressed
            time = now.strftime("%Y-%m-%d %H:%M:%S")    # We changed the format because we don't want milliseconds to be displayed.

            sauce_list2 = []        
            for i in self.sauce_list:
                sauce_list2.append(i)

            user_info = {'Name':self.ui.line_name.text(),'Surname':self.ui.line_id.text(),'Credit Card Number':self.ui.line_credit_number.text(),'Credit Card Password':self.ui.line_credit_pass.text(),'Pizza Base':self.pizza2,'Sauces':sauce_list2,'Date':time}
            self.database_list.append(user_info)
            
            with open("Orders_Database.csv", "w") as file:  # We are printing to the Orders_Database.csv file
                fieldnames = self.database_list[0].keys()
                file_write =csv.DictWriter(file,fieldnames=fieldnames)
                file_write.writeheader()
                file_write.writerows(self.database_list) 
        
            # We clear the line and checkboxes so that the operation can be performed again after the button is pressed.
            self.ui.cbox_sauce_olive.setChecked(False)
            self.ui.cbox_sauce_mushroom.setChecked(False)
            self.ui.cbox_sauce_goatCheese.setChecked(False)
            self.ui.cbox_sauce_meat.setChecked(False)
            self.ui.cbox_sauce_onion.setChecked(False)
            self.ui.cbox_sauce_corn.setChecked(False)
            self.ui.line_name.setText("")
            self.ui.line_id.setText("")
            self.ui.line_credit_number.setText("")
            self.ui.line_credit_pass.setText("")
        
    


# GUI run processes 
app = QApplication([])
window = main()
window.show()
app.exec_()    

