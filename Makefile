SRC_DIR = src
COMPRESS_SCRIPT = util/compress.py
PYTHON = python3

CPP_FILES := $(shell find $(SRC_DIR) -type f -name "*.cpp")
COM_CPP_FILES := $(CPP_FILES:.cpp=.cpp.com)

TEX_FILES := $(shell find $(SRC_DIR) -type f -name "*.tex")

.PHONY: all clean

all: main.pdf $(COM_CPP_FILES)

main.pdf: main.tex $(TEX_FILES) $(COM_CPP_FILES)
	latexmk -synctex=1 -interaction=nonstopmode -shell-escape -file-line-error -lualatex main.tex

%.cpp.com: %.cpp
	$(PYTHON) $(COMPRESS_SCRIPT) $< $@ --line-length 60

clean:
	find $(SRC_DIR) -type f -name "*.cpp.com" -delete