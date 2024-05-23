from typing import List

from pycoris.interface.low.html import ListItemHTML, UnorderedListHTML, AnchorHTML


class NavLink(AnchorHTML):
    active: bool = False
    disabled: bool = False

    def normalize(self) -> None:
        self.add_class('nav-link')
        if self.active:
            self.add_class('active')
        if self.disabled:
            self.add_class('disabled')


class NavItem(ListItemHTML):
    def normalize(self) -> None:
        self.add_class('nav-item')


class Nav(UnorderedListHTML):
    items: List[NavItem] = []

    tabs: bool = False
    pills: bool = False
    underline: bool = False
    fill: bool = False
    justified: bool = False

    def normalize(self) -> None:
        self.add_class('nav')

        if self.tabs:
            self.add_class('nav-tabs')
        if self.pills:
            self.add_class('nav-pills')
        if self.underline:
            self.add_class('nav-underline')
        if self.fill:
            self.add_class('nav-fill')
        if self.justified:
            self.add_class('nav-justified')

        self.update_empty_inner(self.items)
