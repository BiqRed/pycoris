from typing import Union, List, Annotated, Dict, Optional
from typing_extensions import Self

from pydantic import BaseModel, Field


TagHTML = Annotated[str, 'Must be ended with `_tag`. Example: `bold_tag = "strong"`']


class BaseHTML(BaseModel):
    """Base class for low level base classes."""
    @classmethod
    def to_instance(cls, data: str) -> Self:
        """
        Convert various values to an instance of a base class

        This needs to be overridden in the base classes
        :param data: value to convert
        :return: an instance of a base class
        :rtype: Self
        """
        raise NotImplementedError

    @property
    def formatted(self) -> str:
        """
        Converting an object to HTML code

        This needs to be overridden in the base classes
        :return HTML code
        :rtype: str
        """
        raise NotImplementedError

    @property
    def validated(self) -> str:
        """
        Invoking class normalization, validating it, and returning formatted HTML code
        :rtype: str
        """
        self.normalize()
        self.__class__.model_validate(self)
        return self.formatted

    def normalize(self) -> None:
        """
        Converting the attributes of the derived class to the required attributes of the base class

        This needs to be overridden in the derived classes
        :return: None
        """
        pass

    def __str__(self) -> str:
        return self.validated

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.validated})'


class ClassHTML(BaseHTML):
    name: str = Field(alias='name', default='')

    @classmethod
    def to_instance(cls, data: str) -> Self:
        return cls(name=str(data))

    @property
    def formatted(self) -> str:
        return self.name


class StyleCSS(BaseHTML):
    prop: str
    value: str

    @classmethod
    def to_instance(cls, data: str) -> Self:
        prop, value = data.strip().split(':')
        value = value.strip().replace(';', '')
        return cls(prop=prop, value=value)

    @property
    def formatted(self) -> str:
        return f'{self.prop}:{self.value};'


class ElementHTML(BaseHTML):
    tag: str = 'div'
    is_single: bool = False
    inner: Union[str, 'ElementHTML', List[Union['ElementHTML', str]]] = ''
    classes: List[ClassHTML] = []
    styles: List[StyleCSS] = []
    extra_attributes: Dict[str, Optional[str]] = {}

    def set_classes(self, value: Union[ClassHTML, List[Union[ClassHTML, str]], str, None]) -> Self:
        if not value:
            self.classes = []
        elif isinstance(self.classes, str):
            self.classes = [ClassHTML.to_instance(cls) for cls in str(value).strip().split() if cls]
        elif isinstance(self.classes, ClassHTML):
            self.classes = [value]
        elif isinstance(self.classes, list):
            self.classes = []
            for cls in self.classes:
                if isinstance(cls, str):
                    self.classes.extend(ClassHTML.to_instance(c) for c in str(cls).strip().split() if c)
                elif isinstance(cls, ClassHTML):
                    self.classes.append(cls)
        return self

    def set_styles(self, value: Union[StyleCSS, List[Union[StyleCSS]], str, None]) -> Self:
        if not value:
            self.styles = []
        elif isinstance(value, str):
            self.styles = [StyleCSS.to_instance(s) for s in value.strip().split(';') if s.strip()]
        elif isinstance(value, StyleCSS):
            self.styles = [value]
        elif isinstance(value, list):
            self.styles = []
            for s in value:
                if isinstance(s, str):
                    self.styles.extend(StyleCSS.to_instance(s) for s in s.strip().split(';') if s.strip())
                elif isinstance(s, StyleCSS):
                    self.styles.append(s)
        return self

    @classmethod
    def to_instance(cls, data: str) -> Self:
        yield Exception('The method (to_instance) is not implemented yet')

    def _process_inner(self) -> str:
        if not self.inner or self.is_single:
            return ''
        if isinstance(self.inner, str):
            return self.inner
        if isinstance(self.inner, ElementHTML):
            return self.inner.validated
        if isinstance(self.inner, list):
            inner = ''
            for i in self.inner:
                if isinstance(i, str):
                    inner += f'\n{i}'
                else:
                    inner += f'\n{i.validated}'
            return inner

    def _process_classes(self) -> str:
        classes = ' '.join([cls.validated for cls in self.classes])
        return f' class="{classes}"' if classes else ''

    def _process_styles(self) -> str:
        styles = ';'.join([s.validated for s in self.styles])
        return f' style="{styles}"' if styles else ''

    def _process_attributes(self) -> str:
        attributes = ''
        for attr, value in self.extra_attributes.items():
            if value:
                attributes += f' {attr}="{value}"'
            else:
                attributes += f' {attr}'
        return attributes

    @property
    def formatted(self) -> str:
        inner = self._process_inner()
        classes = self._process_classes()
        styles = self._process_styles()
        attributes = self._process_attributes()
        return f'<{self.tag}{classes}{styles}{attributes}>{inner}' + ('' if self.is_single else f'</{self.tag}>')
