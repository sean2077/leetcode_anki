BUILD := `git rev-parse --short HEAD`


DOC_FILES := $(shell find . -name '*.md' -type f)
doc:
	$(foreach DOC,$(DOC_FILES),doctoc --gitlab $(DOC);)


PYCACHE_DIR := $(shell find . -name '__pycache__' -type d)
clean:
	rm -rf $(PYCACHE_DIR)