from typing import Collection

from pydantic import BaseModel


class BaseMenuItem(BaseModel):
    async def on_click(self):
        pass


class Menu(BaseModel):
    items: Collection[BaseMenuItem]


class MenuItem(BaseMenuItem):
    name: str
    icon: str

    url: str = None


class MenuDropItem(BaseMenuItem):
    name: str
    icon: str
    items: Collection[MenuItem]


class MenuDivider(BaseMenuItem):
    text: str = None
    text_color: str = None
