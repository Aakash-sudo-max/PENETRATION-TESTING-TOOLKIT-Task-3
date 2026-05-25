3
"""
Penetration Testing Toolkit
---------------------------
Modules:
1. Port Scanner
2. Brute Force Login
3. Password Generator

This toolkit is for educational and authorized security testing purposes only.
"""

import socket
import requests
import itertools
import threading

# -------------------------------
# Module 1: Port Scanner
# -------------------------------
def port_scanner(target, ports):
    """Scan specified ports on a target host."""
    print(f"\n[INFO] Scanning {target} for open ports...")
    for port in ports:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            result = s.connect_ex((target, port))
            if result == 0:
                print(f"[OPEN] Port {port} is open on {target}")
            s.close()
        except Exception as e:
            print(f"[ERROR] Could not scan port {port}: {e}")

# -------------------------------
# Module 2: Brute Force Login
# -------------------------------
def brute_force_login(url, username, password_list):
    """Attempt brute-force login with a given username and password list."""
    print(f"\n[INFO] Starting brute-force attack on {url} with username: {username}")
    for password in password_list:
        try:
            response = requests.post(url, data={'username': username, 'password': password})
            if "incorrect password" not in response.text.lower():
                print(f"[SUCCESS] Password found: {password}")
                return
        except Exception as e:
            print(f"[ERROR] Request failed: {e}")
            return
    print("[INFO] Brute-force attack complete. No valid password found.")

# -------------------------------
# Module 3: Password Generator
# -------------------------------
def generate_passwords(charset, length):
    """Generate a list of possible passwords using a given character set and length."""
    print(f"\n[INFO] Generating passwords of length {length}...")
    return [''.join(p) for p in itertools.product(charset, repeat=length)]

# -------------------------------
# User-Friendly Menu
# -------------------------------
def main():
    print("\n=== Penetration Testing Toolkit ===")
    print("1. Port Scanner")
    print("2. Brute Force Login")
    print("3. Password Generator")
    choice = input("Select a module (1/2/3): ").strip()
    
    if choice == '1':
        target = input("Enter target IP or domain: ").strip()
        ports = list(map(int, input("Enter ports to scan (comma-separated): ").split(',')))
        port_scanner(target, ports)
    
    elif choice == '2':
        url = input("Enter login URL: ").strip()
        username = input("Enter username: ").strip()
        password_list = input("Enter password list (comma-separated): ").split(',')
        brute_force_login(url, username, password_list)
    
    elif choice == '3':
        charset = input("Enter character set (e.g., abc123): ").strip()
        length = int(input("Enter password length: "))
        passwords = generate_passwords(charset, length)
        print(f"[INFO] Generated {len(passwords)} passwords:")
        print(passwords[:20], "...")  # Show only first 20 for readability
    
    else:
        print("[ERROR] Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
