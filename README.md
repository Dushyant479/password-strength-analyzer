## Password Strength Analyzer with Custom Wordlist Generator
# Analyze password strength and create targeted wordlists for password auditing and security testing—all from a simple CLI.

# Features
+ Realistic password strength analysis using the zxcvbn algorithm.

+ Custom wordlist generation based on user-provided names, dates, pet names, etc.

+ Adds common patterns (case changes, leetspeak, appended years/numbers).

+ Exports wordlists in .txt format for use with password cracking or auditing tools.

# Requirements
 + Python 3.x

 + zxcvbn-python (pip install zxcvbn-python)

# Usage
1. Clone or download this repository.

2. (Optional) Create a folder named wordlists in the project directory if it doesn’t already exist.

3. Install dependencies:

text
pip install zxcvbn-python
Run the script:

text
python analyzer.py
Follow the prompts:

Enter the password to analyze.

Enter comma-separated hints for the wordlist (e.g., names, dates).

Check output:

Password strength details are shown in the terminal.

Generated wordlist is saved to wordlists/generated_wordlist.txt.

Example
text
Enter a password to analyze: Pa$$w0rd2025
Password Analysis:
  Password: Pa$$w0rd2025
  Strength Score (0–4): 2
  Crack time (offline fast hash): 5 hours
  Warning: This is a very common password.
  Suggestions: Add more words that are uncommon.

Enter comma-separated hints (names, dates, pet names, etc.) for a custom wordlist: dushyant,2025,shadow
Custom wordlist generated and saved to: wordlists/generated_wordlist.txt
Project Structure
text
password-strength-analyzer/
├── analyzer.py
├── requirements.txt
├── wordlists/
│   └── generated_wordlist.txt
└── report.pdf
