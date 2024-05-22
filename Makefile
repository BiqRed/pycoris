.PHONY: init extract update compile

locales_dir = pycoris/locales
lang ?= en

init:
	pybabel extract -F babel.cfg -o $(locales_dir)/messages.pot .
	pybabel init -i $(locales_dir)/messages.pot -d $(locales_dir) -l $(lang)

extract:
	pybabel extract -F babel.cfg -o $(locales_dir)/messages.pot .

update:
	pybabel update -i $(locales_dir)/messages.pot -d $(locales_dir)

compile:
	pybabel compile -d $(locales_dir)
