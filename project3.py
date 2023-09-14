import random
import time

OPERATORS = ["+", "-", "*"]
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROBLEMS = 10

#create a funtion to generate math question ramdomly 
def generate_problem():
    left = random.randint(MIN_OPERAND,MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)

    expr = str(left) + " " + operator + " " + str(right)
    answer =eval(expr)
    return expr, answer

wrong = 0
input("press enter to start")
print("-------------------------")

# mark the start time
start_time = time.time()

# funtion of run through all 10 math question 
for i in range(TOTAL_PROBLEMS):
    expr, answer = generate_problem()
    while True:
     guess = input("Problem #" + str(i + 1) + ": " + expr + " = ")
     if guess == str(answer):
        break

# mark the end time
end_time = time.time()
# calculate the used time
total_time = round(end_time - start_time, 2)
     
print("-------------------------")
print("Nice work! You finished in", total_time, "seconds!")
