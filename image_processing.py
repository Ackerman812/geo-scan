from PIL import Image, ImageChops, ImageEnhance
import numpy as np



def analyze_images(img1,img2):


    image1 = Image.open(img1).convert("RGB")


    image2 = Image.open(img2).convert("RGB")



    image2=image2.resize(
        image1.size
    )



    diff = ImageChops.difference(

        image1,

        image2

    )



    gray=diff.convert("L")

    array=np.array(gray)



    # усиление карты изменений

    enhancer=ImageEnhance.Contrast(diff)

    heatmap=enhancer.enhance(3)



    changed_pixels=np.sum(

        array > 40

    )



    total_pixels=array.size



    change_percent=(

        changed_pixels /

        total_pixels

    )*100



    similarity=100-change_percent



    return {


        "before":

        image1,


        "after":

        image2,


        "difference":

        heatmap,


        "change_percent":

        round(change_percent,2),


        "similarity":

        round(similarity,2),


        "pixels":

        total_pixels,


        "changed_pixels":

        int(changed_pixels)

    }