from typing import Union

from enum import Enum


class Color(Enum):
    """
    Base Enum Model with all tabler colors.

    Source: https://tabler.io/docs/base/colors
    """

    # Bootstrap colors
    PRIMARY = ('primary', '#007bff')
    SECONDARY = ('secondary', '#6c757d')
    SUCCESS = ('success', '#28a745')
    INFO = ('info', '#17a2b8')
    WARNING = ('warning', '#ffc107')
    DANGER = ('danger', '#dc3545')
    LIGHT = ('light', '#f8f9fa')
    DARK = ('dark', '#343a40')

    # Base colors
    BLUE = ('blue', '#0054a6')
    AZURE = ('azure', '#4299e1')
    INDIGO = ('indigo', '#4263eb')
    PURPLE = ('purple', '#ae3ec9')
    PINK = ('pink', '#d6336c')
    RED = ('red', '#d63939')
    ORANGE = ('orange', '#f76707')
    YELLOW = ('yellow', '#f59f00')
    LIME = ('lime', '#74b816')
    GREEN = ('green', '#2fb344')
    TEAL = ('teal', '#0ca678')
    CYAN = ('cyan', '#17a2b8')

    # Light colors
    BLUE_LT = ('blue-lt', '#e9f0f9')
    AZURE_LT = ('azure-lt', '#ecf5fc')
    INDIGO_LT = ('indigo-lt', '#eceffd')
    PURPLE_LT = ('purple-lt', '#f7ecfa')
    PINK_LT = ('pink-lt', '#fbebf0')
    RED_LT = ('red-lt', '#fbebeb')
    ORANGE_LT = ('orange-lt', '#fef0e6')
    YELLOW_LT = ('yellow-lt', '#fef5e6')
    LIME_LT = ('lime-lt', '#f1f8e8')
    GREEN_LT = ('green-lt', '#eaf7ec')
    TEAL_LT = ('teal-lt', '#e7f6f2')
    CYAN_LT = ('cyan-lt', '#e8f6f8')

    # Gray palette
    GRAY_50 = ('gray-50', '#f8fafc')
    GRAY_100 = ('gray-100', '#f1f5f9')
    GRAY_200 = ('gray-200', '#e2e8f0')
    GRAY_300 = ('gray-300', '#c8d3e1')
    GRAY_400 = ('gray-400', '#9ba9be')
    GRAY_500 = ('gray-500', '#6c7a91')
    GRAY_600 = ('gray-600', '#49566c')
    GRAY_700 = ('gray-700', '#313c52')
    GRAY_800 = ('gray-800', '#1d273b')
    GRAY_900 = ('gray-900', '#0f172a')

    # Social colors
    FACEBOOK = ('facebook', '#1877F2')
    TWITTER = ('twitter', '#1da1f2')
    LINKEDIN = ('linkedin', '#0a66c2')
    GOOGLE = ('google', '#dc4e41')
    YOUTUBE = ('youtube', '#ff0000')
    VIMEO = ('vimeo', '#1ab7ea')
    DRIBBBLE = ('dribbble', '#ea4c89')
    GITHUB = ('github', '#181717')
    INSTAGRAM = ('instagram', '#e4405f')
    PINTEREST = ('pinterest', '#bd081c')
    VK = ('vk', '#6383a8')
    RSS = ('rss', '#ffa500')
    FLICKR = ('flickr', '#0063dc')
    BITBUCKET = ('bitbucket', '#0052cc')
    TABLER = ('tabler', '#0054a6')

    @classmethod
    def validate(cls, color: Union[str, 'Color']) -> 'Color':
        if isinstance(color, Color):
            return color

        if color.startswith('#'):
            return cls.from_hex(color)

        color = color.upper().replace('-', '_')

        if color not in cls.__members__:
            raise ValueError('Color must be one of: ' + ', '.join([cls.name for cls in cls.__members__.values()]))
        return cls[color]

    @classmethod
    def from_hex(cls, hex_code: str) -> 'Color':
        for color in cls.__members__.values():
            if color.value[1] == hex:
                return color
        raise ValueError('Color must be one of: ' + ', '.join([cls.name for cls in cls.__members__.values()]))

    @property
    def name(self):
        return self.value[0]

    @property
    def hex(self):
        return self.value[1]

    @property
    def bg(self):
        return f'bg-{self.name}'

    @property
    def text(self):
        return f'text-{self.name}'
