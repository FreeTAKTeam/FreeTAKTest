# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.auth import Auth  # noqa: F401,E501
from swagger_server.models.buffer import Buffer  # noqa: F401,E501
from swagger_server.models.certificate_signing import CertificateSigning  # noqa: F401,E501
from swagger_server.models.citrap import Citrap  # noqa: F401,E501
from swagger_server.models.cluster import Cluster  # noqa: F401,E501
from swagger_server.models.dissemination import Dissemination  # noqa: F401,E501
from swagger_server.models.docs import Docs  # noqa: F401,E501
from swagger_server.models.email import Email  # noqa: F401,E501
from swagger_server.models.federation import Federation  # noqa: F401,E501
from swagger_server.models.ferry import Ferry  # noqa: F401,E501
from swagger_server.models.filter import Filter  # noqa: F401,E501
from swagger_server.models.geocache import Geocache  # noqa: F401,E501
from swagger_server.models.locate import Locate  # noqa: F401,E501
from swagger_server.models.model_async import ModelAsync  # noqa: F401,E501
from swagger_server.models.network import Network  # noqa: F401,E501
from swagger_server.models.plugins import Plugins  # noqa: F401,E501
from swagger_server.models.profile import Profile  # noqa: F401,E501
from swagger_server.models.repeater import Repeater  # noqa: F401,E501
from swagger_server.models.repository import Repository  # noqa: F401,E501
from swagger_server.models.security import Security  # noqa: F401,E501
from swagger_server.models.submission import Submission  # noqa: F401,E501
from swagger_server.models.subscription import Subscription  # noqa: F401,E501
from swagger_server.models.vbm import Vbm  # noqa: F401,E501
from swagger_server.models.xmpp import Xmpp  # noqa: F401,E501
from swagger_server import util


class Configuration(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, network: Network=None, auth: Auth=None, submission: Submission=None, subscription: Subscription=None, repository: Repository=None, repeater: Repeater=None, filter: Filter=None, buffer: Buffer=None, dissemination: Dissemination=None, certificate_signing: CertificateSigning=None, security: Security=None, ferry: Ferry=None, _async: ModelAsync=None, federation: Federation=None, geocache: Geocache=None, citrap: Citrap=None, xmpp: Xmpp=None, plugins: Plugins=None, cluster: Cluster=None, docs: Docs=None, email: Email=None, locate: Locate=None, vbm: Vbm=None, profile: Profile=None, force_low_concurrency: bool=None):  # noqa: E501
        """Configuration - a model defined in Swagger

        :param network: The network of this Configuration.  # noqa: E501
        :type network: Network
        :param auth: The auth of this Configuration.  # noqa: E501
        :type auth: Auth
        :param submission: The submission of this Configuration.  # noqa: E501
        :type submission: Submission
        :param subscription: The subscription of this Configuration.  # noqa: E501
        :type subscription: Subscription
        :param repository: The repository of this Configuration.  # noqa: E501
        :type repository: Repository
        :param repeater: The repeater of this Configuration.  # noqa: E501
        :type repeater: Repeater
        :param filter: The filter of this Configuration.  # noqa: E501
        :type filter: Filter
        :param buffer: The buffer of this Configuration.  # noqa: E501
        :type buffer: Buffer
        :param dissemination: The dissemination of this Configuration.  # noqa: E501
        :type dissemination: Dissemination
        :param certificate_signing: The certificate_signing of this Configuration.  # noqa: E501
        :type certificate_signing: CertificateSigning
        :param security: The security of this Configuration.  # noqa: E501
        :type security: Security
        :param ferry: The ferry of this Configuration.  # noqa: E501
        :type ferry: Ferry
        :param _async: The _async of this Configuration.  # noqa: E501
        :type _async: ModelAsync
        :param federation: The federation of this Configuration.  # noqa: E501
        :type federation: Federation
        :param geocache: The geocache of this Configuration.  # noqa: E501
        :type geocache: Geocache
        :param citrap: The citrap of this Configuration.  # noqa: E501
        :type citrap: Citrap
        :param xmpp: The xmpp of this Configuration.  # noqa: E501
        :type xmpp: Xmpp
        :param plugins: The plugins of this Configuration.  # noqa: E501
        :type plugins: Plugins
        :param cluster: The cluster of this Configuration.  # noqa: E501
        :type cluster: Cluster
        :param docs: The docs of this Configuration.  # noqa: E501
        :type docs: Docs
        :param email: The email of this Configuration.  # noqa: E501
        :type email: Email
        :param locate: The locate of this Configuration.  # noqa: E501
        :type locate: Locate
        :param vbm: The vbm of this Configuration.  # noqa: E501
        :type vbm: Vbm
        :param profile: The profile of this Configuration.  # noqa: E501
        :type profile: Profile
        :param force_low_concurrency: The force_low_concurrency of this Configuration.  # noqa: E501
        :type force_low_concurrency: bool
        """
        self.swagger_types = {
            'network': Network,
            'auth': Auth,
            'submission': Submission,
            'subscription': Subscription,
            'repository': Repository,
            'repeater': Repeater,
            'filter': Filter,
            'buffer': Buffer,
            'dissemination': Dissemination,
            'certificate_signing': CertificateSigning,
            'security': Security,
            'ferry': Ferry,
            '_async': ModelAsync,
            'federation': Federation,
            'geocache': Geocache,
            'citrap': Citrap,
            'xmpp': Xmpp,
            'plugins': Plugins,
            'cluster': Cluster,
            'docs': Docs,
            'email': Email,
            'locate': Locate,
            'vbm': Vbm,
            'profile': Profile,
            'force_low_concurrency': bool
        }

        self.attribute_map = {
            'network': 'network',
            'auth': 'auth',
            'submission': 'submission',
            'subscription': 'subscription',
            'repository': 'repository',
            'repeater': 'repeater',
            'filter': 'filter',
            'buffer': 'buffer',
            'dissemination': 'dissemination',
            'certificate_signing': 'certificateSigning',
            'security': 'security',
            'ferry': 'ferry',
            '_async': 'async',
            'federation': 'federation',
            'geocache': 'geocache',
            'citrap': 'citrap',
            'xmpp': 'xmpp',
            'plugins': 'plugins',
            'cluster': 'cluster',
            'docs': 'docs',
            'email': 'email',
            'locate': 'locate',
            'vbm': 'vbm',
            'profile': 'profile',
            'force_low_concurrency': 'forceLowConcurrency'
        }
        self._network = network
        self._auth = auth
        self._submission = submission
        self._subscription = subscription
        self._repository = repository
        self._repeater = repeater
        self._filter = filter
        self._buffer = buffer
        self._dissemination = dissemination
        self._certificate_signing = certificate_signing
        self._security = security
        self._ferry = ferry
        self.__async = _async
        self._federation = federation
        self._geocache = geocache
        self._citrap = citrap
        self._xmpp = xmpp
        self._plugins = plugins
        self._cluster = cluster
        self._docs = docs
        self._email = email
        self._locate = locate
        self._vbm = vbm
        self._profile = profile
        self._force_low_concurrency = force_low_concurrency

    @classmethod
    def from_dict(cls, dikt) -> 'Configuration':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Configuration of this Configuration.  # noqa: E501
        :rtype: Configuration
        """
        return util.deserialize_model(dikt, cls)

    @property
    def network(self) -> Network:
        """Gets the network of this Configuration.


        :return: The network of this Configuration.
        :rtype: Network
        """
        return self._network

    @network.setter
    def network(self, network: Network):
        """Sets the network of this Configuration.


        :param network: The network of this Configuration.
        :type network: Network
        """
        if network is None:
            raise ValueError("Invalid value for `network`, must not be `None`")  # noqa: E501

        self._network = network

    @property
    def auth(self) -> Auth:
        """Gets the auth of this Configuration.


        :return: The auth of this Configuration.
        :rtype: Auth
        """
        return self._auth

    @auth.setter
    def auth(self, auth: Auth):
        """Sets the auth of this Configuration.


        :param auth: The auth of this Configuration.
        :type auth: Auth
        """
        if auth is None:
            raise ValueError("Invalid value for `auth`, must not be `None`")  # noqa: E501

        self._auth = auth

    @property
    def submission(self) -> Submission:
        """Gets the submission of this Configuration.


        :return: The submission of this Configuration.
        :rtype: Submission
        """
        return self._submission

    @submission.setter
    def submission(self, submission: Submission):
        """Sets the submission of this Configuration.


        :param submission: The submission of this Configuration.
        :type submission: Submission
        """
        if submission is None:
            raise ValueError("Invalid value for `submission`, must not be `None`")  # noqa: E501

        self._submission = submission

    @property
    def subscription(self) -> Subscription:
        """Gets the subscription of this Configuration.


        :return: The subscription of this Configuration.
        :rtype: Subscription
        """
        return self._subscription

    @subscription.setter
    def subscription(self, subscription: Subscription):
        """Sets the subscription of this Configuration.


        :param subscription: The subscription of this Configuration.
        :type subscription: Subscription
        """
        if subscription is None:
            raise ValueError("Invalid value for `subscription`, must not be `None`")  # noqa: E501

        self._subscription = subscription

    @property
    def repository(self) -> Repository:
        """Gets the repository of this Configuration.


        :return: The repository of this Configuration.
        :rtype: Repository
        """
        return self._repository

    @repository.setter
    def repository(self, repository: Repository):
        """Sets the repository of this Configuration.


        :param repository: The repository of this Configuration.
        :type repository: Repository
        """
        if repository is None:
            raise ValueError("Invalid value for `repository`, must not be `None`")  # noqa: E501

        self._repository = repository

    @property
    def repeater(self) -> Repeater:
        """Gets the repeater of this Configuration.


        :return: The repeater of this Configuration.
        :rtype: Repeater
        """
        return self._repeater

    @repeater.setter
    def repeater(self, repeater: Repeater):
        """Sets the repeater of this Configuration.


        :param repeater: The repeater of this Configuration.
        :type repeater: Repeater
        """
        if repeater is None:
            raise ValueError("Invalid value for `repeater`, must not be `None`")  # noqa: E501

        self._repeater = repeater

    @property
    def filter(self) -> Filter:
        """Gets the filter of this Configuration.


        :return: The filter of this Configuration.
        :rtype: Filter
        """
        return self._filter

    @filter.setter
    def filter(self, filter: Filter):
        """Sets the filter of this Configuration.


        :param filter: The filter of this Configuration.
        :type filter: Filter
        """
        if filter is None:
            raise ValueError("Invalid value for `filter`, must not be `None`")  # noqa: E501

        self._filter = filter

    @property
    def buffer(self) -> Buffer:
        """Gets the buffer of this Configuration.


        :return: The buffer of this Configuration.
        :rtype: Buffer
        """
        return self._buffer

    @buffer.setter
    def buffer(self, buffer: Buffer):
        """Sets the buffer of this Configuration.


        :param buffer: The buffer of this Configuration.
        :type buffer: Buffer
        """
        if buffer is None:
            raise ValueError("Invalid value for `buffer`, must not be `None`")  # noqa: E501

        self._buffer = buffer

    @property
    def dissemination(self) -> Dissemination:
        """Gets the dissemination of this Configuration.


        :return: The dissemination of this Configuration.
        :rtype: Dissemination
        """
        return self._dissemination

    @dissemination.setter
    def dissemination(self, dissemination: Dissemination):
        """Sets the dissemination of this Configuration.


        :param dissemination: The dissemination of this Configuration.
        :type dissemination: Dissemination
        """
        if dissemination is None:
            raise ValueError("Invalid value for `dissemination`, must not be `None`")  # noqa: E501

        self._dissemination = dissemination

    @property
    def certificate_signing(self) -> CertificateSigning:
        """Gets the certificate_signing of this Configuration.


        :return: The certificate_signing of this Configuration.
        :rtype: CertificateSigning
        """
        return self._certificate_signing

    @certificate_signing.setter
    def certificate_signing(self, certificate_signing: CertificateSigning):
        """Sets the certificate_signing of this Configuration.


        :param certificate_signing: The certificate_signing of this Configuration.
        :type certificate_signing: CertificateSigning
        """

        self._certificate_signing = certificate_signing

    @property
    def security(self) -> Security:
        """Gets the security of this Configuration.


        :return: The security of this Configuration.
        :rtype: Security
        """
        return self._security

    @security.setter
    def security(self, security: Security):
        """Sets the security of this Configuration.


        :param security: The security of this Configuration.
        :type security: Security
        """
        if security is None:
            raise ValueError("Invalid value for `security`, must not be `None`")  # noqa: E501

        self._security = security

    @property
    def ferry(self) -> Ferry:
        """Gets the ferry of this Configuration.


        :return: The ferry of this Configuration.
        :rtype: Ferry
        """
        return self._ferry

    @ferry.setter
    def ferry(self, ferry: Ferry):
        """Sets the ferry of this Configuration.


        :param ferry: The ferry of this Configuration.
        :type ferry: Ferry
        """

        self._ferry = ferry

    @property
    def _async(self) -> ModelAsync:
        """Gets the _async of this Configuration.


        :return: The _async of this Configuration.
        :rtype: ModelAsync
        """
        return self.__async

    @_async.setter
    def _async(self, _async: ModelAsync):
        """Sets the _async of this Configuration.


        :param _async: The _async of this Configuration.
        :type _async: ModelAsync
        """

        self.__async = _async

    @property
    def federation(self) -> Federation:
        """Gets the federation of this Configuration.


        :return: The federation of this Configuration.
        :rtype: Federation
        """
        return self._federation

    @federation.setter
    def federation(self, federation: Federation):
        """Sets the federation of this Configuration.


        :param federation: The federation of this Configuration.
        :type federation: Federation
        """

        self._federation = federation

    @property
    def geocache(self) -> Geocache:
        """Gets the geocache of this Configuration.


        :return: The geocache of this Configuration.
        :rtype: Geocache
        """
        return self._geocache

    @geocache.setter
    def geocache(self, geocache: Geocache):
        """Sets the geocache of this Configuration.


        :param geocache: The geocache of this Configuration.
        :type geocache: Geocache
        """

        self._geocache = geocache

    @property
    def citrap(self) -> Citrap:
        """Gets the citrap of this Configuration.


        :return: The citrap of this Configuration.
        :rtype: Citrap
        """
        return self._citrap

    @citrap.setter
    def citrap(self, citrap: Citrap):
        """Sets the citrap of this Configuration.


        :param citrap: The citrap of this Configuration.
        :type citrap: Citrap
        """

        self._citrap = citrap

    @property
    def xmpp(self) -> Xmpp:
        """Gets the xmpp of this Configuration.


        :return: The xmpp of this Configuration.
        :rtype: Xmpp
        """
        return self._xmpp

    @xmpp.setter
    def xmpp(self, xmpp: Xmpp):
        """Sets the xmpp of this Configuration.


        :param xmpp: The xmpp of this Configuration.
        :type xmpp: Xmpp
        """

        self._xmpp = xmpp

    @property
    def plugins(self) -> Plugins:
        """Gets the plugins of this Configuration.


        :return: The plugins of this Configuration.
        :rtype: Plugins
        """
        return self._plugins

    @plugins.setter
    def plugins(self, plugins: Plugins):
        """Sets the plugins of this Configuration.


        :param plugins: The plugins of this Configuration.
        :type plugins: Plugins
        """

        self._plugins = plugins

    @property
    def cluster(self) -> Cluster:
        """Gets the cluster of this Configuration.


        :return: The cluster of this Configuration.
        :rtype: Cluster
        """
        return self._cluster

    @cluster.setter
    def cluster(self, cluster: Cluster):
        """Sets the cluster of this Configuration.


        :param cluster: The cluster of this Configuration.
        :type cluster: Cluster
        """

        self._cluster = cluster

    @property
    def docs(self) -> Docs:
        """Gets the docs of this Configuration.


        :return: The docs of this Configuration.
        :rtype: Docs
        """
        return self._docs

    @docs.setter
    def docs(self, docs: Docs):
        """Sets the docs of this Configuration.


        :param docs: The docs of this Configuration.
        :type docs: Docs
        """

        self._docs = docs

    @property
    def email(self) -> Email:
        """Gets the email of this Configuration.


        :return: The email of this Configuration.
        :rtype: Email
        """
        return self._email

    @email.setter
    def email(self, email: Email):
        """Sets the email of this Configuration.


        :param email: The email of this Configuration.
        :type email: Email
        """

        self._email = email

    @property
    def locate(self) -> Locate:
        """Gets the locate of this Configuration.


        :return: The locate of this Configuration.
        :rtype: Locate
        """
        return self._locate

    @locate.setter
    def locate(self, locate: Locate):
        """Sets the locate of this Configuration.


        :param locate: The locate of this Configuration.
        :type locate: Locate
        """

        self._locate = locate

    @property
    def vbm(self) -> Vbm:
        """Gets the vbm of this Configuration.


        :return: The vbm of this Configuration.
        :rtype: Vbm
        """
        return self._vbm

    @vbm.setter
    def vbm(self, vbm: Vbm):
        """Sets the vbm of this Configuration.


        :param vbm: The vbm of this Configuration.
        :type vbm: Vbm
        """

        self._vbm = vbm

    @property
    def profile(self) -> Profile:
        """Gets the profile of this Configuration.


        :return: The profile of this Configuration.
        :rtype: Profile
        """
        return self._profile

    @profile.setter
    def profile(self, profile: Profile):
        """Sets the profile of this Configuration.


        :param profile: The profile of this Configuration.
        :type profile: Profile
        """

        self._profile = profile

    @property
    def force_low_concurrency(self) -> bool:
        """Gets the force_low_concurrency of this Configuration.


        :return: The force_low_concurrency of this Configuration.
        :rtype: bool
        """
        return self._force_low_concurrency

    @force_low_concurrency.setter
    def force_low_concurrency(self, force_low_concurrency: bool):
        """Sets the force_low_concurrency of this Configuration.


        :param force_low_concurrency: The force_low_concurrency of this Configuration.
        :type force_low_concurrency: bool
        """

        self._force_low_concurrency = force_low_concurrency
