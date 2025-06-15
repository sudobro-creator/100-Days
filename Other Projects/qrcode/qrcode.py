import qrcode

# Dictionary to store QR code history
qr_history = {}

# Function to generate and save a QR code
def generate_qr(data, filename):
    qr = qrcode.make(data)
    qr.save(f"{filename}.png")
    qr_history[filename] = data
    print(f"✅ QR code saved as {filename}.png")

# Function to display QR history
def show_history():
    if not qr_history:
        print("📭 No QR codes generated yet.")
        return
    print("\n🕘 QR Code History:")
    for name, content in qr_history.items():
        print(f"{name}.png -> {content}")

# Main loop
def main():
    print("=== 🔲 QR Code Generator ===")
    while True:
        print("\n1. Generate QR Code")
        print("2. Show History")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            data = input("Enter the data/text/link: ")
            filename = input("Enter a filename for the QR code: ")
            generate_qr(data, filename)
        elif choice == "2":
            show_history()
        elif choice == "3":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice.")

# Run the program
main()
