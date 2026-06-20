import socket

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    host = input("Enter Website (e.g., google.com): ")

    ip = socket.gethostbyname(host)

    print("\nNetwork Information")
    print("-------------------")
    print("Website:", host)
    print("IP Address:", ip)

except Exception as e:
    print("Error:", e)
Sample Output
Enter Website (e.g., google.com): google.com

Network Information
-------------------
Website: google.com
IP Address: 142.250.193.78
Short Explanation for LinkedIn Video
Hello everyone,

