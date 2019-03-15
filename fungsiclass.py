from PIL import Image
import cv2
import numpy as np
import matplotlib.pyplot as plt

class gambar:
    
    array,histo,pixel = [],[],[]
    width,height = 0,0

    def __init__(self):
        img = Image.open('gambar/img_process.jpg')
        self.width, self.height = img.size
        self.array = [[img.getpixel((i,j)) for j in range(self.height)] for i in range(self.width)]
        self.pixel, self.histo = [],[]
    
    def resetNormal(self):
        img = Image.open('gambar/img_process_normal.jpg')
        self.width, self.height = img.size
        self.array = [[img.getpixel((i,j)) for j in range(self.height)] for i in range(self.width)]
        self.pixel, self.histo = [],[]

    def totalRGB(self):
        r,g,b = 0,0,0 # Inisialisasi variable untuk menampung nilai r,g,b
        for i in range(self.width): # Menjelajagi setiap pixel
            j = 0 # reset index column height
            for j in range(self.height):# pada gambar dengan representasi array 2D
                pixel = self.array[i][j] # Mendapatkan pixel dari titik i,j
                red = pixel[0] # Mendapatkan nilai dari array red pada titik i,j
                green = pixel[1] # Mendapatkan nilai dari array green pada titik i,j
                blue = pixel[2] # Mendapatkan nilai dari array blue pada titik i,j
                r += int(red) # Penjumlahan untuk red
                g += int(green) # Penjumlahan untuk green
                b += int(blue) # Penjumlahan untuk blue
        total = r+g+b # Menjumlahkan total r,g,b
        return total, r, g ,b # Mengeluarkan nilai total dari RGB

    # Mengubah gambar normal menjadi grayscale
    def grayscale(self):
        new = Image.new("RGB",(self.width,self.height),color=255) # Membuat gambar baru dengan width dan height yg sama
        pixels = new.load() # Memuat gambar baru
        total,r,g,b = self.totalRGB() # Memanggil fungsi untuk mendapatkan nilai total RGB
        for i in range(self.width): # Menjelajahi gambar setiap pixel
            for j in range(self.height): # representasi array 2D
                pixel = self.array[i][j] # Mendapatkan pixel dari titik i,j
                gray = round((pixel[0] * (r/total)) + (pixel[1] * (g/total)) + (pixel[2] * (b/total))) # Menghitung nilai gray pada pixel i,j
                pxl = list(pixel)
                pxl[0] = gray
                pxl[1] = gray
                pxl[2] = gray
                self.array[i][j] = tuple(pxl)
                pixels[i,j] = (int(gray), int(gray), int(gray)) # Memasukkan pixel i,j pada gambar baru dengan nilai gray
        new.save('gambar/img_process.jpg') # Save gambar yg sudah diproses
    
    def intensitasplus(self):
        new = Image.new("RGB",(self.width,self.height),color=255) # Membuat gambar baru dengan width dan height yg sama
        pixels = new.load() # Memuat gambar baru
        for i in range(self.width): # Menjelajahi gambar setiap pixel
                for j in range(self.height): # representasi array 2D
                        pixel = self.array[i][j] # Mendapatkan pixel dari titik i,j
                        pxl = list(pixel)
                        pxl[0] += 50
                        pxl[1] += 50
                        pxl[2] += 50
                        self.array[i][j] = tuple(pxl)
                        pixels[i,j] = (int(pixel[0]+50),int(pixel[1]+50),int(pixel[2]+50)) # Memasukkan pixel i,j pada gambar baru dengan nilai R,G,B yang sudah ditambah dengan 50
        new.save('gambar/img_process.jpg') # Save gambar yg sudah diproses

    def intensitasminus(self):
        new = Image.new("RGB",(self.width,self.height),color=255) # Membuat gambar baru dengan width dan height yg sama
        pixels = new.load() # Memuat gambar baru
        for i in range(self.width): # Menjelajahi gambar setiap pixel
                for j in range(self.height): # representasi array 2D
                        pixel = self.array[i][j] # Mendapatkan pixel dari titik i,j
                        pxl = list(pixel)
                        pxl[0] -= 50
                        pxl[1] -= 50
                        pxl[2] -= 50
                        self.array[i][j] = tuple(pxl)
                        pixels[i,j] = (int(pixel[0]-50),int(pixel[1]-50),int(pixel[2]-50)) # Memasukkan pixel i,j pada gambar baru dengan nilai R,G,B yang sudah dikurang dengan 50
        new.save('gambar/img_process.jpg') # Save gambar yg sudah diproses

    def intensitaskali(self):
        new = Image.new("RGB",(self.width,self.height),color=255) # Membuat gambar baru dengan width dan height yg sama
        pixels = new.load() # Memuat gambar baru
        for i in range(self.width): # Menjelajahi gambar setiap pixel
                for j in range(self.height): # representasi array 2D
                        pixel = self.array[i][j] # Mendapatkan pixel dari titik i,j
                        pxl = list(pixel)
                        pxl[0] *= 1.25
                        pxl[1] *= 1.25
                        pxl[2] *= 1.25
                        self.array[i][j] = tuple(pxl)
                        pixels[i,j] = (int(pixel[0]*1.25),int(pixel[1]*1.25),int(pixel[2]*1.25)) # Memasukkan pixel i,j pada gambar baru dengan nilai R,G,B yang sudah dikali dengan 1.25
        new.save('gambar/img_process.jpg') # Save gambar yg sudah diproses

    def intensitasbagi(self):
        new = Image.new("RGB",(self.width,self.height),color=255) # Membuat gambar baru dengan width dan height yg sama
        pixels = new.load() # Memuat gambar baru
        for i in range(self.width): # Menjelajahi gambar setiap pixel
                for j in range(self.height): # representasi array 2D
                        pixel = self.array[i][j] # Mendapatkan pixel dari titik i,j
                        pxl = list(pixel)
                        pxl[0] //= 1.25
                        pxl[1] //= 1.25
                        pxl[2] //= 1.25
                        self.array[i][j] = tuple(pxl)
                        pixels[i,j] = (int(pixel[0]//1.25),int(pixel[1]//1.25),int(pixel[2]//1.25)) # Memasukkan pixel i,j pada gambar baru dengan nilai R,G,B yang sudah dibagi dengan 1.25
        new.save('gambar/img_process.jpg') # Save gambar yg sudah diproses

    def perbesar(self):
        new = Image.new("RGB",(self.width*2,self.height*2),color=255) # Membuat gambar baru dengan width dan height yg dikali 2
        pixels = new.load() # Memuat gambar baru
        r_temp,g_temp,b_temp = [],[],[] # Inisialisasi array temp untuk masing - masing R,G,B
        for i in range(self.width): # Menjelajahi gambar setiap pixel
                for j in range(self.height): # representasi array 2D
                        pixel = self.array[i][j] # Mendapatkan pixel dari titik i,j
                        r_temp.append(pixel[0]) # Memasukkan nilai pixel red i,j kedalam r_temp
                        g_temp.append(pixel[1]) # Memasukkan nilai pixel green i,j kedalam g_temp
                        b_temp.append(pixel[2]) # Memasukkan nilai pixel blue i,j kedalam b_temp
        idx = -1 # Inisialisasi index untuk jalan di array
        for k in range(self.width*2): # Menjelajahi gambar baru setiap pixel
                for l in range(self.height*2): # representasi array 2D
                        if(k%2==0 and l%2==0): # Jika pixel k dan l genap
                                idx+=1 # Increment idx
                                pixels[k,l] = (int(r_temp[idx]),int(g_temp[idx]),int(b_temp[idx])) # Memasukkan pixel k,l pada gambar baru dengan nilai array indek ke idx
                        else: # Jika tidak
                                if(k%2!=0 and l%2!=0): # Jika k ganjil dan l ganjil
                                        pixels[k,l] = pixels[k-1,l-1] # Isi dengan pixel ke k-1 dan l-1
                                elif(k%2!=0): # Jika k ganjil
                                        pixels[k,l] = pixels[k-1,l] # Isi dengan pixel ke k-1 dan l
                                else: # jika l ganjil
                                        pixels[k,l] = pixels[k,l-1] # isi dengan pixel k dan l-1
        new.save('gambar/img_process.jpg') # Save gambar yg sudah diproses
        self.__init__()

    def perkecil(self):
        new = Image.new("RGB",(self.width//2,self.height//2),color=255) # Membuat gambar baru dengan width dan height yg dibagi 2
        pixels = new.load() # Memuat gambar baru
        ikecil = 0 # Inisialisasi ikecil untuk alat bantu idx gambar baru
        i = 0 # Inisialisasi i untuk idx gambar lama
        while(i<self.width): # Ketika i kurang dari width
                jkecil = 0 # Inisialisasi jkecil untuk alat bantu idx gambar baru
                j = 0 # Inisialisasi j untuk idx gambar lama
                while(j<self.height): # Ketika j kurang dari height
                        if (i+1 < self.width and j+1 < self.height): # Jika i+1 kurang dari width dan j+1 kurang dari height 
                                pixel = self.array[i][j] # Mendapatkan pixel dari titik i,j
                                pixel1 = self.array[i][j+1] # Mendapatkan pixel dari titik i,j+1
                                pixel2 = self.array[i+1][j] # Mendapatkan pixel dari titik i+1,j
                                pixel3 = self.array[i+1][j+1] # Mendapatkan pixel dari titik i+1,j+1
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
        self.__init__()

    def parsing(self,x,y,z,n):
        x = int(x)
        y = int(y)
        z = int(z)
        n = int(n)
        return x,y,z,n

    def crop(self,widthf,widthd,heightf,heightd):
        new = Image.new("RGB",(widthd-widthf+1,heightd-heightf+1),color=255) # Membuat gambar baru dengan width dan height sesuai yg di crop
        pixels = new.load() # Memuat gambar baru
        temp_i = 0 # Inisialisasi temp_i
        for i in range(widthf,widthd+1): # Menjelajahi yg ingin di crop
                temp_j = 0 # Inisialisasi temp_j
                for j in range(heightf,heightd+1): # Menjelajahi yg ingin di crop
                        pixels[temp_i,temp_j] = self.array[i][j] # Mengisi pixel temp_i , temp_j dengan nilai pixel ke i,j
                        temp_j += 1 # Increment temp_j
                temp_i += 1 # Increment temp_i
        new.save('gambar/img_process.jpg') # Save gambar yg sudah diproses 
        self.__init__()
    
    def histogram(self): # Fungsi Histogram
            self.grayscale() # Mengubah gambar menjadi grayscale
            self.pixel, self.histo = [],[] # inisiasi array untuk menyimpan frekuensi
            for idx in range(0,256): # Perulangan untuk menghitung frekuensi
                    grey = 0 # variabel untuk menghitung
                    for i in range(self.width): # Perulangan pada gambar
                            for j in range(self.height):
                                    pixel = self.array[i][j] 
                                    if pixel[0] == idx: # Jika pixel r/g/b samadengan idx 
                                        grey += 1 # variabel ditambah 1
                    self.histo.append(grey) # Memasukkan hasil perhitungan kedalam list
                    self.pixel.append(idx) # Memasukkan pixel kedalam list
            plt.bar(self.pixel,self.histo,color='grey') # Plot histogram
            plt.ylim((0,15000)) # Pembatasan y axis
            plt.title('Histogram Awal') # Judul grafik
            plt.savefig('gambar/histo.jpg') # save grafik
            plt.clf() # Reset plot

    def histeq(self):
            new = Image.new("RGB",(self.width,self.height),color=255) # Membuat gambar baru dengan width dan height sesuai dengan gambar
            pixels = new.load() # Memuat gambar baru
            total = sum(self.histo) # Menghitung jumlah semua elemen yang ada didalam list. Cth : a = [1,2,3] jumlah = 6
            cek = True # Inisialisasi variable cek
            i = -1 # Inisialisasi variabel i untuk mencari batas bawah 1
            j = 256 # Inisialisasi variable j untuk mencari batas atas 1
            while i < 256 and cek: # Perulangan dari depan
                    i += 1 
                    if self.histo[i]*100/total >= 0.1: # Jika frekuensi histo pixel i * 100 dibagi dengan total >= 0.1
                            bb1 = i # Set batas bawah 1 dengan i
                            cek = False # Set False supaya perulangan berhenti
            cek = True # Inisialisasi variable cek
            while j >= 0 and cek: # Perulangan dari belakang
                    j -= 1
                    if self.histo[j]*100/total >= 0.1: # Jika frekuensi histo pixel j * 100 dibagi dengan total >= 0.1
                            ba1 = j # Set batas atas 1 dengan j
                            cek = False  # Set False supaya perulangan berhenti
            bb2 = 0 # Set batas bawah 2 dengan 0
            ba2 = 255 # Set batas atas 2 dengan 255
            for k in range(self.width): # Perulangan pada gambar
                    for l in range(self.height):
                            pixel = self.array[k][l]
                            pxl = list(pixel)
                            pxl[0] = round(bb2 + ((pxl[0]-bb2)*((ba2-bb2)/(ba1-bb1)))) # dihitung menggunakan rumus yg bapak berikan
                            pxl[2] = pxl[1] = pxl[0]
                            self.array[k][l] = tuple(pxl)
                            pixels[k,l] = self.array[k][l] # Set pixel pada gambar baru
            new.save('gambar/img_process.jpg') # Save gambar yg sudah diproses 
            self.__init__() # Init gambar baru
            for idx in range(0,256): # Perulangan untuk menghitung frekuensi
                    grey = 0 # variabel untuk menghitung
                    for i in range(self.width): # Perulangan pada gambar
                            for j in range(self.height):
                                    pixel = self.array[i][j]  
                                    if pixel[0] == idx: # Jika pixel r/g/b samadengan idx
                                        grey += 1 # variabel ditambah 1
                    self.histo.append(grey) # Memasukkan frekuensi kedalam list
                    self.pixel.append(idx) # Memasukkan pixel kedalam list
            plt.bar(self.pixel,self.histo,color='grey') # Plot histogram
            plt.ylim((0,15000)) # set y axis
            plt.title('Histogram Equalization') # Set judul
            plt.savefig('gambar/histeq.jpg') # Save plot
            plt.clf() # reset plot

    def proseskernel(self,kernel):
            new = Image.new("RGB",(self.width,self.height),color=255) # Membuat gambar baru dengan width dan height sesuai dengan gambar
            pixels = new.load() # Memuat gambar baru
            newarr = np.asarray(self.array, dtype=np.int)
            for i in range(self.width):
                    for j in range(self.height):
                            pixel = self.array[i][j]
                            if i == 0 and j == 0:
                                e = self.array[i][j+1]
                                s = self.array[i+1][j]
                                se = self.array[i+1][j+1]    
                                red = round(kernel[1][1]*pixel[0] + kernel[1][2]*e[0] + kernel[2][1]*s[0] + kernel[2][2]*se[0])
                                green = round(kernel[1][1]*pixel[1] + kernel[1][2]*e[1] + kernel[2][1]*s[1] + kernel[2][2]*se[1])
                                blue = round(kernel[1][1]*pixel[2] + kernel[1][2]*e[2] + kernel[2][1]*s[2] + kernel[2][2]*se[2])
                            elif i == 0 and j == self.height-1:
                                w = self.array[i][j-1]
                                s = self.array[i+1][j]
                                sw = self.array[i+1][j-1]
                                red = round(kernel[1][1]*pixel[0] + kernel[1][0]*w[0] + kernel[2][1]*s[0] + kernel[2][0]*sw[0])
                                green = round(kernel[1][1]*pixel[1] + kernel[1][0]*w[1] + kernel[2][1]*s[1] + kernel[2][0]*sw[1])
                                blue = round(kernel[1][1]*pixel[2] + kernel[1][0]*w[2] + kernel[2][1]*s[2] + kernel[2][0]*sw[2])
                            elif i == self.width-1 and j == 0:
                                n = self.array[i-1][j]
                                ne = self.array[i-1][j+1]
                                e = self.array[i][j+1]
                                red = round(kernel[1][1]*pixel[0] + kernel[0][1]*n[0] + kernel[0][2]*ne[0] + kernel[1][2]*e[0])
                                green = round(kernel[1][1]*pixel[1] + kernel[0][1]*n[1] + kernel[0][2]*ne[1] + kernel[1][2]*e[1])
                                blue = round(kernel[1][1]*pixel[2] + kernel[0][1]*n[2] + kernel[0][2]*ne[2] + kernel[1][2]*e[2])
                            elif i == self.width-1 and j == self.height-1:
                                n = self.array[i-1][j]
                                nw = self.array[i-1][j-1]
                                w = self.array[i][j-1]
                                red = round(kernel[1][1]*pixel[0] + kernel[0][1]*n[0] + kernel[0][0]*nw[0] + kernel[1][0]*w[0])
                                green = round(kernel[1][1]*pixel[1] + kernel[0][1]*n[1] + kernel[0][0]*nw[1] + kernel[1][0]*w[1])
                                blue = round(kernel[1][1]*pixel[2] + kernel[0][1]*n[2] + kernel[0][0]*nw[2] + kernel[1][0]*w[2])
                            elif i == 0:
                                w = self.array[i][j-1]
                                sw = self.array[i+1][j-1]
                                s = self.array[i+1][j]
                                se = self.array[i+1][j+1]
                                e = self.array[i][j+1]
                                red = round(kernel[1][1]*pixel[0] + kernel[1][0]*w[0] + kernel[1][2]*e[0] + kernel[2][0]*sw[0] + kernel[2][1]*s[0] + kernel[2][2]*se[0])
                                green = round(kernel[1][1]*pixel[1] + kernel[1][0]*w[1] + kernel[1][2]*e[1] + kernel[2][0]*sw[1] + kernel[2][1]*s[1] + kernel[2][2]*se[1])
                                blue = round(kernel[1][1]*pixel[2] + kernel[1][0]*w[2] + kernel[1][2]*e[2] + kernel[2][0]*sw[2] + kernel[2][1]*s[2] + kernel[2][2]*se[2])
                            elif i == self.width-1:
                                w = self.array[i][j-1]
                                nw = self.array[i-1][j-1]
                                n = self.array[i-1][j]
                                ne = self.array[i-1][j+1]
                                e = self.array[i][j+1]
                                red = round(kernel[1][1]*pixel[0] + kernel[1][0]*w[0] + kernel[0][0]*nw[0] + kernel[0][1]*n[0] + kernel[0][2]*ne[0] + kernel[1][2]*e[0])
                                green = round(kernel[1][1]*pixel[1] + kernel[1][0]*w[1] + kernel[0][0]*nw[1] + kernel[0][1]*n[1] + kernel[0][2]*ne[1] + kernel[1][2]*e[1])
                                blue = round(kernel[1][1]*pixel[2] + kernel[1][0]*w[2] + kernel[0][0]*nw[2] + kernel[0][1]*n[2] + kernel[0][2]*ne[2] + kernel[1][2]*e[2])
                            elif j == 0:
                                n = self.array[i-1][j]
                                ne = self.array[i-1][j+1]
                                e = self.array[i][j+1]
                                se = self.array[i+1][j+1]
                                s = self.array[i+1][j]
                                red = round(kernel[1][1]*pixel[0] + kernel[0][1]*n[0] + kernel[0][2]*ne[0] + kernel[1][2]*e[0] + kernel[2][2]*se[0] + kernel[2][1]*s[0])
                                green = round(kernel[1][1]*pixel[1] + kernel[0][1]*n[1] + kernel[0][2]*ne[1] + kernel[1][2]*e[1] + kernel[2][2]*se[1] + kernel[2][1]*s[1])
                                blue = round(kernel[1][1]*pixel[2] + kernel[0][1]*n[2] + kernel[0][2]*ne[2] + kernel[1][2]*e[2] + kernel[2][2]*se[2] + kernel[2][1]*s[2])
                            elif j == self.height-1:
                                n = self.array[i-1][j]
                                nw = self.array[i-1][j-1]
                                w = self.array[i][j-1]
                                sw = self.array[i+1][j-1]
                                s = self.array[i+1][j]
                                red = round(kernel[1][1]*pixel[0] + kernel[0][1]*n[0] + kernel[0][0]*nw[0] + kernel[1][0]*w[0] + kernel[2][0]*sw[0] + kernel[2][1]*s[0])
                                green = round(kernel[1][1]*pixel[1] + kernel[0][1]*n[1] + kernel[0][0]*nw[1] + kernel[1][0]*w[1] + kernel[2][0]*sw[1] + kernel[2][1]*s[1])
                                blue = round(kernel[1][1]*pixel[2] + kernel[0][1]*n[2] + kernel[0][0]*nw[2] + kernel[1][0]*w[2] + kernel[2][0]*sw[2] + kernel[2][1]*s[2])
                            else:
                                n = self.array[i-1][j]
                                ne = self.array[i-1][j+1]
                                e = self.array[i][j+1]
                                se = self.array[i+1][j+1]
                                s = self.array[i+1][j]
                                sw = self.array[i+1][j-1]
                                w = self.array[i][j-1]
                                nw = self.array[i-1][j-1]
                                red = round(kernel[1][1]*pixel[0] + kernel[0][0]*nw[0] + kernel[0][1]*n[0] + kernel[0][2]*ne[0] + kernel[1][0]*w[0] + kernel[1][2]*e[0] + kernel[2][0]*sw[0] + kernel[2][1]*s[0] + kernel[2][2]*se[0])
                                green = round(kernel[1][1]*pixel[1] + kernel[0][0]*nw[1] + kernel[0][1]*n[1] + kernel[0][2]*ne[1] + kernel[1][0]*w[1] + kernel[1][2]*e[1] + kernel[2][0]*sw[1] + kernel[2][1]*s[1] + kernel[2][2]*se[1])
                                blue = round(kernel[1][1]*pixel[2] + kernel[0][0]*nw[2] + kernel[0][1]*n[2] + kernel[0][2]*ne[2] + kernel[1][0]*w[2] + kernel[1][2]*e[2] + kernel[2][0]*sw[2] + kernel[2][1]*s[2] + kernel[2][2]*se[2])
                            if len(newarr[i][j]) == 4:
                                newarr[i][j] = [red,green,blue,255]
                            else:
                                newarr[i][j] = [red,green,blue]
                        #     self.array[i][j] = tuple(newarr[i][j])
                            pixels[i,j] = tuple(newarr[i][j])
            new.save('gambar/img_process.jpg')

    def blur(self):
            kernel = [[0.0625,0.125,0.0625],[0.125,0.25,0.125],[0.0625,0.125,0.0625]]
            self.proseskernel(kernel)
            
    def sharp(self):
            kernel = [[0,-1,0],[-1,5,-1],[0,-1,0]]
            self.proseskernel(kernel)

    def edge(self):
            kernel = [[-1,-1,-1],[-1,8,-1],[-1,-1,-1]]
            self.proseskernel(kernel)