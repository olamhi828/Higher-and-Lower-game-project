import random 
from Data import data_file

score=0
game_over=False
#display art
print(higher)
account_b=random.choice(data_file)

#generate two accounts
while not game_over:
    account_a=account_b
    account_b=random.choice(data_file)
    
    if account_a== account_b:
        account_b=random.choice(data_file)


    #formatting the account
    def format_account(account):
        account_name=account["name"]
        account_follower=account["followers"]
        account_dec=account["description"]
        account_country=account["country"]

        return f"{account_name} ,a {account_dec},from {account_country}"
    def check(guess,a_fol,b_fol):
        if guess=="a" and a_fol>b_fol:
            return True
        elif guess=="b" and b_fol>a_fol:
            return True
        else:
            return False
            
    print(f"Compare A: {format_account(account_a)}")
    print(vs)
    print(f"Compare B: {format_account(account_b)}\n")

    user_input=input("Who has more followers? Type 'A' or 'B' ").lower()
    print("\n"*10)
    print(higher)
    a_follower=account_a["followers"]
    b_follower=account_b["followers"]
    is_correct=check(user_input,a_follower,b_follower)
    if is_correct:
        print(f"You are right! Current Score = {score}")
        score+=1
    else:
        print(f"Sorry, You are wrong!. Final score= {score}")
        game_over=True





