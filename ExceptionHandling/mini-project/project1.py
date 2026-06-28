# Purchase details from a text file

try:
    filename = input("Enter the file name: ")

    file = open(filename, "r")

    total_items = 0
    free_items = 0
    total_amount = 0

    for line in file:
        item, price = line.split()
        price = float(price)

        total_items += 1
        total_amount += price

        if price == 0:
            free_items += 1

    discount = total_amount * 0.10
    final_amount = total_amount - discount

    print("Total items purchased:", total_items)
    print("Free items:", free_items)
    print("Total amount:", total_amount)
    print("Discount amount:", discount)
    print("Final amount after discount:", final_amount)

    file.close()

except FileNotFoundError:
    print("File not found.")

except ValueError:
    print("Invalid data in file.")

except Exception as e:
    print("Error:", e)