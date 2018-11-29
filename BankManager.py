from tkinter import * 
import tkinter.messagebox

class BankManager: 
	def __init__(self): 
		window = Tk()
		window.title("Bank Manager")
		#just some data to start out and test with 
		self.checkingBalance = 150.00
		self.savingsBalance = 500.00
		self.transactionHistory = []
		
		##############
		#deposit section
		##############
		
		mainFrame = Frame(window)
		mainFrame.grid(row = 2, column = 1, stick = W)
		
		pictureFrame = Frame(window)
		pictureFrame.grid(row = 2, column = 2, stick = E)
		
		dollarLogo = PhotoImage(file = "C:/dollarsign.gif")
		
		Label(pictureFrame, image = dollarLogo).pack(side = RIGHT)
		
		Label(mainFrame, text = "Make a Deposit", justify = CENTER, font = "Helvetica 18 bold").grid(row = 1, column = 1, pady = 10) 
		
		Label(mainFrame, text = "Enter Deposit Amount").grid(row = 2, column = 1, stick = W, pady = 10)
		
		self.depositAmount = StringVar()
		Entry(mainFrame, textvariable = self.depositAmount, 
		justify = RIGHT).grid(row = 2, column = 2, stick = W, pady = 10)
				
		self.depositOption = IntVar()
		rbChecking = Radiobutton(mainFrame, text = "Checking", variable = self.depositOption,
			value = 1).grid(row = 2, column = 3, stick = W, pady = 10)
			
		rbSaving = Radiobutton(mainFrame, text = "Savings", variable = self.depositOption,
			value = 2).grid(row = 2, column = 4, stick = W, pady = 10)

		btDeposit = Button(mainFrame, text = "Deposit Now",
			command = self.addDepositInput).grid(row = 2, column = 5, stick = W, pady = 10)
		

		##############
		#account transfer section
		##############
		Label(mainFrame, text = "Funds Transfer", justify = CENTER, font = "Helvetica 18 bold").grid(row = 3, column = 1, pady = 10) 
		
		Label(mainFrame, text = "Enter Transfer Amount").grid(row = 4, column = 1, stick = W, pady = 10)
		
		self.transferAmount = StringVar()
		Entry(mainFrame, textvariable = self.transferAmount, 
		justify = RIGHT).grid(row = 4, column = 2, stick = W, pady = 10)
				
		self.transferOption = IntVar()
		rbChecking = Radiobutton(mainFrame, text = "Checking to Savings", variable = self.transferOption,
			value = 1).grid(row = 4, column = 3, stick = W, pady = 10)
			
		rbSaving = Radiobutton(mainFrame, text = "Savings to Checking", variable = self.transferOption,
			value = 2).grid(row = 4, column = 4, stick = W, pady = 10)

		btDeposit = Button(mainFrame, text = "Transfer Now",
			command = self.addTransferInput).grid(row = 4, column = 5, stick = W, pady = 10)
		
		######################
		#withdrawal section
		######################
		
		Label(mainFrame, text = "Withdraw Funds", justify = CENTER, font = "Helvetica 18 bold").grid(row = 5, column = 1, pady = 10) 
		
		Label(mainFrame, text = "Enter Withdrawal Amount").grid(row = 6, column = 1, stick = W, pady = 10)
		
		self.withdrawAmount = StringVar()
		Entry(mainFrame, textvariable = self.withdrawAmount, 
		justify = RIGHT).grid(row = 6, column = 2, stick = W, pady = 10)
				
		self.withdrawOption = IntVar()
		rbChecking = Radiobutton(mainFrame, text = "Withdraw Checking", variable = self.withdrawOption,
			value = 1).grid(row = 6, column = 3, stick = W, pady = 10)
			
		rbSaving = Radiobutton(mainFrame, text = "Withdraw Savings", variable = self.withdrawOption,
			value = 2).grid(row = 6, column = 4, stick = W, pady = 10)

		btDeposit = Button(mainFrame, text = "Withdraw Now",
			command = self.withdrawInput).grid(row = 6, column = 5, stick = W, pady = 10)
			
		###################
		#View account History section
		####################
		
		btViewHistory = Button(mainFrame, text = "View Account History", 
			command = self.viewTransactionHistory).grid(row = 7, column = 1, stick = W, pady = 10)
		
		window.mainloop()
		
		
	def addDepositInput(self):
	#checking conditions for the radio buttons and which account to add to 
		if(self.depositOption.get() == 1):
			self.checkingBalance += float(self.depositAmount.get())
			self.transactionHistory.append("Account: Checking Type: Deposit " + "Amount: " + self.depositAmount.get() + " Balance: " + str(self.checkingBalance))
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
			
	def withdrawInput(self):
		#checking conditions for the radio buttons and which account to add to 
		if(self.withdrawOption.get() == 1):
			self.checkingBalance -= float(self.withdrawAmount.get())
		else:
			self.savingsBalance -= float(self.withdrawAmount.get())
				
		#clearing the text box 
		self.withdrawAmount.set("")
		tkinter.messagebox.showinfo("Deposit", "Deposit successful! " + "savings " + str(self.savingsBalance) +
			" checking " + str(self.checkingBalance))
			
	def viewTransactionHistory(self):
		outputText = "-----------------Recent Transaction History-----------------------\n"
		for each in self.transactionHistory:
			outputText += each + "\n"
		
		print(outputText)
		tkinter.messagebox.showinfo("Recent Transactions", outputText)
			
BankManager()