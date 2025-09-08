import matplotlib
matplotlib.use("TkAgg") 
from tests import generate_password, characters
import matplotlib.pyplot as plt
import math 

number_of_passwords = 10_000
number_of_characters = len(characters)

def generate_passwords():
    passwords_list = []
    for i in range(number_of_passwords):
        passwords_list.append(generate_password())
    return passwords_list


def calculate_frequencies(passwords):
    frequencies_dict = {}
    for password in passwords:
        for c in password:
            if c in frequencies_dict:
                frequencies_dict[c] += 1
            else:
                frequencies_dict[c] = 1	
    return frequencies_dict 


def chi_square(frequencies_dict):
    expected_frequency = (number_of_passwords * 10) / number_of_characters
    total = 0 
    for character in frequencies_dict:
        total += ((frequencies_dict[character] - expected_frequency) ** 2) / expected_frequency
    return total 


def generate_probabilities(characters):
    probabilities = {}
    probability = 1 / number_of_characters
    for char in characters:
        probabilities[char] = probability
    return probabilities


def calculate_entropy(probabilities):
    entropy = 0
    for char in characters:
        entropy += probabilities[char] * math.log2(probabilities[char])
    return -entropy   # negative because log2(prob) < 0


def main():
    passwords = generate_passwords()
    frequencies = calculate_frequencies(passwords)
    print("Chi-square statistic:", chi_square(frequencies))
    
    probabilities = generate_probabilities(characters)
    entropy = calculate_entropy(probabilities)
    print("Entropy:", entropy)

    # Uncomment to visualize character frequencies
    # plt.bar(frequencies.keys(), frequencies.values())
    # plt.show()


if __name__ == "__main__":
    main()
