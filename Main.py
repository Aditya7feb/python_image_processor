#main program
print('Image Editor')
print('version 1')
print('This is a Menu Driven Image Processor where you can edit and get info for your image')

def switch():
    #displaying menu
    print('list of availaible features for this image are:-\n')
    print('1.Crop (c)\t 2.Rotate (r)\t 3.Face Detection (fd)\n')
    print('4.Enhance Contrast (ct)\t 5.Smoothen (s)\t 6.Edge Detection (ed)\n')
    print('7.Channel Seperation (cs)\t 8.histogram (h)\n\n')

    print('Enter the number before the function to execute program:')

    option = int(input(""))

    def fd():
        from skimage.feature import Cascade
        from skimage import data, color
        import matplotib.pyplot as plt
        from matplotlib.patches import Rectangle

        path=''
        img = plt.imread(path)
        plt.axis('off')
        plt.imshow(img)

        train_set = data.lbp_frontal_face_cascade_filename()
        detector = Cascade(train_set)
        detected = detector.detect_multi_scale(img=img, scale_factor = 1.2, step_ratio = 1, min_size = (10,10), max_size = (200,200))
        print('Detected')

        def show_detected_face(result, detected, title = "Detected Faces"):
            plt.imshow(result)
            img_desc=plt.gca()
            plt.set_cmap('gray')
            plt.title(title)
            plt.axis('off')

            for rec in detected:
                img_desc.add_patch(
                    Rectangle(
                        (rec['c'], rec['r'])
                        rec['width'], rec['height'], fill = False, color = 'g', line_width = 3
                    )
                )
            plt.show()

        show_detected_face(img,detected)

     dict = {
        1 : Sar,
        2 : Lar,
        3 : fd,

    }
    dict.get(option,default)()



