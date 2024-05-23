from pycoris.interface.low.base import ElementHTML, TagHTML, ClassHTML

from pydantic import Field


class Header(ElementHTML):
    """
    Use HTML headings to organize content on your website and make the structure clear and user-friendly.

    Source: https://tabler.io/docs/base/typography#headings
    """
    level: int = Field(default=1, ge=1, le=6)

    def normalize(self) -> None:
        self.tag = f'h{self.level}'


class Paragraph(ElementHTML):
    """
    Organize longer pieces of text into paragraphs using the p tag.

    Source: https://tabler.io/docs/base/typography#paragraphs
    """

    def normalize(self) -> None:
        self.tag = 'p'


class Semantic(ElementHTML):
    """
    Use a variety of semantic text elements, depending on how you want to display particular fragments of content.

    Source: https://tabler.io/docs/base/typography#semantic-text-elements
    """

    i18n: bool = False
    i18n_tag: TagHTML = 'abbr'

    bold: bool = False
    bold_tag: TagHTML = 'strong'

    citation: bool = False
    citation_tag: TagHTML = 'cite'

    code: bool = False
    code_tag: TagHTML = 'code'

    deleted: bool = False
    deleted_tag: TagHTML = 'del'

    emphasis: bool = False
    emphasis_tag: TagHTML = 'em'

    italic: bool = False
    italic_tag: TagHTML = 'i'

    inserted: bool = False
    inserted_tag: TagHTML = 'ins'

    kbd: bool = False
    kbd_tag: TagHTML = 'kbd'

    mark: bool = False
    mark_tag: TagHTML = 'mark'

    strikethrough: bool = False
    strikethrough_tag: TagHTML = 's'

    sample: bool = False
    sample_tag: TagHTML = 'samp'

    sub: bool = False
    sub_tag: TagHTML = 'sub'

    sup: bool = False
    sup_tag: TagHTML = 'sup'

    time: bool = False
    time_tag: TagHTML = 'time'

    underline: bool = False
    underline_tag: TagHTML = 'u'

    var: bool = False
    var_tag: TagHTML = 'var'

    def normalize(self) -> None:
        tags = self.model_dump()
        keys = [k.replace('_tag', '') for k, v in tags.items() if k.endswith('_tag')]
        for key in keys:
            if key in tags and tags[key]:
                self.tag = tags[f'{key}_tag']

                if key == 'i18n':
                    self.extra['title'] = 'Internationalization'

                break


class TextTransform(ClassHTML):
    """
    Transform the content of components with text capitalization classes.

    Source: https://tabler.io/docs/base/typography#text-transform
    """
    lowercase: bool = False
    uppercase: bool = False
    capitalize: bool = False

    def normalize(self) -> None:
        if self.lowercase:
            self.name = 'text-lowercase'
        elif self.uppercase:
            self.name = 'text-uppercase'
        elif self.capitalize:
            self.name = 'text-capitalize'


class LetterSpacing(ClassHTML):
    """
    Control the tracking (letter spacing) of an element and make it tight, wide or normal.

    Source: https://tabler.io/docs/base/typography#letter-spacing
    """
    tight: bool = False
    normal: bool = False
    wide: bool = False

    def normalize(self) -> None:
        if self.tight:
            self.name = 'tracking-tight'
        elif self.normal:
            self.name = 'tracking-normal'
        elif self.wide:
            self.name = 'tracking-wide'


class LineHeight(ClassHTML):
    """
    Control the leading (line height) of an element.

    Source: https://tabler.io/docs/base/typography#line-height
    """
    one: bool = False
    sm: bool = False
    base: bool = False
    lg: bool = False

    def normalize(self) -> None:
        if self.one:
            self.name = 'lh-1'
        elif self.sm:
            self.name = 'lh-sm'
        elif self.base:
            self.name = 'lh-base'
        elif self.lg:
            self.name = 'lh-lg'


class Antialiasing(ClassHTML):
    """
    Control the font smoothing of an element.

    Source: https://tabler.io/docs/base/typography#antialiasing
    """
    antialiased: bool = False
    subpixel: bool = False

    def normalize(self) -> None:
        if self.antialiased:
            self.name = 'antialiased'
        if self.subpixel:
            self.name = 'subpixel-antialiased'


class Markdown(ClassHTML):
    """
    If you can’t use the CSS classes you want or if you just want to use HTML tags,
    use the .markdown class in a container. It can handle almost any HTML tag.

    Source: https://tabler.io/docs/base/typography#markdown-elements
    """
    markdown: bool = True

    def normalize(self) -> None:
        if self.markdown:
            self.name = 'markdown'
