from typing import Optional

from pycoris.interface.low.base import ClassHTML, ElementHTML
from pycoris.interface.low.tabler.colors import Color


class Badge(ClassHTML):
    bg_color: Optional[Color] = None
    text_color: Optional[Color] = None

    secondary: bool = False
    outline: bool = False
    pill: bool = False

    def normalize(self) -> None:
        self.name = 'badge'
        if self.bg_color:
            self.name += f' bg-{self.bg_color.name}'
        if self.text_color:
            self.name += f' text-{self.text_color.name}'
        if self.secondary:
            self.name += ' bg-secondary'
        if self.outline:
            self.name += ' badge-outline'
        if self.pill:
            self.name += ' badge-pill'


class BadgeElement(ElementHTML):
    tag: str = 'span'

    bg_color: Optional[Color] = None
    text_color: Optional[Color] = None

    secondary: bool = False
    outline: bool = False
    pill: bool = False

    def normalize(self) -> None:
        self.classes.append(ClassHTML(name='badge'))
        if self.bg_color:
            self.classes.append(ClassHTML(name=f'bg-{self.bg_color.name}'))
        if self.text_color:
            self.classes.append(ClassHTML(name=f'text-{self.text_color.name}'))
        if self.secondary:
            self.classes.append(ClassHTML(name='bg-secondary'))
        if self.outline:
            self.classes.append(ClassHTML(name='badge-outline'))
        if self.pill:
            self.classes.append(ClassHTML(name='badge-pill'))
