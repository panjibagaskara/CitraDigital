from PIL import Image

def grayscale():
    r,g,b = 0,0,0
    img = Image.open('gambar/img_process.jpg')
    width, height = img.size
    new = Image.new("RGB", (width,height), "white")
    pixels = new.load()
    for i in range(width):
        for j in range(height):
            pixel = img.getpixel((i,j))
            red = pixel[0]
            green = pixel[1]
            blue = pixel[2]
            r += int(red)
            g += int(green)
            b += int(blue)
    total = r+g+b
    for i in range(width):
        for j in range(height):
            pixel = img.getpixel((i,j))
            red = pixel[0]
            green = pixel[1]
            blue = pixel[2]
            gray = (red * (r/total)) + (green * (g/total)) + (blue * (b/total))
            pixels[i,j] = (int(gray), int(gray), int(gray))
    new.save('gambar/img_process.jpg')