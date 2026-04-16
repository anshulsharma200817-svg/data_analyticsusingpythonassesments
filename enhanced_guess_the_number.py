import random
import time
import os

# ANSI Color Codes for terminal styling
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    """Prints a stylish ASCII art banner."""
    banner = f"""
{Colors.CYAN}
  /$$   /$$                                                
 | $$$ | $$                                                
 | $$$$| $$ /$$   /$$ /$$$$$$/$$$$   /$$$$$$$  /$$$$$$     
 | $$ $$ $$| $$  | $$| $$_  $$_  $$ /$$_____/ /$$__  $$    
 | $$  $$$$| $$  | $$| $$ \ $$ \ $$| $$      | $$$$$$$$    
 | $$\  $$$| $$  | $$| $$ | $$ | $$| $$      | $$_____/    
 | $$ \  $$|  $$$$$$/| $$ | $$ | $$|  $$$$$$$|  $$$$$$$    
 |__/  \__/ \______/ |__/ |__/ |__/ \_______/ \_______/    
                                                           
  /$$$$$$                                                  
 /$$__  $$                                                 
| $$  \__/ /$$   /$$  /$$$$$$   /$$$$$$$  /$$$$$$$         
| $$ /$$$$| $$  | $$ /$$__  $$ /$$_____/ /$$_____/         
| $$|_  $$| $$  | $$| $$$$$$$$|  $$$$$$ |  $$$$$$          
| $$  \ $$| $$  | $$| $$_____/ \____  $$ \____  $$         
|  $$$$$$/|  $$$$$$/|  $$$$$$$ /$$$$$$$/ /$$$$$$$/         
 \______/  \______/  \_______/|_______/ |_______/          
{Colors.END}
    """
    print(banner)

def get_difficulty():
    """Prompts the user to select a difficulty level with visual cues."""
    print(f"{Colors.HEADER}{Colors.BOLD}--- SELECT DIFFICULTY ---{Colors.END}")
    print(f"{Colors.GREEN}1. Easy   {Colors.END} (Range: 1-10,  Attempts: 5)")
    print(f"{Colors.YELLOW}2. Medium {Colors.END} (Range: 1-50,  Attempts: 7)")
    print(f"{Colors.RED}3. Hard   {Colors.END} (Range: 1-100, Attempts: 10)")
    
    while True:
        choice = input(f"\n{Colors.BOLD}Enter choice (1/2/3): {Colors.END}").strip()
        if choice == '1':
            return 1, 10, 5, "Easy"
        elif choice == '2':
            return 1, 50, 7, "Medium"
        elif choice == '3':
            return 1, 100, 10, "Hard"
        else:
            print(f"{Colors.RED}Invalid choice. Please enter 1, 2, or 3.{Colors.END}")

def play_game():
    """Enhanced main game loop."""
    clear_screen()
    print_banner()
    
    low, high, max_attempts, level_name = get_difficulty()
    secret_number = random.randint(low, high)
    
    clear_screen()
    print_banner()
    print(f"{Colors.BOLD}Difficulty:{Colors.END} {Colors.BLUE}{level_name}{Colors.END}")
    print(f"{Colors.BOLD}Range:{Colors.END} {low} to {high}")
    print(f"{Colors.BOLD}Attempts Allowed:{Colors.END} {max_attempts}")
    print(f"\n{Colors.YELLOW}I'm thinking of a number...{Colors.END}")
    time.sleep(1)
    
    for attempt in range(1, max_attempts + 1):
        try:
            prompt = f"\n{Colors.BOLD}Attempt {attempt}/{max_attempts} - Enter your guess: {Colors.END}"
            guess = int(input(prompt))
        except ValueError:
            print(f"{Colors.RED}Oops! Please enter a valid integer.{Colors.END}")
            continue

        if guess < secret_number:
            print(f"{Colors.BLUE}Too low! 📉{Colors.END}")
        elif guess > secret_number:
            print(f"{Colors.RED}Too high! 📈{Colors.END}")
        else:
            print(f"\n{Colors.GREEN}{Colors.BOLD}🎉 CONGRATULATIONS! 🎉{Colors.END}")
            print(f"{Colors.GREEN}You guessed the number {secret_number} in {attempt} attempts!{Colors.END}")
            return

    print(f"\n{Colors.RED}{Colors.BOLD}GAME OVER! 💀{Colors.END}")
    print(f"{Colors.RED}You've run out of attempts. The number was {secret_number}.{Colors.END}")

if __name__ == "__main__":
    try:
        while True:
            play_game()
            print(f"\n{'-'*30}")
            play_again = input(f"{Colors.BOLD}Play again? (y/n): {Colors.END}").lower().strip()
            if play_again != 'y':
                print(f"\n{Colors.CYAN}Thanks for playing! Goodbye! 👋{Colors.END}")
                break
    except KeyboardInterrupt:
        print(f"\n\n{Colors.CYAN}Game exited. See you next time!{Colors.END}")
