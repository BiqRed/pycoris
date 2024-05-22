from enum import Enum

from typing import Optional, Union, List, Collection, Literal, Annotated


class LayoutOrientation(Enum):
    HORIZONTAL = 'horizontal'
    VERTICAL = 'vertical'


class SidebarPosition(Enum):
    LEFT = 'left'
    RIGHT = 'right'


class SiteLocale(Enum):
    EN = 'en'
    RU = 'ru'


class ORM(Enum):
    TORTOISE = 'tortoise'


class BaseSettings:
    # ====== General ======
    debug: bool = False
    project_name: str = 'Pycoris'
    root_url: str = '/admin'
    orm: Union[ORM, Literal['tortoise']] = ORM.TORTOISE

    # ====== Auth ======
    secret_key: Annotated[str, "Must be at least 8 characters long"] = ''
    allowed_hosts: Union[Literal['*'], List[str]] = '*'

    # ====== Layout ======
    layout_orientation: LayoutOrientation = LayoutOrientation.HORIZONTAL
    layout_boxed: bool = False
    layout_rtl_mode: bool = False
    layout_fluid: bool = False

    # Only for layout_orientation == LayoutOrientation.VERTICAL
    layout_sidebar_transparent: bool = False
    layout_sidebar_position: SidebarPosition = SidebarPosition.LEFT

    # Only for layout_orientation == LayoutOrientation.HORIZONTAL
    layout_navbar_condensed: bool = False
    layout_navbar_sticky: bool = False
    layout_navbar_overlap: bool = False

    # ====== Design ======
    site_title: Optional[str] = None
    theme_toggle: bool = True
    logo_url: str = '/static/images/logo.svg'
    logo_dark_url: Optional[str] = '/static/images/logo-dark.svg'
    icon_url: str = '/static/images/icon.svg'
    default_user_avatar: Optional[str] = None

    # ====== Locales ======
    language_chooser: bool = True
    locales: Collection[SiteLocale] = list(SiteLocale)
    default_locale: SiteLocale = SiteLocale.EN
    locales_dir: Optional[str] = 'pycoris/locales'

    @classmethod
    def validate(cls: 'BaseSettings') -> None:
        if len(cls.secret_key) < 8:
            raise ValueError(
                'BaseSettings.secret_key must be at least 8 characters long.'
            )


settings = BaseSettings
