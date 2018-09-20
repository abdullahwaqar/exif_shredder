import os, sys, argparse

try:
    from PIL import Image
except ImportError as e:
    print("{}\npip install pillow").format(e)
    sys.exit(1)

def main(file_name):
    image_file = file_name
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

def arg():
    parser = argparse.ArgumentParser()
    parser.add_argument('file_name')
    args = parser.parse_args()
    main(args.file_name)

if __name__ == '__main__':
    arg()