from PIL import Image
import cv2
import numpy as np
import matplotlib.pyplot as plt
import random

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
            newarr = np.asarray(self.array, dtype=np.int) # Membuat duplikasi array gambar
            for i in range(self.width): # Melakukan penjelajahan
                    for j in range(self.height): # Pada Gambar
                            pixel = self.array[i][j] # Mengambil nilai pixel dari index i,j
                            if i == 0 and j == 0: # Jika pixel sedang berada di pojok kiri atas
                                e = self.array[i][j+1] # Mengambil nilai timur dari pixel
                                s = self.array[i+1][j] # Mengambil nilai selatan dari pixel
                                se = self.array[i+1][j+1] # Mengambil nilai tenggara dari pixel
                                # Menhitung menggunakan rumus
                                red = round(kernel[1][1]*pixel[0] + kernel[1][2]*e[0] + kernel[2][1]*s[0] + kernel[2][2]*se[0])
                                green = round(kernel[1][1]*pixel[1] + kernel[1][2]*e[1] + kernel[2][1]*s[1] + kernel[2][2]*se[1])
                                blue = round(kernel[1][1]*pixel[2] + kernel[1][2]*e[2] + kernel[2][1]*s[2] + kernel[2][2]*se[2])
                            elif i == 0 and j == self.height-1: # Jika pixel sedang berada di pojok kanan atas
                                w = self.array[i][j-1] # Mengambil nilai barat dari pixel
                                s = self.array[i+1][j] # Mengambil nilai selatan dari pixel
                                sw = self.array[i+1][j-1] # Mengambil nilai barat daya dari pixel
                                # Menghitung menggunakan rumus
                                red = round(kernel[1][1]*pixel[0] + kernel[1][0]*w[0] + kernel[2][1]*s[0] + kernel[2][0]*sw[0])
                                green = round(kernel[1][1]*pixel[1] + kernel[1][0]*w[1] + kernel[2][1]*s[1] + kernel[2][0]*sw[1])
                                blue = round(kernel[1][1]*pixel[2] + kernel[1][0]*w[2] + kernel[2][1]*s[2] + kernel[2][0]*sw[2])
                            elif i == self.width-1 and j == 0: # Jika pixel sedang berada di pojok kiri bawah
                                n = self.array[i-1][j] # Mengambil nilai utara dari pixel
                                ne = self.array[i-1][j+1] # Mengambil nilai timur laut dari pixel
                                e = self.array[i][j+1] # Mengambil nilai timur dari pixel
                                # Menghitung menggunakan rumus
                                red = round(kernel[1][1]*pixel[0] + kernel[0][1]*n[0] + kernel[0][2]*ne[0] + kernel[1][2]*e[0])
                                green = round(kernel[1][1]*pixel[1] + kernel[0][1]*n[1] + kernel[0][2]*ne[1] + kernel[1][2]*e[1])
                                blue = round(kernel[1][1]*pixel[2] + kernel[0][1]*n[2] + kernel[0][2]*ne[2] + kernel[1][2]*e[2])
                            elif i == self.width-1 and j == self.height-1: # Jika pixel berada di pojok kanan bawah
                                n = self.array[i-1][j] # Mengambil nilai utara dari pixel
                                nw = self.array[i-1][j-1] # Mengambil nilai barat laut dari pixel
                                w = self.array[i][j-1] # Mengambil nilai barat dari pixel
                                # Menghitung menggunakan rumus
                                red = round(kernel[1][1]*pixel[0] + kernel[0][1]*n[0] + kernel[0][0]*nw[0] + kernel[1][0]*w[0])
                                green = round(kernel[1][1]*pixel[1] + kernel[0][1]*n[1] + kernel[0][0]*nw[1] + kernel[1][0]*w[1])
                                blue = round(kernel[1][1]*pixel[2] + kernel[0][1]*n[2] + kernel[0][0]*nw[2] + kernel[1][0]*w[2])
                            elif i == 0: # Jika pixel berada di bagian atas gambar
                                w = self.array[i][j-1] # Mengambil nilai barat dari pixel
                                sw = self.array[i+1][j-1] # Mengambil nilai barat daya dari pixel
                                s = self.array[i+1][j] # Mengambil nilai selatan dari pixel
                                se = self.array[i+1][j+1] # Mengambil nilai tenggara dari pixel
                                e = self.array[i][j+1] # Mengambil nilai timur dari pixel
                                # Menghitung menggunakan rumus
                                red = round(kernel[1][1]*pixel[0] + kernel[1][0]*w[0] + kernel[1][2]*e[0] + kernel[2][0]*sw[0] + kernel[2][1]*s[0] + kernel[2][2]*se[0])
                                green = round(kernel[1][1]*pixel[1] + kernel[1][0]*w[1] + kernel[1][2]*e[1] + kernel[2][0]*sw[1] + kernel[2][1]*s[1] + kernel[2][2]*se[1])
                                blue = round(kernel[1][1]*pixel[2] + kernel[1][0]*w[2] + kernel[1][2]*e[2] + kernel[2][0]*sw[2] + kernel[2][1]*s[2] + kernel[2][2]*se[2])
                            elif i == self.width-1: # Jika pixel berada di bagian bawah gambar 
                                w = self.array[i][j-1] # Mengambil nilai barat dari pixel
                                nw = self.array[i-1][j-1] # Mengambil nilai barat laut dari pixel
                                n = self.array[i-1][j] # Mengambil nilai utara dari pixel
                                ne = self.array[i-1][j+1] # Mengambil nilai timur laut dari pixel
                                e = self.array[i][j+1] # Mengambil nilai timur dari pixel
                                # Menghitung menggunakan rumus
                                red = round(kernel[1][1]*pixel[0] + kernel[1][0]*w[0] + kernel[0][0]*nw[0] + kernel[0][1]*n[0] + kernel[0][2]*ne[0] + kernel[1][2]*e[0])
                                green = round(kernel[1][1]*pixel[1] + kernel[1][0]*w[1] + kernel[0][0]*nw[1] + kernel[0][1]*n[1] + kernel[0][2]*ne[1] + kernel[1][2]*e[1])
                                blue = round(kernel[1][1]*pixel[2] + kernel[1][0]*w[2] + kernel[0][0]*nw[2] + kernel[0][1]*n[2] + kernel[0][2]*ne[2] + kernel[1][2]*e[2])
                            elif j == 0: # Jika pixel berada di bagian kiri gambar
                                n = self.array[i-1][j] # Mengambil nilai utara dari pixel
                                ne = self.array[i-1][j+1] # Mengambil nilai timur laut dari pixel
                                e = self.array[i][j+1] # Mengambil nilai timur dari pixel
                                se = self.array[i+1][j+1] # Mengambil nilai tenggara dari pixel
                                s = self.array[i+1][j] # Mengambil nilai selatan dari pixel
                                # Menghitung menggunakan rumus
                                red = round(kernel[1][1]*pixel[0] + kernel[0][1]*n[0] + kernel[0][2]*ne[0] + kernel[1][2]*e[0] + kernel[2][2]*se[0] + kernel[2][1]*s[0])
                                green = round(kernel[1][1]*pixel[1] + kernel[0][1]*n[1] + kernel[0][2]*ne[1] + kernel[1][2]*e[1] + kernel[2][2]*se[1] + kernel[2][1]*s[1])
                                blue = round(kernel[1][1]*pixel[2] + kernel[0][1]*n[2] + kernel[0][2]*ne[2] + kernel[1][2]*e[2] + kernel[2][2]*se[2] + kernel[2][1]*s[2])
                            elif j == self.height-1: # Jika pixel berada di bagian kanan gambar
                                n = self.array[i-1][j] # Mengambil nilai utara dari pixel
                                nw = self.array[i-1][j-1] # Mengambil nilai barat laut dari pixel
                                w = self.array[i][j-1] # Mengambil nilai barat dari pixel
                                sw = self.array[i+1][j-1] # Mengambil nilai barat daya dari pixel
                                s = self.array[i+1][j] # Mengambil nilai selatan dari pixel
                                # Menghitung menggunakan rumus
                                red = round(kernel[1][1]*pixel[0] + kernel[0][1]*n[0] + kernel[0][0]*nw[0] + kernel[1][0]*w[0] + kernel[2][0]*sw[0] + kernel[2][1]*s[0])
                                green = round(kernel[1][1]*pixel[1] + kernel[0][1]*n[1] + kernel[0][0]*nw[1] + kernel[1][0]*w[1] + kernel[2][0]*sw[1] + kernel[2][1]*s[1])
                                blue = round(kernel[1][1]*pixel[2] + kernel[0][1]*n[2] + kernel[0][0]*nw[2] + kernel[1][0]*w[2] + kernel[2][0]*sw[2] + kernel[2][1]*s[2])
                            else: # Jika pixel tidak berada di sisi gambar
                                # Mengambil nilai sekitar pixel
                                n = self.array[i-1][j]
                                ne = self.array[i-1][j+1]
                                e = self.array[i][j+1]
                                se = self.array[i+1][j+1]
                                s = self.array[i+1][j]
                                sw = self.array[i+1][j-1]
                                w = self.array[i][j-1]
                                nw = self.array[i-1][j-1]
                                # Menghitung menggunakan rumus
                                red = round(kernel[1][1]*pixel[0] + kernel[0][0]*nw[0] + kernel[0][1]*n[0] + kernel[0][2]*ne[0] + kernel[1][0]*w[0] + kernel[1][2]*e[0] + kernel[2][0]*sw[0] + kernel[2][1]*s[0] + kernel[2][2]*se[0])
                                green = round(kernel[1][1]*pixel[1] + kernel[0][0]*nw[1] + kernel[0][1]*n[1] + kernel[0][2]*ne[1] + kernel[1][0]*w[1] + kernel[1][2]*e[1] + kernel[2][0]*sw[1] + kernel[2][1]*s[1] + kernel[2][2]*se[1])
                                blue = round(kernel[1][1]*pixel[2] + kernel[0][0]*nw[2] + kernel[0][1]*n[2] + kernel[0][2]*ne[2] + kernel[1][0]*w[2] + kernel[1][2]*e[2] + kernel[2][0]*sw[2] + kernel[2][1]*s[2] + kernel[2][2]*se[2])
                            if len(newarr[i][j]) == 4: # Jika format file .png
                                newarr[i][j] = [red,green,blue,255]
                            else: # Jika format file .jpg/.jpeg
                                newarr[i][j] = [red,green,blue]
                        #     self.array[i][j] = tuple(newarr[i][j])
                            pixels[i,j] = tuple(newarr[i][j])
            new.save('gambar/img_process.jpg')
            self.__init__()

    
    # Fungsi blur
    def blur(self):
            kernel = [[0.0625,0.125,0.0625],[0.125,0.25,0.125],[0.0625,0.125,0.0625]]
            self.proseskernel(kernel)
            
    # Fungsi sharp
    def sharp(self):
            kernel = [[0,-1,0],[-1,5,-1],[0,-1,0]]
            self.proseskernel(kernel)
    
    # Fungsi edge
    def edge(self):
            kernel = [[-1,-1,-1],[-1,8,-1],[-1,-1,-1]]
            self.proseskernel(kernel)

    # Cek Threshold
    def isThreshold(self, t, rgb):
            status = False
            t = int(t)
            rgb = int(rgb)
            if rgb >= t:
                    status = True
            return status
    
    # Algoritma Threshold Base
    def thresholdbase(self,t_red,t_green,t_blue):
            new = Image.new("RGB",(self.width,self.height),color=255) # Membuat gambar baru dengan width dan height sesuai dengan gambar
            pixels = new.load() # Memuat gambar baru
            for i in range(self.width):
                    for j in range(self.height):
                            pixel = self.array[i][j]
                            # Jika pixel i,j termasuk, maka menjadi warna hitam, else maka menjadi putih
                            if self.isThreshold(t_red,pixel[0]) and self.isThreshold(t_green,pixel[1]) and self.isThreshold(t_blue,pixel[2]):
                                    pixels[i,j] = (0,0,0)
                            else:
                                    pixels[i,j] = (255,255,255)
            new.save('gambar/img_threshold.jpg')
    
    # Algoritma Seed Region Growth non Recursion
    def seedRegion(self, t, Seed):
            new = Image.new("RGB",(self.width,self.height),color=255) # Membuat gambar baru dengan width dan height sesuai dengan gambar
            pixels = new.load() # Memuat gambar baru

            def rangeThreshold(t, Seed, Curpix): # Cek Jarak
                status = False
                t = int(t)
                if Curpix - Seed in range(0-t, t+1):
                    status = True
                return status
    
            def safeZone(x, y):  # Cek Zona
                if x >= 0 and y >= 0 and x < self.width and y < self.height:
                    return True
                else:
                    return False

            def cekTetangga(Seed, x, y, t): # Cek kandidat tetangga apakah termasuk kedalam threshold
                tetangga = []
                up = (x, y-1)
                down = (x, y+1)
                left = (x-1,y)
                right = (x+1, y)
                pusat = self.array[Seed[0]][Seed[1]]
                # jika masih didalam zona aman
                if safeZone(x,y-1):
                        # Jika belum pernah ditetapkan sebagai tetangga yg sesuai threshold
                        if visited[up[0]][up[1]] == False:
                                calon = self.array[x][y-1]
                                # Jika range antara seed dan current masih sesuai dengan threshold
                                if rangeThreshold(t, pusat[0], calon[0]) and rangeThreshold(t, pusat[1], calon[1]) and rangeThreshold(t, pusat[2], calon[2]):
                                        tetangga.append(up)
                # Sama halnya seperti flow control pertama
                if safeZone(x,y+1):
                        if visited[down[0]][down[1]] == False:
                                calon = self.array[x][y+1]
                                if rangeThreshold(t, pusat[0], calon[0]) and rangeThreshold(t, pusat[1], calon[1]) and rangeThreshold(t, pusat[2], calon[2]):
                                        tetangga.append(down)
                if safeZone(x-1,y):
                        if visited[left[0]][left[1]] == False:
                                calon = self.array[x-1][y]
                                if rangeThreshold(t, pusat[0], calon[0]) and rangeThreshold(t, pusat[1], calon[1]) and rangeThreshold(t, pusat[2], calon[2]):
                                        tetangga.append(left)
                if safeZone(x+1,y):
                        if visited[right[0]][right[1]] == False:
                                calon = self.array[x+1][y]
                                if rangeThreshold(t, pusat[0], calon[0]) and rangeThreshold(t, pusat[1], calon[1]) and rangeThreshold(t, pusat[2], calon[2]):
                                        tetangga.append(right)
                # Jika ada tetangga yang tersedia
                if len(tetangga) > 0:
                        # r = random.randint(0,len(tetangga)-1)
                        # Mengeluarkan tetangga yang akan menjadi current
                        return tetangga
                else:
                        return None
            
            # Memulai proses pencarian
            visited = [[False for j in range(self.height)] for i in range(self.width)]
            search = True
            stack, choosen = [],[]
            current = Seed
            while search:
                visited[current[0]][current[1]] = True # Akan menjadi visited ketika sudah menjadi current
                choosen_pixel = cekTetangga(Seed, current[0], current[1], t) # Cek tetangga
                if choosen_pixel is not None:
                        for i in range(len(choosen_pixel)):
                                choosen.append(choosen_pixel[i]) # Pixel yg termasuk akan dimasukkan kedalam list
                                # choosen.append(current) 
                                stack.append(current) # Memasukkan pixel - pixel sebelumnya supaya bisa di backtrack
                        current = choosen_pixel[-1] # Current diupdate dari hasil cek tetangga
                elif len(stack) > 0: # Jika tidak ada kandidat yg terpilih
                        current = stack[-1] # Melakukan backtracking
                        stack.pop(-1)
                else:
                        search = False # Jika sudah kosong, maka selesai sudah proses
            
            for k in range(self.width):
                    for l in range(self.height):
                            pix = (k,l)
                            if pix in choosen: # Jika pix ada di dalam list choosen
                                    pixels[k,l] = (0,0,0) # Diubah intensitasnya menjadi hitam
                            else:
                                    pixels[k,l] = self.array[k][l]
            new.save('gambar/img_threshold.jpg')
    
    def penebalan(self, xf, xd, yf, yd):
            self.grayscale() # Grayscale
        #   Membuat gambar baru dengan width dan height sesuai dengan gambar
            new = Image.new("RGB", (self.width, self.height), color=255)
            pixels = new.load()  # Memuat gambar baru
            for i in range(self.width): # Mengubah gambar menjadi hitam putih dengan threshold 128
                    for j in range(self.height):
                            pixel = self.array[i][j]
                            if pixel[0] < 128:
                                    pixels[i,j] = (0,0,0)
                            else:
                                    pixels[i,j] = (255,255,255)
            new.save('gambar/img_process.jpg')
            self.__init__() 
            for i in range(self.width): # Memulai penebalan yang warnanya hitam dengan anggapan kernel atas 1 bawah 1 dan
                    for j in range(self.height): # Hitam(0) adalah 1 dan Putih(255) adalah 0
                            pixel = self.array[i][j]
                            if i != 0:
                                    if i in range(xf,xd+1) and j in range(yf,yd+1): # Jika i dan j termasuk yang ditebalkan
                                            if pixel[0] == 0: # Jika pixel pada i,j berwarna hitam
                                                pixels[i-1,j] = (0,0,0) # Pixel atasnya maka ikut menjadi 1 atau hitam(0)
                                                pixels[i,j] = (0,0,0) # Begitupun pixel i,j
                                            else:
                                                pixels[i,j] = pixel
                                    else:
                                            pixels[i,j] = pixel
                            else:
                                    pixels[i,j] = pixel
            new.save('gambar/img_process.jpg')
            self.__init__()
        
    def penipisan(self, xf, xd, yf, yd):
            self.grayscale()
        #   Membuat gambar baru dengan width dan height sesuai dengan gambar
            new = Image.new("RGB", (self.width, self.height), color=255)
            pixels = new.load()  # Memuat gambar baru
            for i in range(self.width): # Mengubah gambar menjadi hitam putih dengan threshold 128
                    for j in range(self.height):
                            pixel = self.array[i][j]
                            if pixel[0] < 128:
                                    pixels[i,j] = (0,0,0)
                            else:
                                    pixels[i,j] = (255,255,255)
            new.save('gambar/img_process.jpg')
            self.__init__() 
            for i in range(self.width): # Memulai penipisan yang warnanya hitam dengan anggapan kernel atas 1 bawah 1 dan
                    for j in range(self.height): # Hitam(0) adalah 1 dan Putih(255) adalah 0
                            pixel = self.array[i][j]
                            if i != 0:
                                    if i in range(xf,xd+1) and j in range(yf,yd+1): # Jika i dan j termasuk yang ditipiskan
                                            if pixel[0] == 0:  # Jika pixel pada i,j berwarna hitam
                                                north = self.array[i-1][j] # Mengambil pixel utaranya (atasnya)
                                                if north[0] == 255: # Jika atasnya Putih(255) atau 0
                                                    pixels[i-1,j] = (255,255,255) # maka pixel yang terkena kernel
                                                    pixels[i,j] = (255,255,255) # akan berubah menjadi putih
                                                else:
                                                    pixels[i, j] = pixel
                                            else:
                                                pixels[i,j] = pixel
                                    else:
                                            pixels[i,j] = pixel
                            else:
                                    pixels[i,j] = pixel
            new.save('gambar/img_process.jpg')
            self.__init__()
