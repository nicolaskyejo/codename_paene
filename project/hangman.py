import random

def guess_letter(word, letter, guessed_list):

    if letter not in guessed_list:
        guessed_list.append(letter)
        for c in word:
            if letter == c:
                return True
    return False

def check_if_solved(guessed_list: list, correct_list: list) -> bool:
    if guessed_list == correct_list:
        return True
    else:
        return False

def show_puzzle(word, correct_list):
    hidden_word = ""
    for c in word:
        if c in correct_list:
           hidden_word += c
           hidden_word += ' '
        else:
            hidden_word += '_ '
    return hidden_word

def ask_letter():
    letter = str(input("Guess a letter: "))
    return letter

if __name__ == '__main__':

    words = open('words.txt')
    ff = words.read()
    d = ff.splitlines()
    lista = []

    for word in d:
        if len(word) > 5:
            lista.append(word)

    guess_word = lista[random.randint(0, len(lista)-1)]
    letters = []

    for c in guess_word:
       if c not in letters:
           letters.append(c)
    letters.sort()

    guess_count = 0
    guessed_list = []
    correct_list = []

    while guess_count < 6 and correct_list != letters:
        print("The word is: \n", show_puzzle(guess_word, correct_list))
        let = ask_letter()

        if let.isalpha() and len(let) == 1:

            if guess_letter(guess_word, let, guessed_list):
                correct_list.append(let)
                correct_list.sort()

                if check_if_solved(correct_list, letters):
                    print("you guessed right, YOU WIN!")
            else:
                guess_count += 1
                ss = "You guessed wrong... STRIKE"
                print(ss, guess_count)
        else:
            print("Not a letter.")

    print("the correct word was: ", guess_word)





