# --------------------------
# Configuration
# --------------------------

# Output directory for generated files
OUT_DIR = out

# Name of the main LaTeX file (without .tex extension)
DOCUMENT_NAME = example

# LaTeX compiler (pdflatex, xelatex, lualatex)
LATEX = pdflatex

# Bibliography processor (biber for biblatex, bibtex for traditional BibTeX)
BIBER = biber

# Cleanup command
RM = rm -rf

# --------------------------
# Targets
# --------------------------

# Default target: compile the document
all: $(OUT_DIR)/$(DOCUMENT_NAME).pdf

# Rule to compile the PDF
$(OUT_DIR)/$(DOCUMENT_NAME).pdf: $(DOCUMENT_NAME).tex | $(OUT_DIR)
	# First pass: generate auxiliary files
	$(LATEX) -output-directory=$(OUT_DIR) $<
	# Run biber to process bibliography (if using biblatex)
	$(BIBER) $(OUT_DIR)/$(DOCUMENT_NAME)
	# Second pass: resolve references
	$(LATEX) -output-directory=$(OUT_DIR) $<
	# Third pass: ensure all references are resolved
	$(LATEX) -output-directory=$(OUT_DIR) $<

# Ensure the output directory exists
$(OUT_DIR):
	mkdir -p $@

# Clean up auxiliary files (keep the PDF)
clean:
	$(RM) $(OUT_DIR)/*.aux $(OUT_DIR)/*.log $(OUT_DIR)/*.out \
	      $(OUT_DIR)/*.toc $(OUT_DIR)/*.bbl $(OUT_DIR)/*.blg \
	      $(OUT_DIR)/*.lof $(OUT_DIR)/*.lot $(OUT_DIR)/*.thm \
	      $(OUT_DIR)/*.idx $(OUT_DIR)/*.ilg $(OUT_DIR)/*.ind \
	      $(OUT_DIR)/*.bcf $(OUT_DIR)/*.run.xml $(OUT_DIR)/*.gz

# Clean up all generated files (including PDF)
distclean: clean
	$(RM) $(OUT_DIR)/$(DOCUMENT_NAME).pdf

# Help message
help:
	@echo "Usage: make [target]"
	@echo ""
	@echo "Targets:"
	@echo "  all        Compile the LaTeX document (default)"
	@echo "  clean      Remove auxiliary files (keep PDF)"
	@echo "  distclean  Remove all generated files (including PDF)"
	@echo "  help       Display this help message"

# Declare phony targets
.PHONY: all clean distclean help
