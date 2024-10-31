import random

max_score = 21

def score2points ():
    return random.randint(0,1)

def rebound ():
    return random.choice(["You got the ball back!", "Your Opponent rebounded the ball!" ])

def opponent_offense ():
    return random.choice (["Your opponent passed the ball!", "Your Opponent shot the ball!"])

steal_chance = 8

# This is the function that checks if the ball is stolen
def steal_ball():
    # Generate a random number between 0 and 1
    random_number = random.randint(0,10)
    # If the random number is less than the steal chance, the ball is stolen
    if random_number > steal_chance:
        return True
    # Otherwise, the ball is not stolen
    else:
        return False

def main():
    my_score = 0
    opponent_score = 0

    print("Welcome to the Basketball Game 21!")
    print("You have to score more points than your opponent to win.")
    print("You can choose to pass or shoot the ball.")
   

   
   

    while True:
        shot = input("Will you pass, or shoot? : ")
        if shot.lower() == "shoot":
            if score2points() == 1:
               my_score += 2
               print(f"You scored 2 points! Your team score is now {my_score}, Your opponents team score is {opponent_score}. ")

               if my_score >= max_score:
                   print(f"You won the game {my_score} to {opponent_score}!")
                   break
            else:
                print("You missed")
                rebound_result = rebound()
                print(rebound_result)
                if rebound_result == "You got the ball back!":
                    continue
                else:
                    while True:
                        opponent_offense_result = opponent_offense()
                        print(opponent_offense_result)
                        if opponent_offense_result == "Your opponent passed the ball!":
                            steal = input("Will you go for the steal? Type yes or no:")
                            if steal.lower() == "yes":
                               
                                steal_ball()
                                if steal_ball() == True:
                                   
                                    print("You stole the ball!")
                                    break
                                else:
                                    steal_ball() == False
                                   
                                    print("You didn't get the steal!")
                                   
                            else:
                               
                           
                                continue
                        else:
                            if score2points() == 1:
                                opponent_score += 2
                                print(f"Your opponent scored 2 points! Your opponents team score is now {opponent_score}, Your team score is {my_score}.. ")
                                if opponent_score >= max_score:
                                    print(f"You lost the game {opponent_score} to {my_score}")
                                    break
                            else:
                                print("Your opponent missed.")
                                rebound_result = rebound()
                                print(rebound_result)
                                if rebound_result == "Your Opponent rebounded the ball!":
                                    continue

                                else:
                                    break
                   
       
                    if opponent_score >= max_score:
                        break
       
           
       
        elif shot.lower() == "pass":
            print("You passed the ball.")
        else:
            print("Invalid input. Please enter eiter 'pass' or 'shoot'.")
            continue

if __name__ == "__main__":
    main()