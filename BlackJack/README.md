## 🃏 Blackjack Game (Python CLI)

This project is a command-line implementation of the classic Blackjack card game using Python. The game allows a user to play against a computer dealer by drawing cards and trying to reach a score as close to 21 as possible without exceeding it. At the start, both the user and the computer are dealt two cards. The user can choose to draw additional cards or stop, while the computer follows a predefined rule of drawing cards until its total reaches at least 17. The program automatically calculates scores, adjusts Ace values (11 to 1 when needed), and determines the final winner based on standard Blackjack rules.

## 🚀 Features
- Interactive command-line gameplay  
- Random card generation using Python  
- Real-time score calculation  
- Automatic Ace value adjustment (11 or 1)  
- Computer dealer logic (draws until 17)  
- Win / Lose / Draw result system  
- Clean and readable output  

## 🛠️ Tech Stack
- Python 3  
- Random module  
- Command Line Interface (CLI)

## 📌 Game Rules
- Both player and computer receive 2 cards  
- Number cards = face value  
- Face cards (J, Q, K) = 10  
- Ace = 11 or 1 (auto-adjusted)  
- Player can choose to hit or stand  
- Computer draws until score ≥ 17  
- Closest to 21 wins  
- Score > 21 = Bust (lose)  

## ▶️ How to Run
1. Clone the repository  
2. Open the project in any Python IDE  
3. Run main.py  
4. Follow the instructions in the terminal  

## 🎯 Learning Outcomes
- Understanding game logic implementation  
- Working with loops and conditions  
- Handling user input  
- Using lists and random module  
- Writing structured Python code  

## 📷 Sample Output

Your cards: [10, 6], total: 16
Computer first card: 10
Do you want another card? y/n: n

Final Results:
Your cards: [10, 6], total: 16
Computer cards: [10, 2, 7], total: 19
Computer wins.


## 💡 Future Improvements
- Add GUI (Tkinter / Streamlit)  
- Add betting system  
- Multiplayer support  
- Improve UI experience
