import random
import string
import math
import os

# 1. Generate random password
def generate_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    return password


# 2 & 3. Check strength and count characters
def analyze_password(password):
    counts = {
        "length": len(password),
        "uppercase": 0,
        "lowercase": 0,
        "digits": 0,
        "special": 0
    }

    for ch in password:
        if ch.isupper():
            counts["uppercase"] += 1
        elif ch.islower():
            counts["lowercase"] += 1
        elif ch.isdigit():
            counts["digits"] += 1
        else:
            counts["special"] += 1

    return counts


# 4. Strength score using math
def strength_score(counts):
    score = (
        counts["length"] +
        counts["uppercase"] * 2 +
        counts["lowercase"] * 2 +
        counts["digits"] * 3 +
        counts["special"] * 4
    )

    entropy = math.log2(score + 1)
    return round(entropy, 2)


# 5. Save result in a file using os
def save_to_file(password, counts, score):
    folder = "results"
    os.makedirs(folder, exist_ok=True)

    file_path = os.path.join(folder, "password_report.txt")

    with open(file_path, "w") as f:
        f.write(f"Password: {password}\n")
        f.write(f"Length: {counts['length']}\n")
        f.write(f"Uppercase: {counts['uppercase']}\n")
        f.write(f"Lowercase: {counts['lowercase']}\n")
        f.write(f"Digits: {counts['digits']}\n")
        f.write(f"Special chars: {counts['special']}\n")
        f.write(f"Strength score: {score}\n")

    return file_path


# -------- MAIN PROGRAM --------
password = generate_password()
counts = analyze_password(password)
score = strength_score(counts)
file_saved = save_to_file(password, counts, score)

print("Generated Password:", password)
print("Character Count:", counts)
print("Strength Score:", score)
print("Saved in file:", file_saved)