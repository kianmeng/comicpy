# -*- coding: utf-8 -*-
"""
`ImageComicData` handles image-related issues, such as resizing, resizing in
the future, formatting, and other related issues, if required.
"""


from comicpy.models import ImageComicData

from PIL import Image
import io

from typing import TypeVar, Union

ImageInstancePIL = TypeVar("ImageInstancePIL")


class ImagesHandler:
    """
    Class dealing with image issues, such as resizing.
    """
    validFormats = {
        'JPEG': 'jpeg',
        'PNG': 'png',
        'JPG': 'jpeg'
    }
    sizeImageDict = {
        'sizeImage': None,
        'small': (800, 1200),
        'medium': (1000, 1500),
        'large': (1200, 1800),
    }

    def get_size(
        self,
        size: str = 'preserve'
    ) -> tuple:
        """
        Returns tupe of size.
        """
        try:
            return ImagesHandler.sizeImageDict[size]
        except KeyError:
            return ImagesHandler.sizeImageDict['small']

    def new_image(
        self,
        name_image: str,
        currentImage: Union[bytes, ImageInstancePIL],
        extention: str,
        unit: str,
        sizeImage: str = 'preserve',
    ) -> ImageComicData:
        """
        Resize image.

        Args:
            name_image: name of image.
            currentImage: `PIL` instance with data of original image.
            extension: extention of original image.
            sizeImage: category of size to resize original image. Default is
                       'small'.
            unit: unit of measure data.

        Returns:
            ImageComicData: `ImageComicData` instance with data of image.
        """
        size_tuple = self.get_size(size=sizeImage)
        newImageIO = io.BytesIO()

        if type(currentImage) is bytes:
            currentImage = Image.open(io.BytesIO(currentImage))

        if size_tuple is not None:
            imageResized = currentImage.resize(
                                    size_tuple,
                                    resample=Image.Resampling.LANCZOS
                                )
        imageResized.save(
                newImageIO,
                format=ImagesHandler.validFormats[extention],
                quality=90
            )

        image_comic = ImageComicData(
                        filename=name_image,
                        bytes_data=newImageIO,
                        unit=unit
                    )
        return image_comic
