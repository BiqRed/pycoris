from typing import Optional

from pycoris.interface.low.base import ClassHTML, ElementHTML
from pycoris.interface.low.html import SpanHTML
from pycoris.interface.low.tabler.colors import Color


class SVGIconClass(ClassHTML):
    pulse: bool = False
    tada: bool = False
    rotate: bool = False

    def normalize(self) -> None:
        if self.pulse:
            self.name = 'icon-pulse'
        elif self.tada:
            self.name = 'icon-tada'
        elif self.rotate:
            self.name = 'icon-rotate'


class Icon(SpanHTML):
    svg_icon: Optional[ElementHTML] = None

    name: Optional[str] = None
    color: Optional[Color] = None

    pulse: bool = False
    tada: bool = False
    rotate: bool = False

    def normalize(self) -> None:
        if not self.svg_icon:
            self.svg_icon = ElementHTML(
                inner='ICON'  # TODO
            ).add_class(SVGIconClass(
                pulse=self.pulse,
                tada=self.tada,
                rotate=self.rotate
            ))
        if self.color:
            self.add_class(self.color.text)
