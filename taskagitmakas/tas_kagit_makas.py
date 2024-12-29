from abc import ABC, abstractmethod
import random

# Abstract sınıflar
class Player(ABC):
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.moves = []

    @abstractmethod
    def make_move(self):
        """Hamle yapma davranışı, alt sınıflar tarafından uygulanacak."""
        pass

class ComputerPlayer(Player):
    def __init__(self, name="Computer"):
        super().__init__(name)

# İnsan ve Bilgisayar Oyuncuları
class HumanPlayer(Player):
    def make_move(self):
        move = input(f"{self.name}, seçiminizi yapın (taş, kağıt, makas): ").lower()
        while move not in ["taş", "kağıt", "makas"]:
            move = input("Geçersiz seçim. Lütfen 'taş', 'kağıt' veya 'makas' yazın: ").lower()
        self.moves.append(move)
        return move

class RandomComputerPlayer(ComputerPlayer):
    def make_move(self):
        move = random.choice(["taş", "kağıt", "makas"])
        self.moves.append(move)
        return move

# Yardımcı Fonksiyonlar
def determine_winner(player1, player2):
    move1 = player1.moves[-1]
    move2 = player2.moves[-1]

    if move1 == move2:
        return "Berabere"
    elif (move1 == "taş" and move2 == "makas") or \
         (move1 == "kağıt" and move2 == "taş") or \
         (move1 == "makas" and move2 == "kağıt"):
        return player1
    else:
        return player2

def display_scores(player1, player2):
    print(f"\nSkor Tablosu:\n{player1.name}: {player1.score} puan\n{player2.name}: {player2.score} puan\n")

def display_move_history(player1, player2):
    print("\nHamle Geçmişi:")
    for i, (move1, move2) in enumerate(zip(player1.moves, player2.moves), start=1):
        print(f"Tur {i}: {player1.name} - {move1}, {player2.name} - {move2}")

# Ana Oyun Döngüsü
def play_game():
    print("Taş Kağıt Makas Oyununa Hoşgeldiniz!")

    player_name = input("Lütfen kullanıcı adınızı girin: ")
    human = HumanPlayer(player_name)
    computer = RandomComputerPlayer()

    while True:
        print("\nYeni bir tur başlıyor!")
        human_move = human.make_move()
        computer_move = computer.make_move()

        print(f"{human.name} seçimi: {human_move}")
        print(f"{computer.name} seçimi: {computer_move}")

        winner = determine_winner(human, computer)
        if winner == "Berabere":
            print("Bu tur berabere!")
        else:
            print(f"{winner.name} kazandınız!")
            winner.score += 1

        display_scores(human, computer)

        cont = input("Oyuna devam etmek istiyor musunuz? (e/h): ").lower()
        while cont not in ["e", "h"]:
            cont = input("Geçersiz seçim. Devam etmek istiyor musunuz? (e/h): ").lower()
        if cont != "e":
            print("Oyun bitti! Toplam sonuçlar:")
            display_scores(human, computer)
            display_move_history(human, computer)
            break

# Oyunu başlat
if __name__ == "__main__":
    play_game()
