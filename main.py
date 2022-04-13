while True:

    print("\nChoose option \n\n[1] Fixed Path \n[2] User Provided Path")
    choice = int(input("Choice: "))
    
    if choice == 1:
        import fixed 
        break

    elif choice == 2:
        import user
        break
    
    else:
        print("Invalid Input...")