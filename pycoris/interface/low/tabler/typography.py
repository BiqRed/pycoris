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
    t_i18n_tag: TagHTML = 'abbr'

    bold: bool = False
    t_bold_tag: TagHTML = 'strong'

    citation: bool = False
    t_citation_tag: TagHTML = 'cite'

    code: bool = False
    t_code_tag: TagHTML = 'code'

    deleted: bool = False
    t_deleted_tag: TagHTML = 'del'

    emphasis: bool = False
    t_emphasis_tag: TagHTML = 'em'

    italic: bool = False
    t_italic_tag: TagHTML = 'i'

    inserted: bool = False
    t_inserted_tag: TagHTML = 'ins'

    kbd: bool = False
    t_kbd_tag: TagHTML = 'kbd'

    mark: bool = False
    t_mark_tag: TagHTML = 'mark'

    strikethrough: bool = False
    t_strikethrough_tag: TagHTML = 's'

    sample: bool = False
    t_sample_tag: TagHTML = 'samp'

    sub: bool = False
    t_sub_tag: TagHTML = 'sub'

    sup: bool = False
    t_sup_tag: TagHTML = 'sup'

    time: bool = False
    t_time_tag: TagHTML = 'time'

    underline: bool = False
    t_underline_tag: TagHTML = 'u'

    var: bool = False
    t_var_tag: TagHTML = 'var'

    def normalize(self) -> None:
        tags = self.model_dump()
        keys = [k.replace('_tag', '')[2:] for k, v in tags.items() if k.endswith('_tag') and k.startswith('t_')]
        for key in keys:
            if key in tags and tags[key]:
                self.tag = tags[f't_{key}_tag']

                if key == 'i18n':
                    self.extra_attributes.update({'title': 'Internationalization'})

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
