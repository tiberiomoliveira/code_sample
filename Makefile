# Register all subdirectories in the project's root directory.
SUBDIRS := $(sort $(dir $(wildcard */*/*/Makefile)))
# Register all top-level targets
TOPTARGETS := all check lint-check

# Top-level phony targets.
$(TOPTARGETS): $(SUBDIRS)

# Recurse `make` into each subdirectory
# Pass along targets specified at command-line (if any).
$(SUBDIRS):
	$(MAKE) -C $@ $(MAKECMDGOALS)

.PHONY: $(TOPTARGETS) $(SUBDIRS)
