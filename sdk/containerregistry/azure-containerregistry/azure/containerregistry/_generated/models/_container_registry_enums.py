# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator (autorest: 3.1.3, generator: {generator})
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class ArtifactArchitecture(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The artifact platform's architecture.
    """

    #: i386.
    I386 = "386"
    #: AMD64.
    AMD64 = "amd64"
    #: ARM.
    ARM = "arm"
    #: ARM64.
    ARM64 = "arm64"
    #: MIPS.
    MIPS = "mips"
    #: MIPSLE.
    MIPS_LE = "mipsle"
    #: MIPS64.
    MIPS64 = "mips64"
    #: MIPS64LE.
    MIPS64_LE = "mips64le"
    #: PPC64.
    PPC64 = "ppc64"
    #: PPC64LE.
    PPC64_LE = "ppc64le"
    #: RISCv64.
    RISC_V64 = "riscv64"
    #: s390x.
    S390_X = "s390x"
    #: Wasm.
    WASM = "wasm"

class ArtifactManifestOrder(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Sort options for ordering manifests in a collection.
    """

    #: Do not provide an orderby value in the request.
    NONE = "none"
    #: Order manifests by LastUpdatedOn field, from most recently updated to least recently updated.
    LAST_UPDATED_ON_DESCENDING = "timedesc"
    #: Order manifest by LastUpdatedOn field, from least recently updated to most recently updated.
    LAST_UPDATED_ON_ASCENDING = "timeasc"

class ArtifactOperatingSystem(str, Enum, metaclass=CaseInsensitiveEnumMeta):

    AIX = "aix"
    ANDROID = "android"
    DARWIN = "darwin"
    DRAGONFLY = "dragonfly"
    FREE_BSD = "freebsd"
    ILLUMOS = "illumos"
    I_OS = "ios"
    JS = "js"
    LINUX = "linux"
    NET_BSD = "netbsd"
    OPEN_BSD = "openbsd"
    PLAN9 = "plan9"
    SOLARIS = "solaris"
    WINDOWS = "windows"

class ArtifactTagOrder(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Sort options for ordering tags in a collection.
    """

    #: Do not provide an orderby value in the request.
    NONE = "none"
    #: Order tags by LastUpdatedOn field, from most recently updated to least recently updated.
    LAST_UPDATED_ON_DESCENDING = "timedesc"
    #: Order tags by LastUpdatedOn field, from least recently updated to most recently updated.
    LAST_UPDATED_ON_ASCENDING = "timeasc"

class PostContentSchemaGrantType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Can take a value of access_token_refresh_token, or access_token, or refresh_token
    """

    ACCESS_TOKEN_REFRESH_TOKEN = "access_token_refresh_token"
    ACCESS_TOKEN = "access_token"
    REFRESH_TOKEN = "refresh_token"

class TokenGrantType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Grant type is expected to be refresh_token
    """

    REFRESH_TOKEN = "refresh_token"
    PASSWORD = "password"
