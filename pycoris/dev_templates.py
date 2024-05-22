from typing import Annotated, Callable
from typing import Annotated, Callable

from fastapi import Depends
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
# from fastapi_babel import _  # noqa
from fastapi_babel import BabelConfigs, BabelMiddleware
from fastapi_babel.core import make_gettext

from settings import settings

settings.root_url = '/'

app = FastAPI()
templates = Jinja2Templates(directory="templates")
templates.env.globals['settings'] = settings


class Language:
    def __init__(self, code: str, name: str, flag_code: str):
        self.code = code
        self.name = name
        self.flag_code = flag_code


templates.env.globals["languages"] = [
    Language('en', 'English', 'gb'),
    Language('ru', 'Русский', 'ru')
]


class User:
    def __init__(self):
        self.id = 1
        self.username = 'BiqRed'
        self.first_name = 'Nikita'
        self.last_name = 'Petrunin'
        self.avatar = None
        self.superuser = False
        self.role = 'Redactor'

    @property
    def two_letters(self):
        if self.first_name and self.last_name:
            return self.first_name[0] + self.last_name[0]
        return self.username[:2]


templates.env.globals['user'] = User()


class Notification:
    def __init__(self, title: str, desc: str, at: str,
                 user: User = None, link: str = None,
                 template: str = None, html: str = None):
        self.title = title
        self.desc = desc
        self.at = at
        self.user = user
        self.link = link
        self.template = template
        self.html = html


templates.env.globals['notifications'] = [
    Notification('Notification title', 'Notification description'*3, '2022-01-01 00:00:00', user=User()),
    Notification('Notification title', 'Notification description', '2022-01-01 00:00:00', user=User()),
]


babel_configs = BabelConfigs(
    ROOT_DIR=__file__,
    BABEL_DEFAULT_LOCALE=settings.default_locale.value,
    BABEL_TRANSLATION_DIRECTORY="locales",
)

app.add_middleware(
    BabelMiddleware,  # type: ignore
    babel_configs=babel_configs,
    jinja2_templates=templates
)
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def index(request: Request, _: Annotated[Callable[[str], str], Depends(make_gettext)]):
    print(request.headers.get("Accept-Language"))
    return templates.TemplateResponse(
        "layouts/horizontal.html",
        {
            "request": request,
        }
    )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run('dev_templates:app', host="0.0.0.0", port=8789, reload=True)
