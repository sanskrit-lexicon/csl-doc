# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**csl-doc** (csldoc) is the Sphinx-based documentation repository for the Cologne Digital Sanskrit Lexicon (CDSL) project. It contains the documentation source and generated build output.

Deployed at the Cologne server. The `build/` directory contains the rendered HTML output.

## Architecture

| Directory/File | Purpose |
|---|---|
| `source/` | Sphinx RST source files for the documentation |
| `build/` | Generated HTML documentation (tracked by git for deployment) |
| `Makefile` / `make.bat` | Sphinx build commands |
| `move_images.py` | Utility to move image files into the Sphinx source structure |
| `readme_dev.md` | Developer setup instructions |
| `readme_dev_ap.md` | Developer notes for the AP dictionary documentation |

## Common Commands

### Build documentation
```bash
make html          # Linux/Mac
make.bat html      # Windows
```

### Setup notes

The Sphinx build requires:
- A Python virtual environment (not tracked — set up per `readme_dev.md`)
- `virtualenv` installed locally

## Dependencies

- **Python 3** with **Sphinx** (`pip install sphinx`)
- Virtual environment setup (see `readme_dev.md`)
