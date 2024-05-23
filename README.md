![Logo](https://github.com/biqred/pycoris/raw/main/assets/logo2.svg)

**Pycoris** is a powerful framework for creating admin panels using only Python code with [Tabler UI](https://tabler.io/) and [FastAPI](https://fastapi.tiangolo.com/). Pycoris allows you to create web interfaces with just a few lines of code or fully customize it down to the smallest details.
---

> [!CAUTION]
> The project is under development and does not have a working version yet. If you want to help with the development, please contact me on [Telegram](https://t.me/biqred).

## Features

### Supported ORMs
- [x] TortoiseORM - *under development*
- [x] Custom implementation - *under development*
- [ ] SQLAlchemy - *coming soon*
- [ ] Pony ORM - *coming soon*
- [ ] Django ORM - *в будущем, по возможности*
- [ ] SQLObject - *coming soon*
- [ ] peewee - *coming soon*
- [ ] other - *other popular Python ORMs*

## Installation
The project is not yet published on PyPI.
```bash
# Via github
pip install git+https://github.com/BiqRed/pycoris
```

---

## Development Plan
### :fire: Dev Version (0.1.0.dev)
1. **Implementation of the low-level interface for interacting with Tabler.**
2. **Creation of ready-made HTML templates.**
3. **Implementation of the high-level interface for interacting with Pycoris** (layouts, lists, edit_pages, fields, forms, etc.).
4. **Creating a template for connecting ORM systems.**
5. **Implementation of TortoiseORM interaction with the database using the template from step 4.**
6. **Development of code for the customization systems** (steps 1 and 3) **to work with the database **(step 4)**.**
7. **Creation of the main Pycoris class for creating and configuring the admin panel.**
8. **Writing minimal documentation for the framework.**
9. **Testing the project and fixing issues.**
### :gear: Release Version (0.1)
1. **Writing tests.**
2. **Improving base classes for more comfortable interaction with interfaces.**
3. **Lowering the minimum Python version to 3.8 and dependencies.**
4. **Implementing all Tabler features in Python code.**
5. **Adding new types of authorization, 2FA, password recovery, etc.**
6. **Adding new ready-made admin panel templates.**
7. **Writing full documentation.**
8. **Launching a demo version of the admin panel.**
9. **...**
### :shield: Stable Version (1.0)
1. **Separating the Tabler interaction interface into a separate Python package.**
2. **...**

## Project Support

If you have any ideas, the ability to support development, or a desire to develop the project with me, please write to me [here](https://t.me/biqred). Thank you!
