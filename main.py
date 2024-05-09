import laptoplist as ll
import webwork as www
import extracter

available_commands = extracter.commands
OMEN_list = []
ASUS_list = []
Envy_list = []
Laptops = ll.Laptops

print(available_commands)               # Prints all the available commands

for laptop in Laptops:                  # Adding laptops in different categories
    if laptop.startswith("ASUS"):       # ASUS's laptops
        ASUS_list.append(laptop)
    elif laptop.startswith("HP"):       # HP's laptops
        if laptop.startswith("HP OMEN"):                # HP's OMEN series
            OMEN_list.append(laptop)
        elif laptop.startswith("HP Envy"):              # HP's Envy series
            Envy_list.append(laptop)
            

def ask_ques():
    ans = input("\nPlease enter your command: ")
    mes = ans.lower()
    print("\n")

    if mes == "list":                                       # If answer is "list" it will list all the laptops.
        for x in Laptops:
            print(x)

    if mes.startswith("specs"):                             # If answer is "specs" It will give specs of the given laptop.
        laptop_name = input("Enter laptop name you want to find specs of: ")
        ll.find_laptop(laptop_name)
        final_specs = ll.final_product
        print("\n")
        for key, value in final_specs.items():
            print(f"{key}: {value}")

    if mes == "list specs":                             # If answer is "list specs". What it will do is that it will give specs of all the laptops
        for x in Laptops:
            laptop_name = x
            ll.find_laptop(laptop_name)
            print("\n")
            print(laptop_name)
            final_specs = ll.final_product
            print("\n")
            for key, value in final_specs.items():
                print(f"{key}: {value}")

    if mes.startswith("buy"):                            # If answer is "buy" it will give the specs and open the link of the given laptop.
        laptop_name = input("Enter laptop name you want to view: ")
        ll.find_laptop(laptop_name)
        url = ll.url
        final_specs = ll.final_product
        print("\n")
        for key, value in final_specs.items():
            print(f"{key}: {value}")
        www.open_site(url)

    if mes == "recommended":                                # If answer is "recommened" it will show the recommended laptop(s).
        print("I recommend the ASUS Zenbook 14 OLED for many reasons like its extraordinary performance, design, portability, battery life, keyboard and trackpad, the screen etc.")
        laptop_name = "ASUS Zenbook 14 OLED"
        ll.find_laptop(laptop_name)
        final_specs = ll.final_product
        for key, value in final_specs.items():
            print(f"{key}: {value}")

        print("\nI recommend the HP Envy x360 for many reasons like its extraordinary performance, design, portability, battery life, keyboard and trackpad, the screen etc. The only reason that it is at 2 no. because of its price.")
        laptop_name = "HP Envy x360-fc0100TU"
        ll.find_laptop(laptop_name)
        final_specs = ll.final_product
        for key, value in final_specs.items():
            print(f"{key}: {value}")

    if mes == "envy":                                       # If the answer is "Envy" it will show the list of Envy laptops.
        for laptop in Envy_list:
            print(laptop)
    
    if mes == "asus":                                       # If the answer is "ASUS" it will show the list of ASUS laptops.
        for laptop in ASUS_list:
            print(laptop)

    if mes == "omen":                                       # If the answer is "OMEN" it will show the list of OMEN laptops.
        for laptop in OMEN_list:
            print(laptop)

    if mes.endswith("specs"):                               # For knowing different specs of all laptops in a list
        if mes.startswith("envy"):                          # If wanna know specs of all Envy laptops
            for laptop in Envy_list:
                laptop_name = laptop
                ll.find_laptop(laptop_name)
                print("\n")
                print(laptop_name)
                final_specs = ll.final_product
                for key, value in final_specs.items():
                    print(f"{key}: {value}")

        if mes.startswith("omen"):                      # If wanna know specs of all OMEN laptops.
            for laptop in OMEN_list:
                laptop_name = laptop
                ll.find_laptop(laptop_name)
                print("\n")
                print(laptop_name)
                final_specs = ll.final_product
                for key, value in final_specs.items():
                    print(f"{key}: {value}")

        if mes.startswith("asus"):                      # If wanna know specs of all ASUS laptops.
            for laptop in ASUS_list:
                laptop_name = laptop
                ll.find_laptop(laptop_name)
                print("\n")
                print(laptop_name)
                final_specs = ll.final_product
                for key, value in final_specs.items():
                    print(f"{key}: {value}")

        
    if mes == "help":
        print(available_commands)

    if not mes == "exit":
        loopin() # Make it a perfect loop and if it is exit then stop looping.
    else:
        print("Bye...")


def loopin(): # The loop.
    try:
        ask_ques()
    except KeyboardInterrupt:
        print("\nBye...")

ask_ques() # Its like one-time activation.