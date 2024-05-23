from typing import Union

from pycoris.interface.high.base import Base
from pycoris.interface.low.tabler.dropdowns import (Dropdown, DropdownDivider, DropdownHeader,
                                                    DropdownItem, DropdownMenu, DropdownToggle)


class MenuButton(Base):
    def render(self) -> str:
        raise self.validated


class Menu(Base):

    def render(self) -> str:
        raise self.validated

