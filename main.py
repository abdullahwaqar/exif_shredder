import os, sys

try:
    from PIL import Image
except ImportError as e:
    print("{}\npip install pillow").format(e)
    sys.exit(1)

image_file = 'test.png'# input("[*] Enter Image Path: ")


if os.path.isfile(image_file):
    directory, filename = os.path.split(image_file)
    print(filename)
    image = Image.open(image_file)
    data = list(image.getdata())
    image_without_exif = Image.new(image.mode, image.size)
    image_without_exif.putdata(data)
    image_without_exif.save("EXIF_Stripped_" + filename)
    print("[#] File Saved: %s/EXIF_STRIPPED_%s" % (directory, filename))
    sys.exit(0)
else:
    print("[=] Image Path Does not Exist.")
    sys.exit(1)