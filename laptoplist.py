Laptops = []
final_product = {}
url = ""

def add_laptop(laptop):
    global Laptops
    Laptops.append(laptop)

# If you want to add a laptop, add here.
add_laptop("ASUS Zenbook 14 OLED")
add_laptop("ASUS Vivobook S 15 OLED K3502ZA-L701WS")
add_laptop("ASUS Vivobook S 15 OLED S5504VA-MA741WS")
add_laptop("ASUS Vivobook Pro 15 OLED")
add_laptop("HP OMEN 16-wf0179TX")
add_laptop("HP OMEN 16-wd0770TX")
add_laptop("HP OMEN 16-xd0007AX")
add_laptop("HP OMEN 16-xd0005AX")
add_laptop("HP Envy x360-fc0100TU")
add_laptop("HP Envy x360-fe0011TX")
add_laptop("HP Envy x360-fc0078TU")
add_laptop("HP Envy x360-fc0105TU")
add_laptop("HP Envy x360-fc0106TU")




def find_laptop(laptop): # If added a new laptop update information here too.
    global url
    global final_product

    if laptop == "ASUS Vivobook S 15 OLED K3502ZA-L701WS":
        name = "ASUS Vivobook S 15 OLED"
        ram = "16 GB"
        storage = "512 GB"
        cpu = "Intel Core i5-12500H"
        gpu = "Iris Xe Graphics"
        price = "77,990"
        url = "https://in.store.asus.com/light-weight-laptop-asus-vivobook-s-15-oled-k3502z.html"
        notes = "It is a nice laptop but the intergrated GPU is not that powerful and the CPU power is mid-high. 1080P Screen. 15 inch 16:9 ratio screen."
        final_product.clear()
        final_product["Name"] = name
        final_product["CPU"] = cpu
        final_product["GPU"] = gpu
        final_product["Ram"] = ram
        final_product["Storage"] = storage
        final_product["Price"] = price
        final_product["Additional Notes"] = notes
    
    if laptop == "ASUS Zenbook 14 OLED":
        name = "ASUS Zenbook 14 OLED"
        ram = "32 GB"
        storage = "1 TB"
        cpu = "Intel Core Ultra 7 155H"
        gpu = "Intergrated Intel Arc Graphics"
        price = "1,20,990"
        url = "https://in.store.asus.com/light-weight-laptop-asus-zenbook-14-oled-ux3405ma.html"
        notes = "It is the best laptop for price to performance while also maintaining a good keyboard and trackpad. It has military grade certification. It has the latest series of processor which is pretty fast with AI features and good graphics. The ram and storage is enough for any task you throw at it. It has top of the line specs while remaining in a budget. It has a 14 inch 3K 16:10 ratio and 120Hz screen. It is the recommended laptop. The good side one and only downside is its ports. It has 2 USB-C ports, a single USB-A port and an HDMI port. The upside is that because of this, the laptop is slim and light.But due to the shortage of port, we might need to use an adapter."
        final_product.clear()
        final_product["Name"] = name
        final_product["CPU"] = cpu
        final_product["GPU"] = gpu
        final_product["Ram"] = ram
        final_product["Storage"] = storage
        final_product["Price"] = price
        final_product["Additional Notes"] = notes

    if laptop == "ASUS Vivobook S 15 OLED S5504VA-MA741WS":
        name = "ASUS Vivobook S 15 OLED"
        ram = "16 GB"
        storage = "512 GB"
        cpu = "Intel Core i7-13700H"
        gpu = "Iris Xe Graphics"
        price = "91,990"
        url = "https://in.store.asus.com/light-weight-laptop-asus-vivobook-s-15-oled-s5504v.html"
        notes = "It is a nice laptop but the intergrated GPU is not that powerful and the CPU power is kinda high.2.8K Screen. 15.6 inch 16:9 ratio 120Hz screen."
        final_product.clear()
        final_product["Name"] = name
        final_product["CPU"] = cpu
        final_product["GPU"] = gpu
        final_product["Ram"] = ram
        final_product["Storage"] = storage
        final_product["Price"] = price
        final_product["Additional Notes"] = notes

    if laptop == "ASUS Vivobook Pro 15 OLED":
        name = "ASUS Vivobook Pro 15 OLED"
        ram = "16 GB"
        storage = "512 GB"
        cpu = "Intel Core i5-13500H"
        gpu = "Nvidia Geoforce RTX 4050 6GB Vram"
        price = "1,04,990"
        url = "https://in.store.asus.com/creator-laptop-asus-vivobook-pro-15-oled-k6502.html"
        notes = "It is a nice laptop because the GPU is powerful and the CPU power is kinda Mid-low.2.8K Screen. 15.6 inch 16:9 ratio 120Hz screen. The keyboard on this laptop is decent."
        final_product.clear()
        final_product["Name"] = name
        final_product["CPU"] = cpu
        final_product["GPU"] = gpu
        final_product["Ram"] = ram
        final_product["Storage"] = storage
        final_product["Price"] = price
        final_product["Additional Notes"] = notes

    # HP's OMEN Series

    if laptop == "HP OMEN 16-wf0179TX":
        name = "HP OMEN 16 Gaming Laptop"
        ram = "16 GB"
        storage = "512 GB"
        cpu = "Intel Core i7-13700H"
        gpu = "Nvidia Geoforce RTX 3050 6GB Vram"
        price = "1,10,999"
        url = "https://www.hp.com/in-en/shop//omen-gaming-laptop-16-wf0179tx-9q9m6pa.html"
        notes = "It is a nice laptop because the GPU is powerful and the CPU power is kinda Mid-High. 1080p Screen, 15.6 inch 16:9 ratio 165Hz screen. The keyboard and other hardware things on this laptop is not very good nor very bad cuz its a gaming laptop so it also has RGB which I will probably never use. It is a thick boi and its bulky, heavy and noisy. On the bright side, it is more upgradable than others."
        final_product.clear()
        final_product["Name"] = name
        final_product["CPU"] = cpu
        final_product["GPU"] = gpu
        final_product["Ram"] = ram
        final_product["Storage"] = storage
        final_product["Price"] = price
        final_product["Additional Notes"] = notes

    if laptop == "HP OMEN 16-wd0770TX":
        name = "HP OMEN 16 Gaming Laptop"
        ram = "16 GB"
        storage = "512 GB"
        cpu = "Intel Core i5-13500H"
        gpu = "Nvidia Geoforce RTX 4050 6GB Vram"
        price = "90,990"
        url = "https://www.hp.com/in-en/shop/omen-gaming-laptop-16-wd0770tx-88y64pa.html"
        notes = "It is a nice laptop because the GPU is powerful and the CPU power is Mid. 1080p Screen, 15.6 inch 16:9 ratio 144Hz screen. The keyboard and other hardware things on this laptop is not very good nor very bad cuz its a gaming laptop so it also has RGB which I will probably never use. It is a thick boi and its bulky, heavy and noisy. On the bright side, it is more upgradable than others."
        final_product.clear()
        final_product["Name"] = name
        final_product["CPU"] = cpu
        final_product["GPU"] = gpu
        final_product["Ram"] = ram
        final_product["Storage"] = storage
        final_product["Price"] = price
        final_product["Additional Notes"] = notes

    if laptop == "HP OMEN 16-xd0007AX":
        name = "HP OMEN 16 Gaming Laptop"
        ram = "16 GB"
        storage = "1 TB"
        cpu = "AMD Ryzen™ 7-7840HS"
        gpu = "Nvidia Geoforce RTX 4050 6GB Vram"
        price = "1,16,599"
        url = "https://www.hp.com/in-en/shop//omen-gaming-laptop-16-xd0007ax-90l48pa.html"
        notes = "It is a nice laptop because the GPU is powerful and the CPU power is kinda Mid-High. 1080p Screen, 15.6 inch 16:9 ratio 165Hz screen. The keyboard and other hardware things on this laptop is not very good nor very bad cuz its a gaming laptop. It is a thick boi and its bulky, heavy and noisy. On the bright side, it is more upgradable than others."
        final_product.clear()
        final_product["Name"] = name
        final_product["CPU"] = cpu
        final_product["GPU"] = gpu
        final_product["Ram"] = ram
        final_product["Storage"] = storage
        final_product["Price"] = price
        final_product["Additional Notes"] = notes
    if laptop == "HP OMEN 16-xd0005AX":
        name = "HP OMEN 16 Gaming Laptop"
        ram = "16 GB"
        storage = "1 TB"
        cpu = "AMD Ryzen™ 7-7840HS"
        gpu = "Nvidia Geoforce RTX 4050 6GB Vram"
        price = "1,04,479"
        url = "https://www.hp.com/in-en/shop//omen-gaming-laptop-16-xd0005ax-90l47pa.html"
        notes = "It is a nice laptop because the GPU is powerful and the CPU power is kinda Mid-High. 1080p Screen, 15.6 inch 16:9 ratio 165Hz screen. The keyboard and other hardware things on this laptop is not very good nor very bad cuz its a gaming laptop. It is a thick boi and its bulky, heavy and noisy. On the bright side, it is more upgradable than others."
        final_product.clear()
        final_product["Name"] = name
        final_product["CPU"] = cpu
        final_product["GPU"] = gpu
        final_product["Ram"] = ram
        final_product["Storage"] = storage
        final_product["Price"] = price
        final_product["Additional Notes"] = notes

    # HP's Envy series

    if laptop == "HP Envy x360-fe0011TX":
        name = "HP Envy x360"
        ram = "16 GB"
        storage = "512 GB"
        cpu = "Intel Core i7 1355U"
        gpu = "Nvidia Geoforce RTX 3050 4GB Vram"
        price = "1,30,999"
        url = "https://www.hp.com/in-en/shop/hp-envy-x360-2-in-1-laptop-15-fe0011tx-8d667pa.html"
        notes = "It is a nice laptop becuase of the GPU being powerful and the CPU power is mid-high. 1080P Screen. 15.6 inch 16:9 ratio screen. The keyboard, trackpad and everything else is good since it is from hp. It would have been a recommended laptop if it was not for its heavy price and only 4 GB Vram."
        final_product.clear()
        final_product["Name"] = name
        final_product["CPU"] = cpu
        final_product["GPU"] = gpu
        final_product["Ram"] = ram
        final_product["Storage"] = storage
        final_product["Price"] = price
        final_product["Additional Notes"] = notes

    if laptop == "HP Envy x360-fc0078TU":
        name = "HP Envy x360"
        ram = "16 GB"
        storage = "512 GB"
        cpu = "Intel Core Ultra 5"
        gpu = "Intergrated Intel Arc Graphics"
        price = "1,07,999"
        url = "https://www.hp.com/in-en/shop/hp-envy-x360-2-in-1-laptop-14-fc0078tu-9w638pa.html"
        notes = "It is a nice laptop. The GPU is kinda powerful and the CPU power is mid-high. 2.8K Screen. 14 inch 16:9 ratio screen. The keyboard, trackpad and everything else is good since it is from HP. It would have been a recommended laptop if it was not for its price to performance in software things."
        final_product.clear()
        final_product["Name"] = name
        final_product["CPU"] = cpu
        final_product["GPU"] = gpu
        final_product["Ram"] = ram
        final_product["Storage"] = storage
        final_product["Price"] = price
        final_product["Additional Notes"] = notes

    if laptop == "HP Envy x360-fc0105TU":
        name = "HP Envy x360"
        ram = "16 GB"
        storage = "512 GB"
        cpu = "Intel Core Ultra 5"
        gpu = "Intergrated Intel Arc Graphics"
        price = "99,999"
        url = "https://www.hp.com/in-en/shop/hp-envy-x360-2-in-1-laptop-14-fc0105tu-a00pppa.html"
        notes = "It is a nice laptop. The GPU is kinda powerful and the CPU power is mid-high. 1080P Screen. 14 inch 16:9 ratio screen. The keyboard, trackpad and everything else is good since it is from HP. It would have been a recommended laptop if it was not for its display since its display is mid and also for the processor."
        final_product.clear()
        final_product["Name"] = name
        final_product["CPU"] = cpu
        final_product["GPU"] = gpu
        final_product["Ram"] = ram
        final_product["Storage"] = storage
        final_product["Price"] = price
        final_product["Additional Notes"] = notes

    if laptop == "HP Envy x360-fc0106TU":
        name = "HP Envy x360"
        ram = "16 GB"
        storage = "512 GB"
        cpu = "Intel Core Ultra 7"
        gpu = "Intergrated Intel Arc Graphics"
        price = "1,11,999"
        url = "https://www.hp.com/in-en/shop/hp-envy-x360-2-in-1-laptop-14-fc0106tu-a00pqpa.html"
        notes = "It is a nice laptop. The GPU is kinda powerful and the CPU power is mid-high. 1080P Screen. 14 inch 16:9 ratio screen. The keyboard, trackpad and everything else is good since it is from HP. It would have been a recommended laptop if it was not for its storage and ram compared to the recommended laptop and the storage is low other specs are same to the recommened laptop."
        final_product.clear()
        final_product["Name"] = name
        final_product["CPU"] = cpu
        final_product["GPU"] = gpu
        final_product["Ram"] = ram
        final_product["Storage"] = storage
        final_product["Price"] = price
        final_product["Additional Notes"] = notes

    if laptop == "HP Envy x360-fc0100TU":
        name = "HP Envy x360"
        ram = "32 GB"
        storage = "1 TB"
        cpu = "Intel Core Ultra 7"
        gpu = "Intergrated Intel Arc Graphics"
        price = "1,36,999"
        url = "https://www.hp.com/in-en/shop/hp-envy-x360-2-in-1-laptop-14-fc0100tu-9z835pa.html"
        notes = "It is a nice laptop. The GPU is kinda powerful and the CPU power is mid-high. 2.8K OLED Screen. 14 inch 16:9 ratio screen. The keyboard, trackpad and everything else is good since it is from HP. It would have been a recommended laptop if it was not for its price since its price is kinda high but if price was not a concern then it is a recommended laptop. I could recommend this as it has benefits of a respectable company and its keyboard, trackpad and all the specs are same as the recommended laptop."
        final_product.clear()
        final_product["Name"] = name
        final_product["CPU"] = cpu
        final_product["GPU"] = gpu
        final_product["Ram"] = ram
        final_product["Storage"] = storage
        final_product["Price"] = price
        final_product["Additional Notes"] = notes







def template(laptop):
    if laptop == "Laptop name/ID":
        name = ""
        ram = ""
        storage = ""
        cpu = ""
        gpu = ""
        price = ""
        url = ""
        notes = "It is a nice laptop but the intergrated GPU is not that powerful and the CPU power is mid-high. 1080P Screen. 15 inch 16:9 ratio screen."
        final_product.clear()
        final_product["Name"] = name
        final_product["CPU"] = cpu
        final_product["GPU"] = gpu
        final_product["Ram"] = ram
        final_product["Storage"] = storage
        final_product["Price"] = price
        final_product["Additional Notes"] = notes