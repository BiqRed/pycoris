from typing import Optional

from pycoris.interface.low.base import ElementHTML
from pycoris.interface.low.tabler.colors import Color


class Divider(ElementHTML):
    label: Optional[str] = None
    left: bool = False
    right: bool = False
    text_color: Optional[Color] = None

    def normalize(self) -> None:
        if self.label:
            self.update_empty_inner(self.label)

        if self.inner and self.left:
            self.add_class('hr-text-left')
        elif self.inner and self.right:
            self.add_class('hr-text-right')
        elif self.inner:
            self.add_class('hr-text')
        else:
            self.tag = 'hr'
            self.is_single = True

        if self.inner and self.text_color:
            self.add_class(self.text_color.text)
