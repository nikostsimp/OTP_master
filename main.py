# Άσκηση 2.6 - One Time Pad (OTP) με κωδικοποίηση 5 bits

import secrets # Βιβλιοθήκη για δημιουργία τυχαίου κλειδιού

# Πίνακας : κάθε σύμβολο αντιστοιχεί σε έναν αριθμό 0..31
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ.!?()-"


# Μετατροπή κειμένου σε bits
def text_to_bits(text):
    bits = ""
    for charachter in text:
        number = ALPHABET.index(charachter) # Ποια θέση έχει ο χαρακτήρας μέσα στο ALPHABET
        bits += format(number, "05b") # Ο χαρακτήρας σε 5 Bit
    return bits

# Μετατροπή bits σε κείμενο
def bits_to_text(bits):
    text = ""
    for part_of_bit in range(0, len(bits), 5):
        number = int(bits[part_of_bit:part_of_bit+5], 2)
        text += ALPHABET[number]
    return text


# XOR του κειμένου (κρυπτογραφημένου ή αποκρυπτογραφημένου) με το κλειδί
def xor_of_bits(m, k):
    result = ""
    for x, y in zip(m, k):  # 1ο bit του m με το 1ο bit του k κτλ.
        if x == y:
            result += "0"
        else:
            result += "1"
    return result


# Δημιουργία τυχαίου κλειδιού ανάλογα το μέγεθος του μηνύματος
def generate_key(n):
    key = ""
    for _ in range(n):
        bit = secrets.randbits(1)
        key += str(bit)
    return key


# Κρυπτογράφηση του μηνύματος E(m, k) = m XOR k
def encrypt(message, key_bits):
    m_bits = text_to_bits(message) # Με την συνάρτηση γίνεται μετατροπή του μηνύματος σε bits
    c_bits = xor_of_bits(m_bits, key_bits) # XOR του μηνύματος και του κλειδιού που ήταν ήδη σε bits = κρυπτογραφημένο μήνυμα
    return bits_to_text(c_bits)

# Αποκρυπτογράφηση του κρυπτογραφημένου μηνύματος  D(c, k) = c XOR k
def decrypt(ciphertext, key_bits):
    c_bits = text_to_bits(ciphertext)  # Με την συνάρτηση γίνεται μετατροπή του κρυπτογραφημένου μηνύματος σε bits
    m_bits = xor_of_bits(c_bits, key_bits) # XOR του κρυπτογραφημένου μηνύματος και του κλειδιού που ήταν ήδη σε bits = αρχικό μήνυμα
    return bits_to_text(m_bits)



if __name__ == "__main__":
    message = input("Δώσε μήνυμα (A-Z, ., !, ?, (, ), -) χωρίς κενά.").upper()

    for charachter in message:
        if charachter not in ALPHABET:
            raise ValueError (f"Ο χαρακτήρας '{charachter}' δεν υπάρχει στον πίνακα")

    # Το κλειδί έχει μήκος όσο το μήνυμα σε bits
    key_bits = generate_key(5 * len(message))

    c = encrypt(message, key_bits)
    m = decrypt(c, key_bits)

    print("Μήνυμα σε bits:     ", text_to_bits(message))
    print("Κλειδί σε bits:     ", key_bits)
    print("Κλειδί σε χαρακτ.:  ", bits_to_text(key_bits))
    print("Κρυπτοκείμενο:      ", c)
    print("Κρυπτοκείμ. σε bits:", text_to_bits(c))
    print("Αποκρυπτογράφηση:   ", m)

    if (m == message):
        print("Σωστή αποκρυπτογράφηση.")
    else:
        print("Λάθος αποκρυπτογράφηση.")
