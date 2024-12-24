from tkinter import *

# Function to load boycott brands from the file
def boycott_brands_function():
   with open(r'C:\Users\malak\Desktop\Boycott Brands.txt', 'r') as file:
           brands = file.read() .splitlines()
           return brands
        
    

# Function to check if the company is on the boycott list
def check_boycott():
    company_name = entry1.get() .capitalize()
    if company_name in boycott_brands:
        result_lable.config(text=f"{company_name} this company on the boycott list.")
    else:
        result_lable.config(text=f"{company_name} this company isn't on the boycott list.")

# Load the boycott brands from the file
boycott_brands = boycott_brands_function()

# Create the main window
window = Tk()  
window.title("Boycott Brands Checker")
window.geometry('1500x1000')
window.config(bg='pink')

# Create and place the Entry widget
entry1 = Entry(window, font=('sansserif',20) ,fg='maroon',bg='snow2')  
entry1.place(x=300,y=200)

# Create and place the Check Button
check_button =Button(window, text="Check Boycott Status", command=check_boycott,bg='lavender')  
check_button.place(x=390,y=250)


# Create and place the Result Label
label1 = Label(window, text="company name:",font=('sansserif',20),bg='sky blue', fg='navy blue')  
label1.place(x=350,y=150)

#create and place the result for output
result_lable=Label(window, text="the result",font=('sansserif',20),bg='sky blue', fg='navy blue')
result_lable.place(x=200,y=400)

# Run the application
window.mainloop() 