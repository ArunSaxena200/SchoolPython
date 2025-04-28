# check_writer.py

def number_to_words(n):
    ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    teens = ["Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen",
             "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

    if n == 0:
        return "Zero"
    
    words = ""
    if n >= 1000:
        words += ones[n // 1000] + " Thousand "
        n = n % 1000

    if n >= 100:
        words += ones[n // 100] + " Hundred "
        n = n % 100

    if n >= 20:
        words += tens[n // 10] + " "
        n = n % 10
    elif n >= 11:
        words += teens[n - 11] + " "
        n = 0
    elif n == 10:
        words += tens[1] + " "

    if n > 0:
        words += ones[n] + " "
    
    return words.strip()

def convert_check_amount(amount):
    dollars = int(amount)
    cents = int(round((amount - dollars) * 100))

    dollar_words = number_to_words(dollars)
    cent_words = number_to_words(cents)

    result = ""
    if dollars > 0:
        result += f"{dollar_words} Dollar{'s' if dollars != 1 else ''}"
    if cents > 0:
        if dollars > 0:
            result += " and "
        result += f"{cent_words} Cent{'s' if cents != 1 else ''}"
    
    return result

if __name__ == "__main__":
    try:
        amount = float(input("Enter the check amount (e.g., 1245.67): "))
        print("Amount in words:")
        print(convert_check_amount(amount))
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
