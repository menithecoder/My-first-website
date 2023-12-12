from PIL import Image
import os


#corner == witch corner you want the non dominate to show 1 ==0 0  2== x,0  3== x,y 4== 0,y

def resize_images_to_equal_size(image1_path, image2_path):
    img1 = Image.open(image1_path)
    img2 = Image.open(image2_path)

    # Get the sizes of both images
    width1, height1 = img1.size
    width2, height2 = img2.size

    # Calculate the minimum dimensions to resize both images
    min_width = max(width1, width2)
    min_height = max(height1, height2)

    # Resize both images to have equal dimensions
    img1_resized = img1.resize((min_width, min_height))
    img2_resized = img2.resize((min_width, min_height))

    return img1_resized, img2_resized
def image1_dominate(img1, width1, height1, width_ratio, height_ratio):
    new_width1 = int(width1 * width_ratio)
    new_height1 = int(height1 * height_ratio)
    img1 = img1.resize((new_width1, new_height1))
    return img1

def image2_dominate(img2, width2, height2, width_ratio, height_ratio):
    new_width2 = int(width2 * width_ratio)
    new_height2 = int(height2 * height_ratio)
    img2 = img2.resize((new_width2, new_height2))

    return img2

def merge_images_custom( ):
    image1_path=input()
    image2_path=input()
    output_path=input()
    width_ratio=input()
    height_ratio=input()




    if width_ratio != 1 and height_ratio != 1:
        dominate = int(input("Enter '1' or '2' to indicate which image should dominate: "))
    else:
        dominate=1


    corner = int(input())
    output_filename = "merged_image.jpg"  # Define the output filename
    download_path = os.path.join(os.path.expanduser("~"), "Downloads", output_filename)
    img1_resized, img2_resized = resize_images_to_equal_size(image1_path, image2_path)

    width1, height1 = img1_resized.size
    width2, height2 = img2_resized.size
    wi=0
    hi=0

    if dominate == 1:
        if width_ratio == 1 and height_ratio != 1:

            print((1-height_ratio))
            new_height1 = int(height1 * (1-height_ratio))
            img1_resized = img1_resized.resize((width1, new_height1))
            hi=int(height2 * height_ratio)




        if width_ratio != 1 and height_ratio == 1:

            new_width1 = int(width1 * (1-width_ratio))
            img1_resized = img1_resized.resize((new_width1, height1))
            wi = int(width2 * width_ratio)




        img2 = image1_dominate(img2_resized, width2, height2, width_ratio, height_ratio)

        merged_image = Image.new('RGB', (width1, height1))


        if corner==1:
            print(corner)
            merged_image.paste(img1_resized, (wi, hi))
            merged_image.paste(img2, (0, 0))
            merged_image.save(download_path)
            print(f"Images merged with custom proportions and saved to {output_path}")
        elif corner==2:
            merged_image.paste(img1_resized, (0, hi))
            position_x = int(width1 * (1 - width_ratio))
            merged_image.paste(img2, (position_x, 0))
            merged_image.save(download_path)
            print(f"Images merged with custom proportions and saved to {output_path}")
        elif corner==3:
            merged_image.paste(img1_resized, (0, 0))
            position_x = int(width1 * (1 - width_ratio))
            position_y = int(height1 * (1 - height_ratio))
            merged_image.paste(img2, (position_x, position_y))
            merged_image.save(download_path)
            print(f"Images merged with custom proportions and saved to {output_path}")
        elif corner==4:
            merged_image.paste(img1_resized, (wi, 0))
            position_y = int(height1 * (1 - height_ratio))
            merged_image.paste(img2, (0, position_y))
            merged_image.save(download_path)
            print(f"Images merged with custom proportions and saved to {output_path}")






    elif dominate == 2:
        img1 = image2_dominate(img1_resized, width1, height1, width_ratio, height_ratio)
        merged_image = Image.new('RGB', (width2, height2))
        merged_image.paste(img2_resized, (0, 0))
        if corner==1:
            print(corner)
            merged_image.paste(img1, (0, 0))
            merged_image.save(download_path)
            print(f"Images merged with custom proportions and saved to {output_path}")
        elif corner==2:
            position_x = int(width1 * (1 - width_ratio))
            merged_image.paste(img1, (position_x, 0))
            merged_image.save(download_path)
            print(f"Images merged with custom proportions and saved to {output_path}")
        elif corner==3:
            position_x = int(width1 * (1 - width_ratio))
            position_y = int(height1 * (1 - height_ratio))
            merged_image.paste(img1, (position_x, position_y))
            merged_image.save(download_path)
            print(f"Images merged with custom proportions and saved to {output_path}")
        elif corner==4:
            position_y = int(height1 * (1 - height_ratio))
            merged_image.paste(img1, (0, position_y))
            merged_image.save(download_path)
            print(f"Images merged with custom proportions and saved to {output_path}")


merge_images_custom('image1.jpg', 'image2.jpg', 'merged_custom.jpg', 0.75, 0.75)




