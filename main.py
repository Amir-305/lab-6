# Amir Amritt
def encode(oldPass):
    newPass = ""
    for x in oldPass:
        if int(x) > 6:
            newPass += str(int(x) - 7)
        else:
            newPass += str(int(x) + 3)
    return newPass

if __name__ == '__main__':
    ans = 0
    data = ""

    while True:
        print("Menu")
        print("--------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")

        ans = input("Please enter an option: ")

        if ans == "1":
            data = input("Please enter your 8-digit password to encode: ")
            if len(data) == 8 and data.isdigit():
                encoded_data = encode(data)
                print("Your password has been encoded and stored!")
                print("Encoded Password:", encoded_data)
            else:
                print("Error: Please enter a valid 8-digit numeric password.")

        elif ans == "2":
            if data:
                decoded_data = decode(data)
                print(f"The encoded password is {data}, and the original password is {decoded_data}.")
            else:
                print("Error: No encoded password found. Please encode a password first.")

        elif ans == "3":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid option. Please select 1, 2, or 3.")


