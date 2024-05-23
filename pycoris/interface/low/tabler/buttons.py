from typing import Optional

from pycoris.interface.low.base import ElementHTML, ClassHTML, BaseHTML
from pycoris.interface.low.html import AnchorHTML, InputHTML, ButtonHTML as ButtonHTML
from pycoris.interface.low.tabler.colors import Color


class _Button(BaseHTML):
    disabled: bool = False

    color: Optional[Color] = None
    ghost: bool = False
    outline: bool = False

    square: bool = False
    pill: bool = False

    large: bool = False
    small: bool = False

    icon: bool = False
    loading: bool = False


class Button(_Button, ButtonHTML):
    tag: str = 'button'

    def normalize(self) -> None:
        self.add_class(ButtonClass(
            disabled=self.disabled,
            color=self.color,
            ghost=self.ghost,
            outline=self.outline,
            square=self.square,
            pill=self.pill,
            large=self.large,
            small=self.small,
            icon=self.icon,
            loading=self.loading
        ))


class InputButton(InputHTML, Button):
    pass


class ButtonLink(AnchorHTML, Button):

    def normalize(self) -> None:
        super().normalize()
        self.extra['role'] = 'button'


class ButtonClass(_Button, ClassHTML):
    def normalize(self) -> None:
        self.name = 'btn'

        if self.disabled:
            self.name += ' disabled'
        if self.square:
            self.name += ' btn-square'
        if self.pill:
            self.name += ' btn-pill'
        if self.large:
            self.name += ' btn-lg'
        if self.small:
            self.name += ' btn-sm'
        if self.icon:
            self.name += ' btn-icon'
        if self.loading:
            self.name += ' btn-loading'

        if self.color:
            if self.ghost:
                self.name += f' btn-ghost-{self.color.name}'
            elif self.outline:
                self.name += f' btn-outline-{self.color.name}'
            else:
                self.name += f' btn-{self.color.name}'


class ButtonsList(ElementHTML):
    def normalize(self) -> None:
        self.add_class('btn-list')
