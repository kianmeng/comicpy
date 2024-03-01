# -*- coding: utf-8 -*-
"""
Utils
"""

import os
import sys

from typing import Union, Tuple, TypeVar

CurrentFile = TypeVar('CurrentFile')


class Paths:
    """
    Centralized class in charge of matters related to paths.
    """
    DIR = 'comicpyData'
    HOME_DIR = os.path.expanduser('~')
    ROOT_PATH = os.path.join(HOME_DIR, DIR)

    def get_separator(self) -> str:
        return os.sep

    def splitext(
        self,
        path: str
    ) -> tuple:
        """
        Gets name and extention of file.

        Args
            path: string of path

        Returns
            tuple: name and extention of file.
        """
        return os.path.splitext(path)

    def get_basename(
        self,
        path: str
    ) -> str:
        """
        Gets file name.

        Args
            path: string of path

        Returns
            str: filename of file.
        """
        return os.path.basename(path)

    def get_dirname(
        self,
        path: str
    ) -> str:
        """
        Gets name of directory.

        Args
            path: string of path

        Returns
            str: name of directory.
        """
        return os.path.dirname(path)

    def exists(
        self,
        path: str
    ) -> bool:
        """
        Check if path exists.

        Args
            path: string of path

        Returns
            bool: `True` if exists, otherwise, `False`
        """
        return os.path.exists(path)

    def get_abs_path(
        self,
        path: str
    ) -> str:
        """
        Gets absolute path.

        Args
            path: string of path

        Returns
            str: string of absolute path.
        """
        return os.path.abspath(path)

    def build(
        self,
        *path: Union[str, Tuple[str]],
        make: bool = False
    ) -> str:
        """
        It builds paths, and creates them if necessary.

        Args
            path: string of path

        Returns
            str: string of path.
        """
        path_ = os.path.join(*path)
        if make:
            self.check_and_create(path=path_)
        return path_

    def check_and_create(
        self,
        path: str
    ) -> None:
        """
        Check if the route exists, if not, create it.

        Args
            path: string of path
        """
        if not self.exists(path):
            os.makedirs(path)

    def get_dirname_level(
        self,
        path: str,
        level: int = 0
    ) -> str:
        """
        Gets and returns the directory name depending on the level.

        Args
            path: string of path
            level: integer, indicate the level of directory. Default is `0`.

        Returns
            str: string of path.
        """
        return os.path.normpath(path).split(os.sep)[level]


class VarEnviron:
    """
    Class in charge of add rar executable path to `PATH` environment.
    Binaries downloaded from `https://www.rarlab.com/download.htm`.
    """

    HOME = Paths.HOME_DIR
    rarWin32 = 'C:\\Program Files\\WinRar'
    linuxPath = ('.local', 'bin')
    bin_rar_path = ('comicpy', 'bin_rar')

    def setup(
        path_exec: str = None
    ):
        """
        Sets the paths in the `PATH` environment.

        Default set RAR path from RAR/UNRAR binaries in the `ComicPy` package.
        """
        plat = sys.platform

        paths = Paths()
        path_rar_comicpy = paths.build(
                                        os.getcwd(),
                                        VarEnviron.bin_rar_path[0],
                                        VarEnviron.bin_rar_path[1]
                                    )

        if plat == 'win32':
            os.environ['PATH'] += ';%s' % (path_rar_comicpy)
            if path_exec is not None:
                os.environ['PATH'] += ';%s' % (path_exec)
            else:
                os.environ['PATH'] += ';%s' % (VarEnviron.rarWin32)
        elif plat == 'linux':
            os.environ['PATH'] += ':%s' % (path_rar_comicpy)
            if path_exec is not None:
                os.environ['PATH'] += ':%s' % (path_exec)
