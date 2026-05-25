# PENETRATION-TESTING-TOOLKIT-Task-3
🛡️ Penetration Testing Toolkit
A Python toolkit for educational and authorized security testing.
This toolkit provides three modules: Port Scanner, Brute Force Login, and Password Generator.

🚀 Features
Port Scanner

Scans specified ports on a target host.

Reports open ports for further investigation.

Brute Force Login

Attempts login with a given username and password list.

Reports if a valid password is found.

Password Generator

Generates all possible password combinations from a given character set and length.

Useful for creating test wordlists.

🛠️ How It Works
Port Scanner: Uses Python’s socket library to connect to target ports.

Brute Force Login: Sends POST requests with different passwords to test login forms.

Password Generator: Uses itertools.product to generate combinations.

📦 Requirements
Python 3.7+
python libraries
like, pentest tools

🔍 Example Runs:

Port Scanner

Enter target IP or domain: scanme.nmap.org
Enter ports to scan (comma-separated): 22,80,443

[INFO] Scanning scanme.nmap.org for open ports...
[OPEN] Port 22 is open on scanme.nmap.org
[OPEN] Port 80 is open on scanme.nmap.org


Brute Force Login:

Enter login URL: http://demo.testfire.net/login.jsp
Enter username: admin
Enter password list (comma-separated): 1234,password,admin123

[INFO] Starting brute-force attack on http://demo.testfire.net/login.jsp with username: admin
[SUCCESS] Password found: admin123


Password Generator:

Enter character set (e.g., abc123): ab
Enter password length: 3

[INFO] Generating passwords of length 3...
[INFO] Generated 8 passwords:
['aaa', 'aab', 'aba', 'abb', 'baa', 'bab', 'bba', 'bbb'] ...


📁 Project Structure
Code
penetration-testing-toolkit/
│── toolkit.py          # Main script
│── README.md           # Documentation


⚠️ Disclaimer
This toolkit is for educational purposes only.

Use it only on systems you own or have explicit permission to test.

Unauthorized use against third-party systems may be illegal.

 OUTPUT:
 
