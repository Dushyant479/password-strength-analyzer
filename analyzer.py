import os
from zxcvbn import zxcvbn

def analyze_password(pw, user_inputs=None):
    result = zxcvbn(pw, user_inputs=user_inputs or [])
    print("\nPassword Analysis:")
    print(f"  Password: {pw}")
    print(f"  Strength Score (0–4): {result['score']}")
    print(f"  Crack time (offline fast hash): {result['crack_times_display']['offline_fast_hashing_1e10_per_second']}")
    if result['feedback']['warning']:
        print(f"  Warning: {result['feedback']['warning']}")
    if result['feedback']['suggestions']:
        print(f"  Suggestions: {'; '.join(result['feedback']['suggestions'])}")

def create_wordlist(hints):
    variations = set()
    for item in hints:
        item = item.strip()
        variations.add(item)
        variations.add(item.lower())
        variations.add(item.upper())
        variations.add(item.capitalize())
        # Example: simple leetspeak
        variations.add(item.replace('a', '@').replace('s', '$').replace('o', '0'))
        # Add number variations
        variations.add(item + "123")
        variations.add(item + "2025")
    return list(variations)

def main():
    pw = input("Enter a password to analyze: ")
    analyze_password(pw)

    hints = input("\nEnter comma-separated hints (names, dates, pet names, etc.) for a custom wordlist: ").split(",")
    wordlist = create_wordlist(hints)

    wordlists_dir = "wordlists"
    if not os.path.exists(wordlists_dir):
        os.makedirs(wordlists_dir)

    out_path = os.path.join(wordlists_dir, "generated_wordlist.txt")
    with open(out_path, "w") as f:
        for word in wordlist:
            f.write(word.strip() + "\n")
    print(f"\nCustom wordlist generated and saved to: {out_path}")

if __name__ == "__main__":
    main()
