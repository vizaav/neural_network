import random
import os
import tkinter

number_of_eras = 250
font_style = ("Century Gothic", 20)

"""
Progress bar - just to make training look a bit nicer
"""


def progress_bar(current, total):
    percent = 100 * (current / float(total))
    bar = '█' * int(percent) + '-' * int((100 - percent))
    print(f"\r|{bar}|{percent:.2f}%", end="")


"""
perceptron
"""


class Perceptron:
    """An integral part of our neural network. It contains information about its weights and language."""
    learning_rate = 0.01

    def __init__(self, language):
        self.language = language.upper()
        self.weights = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0,
                        'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0,
                        'Y': 0, 'Z': 0}
        self.fully_train()
        self.nonbinary = 0

    def train(self, file, expected_language):
        letters = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0,
                   'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0,
                   'Y': 0, 'Z': 0}

        with open(file, 'r', encoding="utf-8") as f:
            # counting letters
            for line in f:
                for char in line:
                    if char.upper() in letters:
                        letters[char.upper()] += 1
                    else:
                        continue

        outer_net = self.compare(**letters)
        # for the network
        self.nonbinary = outer_net

        # k = 0 means that the perceptron is correct
        k = 0
        if outer_net > 0 and expected_language != self.language:
            k = -1
        elif outer_net <= 0 and expected_language == self.language:
            k = 1

        if k != 0:
            for letter in letters:
                self.weights[letter] += letters[letter] * Perceptron.learning_rate * k

    def fully_train(self):

        data_folder = 'data'
        files = []
        for language_folder in os.listdir(data_folder):
            language_folder_path = os.path.join(data_folder, language_folder)
            if os.path.isdir(language_folder_path):
                for file_name in os.listdir(language_folder_path):
                    file_path = os.path.join(language_folder_path, file_name)
                    files.append(file_path)
                    # print(file_path)
        random.shuffle(files)

        for i in range(0, number_of_eras):
            progress_bar(i, number_of_eras)
            for file in files:
                divided_path = file.split('\\')
                self.train(file, divided_path[1].upper())
                # else:
                #     Exception('Something went wrong in train() while comparing file and expected_language.')
            if i == number_of_eras - 1:
                progress_bar(i + 1, number_of_eras)

    def compare(self, **letters):
        # compares the weights of the perceptron with the weights of the file
        net = 0
        for letter in letters:
            net += self.weights[letter] * letters[letter]
        return net


language_folders = os.listdir('data')
perceptrons = []
for language_folder in language_folders:
    print('TRAINING ' + language_folder.upper())
    perceptrons.append(Perceptron(language_folder.upper()))
    print("")


class NeuralNetwork:
    """ A neural network that consists of three perceptrons."""

    def __init__(self, *perceptrons):
        self.perceptrons = []
        for perceptron in perceptrons:
            self.perceptrons.append(perceptron)

    def recognize(self, file):
        nonbinaries = []
        file_language = file.split('\\')[-2].upper()
        for perceptron in self.perceptrons:
            perceptron.train(file, file_language)
            nonbinaries.append(perceptron.nonbinary)
        for perceptron in self.perceptrons:
            if perceptron.nonbinary == max(nonbinaries):
                return perceptron.language
        return 'UNKNOWN'

    def recognize_from_input(self, file):
        nonbinaries = []

        for perceptron in self.perceptrons:
            perceptron.train(file, perceptron.language)
            nonbinaries.append(perceptron.nonbinary)
        for perceptron in self.perceptrons:
            if perceptron.nonbinary == max(nonbinaries):
                return perceptron.language
        return 'UNKNOWN'


network = NeuralNetwork(*perceptrons)

correct = 0
incorrect = 0
files = []

for language_folder in os.listdir('data'):
    language_folder_path = os.path.join('data', language_folder)
    if os.path.isdir(language_folder_path):
        for file_name in os.listdir(language_folder_path):
            file_path = os.path.join(language_folder_path, file_name)
            files.append(file_path)
            # print(file_path)
random.shuffle(files)
for file in files:
    if network.recognize(file) == file.split('\\')[-2].upper():
        correct += 1
    else:
        incorrect += 1

print('\nMy rate of success is ' + str(correct / (correct + incorrect) * 100) + '% for long texts.')

"""
GUI
"""


def button_click():
    # deletes the previous answer
    for x in range(window.winfo_children().__len__()):
        if x == window.winfo_children().__len__() - 1 and window.winfo_children()[x].winfo_class() == 'Label':
            window.winfo_children()[x].destroy()

    # writes the input to a file
    with open('input.txt', 'w', encoding="utf-8") as f:
        f.write(input.get())
    language = network.recognize_from_input('input.txt')
    answer_label = tkinter.Label(window, text="I think it's " + language, font=font_style)
    answer_label.pack()


window = tkinter.Tk()

window.title("Neural Network")
window.geometry("600x300")
# frame = tkinter.Frame(window, width=500, height=500)
# frame.grid()
label1 = tkinter.Label(window, text="Welcome to my neural network app!", font=font_style)
label1.pack()
input = tkinter.Entry(window, width=30, font=font_style)
input.pack()
print(input.get())

button1 = tkinter.Button(window, text="Detect language", font=font_style, command=button_click)
button1.pack()

button3 = tkinter.Button(window, text="Quit", font=font_style, command=window.destroy)
button3.pack()

window.mainloop()
