# import list kata dari file words.py
from words import word_list
import random


def get_word():
    # mengambil 1 kata random dari word_list
    word = random.choice(word_list)
    return word.upper()


def play(word):
    # membuat garis kosong sebanyak karakter banyak huruf tebak
    word_completion = "_" * len(word)
    guessed = False  # apakah sudah tertebak
    guessed_letters = []
    guessed_words = []
    tries = 6  # banyaknya percobaan dengan banyaknya anggota tubuh hangman
    print("Let's play Hangman!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:  # selama tebakan belum benar
        guess = input(
            "Please guess a letter or word: "
        ).upper()  # dibuat upper karena kata yang ditebak juga upper
        # jika menebak dengan huruf
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:  # tebakan sudah pernah dikeluarkan
                print("You already guessed the letter", guess)
            elif guess not in word:  # tebakan salah
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(
                    guess
                )  # masukkan tebakan ke list yang sudah ditebak
            else:
                print("Good job,", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                # buka semua huruf yang berhasil ketebak
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                # cek apakah kata misteri sudah tertebak
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            # jika tebakannya langsung kata
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != word:  # tebakannya salah
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:  # tebakannya benar
                guessed = True
                word_completion = word
        else:  # salah inputan
            print("Not a valid guess.")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")

    if guessed:
        print("Congrats, you guessed the word! you win!")
    else:
        print(
            "Sorry, you ran out of tries. The word was " + word + ". Maybe next time!"
        )


def display_hangman(tries):
    stages = [
        # final state : head, torso, both arms, and both legs
        """
            --------
            |      |
            |      O
            |     \\|/
            |      |
            |     / \\
        """,
        # head, torso, both arms, and one leg
        """
            --------
            |      |
            |      O
            |     \\|/
            |      |
            |     / 
        """,
        # head, torso, and both arms
        """
            --------
            |      |
            |      O
            |     \\|/
            |      |
            |     
        """,
        # head,torso, and one arm
        """
            --------
            |      |
            |      O
            |     \\|
            |      |
            |     
        """,
        # head, and torso
        """
            --------
            |      |
            |      O
            |      |
            |      |
            |     
        """,
        # head
        """
            --------
            |      |
            |      O
            |     
            |      
            |     
        """,
        # initial empty state
        """
            --------
            |      |
            |      
            |     
            |      
            |     
        """,
    ]
    return stages[tries]


def main():
    word = get_word()
    play(word)
    # kalo mau main lagi
    while input("Play Again? (Y/N)").upper() == "Y":
        word = get_word()
        play(word)
    print("thank for playing this game!")


if __name__ == "__main__":
    main()