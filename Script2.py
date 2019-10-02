#asks user for inputs
#returns string 
Temp = raw_input("Enter Fahrenheit or Celsius: ")
#returns number
num = input("Enter temperature: ")

#variables used to check input
F = "Fahrenheit"
C = "Celsius"

#function for celsius categories
def tempCelsius(num):
  if num >= 37:
    print "It is hot."
  elif 21 < num < 37:
    print "It is warm."
  elif 0 < num <= 21:
    print "It is cool."
  else:
    print "It is cold." 

#functions for fahrenheit categories
def tempFahrenheit(num):
  if num >= 100:
    print "It is hot."
  elif 70 < num < 100:
    print "It is warm."
  elif 32 < num <= 70:
    print "It is cool."
  else:
    print "It is cold."

#checks inputs
def answer(Temp):
  #if fahrenheit chosen call its function
  if F in Temp:
    tempFahrenheit(num)
  # if celsius chosen call its function
  elif C in Temp: 
    tempCelsius(num)
  # if input doesnt equal fahrenheit/celsius print..
  else:
    print ('Could Not Read')

#calls function
answer(Temp)
