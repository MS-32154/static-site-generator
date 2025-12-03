# Static Site Generator

A Python-based static site generator that converts Markdown files into a complete HTML website.

## Overview

This tool processes Markdown content and generates a static website with proper HTML structure, supporting inline formatting, code blocks, lists, quotes, headings, images, and links.

## Project Structure

```
root/
├── content/     # Markdown source files
├── docs/        # Generated HTML output
├── src/         # Python source code
├── static/      # Static assets (CSS, images, etc.)
├── build.sh     # Build script for deployment
├── main.sh      # Development server script
├── template.html # HTML template
└── test.sh      # Run test suite
```

## Features

- **Markdown to HTML conversion** with support for:
  - Headings (h1-h6)
  - Bold, italic, and code formatting
  - Links and images
  - Ordered and unordered lists
  - Blockquotes
  - Code blocks
- **Recursive directory processing** - maintains content structure in output
- **Template system** - customize the HTML wrapper
- **Static file copying** - automatically copies assets to output directory

## Usage

### Development

Run the development server:

```bash
./main.sh
```

This generates the site in `public/` and starts a local server at `http://localhost:8888`

### Building for Production

Build with custom base path:

```bash
./build.sh
```

This generates the site in `docs/` with the configured base path for GitHub Pages deployment.

### Running Tests

```bash
./test.sh
```

## Requirements

- Python 3.10+
- No external dependencies required

## How It Works

1. Markdown files in `content/` are parsed into blocks
2. Each block is converted to appropriate HTML nodes
3. Inline formatting is processed (bold, italic, links, etc.)
4. HTML is injected into the template
5. Static files are copied to the output directory
6. Final site is generated with proper relative paths

## Template Variables

The `template.html` file supports these placeholders:

- `{{ Title }}` - Extracted from the first h1 heading
- `{{ Content }}` - Generated HTML content
