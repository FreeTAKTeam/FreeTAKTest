# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class ProfileDirectory(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: int=None, path: str=None):  # noqa: E501
        """ProfileDirectory - a model defined in Swagger

        :param id: The id of this ProfileDirectory.  # noqa: E501
        :type id: int
        :param path: The path of this ProfileDirectory.  # noqa: E501
        :type path: str
        """
        self.swagger_types = {
            'id': int,
            'path': str
        }

        self.attribute_map = {
            'id': 'id',
            'path': 'path'
        }
        self._id = id
        self._path = path

    @classmethod
    def from_dict(cls, dikt) -> 'ProfileDirectory':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ProfileDirectory of this ProfileDirectory.  # noqa: E501
        :rtype: ProfileDirectory
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this ProfileDirectory.


        :return: The id of this ProfileDirectory.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this ProfileDirectory.


        :param id: The id of this ProfileDirectory.
        :type id: int
        """

        self._id = id

    @property
    def path(self) -> str:
        """Gets the path of this ProfileDirectory.


        :return: The path of this ProfileDirectory.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path: str):
        """Sets the path of this ProfileDirectory.


        :param path: The path of this ProfileDirectory.
        :type path: str
        """

        self._path = path