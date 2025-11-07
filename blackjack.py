import tkinter as tk
from tkinter import messagebox
import random
import os
import sys

class BlackjackGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Blackjack - Bank: $100")
        self.bank = 100.0  # start bank
        self.bet = 0.0
        self.deck = []
        self.player_hand = []
        self.dealer_hand = []
        self.in_round = False

        # UI Setup
        self.top_frame = tk.Frame(root)
        self.top_frame.pack(pady=10)

        self.dealer_label = tk.Label(self.top_frame, text="Dealer:", font=("Helvetica", 14))
        self.dealer_label.pack()
        self.dealer_cards = tk.Label(self.top_frame, text="", font=("Courier", 14))
        self.dealer_cards.pack()

        self.mid_frame = tk.Frame(root)
        self.mid_frame.pack(pady=10)

        # Bet and chips
        self.bank_label = tk.Label(self.mid_frame, text=f"Bank: ${self.bank:.2f}", font=("Helvetica", 12))
        self.bank_label.grid(row=0, column=0, padx=5)
        self.bet_label = tk.Label(self.mid_frame, text=f"Bet: ${self.bet:.2f}", font=("Helvetica", 12))
        self.bet_label.grid(row=0, column=1, padx=5)

        chips = [1, 5, 10, 25]
        for i, c in enumerate(chips):
            btn = tk.Button(self.mid_frame, text=f"+${c}", command=lambda c=c: self.add_chip(c))
            btn.grid(row=1, column=i, padx=3)

        self.clear_bet_btn = tk.Button(self.mid_frame, text="Clear Bet", command=self.clear_bet)
        self.clear_bet_btn.grid(row=2, column=0, pady=5)
        self.deal_btn = tk.Button(self.mid_frame, text="Deal", command=self.start_round)
        self.deal_btn.grid(row=2, column=1)

        # Player area
        self.player_label = tk.Label(root, text="Player:", font=("Helvetica", 14))
        self.player_label.pack()
        self.player_cards = tk.Label(root, text="", font=("Courier", 14))
        self.player_cards.pack()

        # Controls
        self.controls = tk.Frame(root)
        self.controls.pack(pady=10)
        self.hit_btn = tk.Button(self.controls, text="Hit", state=tk.DISABLED, command=self.player_hit)
        self.hit_btn.grid(row=0, column=0, padx=5)
        self.stand_btn = tk.Button(self.controls, text="Stand", state=tk.DISABLED, command=self.player_stand)
        self.stand_btn.grid(row=0, column=1, padx=5)
        self.new_round_btn = tk.Button(self.controls, text="New Round", state=tk.DISABLED, command=self.reset_round)
        self.new_round_btn.grid(row=0, column=2, padx=5)

        self.message_label = tk.Label(root, text="", font=("Helvetica", 12))
        self.message_label.pack(pady=5)

        # Prepare deck
        self.new_deck()

    # Deck and helper methods
    def new_deck(self):
        ranks = ['A'] + [str(n) for n in range(2, 11)] + ['J', 'Q', 'K']
        suits = ['♠', '♥', '♦', '♣']
        self.deck = [r + s for r in ranks for s in suits]
        random.shuffle(self.deck)

    def draw_card(self):
        if len(self.deck) < 10:
            self.new_deck()
        return self.deck.pop()

    def card_value(self, card):
        rank = card[:-1]  # card like '10♠' or 'A♥'
        if rank in ['J', 'Q', 'K']:
            return 10
        if rank == 'A':
            return 11  # treat Ace as 11 initially
        return int(rank)

    def hand_value(self, hand):
        total = 0
        aces = 0
        for c in hand:
            rank = c[:-1]
            if rank == 'A':
                aces += 1
                total += 11
            elif rank in ['J', 'Q', 'K']:
                total += 10
            else:
                total += int(rank)
        # degrade aces from 11 to 1 as needed
        while total > 21 and aces > 0:
            total -= 10
            aces -= 1
        return total

    # Betting methods
    def add_chip(self, amount):
        if self.in_round:
            return
        if self.bet + amount > self.bank:
            self.bet = self.bank  # can't bet more than you have
        else:
            self.bet += amount
        self.update_labels()

    def clear_bet(self):
        if self.in_round:
            return
        self.bet = 0.0
        self.update_labels()

    def update_labels(self):
        self.bank_label.config(text=f"Bank: ${self.bank:.2f}")
        self.bet_label.config(text=f"Bet: ${self.bet:.2f}")

    # Round control
    def start_round(self):
        if self.in_round:
            return
        if self.bet <= 0:
            messagebox.showinfo("Bet", "Place a bet first.")
            return
        if self.bet > self.bank:
            messagebox.showinfo("Bet", "You cannot bet more than your bank.")
            return
        # subtract bet from bank (we hold it)
        self.bank -= self.bet
        self.in_round = True
        self.dealer_hand = [self.draw_card(), self.draw_card()]
        self.player_hand = [self.draw_card(), self.draw_card()]
        self.update_labels()
        self.show_hands(initial=True)
        self.hit_btn.config(state=tk.NORMAL)
        self.stand_btn.config(state=tk.NORMAL)
        self.deal_btn.config(state=tk.DISABLED)
        self.clear_bet_btn.config(state=tk.DISABLED)
        self.message_label.config(text="Round started. Good luck!")
        # check for immediate blackjack
        pval = self.hand_value(self.player_hand)
        if pval == 21:
            self.end_round(check_blackjack=True)

    def show_hands(self, initial=False, reveal_dealer=False):
        # show player
        self.player_cards.config(text="  ".join(self.player_hand) + f"   ({self.hand_value(self.player_hand)})")
        # show dealer (hide hole card if initial)
        if initial and not reveal_dealer:
            if len(self.dealer_hand) >= 2:
                shown = [self.dealer_hand[0], "??"]
                self.dealer_cards.config(text="  ".join(shown))
            else:
                self.dealer_cards.config(text="")
        else:
            self.dealer_cards.config(text="  ".join(self.dealer_hand) + f"   ({self.hand_value(self.dealer_hand)})")
        self.update_labels()

    def player_hit(self):
        if not self.in_round:
            return
        self.player_hand.append(self.draw_card())
        self.show_hands(initial=True)
        pval = self.hand_value(self.player_hand)
        if pval > 21:
            self.end_round()

    def player_stand(self):
        if not self.in_round:
            return
        # Dealer plays
        self.dealer_play()
        self.end_round()

    def dealer_play(self):
        # reveal dealer card and draw until 17 or more
        while self.hand_value(self.dealer_hand) < 17:
            self.dealer_hand.append(self.draw_card())
        self.show_hands(initial=False, reveal_dealer=True)

    def end_round(self, check_blackjack=False):
        # Determine outcome and pay
        self.show_hands(initial=False, reveal_dealer=True)
        pval = self.hand_value(self.player_hand)
        dval = self.hand_value(self.dealer_hand)
        result = ""
        # Blackjack handling
        if check_blackjack and pval == 21:
            if dval == 21:
                result = "Push (both Blackjack)"
                self.bank += self.bet  # return bet
            else:
                result = "Blackjack! You win 3:2"
                self.bank += self.bet * 2.5  # return bet + 1.5*bet
        else:
            if pval > 21:
                result = "Bust! You lose."
                # bet already lost
            elif dval > 21:
                result = "Dealer busts! You win."
                self.bank += self.bet * 2
            elif pval > dval:
                result = "You win!"
                self.bank += self.bet * 2
            elif pval == dval:
                result = "Push."
                self.bank += self.bet
            else:
                result = "You lose."
        # reset in_round and buttons
        self.in_round = False
        self.hit_btn.config(state=tk.DISABLED)
        self.stand_btn.config(state=tk.DISABLED)
        self.new_round_btn.config(state=tk.NORMAL)
        self.deal_btn.config(state=tk.DISABLED)
        self.clear_bet_btn.config(state=tk.NORMAL)
        self.message_label.config(text=result)
        self.bet = 0.0
        self.update_labels()
        # check bank zero
        if self.bank <= 0:
            # Safety: we will NOT automatically shut down the user's PC.
            # Instead show a clear game-over dialog and close the program.
            messagebox.showwarning("Game over", "Sei arrivato a $0. Il gioco si chiuderà per sicurezza.\n\nNota: non spegnerò automaticamente il tuo PC per motivi di sicurezza.")
            self.root.after(1000, self.root.destroy)
            # If you *really* want to enable automatic shutdown on your own machine,
            # you could uncomment the following line and implement `attempt_shutdown()`.
            # BE VERY CAREFUL: shutdown commands will close your system!
            # self.attempt_shutdown()

    def reset_round(self):
        self.player_hand = []
        self.dealer_hand = []
        self.bet = 0.0
        self.in_round = False
        self.hit_btn.config(state=tk.DISABLED)
        self.stand_btn.config(state=tk.DISABLED)
        self.new_round_btn.config(state=tk.DISABLED)
        self.deal_btn.config(state=tk.NORMAL)
        self.clear_bet_btn.config(state=tk.NORMAL)
        self.message_label.config(text="")
        self.show_hands(initial=False, reveal_dealer=False)
        self.update_labels()

    # Optional dangerous method (disabled by default)
    def attempt_shutdown(self):
        """
        Dangerous: will attempt to shut down the machine. Requires permissions and may prompt for password.
        This method is intentionally NOT called by default. If you uncomment the call in end_round(),
        use at your own risk.
        """
        if sys.platform.startswith("win"):
            # Windows
            try:
                os.system("shutdown /s /t 0")
            except Exception as e:
                messagebox.showerror("Shutdown failed", str(e))
        elif sys.platform.startswith("linux") or sys.platform.startswith("darwin"):
            # Linux / macOS (may require sudo)
            try:
                os.system("shutdown -h now")
            except Exception as e:
                messagebox.showerror("Shutdown failed", str(e))
        else:
            messagebox.showinfo("Shutdown", "Shutdown not supported on this platform by this script.")


if __name__ == "__main__":
    root = tk.Tk()
    app = BlackjackGame(root)
    root.mainloop()
