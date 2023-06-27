# Calculate the accuracy of a baseline that simply predicts "London" for every
#   example in the dev set.
# Hint: Make use of existing code.
# Your solution here should only be a few lines.
import os

if __name__ == '__main__':
    correct, total = 0, 0
    file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'birth_dev.tsv')
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            total += 1
            if line.strip().split('\t')[1] == 'London':
                correct += 1

    print(f'Total: {total}, Correct: {correct}, {correct / total} % Correct')
