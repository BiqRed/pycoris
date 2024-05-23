from typing import Optional, Literal, List
from pycoris.interface.low.base import ElementHTML


class AnchorHTML(ElementHTML):
    tag: str = 'a'

    href: str = '#'
    target: Optional[Literal['_blank', '_self', '_parent', '_top']] = None
    rel: Optional[str] = None
    download: Optional[str] = None
    title: Optional[str] = None

    @property
    def formatted(self):
        self.extra['href'] = self.href
        if self.target:
            self.extra['target'] = self.target
        if self.rel:
            self.extra['rel'] = self.rel
        if self.download:
            self.extra['download'] = self.download
        if self.title:
            self.extra['title'] = self.title
        return super().formatted


class ImageHTML(ElementHTML):
    tag: str = 'img'

    src: str = ''
    alt: str = ''
    width: Optional[int] = None
    height: Optional[int] = None
    title: Optional[str] = None
    loading: Optional[Literal['lazy', 'eager']] = None

    @property
    def formatted(self):
        self.extra['src'] = self.src
        self.extra['alt'] = self.alt
        if self.width:
            self.extra['width'] = str(self.width)
        if self.height:
            self.extra['height'] = str(self.height)
        if self.title:
            self.extra['title'] = self.title
        if self.loading:
            self.extra['loading'] = self.loading
        return super().formatted


class ListItemHTML(ElementHTML):
    tag: str = 'li'

    value: Optional[int] = None

    @property
    def formatted(self):
        if self.value:
            self.extra['value'] = str(self.value)
        return super().formatted


class UnorderedListHTML(ElementHTML):
    tag: str = 'ul'

    type: Optional[Literal['disc', 'circle', 'square']] = None

    @property
    def formatted(self):
        if self.type:
            self.extra['type'] = self.type
        return super().formatted


class OrderedListHTML(ElementHTML):
    tag: str = 'ol'

    type: Optional[Literal['1', 'A', 'a', 'I', 'i']] = None
    start: Optional[int] = None
    reversed: bool = False

    @property
    def formatted(self):
        if self.type:
            self.extra['type'] = self.type
        if self.start:
            self.extra['start'] = str(self.start)
        if self.reversed:
            self.extra['reversed'] = None
        return super().formatted


class TableHTML(ElementHTML):
    tag: str = 'table'

    border: Optional[int] = None
    cellpadding: Optional[int] = None
    cellspacing: Optional[int] = None

    @property
    def formatted(self):
        if self.border:
            self.extra['border'] = str(self.border)
        if self.cellpadding:
            self.extra['cellpadding'] = str(self.cellpadding)
        if self.cellspacing:
            self.extra['cellspacing'] = str(self.cellspacing)
        return super().formatted


class TableRowHTML(ElementHTML):
    tag: str = 'tr'


class TableHeaderHTML(ElementHTML):
    tag: str = 'th'

    colspan: Optional[int] = None
    rowspan: Optional[int] = None
    scope: Optional[Literal['col', 'row', 'colgroup', 'rowgroup']] = None

    @property
    def formatted(self):
        if self.colspan:
            self.extra['colspan'] = str(self.colspan)
        if self.rowspan:
            self.extra['rowspan'] = str(self.rowspan)
        if self.scope:
            self.extra['scope'] = self.scope
        return super().formatted


class TableDataHTML(ElementHTML):
    tag: str = 'td'

    colspan: Optional[int] = None
    rowspan: Optional[int] = None

    @property
    def formatted(self):
        if self.colspan:
            self.extra['colspan'] = str(self.colspan)
        if self.rowspan:
            self.extra['rowspan'] = str(self.rowspan)
        return super().formatted


class FormHTML(ElementHTML):
    tag: str = 'form'

    action: Optional[str] = None
    method: Optional[Literal['GET', 'POST']] = 'GET'
    enctype: Optional[Literal['application/x-www-form-urlencoded', 'multipart/form-data', 'text/plain']] = None

    @property
    def formatted(self):
        if self.action:
            self.extra['action'] = self.action
        if self.method:
            self.extra['method'] = self.method
        if self.enctype:
            self.extra['enctype'] = self.enctype
        return super().formatted


class _Input(ElementHTML):
    name: Optional[str] = None
    placeholder: Optional[str] = None
    required: bool = False
    readonly: bool = False
    disabled: bool = False

    @property
    def formatted(self):
        if self.name:
            self.extra['name'] = self.name
        if self.placeholder:
            self.extra['placeholder'] = self.placeholder
        if self.required:
            self.extra['required'] = None
        if self.readonly:
            self.extra['readonly'] = None
        if self.disabled:
            self.extra['disabled'] = None
        return super().formatted


class InputHTML(_Input):
    tag: str = 'input'

    type: Optional[str] = 'text'
    value: Optional[str] = None

    @property
    def formatted(self):
        if self.type:
            self.extra['type'] = self.type
        if self.value:
            self.extra['value'] = self.value
        return super().formatted


class ButtonHTML(ElementHTML):
    tag: str = 'button'

    type: Optional[Literal['button', 'submit', 'reset']] = 'button'
    name: Optional[str] = None
    value: Optional[str] = None

    @property
    def formatted(self):
        if self.type:
            self.extra['type'] = self.type
        if self.name:
            self.extra['name'] = self.name
        if self.value:
            self.extra['value'] = self.value
        return super().formatted


class TextareaHTML(_Input):
    tag: str = 'textarea'

    rows: Optional[int] = None
    cols: Optional[int] = None

    @property
    def formatted(self):
        if self.rows:
            self.extra['rows'] = str(self.rows)
        if self.cols:
            self.extra['cols'] = str(self.cols)
        return super().formatted


class SelectHTML(ElementHTML):
    tag: str = 'select'

    name: Optional[str] = None
    multiple: bool = False
    required: bool = False
    disabled: bool = False

    @property
    def formatted(self):
        if self.name:
            self.extra['name'] = self.name
        if self.multiple:
            self.extra['multiple'] = None
        if self.required:
            self.extra['required'] = None
        if self.disabled:
            self.extra['disabled'] = None
        return super().formatted


class OptionHTML(ElementHTML):
    tag: str = 'option'

    value: Optional[str] = None
    selected: bool = False
    disabled: bool = False

    @property
    def formatted(self):
        if self.value:
            self.extra['value'] = self.value
        if self.selected:
            self.extra['selected'] = None
        if self.disabled:
            self.extra['disabled'] = None
        return super().formatted


class LinkHTML(ElementHTML):
    tag: str = 'link'

    rel: str = ''
    href: str = ''
    type: Optional[str] = None

    @property
    def formatted(self):
        self.extra['rel'] = self.rel
        self.extra['href'] = self.href
        if self.type:
            self.extra['type'] = self.type
        return super().formatted


class MetaHTML(ElementHTML):
    tag: str = 'meta'

    name: Optional[str] = None
    content: Optional[str] = None
    charset: Optional[str] = None

    @property
    def formatted(self):
        if self.name:
            self.extra['name'] = self.name
        if self.content:
            self.extra['content'] = self.content
        if self.charset:
            self.extra['charset'] = self.charset
        return super().formatted


class ScriptHTML(ElementHTML):
    tag: str = 'script'

    src: Optional[str] = None
    type: Optional[str] = 'text/javascript'
    async_: bool = False
    defer: bool = False

    @property
    def formatted(self):
        if self.src:
            self.extra['src'] = self.src
        if self.type:
            self.extra['type'] = self.type
        if self.async_:
            self.extra['async'] = None
        if self.defer:
            self.extra['defer'] = None
        return super().formatted


class SpanHTML(ElementHTML):
    tag: str = 'span'
