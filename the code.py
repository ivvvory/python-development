import cv2
import numpy as np 

print("calculator")

# Define mathematical functions
def Mod_maths():
    ab = int(input("Pick a value for A (must be a whole number): "))
    bc = int(input("Pick a value for B (must be a whole number): "))
    result = ab % bc
    print("Your MOD value is:", result)
    return result

def Divd_maths():
    aa = int(input("Pick a value for A (must be a whole number): "))
    bb = int(input("Pick a value for B (must be a whole number): "))
    result = aa / bb
    print("Your floating point divided value is:", result)
    return result

def addition_maths():
    ac = int(input("Pick a value for A (must be a whole number): "))
    bc = int(input("Pick a value for B (must be a whole number): "))
    result = ac + bc
    print("Your addition value is:", result)
    return result

def floordiv_maths():
    ac = int(input("Pick a value for A (must be a whole number): "))
    bc = int(input("Pick a value for B (must be a whole number): "))
    result = ac // bc
    print("Your floor division value is:", result)
    return result

def exp_maths():
    ac = int(input("Pick a value for A (must be a whole number): "))
    bc = int(input("Pick a value for B (must be a whole number): "))
    result = ac ** bc
    print("Your exponent value is:", result)
    return result

def sub_maths():
    ac = int(input("Pick a value for A (must be a whole number): "))
    bc = int(input("Pick a value for B (must be a whole number): "))
    result = ac - bc
    print("Your subtraction value is:", result)
    return result

def multi_maths():
    ac = int(input("Pick a value for A (must be a whole number): "))
    bc = int(input("Pick a value for B (must be a whole number): "))
    result = ac * bc
    print("Your multiplication value is:", result)
    return result

# List to store past answers
past_answers = []

# Main loop
while True:
    # Prompt user for mathematical function
    x = input("Choose your mathematical function (Mod_maths, Divd_maths, multi_maths, sub_maths, exp_maths, floordiv_maths, addition_maths), or type 'history' to view past answers, or 'exit' to quit: ")

    if x == "Mod_maths":
        past_answers.append(Mod_maths())
    elif x == "Divd_maths":
        past_answers.append(Divd_maths())
    elif x == "multi_maths":
        past_answers.append(multi_maths())
    elif x == "sub_maths":
        past_answers.append(sub_maths())
    elif x == "exp_maths":
        past_answers.append(exp_maths())
    elif x == "addition_maths":
        past_answers.append(addition_maths())
    elif x == "floordiv_maths":
        past_answers.append(floordiv_maths())
    elif x.lower() == "history":
        print("Past answers: ", past_answers)
    elif x.lower() == "exit":
        print("Exiting calculator.")
        break
    else:
        print("Invalid option. Please try again.")

img = cv2.imread('OIP(8).JFIF', 1) ##image read.
cv2.imshow('OIP(8)', img) ##show image
##wait for key to close
cv2.waitKey(0)
cv2.destroyAllWindows()
