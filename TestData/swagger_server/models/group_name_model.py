# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class GroupNameModel(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, groupname: str=None):  # noqa: E501
        """GroupNameModel - a model defined in Swagger

        :param groupname: The groupname of this GroupNameModel.  # noqa: E501
        :type groupname: str
        """
        self.swagger_types = {
            'groupname': str
        }

        self.attribute_map = {
            'groupname': 'groupname'
        }
        self._groupname = groupname

    @classmethod
    def from_dict(cls, dikt) -> 'GroupNameModel':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The GroupNameModel of this GroupNameModel.  # noqa: E501
        :rtype: GroupNameModel
        """
        return util.deserialize_model(dikt, cls)

    @property
    def groupname(self) -> str:
        """Gets the groupname of this GroupNameModel.


        :return: The groupname of this GroupNameModel.
        :rtype: str
        """
        return self._groupname

    @groupname.setter
    def groupname(self, groupname: str):
        """Sets the groupname of this GroupNameModel.


        :param groupname: The groupname of this GroupNameModel.
        :type groupname: str
        """

        self._groupname = groupname
