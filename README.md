# FinalProjectPython
Python Final Project

from tkinter import *
import tkinter.messagebox

class BankManager:
	def __init__(self):
		window = Tk()
		window.title("Bank Manager")
		
		#just some data to start out and test with 
		self.checkingBalance = 150.00
		self.savingsBalance = 500.00
		
		##############
		#deposit section
		##############
		
		Label(window, text = "Make a Deposit", justify = CENTER, font = "Times 15 bold").grid(row = 1, column = 1) 
		
		Label(window, text = "Enter Deposit Amount").grid(row = 2, column = 1, stick = W)
		
		self.depositAmount = StringVar()
		Entry(window, textvariable = self.depositAmount, 
		justify = RIGHT).grid(row = 2, column = 2, stick = W)
				
		self.depositOption = IntVar()
		rbChecking = Radiobutton(window, text = "Checking", variable = self.depositOption,
			value = 1).grid(row = 2, column = 3, stick = W)
			
		rbSaving = Radiobutton(window, text = "Savings", variable = self.depositOption,
			value = 2).grid(row = 2, column = 4, stick = W)

		btDeposit = Button(window, text = "Deposit Now",
			command = self.addDepositInput).grid(row = 2, column = 5, stick = W)
		

		##############
		#account transfer section
		##############
		Label(window, text = "Funds Transfer", justify = CENTER, font = "Times 15 bold").grid(row = 3, column = 1) 
		
		Label(window, text = "Enter Transfer Amount").grid(row = 4, column = 1, stick = W)
		
		self.transferAmount = StringVar()
		Entry(window, textvariable = self.transferAmount, 
		justify = RIGHT).grid(row = 4, column = 2, stick = W)
				
		self.transferOption = IntVar()
		rbChecking = Radiobutton(window, text = "Checking to Savings", variable = self.transferOption,
			value = 1).grid(row = 4, column = 3, stick = W)
			
		rbSaving = Radiobutton(window, text = "Savings to Checking", variable = self.transferOption,
			value = 2).grid(row = 4, column = 4, stick = W)

		btDeposit = Button(window, text = "Transfer Now",
			command = self.addTransferInput).grid(row = 4, column = 5, stick = W)
		
			
		window.mainloop()
		
		
	def addDepositInput(self):
	#checking conditions for the radio buttons and which account to add to 
		if(self.depositOption.get() == 1):
			self.checkingBalance += float(self.depositAmount.get())
		else:
			self.savingsBalance += float(self.depositAmount.get())
				
		#clearing the text box 
		self.depositAmount.set("")
		tkinter.messagebox.showinfo("Deposit", "Deposit successful! " + "savings " + str(self.savingsBalance) +
			" checking " + str(self.checkingBalance))
		
	def addTransferInput(self):
	#checking conditions for the radio buttons and which account to transfer to and from  
		if(self.transferOption.get() == 1):
			self.checkingBalance -= float(self.transferAmount.get())
			self.savingsBalance += float(self.transferAmount.get())
		else:
			self.savingsBalance -= float(self.transferAmount.get())
			self.checkingBalance += float(self.transferAmount.get())
			
			#clearing the text box
		self.transferAmount.set("")
		tkinter.messagebox.showinfo("Transfer", "Transfer successful! " + "savings " + str(self.savingsBalance) + 
			" checking " + str(self.checkingBalance))
		
BankManager()
