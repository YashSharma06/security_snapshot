import cv2
import dropbox
import time
import random

start_time = time.time()

def take_snapshot():
    number = random.randint(0,100)
    
    videoCamera = cv2.VideoCapture(0)
    result = True

    while(result):
        ret,frame = videoCamera.read()
        image_name = "img"+str(number)+".png"
        cv2.imwrite(image_name,frame)
        start_time = time.time
        result = False
    
    return image_name
    print("snapshot_taken")
    videoCamera.release()
    cv2.destroyAllWindows()

def upload_image(img_name):
    access_token = "McfFQUW_RWwAAAAAAAAAAd0MW3V1zlnibGo96jPegh4MtIPlodRJBXpi_24uNRk9"
    files = img_name

    file_from = files
    file_to = "/photos/"+(img_name)

    dbx = dropbox.Dropbox(access_token)

    with open(file_from, "rb") as f:
        dbx.files_upload(f.read(),file_to,mode = dropbox.files.WriteMode.overwrite)
        print("file uploaded")


def main():
    while(True):
        if((time.time()-start_time)>= 30):
            name = take_snapshot()
            upload_image(name)

main()






