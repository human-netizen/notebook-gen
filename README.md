
# Notebook Generator

This project helps you generate a LaTeX-based PDF notebook. Follow the steps below to install the required dependencies and create your customized notebook.

---

## Prerequisites

Ensure your system has Python3 installed. Then, proceed with the following steps:

### Installation Instructions

1. Install `latexmk`:
   ```bash
   sudo apt-get install latexmk
   ```
2. Install LaTeX packages:
   ```bash
   sudo apt-get install texlive-latex-base texlive-latex-extra
   ```
3. Update the TeX file database:
   ```bash
   sudo texhash
   ```
4. Install the `pygments` package for Python:
   ```bash
   sudo apt-get install python3-pygments
   ```

---

## Customization

- To change the **team name** and **author name**, edit the `notebook.tex` file.
- Modify any additional content or structure in `notebook.tex` as needed.

---

## Usage

1. After customizing `notebook.tex`, generate the PDF by running:
   ```bash
   python3 generate.py
   ```
2. This will create a file named `notebook.pdf`.
3. If the generated notebook does not look as desired, make further edits in `notebook.tex` and re-run:
   ```bash
   python3 generate.py
   ```

---

## Output

The generated file, `notebook.pdf`, will be created in the project directory. Open it to review your notebook!  

---

Happy coding! 🎉
