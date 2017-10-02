def main():
    import Program.FoodBarcode
    import Program.Lift
    import Program.BarcodeV2

    d = input("\nWhich program do you want to access? (Lift (a) or Food Barcode (b)").title().strip()
    if d == "B":
        Program.FoodBarcode.barcode()
    elif d == "A":
        Program.Lift.lift()
    elif d == "V2":
        Program.BarcodeV2.barcode2()
    elif d == "Exit":
        return False
    else :
        print ("No such program.")

    return main()
main()
