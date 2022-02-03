import os

import cv2
import numpy as np
import PySide6.QtWidgets as qtw

# Display result saved image
class ResultDialog(qtw.QMessageBox):
    def __init__(self, imgPath=None, errorStackTrace=None):
        super().__init__()

        if imgPath == None and errorStackTrace != None:
            # Error msg
            self.setStandardButtons(qtw.QMessageBox.Ok)
            self.setIcon(qtw.QMessageBox.Critical)
            self.setWindowTitle("Export failed")
            self.setText("Failed to export!\n")
            self.setInformativeText("Error:\n" + str(errorStackTrace))
        elif imgPath != None and errorStackTrace == None:
            # Success msg
            self.setStandardButtons(qtw.QMessageBox.Ok)
            self.setIcon(qtw.QMessageBox.Information)
            self.setWindowTitle("Export success")
            self.setText(
                "Successfully exported output image.\n"
                + "File size is: "
                + str(round(os.path.getsize(imgPath) / 1024 / 1024, 2))
                + "MB.\n"
            )
            self.setInformativeText("File location:\n" + imgPath)


def createDialog(imageArray, imgType, chosenPath):
    imgPath = None
    errorStackTrace = None

    # Convert float32 to uint8
    print(imageArray.dtype)  # float32
    imageArray = np.around(imageArray)
    imageArray[imageArray > 255] = 255
    imageArray[imageArray < 0] = 0
    imageArray = imageArray.astype(np.uint8)
    # TODO: Allow user to change compression settings (for jpg and png)
    if imgType == "jpg":
        try:
            # 0-100 quality
            cv2.imwrite(chosenPath, imageArray, [cv2.IMWRITE_JPEG_QUALITY, 100])
            imgPath = chosenPath
        except Exception as e:
            errorStackTrace = e
    elif imgType == "png":
        try:
            # 9-0 compression
            cv2.imwrite(chosenPath, imageArray, [cv2.IMWRITE_PNG_COMPRESSION, 0])
            imgPath = chosenPath
        except Exception as e:
            errorStackTrace = e
    elif imgType == "tiff":
        try:
            cv2.imwrite(chosenPath, imageArray)
            imgPath = chosenPath
        except Exception as e:
            errorStackTrace = e

    ResultDialog(imgPath, errorStackTrace).exec()
