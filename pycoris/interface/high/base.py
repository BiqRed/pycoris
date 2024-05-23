from pycoris.interface.low.base import ElementHTML


class Base(ElementHTML):
    def render(self) -> str:
        raise NotImplementedError
