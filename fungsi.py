from PIL import Image

# Menghitung Nilai Total dari RGB (R + G + B)
def totalRGB(img,width,height):
    r,g,b = 0,0,0 # Inisialisasi variable untuk menampung nilai r,g,b
    for i in range(width): # Menjelajagi setiap pixel 
        for j in range(height):# pada gambar dengan representasi array 2D
            pixel = img.getpixel((i,j)) # Mendapatkan pixel dari titik i,j
            red = pixel[0] # Mendapatkan nilai dari array red pada titik i,j
            green = pixel[1] # Mendapatkan nilai dari array green pada titik i,j
            blue = pixel[2] # Mendapatkan nilai dari array blue pada titik i,j
            r += int(red) # Penjumlahan untuk red
            g += int(green) # Penjumlahan untuk green
            b += int(blue) # Penjumlahan untuk blue
    total = r+g+b # Menjumlahkan total r,g,b
    return total, r, g ,b # Mengeluarkan nilai total dari RGB

# Mengubah gambar normal menjadi grayscale
def grayscale():
    img = Image.open('gambar/img_process.jpg') # Membuka gambar
    width, height = img.size # Mendapatkan nilai width dan height
    new = Image.new("RGB", (width,height),color=255) # Membuat gambar baru dengan width dan height yg sama
    pixels = new.load() # Memuat gambar baru
    total,r,g,b = totalRGB(img,width,height) # Memanggil fungsi untuk mendapatkan nilai total RGB
    for i in range(width): # Menjelajahi gambar setiap pixel
        for j in range(height): # representasi array 2D
            pixel = img.getpixel((i,j)) # Mendapatkan pixel dari titik i,j
            red = pixel[0] # Mendapatkan nilai dari array red pada titik i,j
            green = pixel[1] # Mendapatkan nilai dari array green pada titik i,j
            blue = pixel[2] # Mendapatkan nilai dari array blue pada titik i,j
            gray = (red * (r/total)) + (green * (g/total)) + (blue * (b/total)) # Menghitung nilai gray pada pixel i,j
            pixels[i,j] = (int(gray), int(gray), int(gray)) # Memasukkan pixel i,j pada gambar baru dengan nilai gray
    new.save('gambar/img_process.jpg') # Save gambar yg sudah diproses

# Mengubah intensitas menjadi +50
def intensitasplus():
        img = Image.open('gambar/img_process.jpg') # Membuka gambar
        width, height = img.size # Mendapatkan nilai width dan height
        new = Image.new("RGB",(width,height),color=255) # Membuat gambar baru dengan width dan height yg sama
        pixels = new.load() # Memuat gambar baru
        for i in range(width): # Menjelajahi gambar setiap pixel
                for j in range(height): # representasi array 2D
                        pixel = img.getpixel((i,j)) # Mendapatkan pixel dari titik i,j
                        pixels[i,j] = (int(pixel[0]+50),int(pixel[0]+50),int(pixel[2]+50)) # Memasukkan pixel i,j pada gambar baru dengan nilai R,G,B yang sudah ditambah dengan 50
        new.save('gambar/img_process.jpg') # Save gambar yg sudah diproses

# Mengubah intensitas menjadi -50
def intensitasminus():
        img = Image.open('gambar/img_process.jpg') # Membuka gambar
        width, height = img.size # Mendapatkan nilai width dan height
        new = Image.new("RGB",(width,height),color=255) # Membuat gambar baru dengan width dan height yg sama
        pixels = new.load() # Memuat gambar baru
        for i in range(width): # Menjelajahi gambar setiap pixel
                for j in range(height): # representasi array 2D
                        pixel = img.getpixel((i,j)) # Mendapatkan pixel dari titik i,j
                        red = pixel[0] # Mendapatkan nilai dari array red pada titik i,j
                        green = pixel[1] # Mendapatkan nilai dari array green pada titik i,j
                        blue = pixel[2] # Mendapatkan nilai dari array blue pada titik i,j
                        pixels[i,j] = (int(red-50),int(green-50),int(blue-50)) # Memasukkan pixel i,j pada gambar baru dengan nilai R,G,B yang sudah dikurang dengan 50
        new.save('gambar/img_process.jpg') # Save gambar yg sudah diproses

# Mengubah intensitas menjadi x1.25
def intensitaskali():
        img = Image.open('gambar/img_process.jpg') # Membuka gambar
        width, height = img.size # Mendapatkan nilai width dan height
        new = Image.new("RGB",(width,height),color=255) # Membuat gambar baru dengan width dan height yg sama
        pixels = new.load() # Memuat gambar baru
        for i in range(width): # Menjelajahi gambar setiap pixel
                for j in range(height): # representasi array 2D
                        pixel = img.getpixel((i,j)) # Mendapatkan pixel dari titik i,j
                        red = pixel[0] # Mendapatkan nilai dari array red pada titik i,j
                        green = pixel[1] # Mendapatkan nilai dari array green pada titik i,j
                        blue = pixel[2] # Mendapatkan nilai dari array blue pada titik i,j
                        pixels[i,j] = (int(red*1.25),int(green*1.25),int(blue*1.25)) # Memasukkan pixel i,j pada gambar baru dengan nilai R,G,B yang sudah dikali dengan 1.25
        new.save('gambar/img_process.jpg') # Save gambar yg sudah diproses

# Mengubah intensitas menjadi /1.25
def intensitasbagi():
        img = Image.open('gambar/img_process.jpg') # Membuka gambar
        width, height = img.size # Mendapatkan nilai width dan height
        new = Image.new("RGB",(width,height),color=255) # Membuat gambar baru dengan width dan height yg sama
        pixels = new.load() # Memuat gambar baru
        for i in range(width): # Menjelajahi gambar setiap pixel
                for j in range(height): # representasi array 2D
                        pixel = img.getpixel((i,j)) # Mendapatkan pixel dari titik i,j
                        red = pixel[0] # Mendapatkan nilai dari array red pada titik i,j
                        green = pixel[1] # Mendapatkan nilai dari array green pada titik i,j
                        blue = pixel[2] # Mendapatkan nilai dari array blue pada titik i,j
                        pixels[i,j] = (int(red//1.25),int(green//1.25),int(blue//1.25)) # Memasukkan pixel i,j pada gambar baru dengan nilai R,G,B yang sudah dibagi dengan 1.25
        new.save('gambar/img_process.jpg') # Save gambar yg sudah diproses

# Mengubah gambar menjadi 2x size
def perbesar():
        img = Image.open('gambar/img_process.jpg') # Membuka gambar
        width, height = img.size # Mendapatkan nilai width dan height
        new = Image.new("RGB",(width*2,height*2),color=255) # Membuat gambar baru dengan width dan height yg dikali 2
        pixels = new.load() # Memuat gambar baru
        r_temp,g_temp,b_temp = [],[],[] # Inisialisasi array temp untuk masing - masing R,G,B
        for i in range(width): # Menjelajahi gambar setiap pixel
                for j in range(height): # representasi array 2D
                        pixel = img.getpixel((i,j)) # Mendapatkan pixel dari titik i,j
                        r_temp.append(pixel[0]) # Memasukkan nilai pixel red i,j kedalam r_temp
                        g_temp.append(pixel[1]) # Memasukkan nilai pixel green i,j kedalam g_temp
                        b_temp.append(pixel[2]) # Memasukkan nilai pixel blue i,j kedalam b_temp
        idx = -1 # Inisialisasi index untuk jalan di array
        for k in range(width*2): # Menjelajahi gambar baru setiap pixel
                for l in range(height*2): # representasi array 2D
                        if(k%2==0 and l%2==0): # Jika pixel k dan l genap
                                idx+=1 # Increment idx
                                pixels[k,l] = (int(r_temp[idx]),int(g_temp[idx]),int(b_temp[idx])) # Memasukkan pixel k,l pada gambar baru dengan nilai array indek ke idx
                        else: # Jika tidak
                                if(k%2!=0 and l%2!=0): # Jika k ganjil dan l ganjil
                                        pixels[k,l] = new.getpixel((k-1,l-1)) # Isi dengan pixel ke k-1 dan l-1
                                elif(k%2!=0): # Jika k ganjil
                                        pixels[k,l] = new.getpixel((k-1,l)) # Isi dengan pixel ke k-1 dan l
                                else: # jika l ganjil
                                        pixels[k,l] = new.getpixel((k,l-1)) # isi dengan pixel k dan l-1
        new.save('gambar/img_process.jpg') # Save gambar yg sudah diproses

def perkecil():
        img = Image.open('gambar/img_process.jpg') # Membuka gambar
        width, height = img.size # Mendapatkan image size
        new = Image.new("RGB",(width//2,height//2),color=255) # Membuat gambar baru dengan width dan height yg dibagi 2
        pixels = new.load() # Memuat gambar baru
        ikecil = 0 # Inisialisasi ikecil untuk alat bantu idx gambar baru
        i = 0 # Inisialisasi i untuk idx gambar lama
        while(i<width): # Ketika i kurang dari width
                jkecil = 0 # Inisialisasi jkecil untuk alat bantu idx gambar baru
                j = 0 # Inisialisasi j untuk idx gambar lama
                while(j<height): # Ketika j kurang dari height
                        if (i+1 < width and j+1 < height): # Jika i+1 kurang dari width dan j+1 kurang dari height 
                                pixel = img.getpixel((i,j)) # Mendapatkan pixel dari titik i,j
                                pixel1 = img.getpixel((i,j+1)) # Mendapatkan pixel dari titik i,j+1
                                pixel2 = img.getpixel((i+1,j)) # Mendapatkan pixel dari titik i+1,j
                                pixel3 = img.getpixel((i+1,j+1)) # Mendapatkan pixel dari titik i+1,j+1
                                temp_r = pixel[0] + pixel1[0] + pixel2[0] + pixel3[0] # Menjumlahkan 4 pixel red di temp_r
                                temp_g = pixel[1] + pixel1[1] + pixel2[1] + pixel3[1] # Menjumlahkan 4 pixel green di temp_g
                                temp_b = pixel[2] + pixel1[2] + pixel2[2] + pixel3[2] # Menjumlahkan 4 pixel blue di temp_b
                                temp_r = temp_r//4 # Merata rata Red
                                temp_g = temp_g//4 # Merata rata Green
                                temp_b = temp_b//4 # Merata rata Blue
                                pixels[ikecil,jkecil] = (int(temp_r),int(temp_g),int(temp_b)) # Memasukkan pixel ikecil, jkecil pada gambar baru dengan nilai yg sudah di rata rata
                                temp_r,temp_g,temp_b = 0,0,0 # Reset temp
                        j += 2 # j ditambah 2 karena 2x
                        jkecil += 1 # Increment jkecil
                i += 2 # i ditambah 2 karena 2x
                ikecil += 1 # Increment ikecil
        new.save('gambar/img_process.jpg') # Save gambar yg sudah diproses

# Parsing dari input ke integer
def parsing(x,y,z,n):
        x = int(x)
        y = int(y)
        z = int(z)
        n = int(n)
        return x,y,z,n

def crop(widthf,widthd,heightf,heightd):
        img = Image.open('gambar/img_process.jpg') # Membuka gambar
        new = Image.new("RGB",(widthd-widthf+1,heightd-heightf+1),color=255) # Membuat gambar baru dengan width dan height sesuai yg di crop
        pixels = new.load() # Memuat gambar baru
        temp_i = 0 # Inisialisasi temp_i
        for i in range(widthf,widthd+1): # Menjelajahi yg ingin di crop
                temp_j = 0 # Inisialisasi temp_j
                for j in range(heightf,heightd+1): # Menjelajahi yg ingin di crop
                        pixels[temp_i,temp_j] = img.getpixel((i,j)) # Mengisi pixel temp_i , temp_j dengan nilai pixel ke i,j
                        temp_j += 1 # Increment temp_j
                temp_i += 1 # Increment temp_i
        new.save('gambar/img_process.jpg') # Save gambar yg sudah diproses 