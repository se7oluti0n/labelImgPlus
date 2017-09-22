
all: resources.py

%.py: %.qrc
	pyrcc5 -o $@ $<

