# Queens College
# Internet And Web Technologies (CSCI 355)
# Winter 2024
# Assignment #8A- Classic and Modern Cryptography
# Frederick Burke
# I did this assignment along with the class
import math


def read_file(file_name):
    with open(file_name) as f:
        return f.read()


def write_file(file_name, text):
    with open(file_name, "w") as f:
        f.write(text)


freqs_expected = [8.2, 1.5, 2.8, 4.3, 12.581, 2.2, 2.0, 6.1, 7.0, 0.15, 0.77, 4.0, 2.4,
                  6.7, 7.5, 1.9, 0.095, 6.0, 6.3, 9.1, 2.8, 0.98, 2.4, 0.15, 2.0, 0.074]


def distance(x, y):
    return math.sqrt(sum([(x[i] - y[i])**2 for i in range(len(x))]))


def calc_freqs(text):
    freqs = [0] * 26
    for c in text:
        freqs[ord(c) - ord('A')] += 1
    n = len(text)
    freqs = [100 * freqs[i]/n for i in range(26)]
    return freqs


def shift_char(c, shift):
    return chr(ord('A') + ((ord(c) - ord('A') + shift) % 26))


def shift_text(text, shift):
    return ''.join([shift_char(c, shift)for c in text])


def find_best_shift(text):
    best_shift = -1
    best_dist = 99999
    for shift in range(26):
        shifted_text = shift_text(text, shift)
        freqs_shifted = calc_freqs(shifted_text)
        dist_shifted = distance(freqs_shifted, freqs_expected)
        print(shift, dist_shifted)
        if dist_shifted < best_dist:
            best_shift = shift
            best_dist = dist_shifted
    return best_shift


def main():
    text_encrypted = read_file('Assignment8e.txt')
    best_shift = find_best_shift(text_encrypted)
    text_decrypted = shift_text(text_encrypted, best_shift)
    write_file('Assignment8d.txt', text_decrypted)


if __name__ == '__main__':
    main()
