from copy import copy
from typing import List, Union, Optional

from interface.low.base import ElementHTML, ClassHTML
from interface.low.html import AnchorHTML, SpanHTML

from fastapi_babel.core import lazy_gettext as _


class DropdownToggle(AnchorHTML):
    label: str = _('Open dropdown')
    button: Optional[str] = 'btn'

    def normalize(self) -> None:
        self.add_class('dropdown-toggle')
        self.extra['data-bs-toggle'] = 'dropdown'
        self.update_empty_inner(self.label)
        if self.button:
            self.add_class(self.button)


class DropdownItem(AnchorHTML):
    label: str = _('Dropdown item')
    active: bool = False
    disabled: bool = False

    def normalize(self) -> None:
        self.classes.append(ClassHTML(name='dropdown-item'))
        if self.active:
            self.classes.append(ClassHTML(name='active'))
        if self.disabled:
            self.classes.append(ClassHTML(name='disabled'))

        self.update_empty_inner(self.label)


class DropdownDivider(ElementHTML):
    def normalize(self) -> None:
        self.classes.append(ClassHTML(name='dropdown-divider'))


class DropdownHeader(SpanHTML):
    label: str = _('Dropdown header')

    def normalize(self) -> None:
        self.classes.append(ClassHTML(name='dropdown-header'))
        self.update_empty_inner(self.label)


class DropdownMenu(ElementHTML):
    items: List[Union['DropdownItem', 'DropdownDivider', 'DropdownHeader', 'Dropdown']] = []
    arrow: bool = False

    def normalize(self) -> None:
        self.add_class('dropdown-menu')
        if self.arrow:
            self.add_class('dropdown-menu-arrow')

        for n, item in enumerate(self.items):
            if isinstance(item, Dropdown):
                new_item = copy(item)
                new_item.add_class('dropdown-item')

                if not new_item.drop_end and not new_item.drop_start:
                    new_item.drop_end = True

                self.items.pop(n)
                self.items.insert(n, new_item)

        self.update_empty_inner(self.items)


class Dropdown(ElementHTML):
    toggle: DropdownToggle = DropdownToggle()
    menu: Optional[DropdownMenu] = None

    centered: bool = False
    drop_up: bool = False
    drop_end: bool = False
    drop_start: bool = False

    def normalize(self) -> None:
        if not self.menu:
            self.menu = DropdownMenu()

        if self.drop_up and self.centered:
            self.add_class('dropup').add_class('dropup-center')
        elif self.drop_up:
            self.add_class('dropup')
        elif self.centered:
            self.add_class('dropdown-center')
        elif self.drop_end:
            self.add_class('dropdown-end')
        elif self.drop_start:
            self.add_class('dropdown-start')
        else:
            self.add_class('dropdown')

        self.update_empty_inner([self.toggle, self.menu])
