from typing import Optional

from pycoris.interface.low.base import ClassHTML, ElementHTML
from pycoris.interface.low.tabler.colors import Color


class Badge(ElementHTML):
    tag: str = 'span'

    bg_color: Optional[Color] = None
    text_color: Optional[Color] = None

    secondary: bool = False
    outline: bool = False
    pill: bool = False

    def normalize(self) -> None:
        self.add_class('badge')
        if self.bg_color:
            self.add_class(self.bg_color.bg)
        if self.text_color:
            self.add_class(self.text_color.text)
        if self.secondary:
            self.add_class('bg-secondary')
        if self.outline:
            self.add_class('badge-outline')
        if self.pill:
            self.add_class('badge-pill')
