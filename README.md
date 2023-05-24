# Neural Network Documentation

## Introduction
This code implements a simple neural network in Python that accurately detects languages based on the frequency of letters in a given input. The neural network consists of perceptrons, which are the building blocks of the network. The code trains the perceptrons using a set of language data and provides a graphical user interface (GUI) for language detection.

## Dependencies
The following dependencies are required:
- `random`: A module for generating random numbers.
- `os`: A module for interacting with the operating system.
- `tkinter`: A module for creating GUI applications.

## Perceptron
The `Perceptron` class represents an integral part of the neural network. It contains information about its weights and the language it represents. The perceptron can be trained using language data files, and its weights are adjusted based on the provided expected language.

## Neural Network
The `NeuralNetwork` class represents the neural network itself, consisting of three perceptrons. It allows for language recognition by comparing the nonbinary output of each perceptron and determining the most likely language.

## Main Code
The main code starts by initializing the perceptrons for each language using the language data available. It then trains the neural network by iterating over the data and adjusting the perceptron weights. After training, the code evaluates the network's accuracy by comparing the recognized language with the actual language of the data.

The code also includes a GUI created using the `tkinter` module. The GUI provides an input field where users can enter text, and a button to initiate language detection. The detected language is displayed in the GUI.

Please note that this code assumes the presence of language data files in a directory named "data" for training the network.

To run the code, execute the script and interact with the GUI to detect the language of input text.
