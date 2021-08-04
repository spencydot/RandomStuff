import time

def clime():
    print("3N+1 Problem, define N and see how far you can go: ")
    start_number = int(input())
    count = 0
    while True:
        time.sleep(.05)
        if (start_number % 2) == 0:
            start_number = start_number / 2
            count += 1
            print("Even " , start_number)
        else:
            start_number = (start_number * 3) + 1
            count += 1
            
            print("Odd  " , start_number)
        if start_number == 1:
            print("You got ", count, "m far")
            clime()#Restart the program
clime()            

#This program uses the 3N+1 Formular for this Clime program
#Enter a number, if its odd it will * 3 + 1 the number else it will / 2 this formular will allways end in a loop of 2 / 2 = 1 * 3 + 1 = 4 / 2 = 2 ect ect 
#This prgram was made by Me SPENCY - feel free to use this for what you want i dont care
