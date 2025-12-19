#!/usr/bin/python
import os
import subprocess
import shutil
import hashlib

code_dir = "code"

def is_binary_file(filepath):
    """Check if a file is binary by looking for null bytes."""
    try:
        with open(filepath, 'rb') as f:
            chunk = f.read(8192)
            if b'\x00' in chunk:
                return True
        return False
    except Exception:
        return True

def get_sections():
    sections = []
    for (root, dirs, files) in os.walk(code_dir):
        subsections = []
        section_name = os.path.basename(root)
        sections.append((section_name, subsections))
        for file_name in sorted(files):
            subsection_name = os.path.splitext(file_name)[0]
            if subsection_name[0] == '.': # Skipping hidden files in Unix
                continue
            relative_path = os.path.join(root, file_name)
            if is_binary_file(relative_path):  # Skip binary files
                print(f"Skipping binary file: {subsection_name}")
                continue
            print(subsection_name)
            number_of_lines = len(open(relative_path, encoding='utf-8', errors='replace').readlines())
 
 # Use MD5 and truncate to 8 characters
            hash_value = hashlib.md5(open(relative_path, 'rb').read()).hexdigest()[:8]
            subsections.append((relative_path, subsection_name, number_of_lines, hash_value))
    return sections[1:]

def get_style(filename):
    ext = filename.lower().split('.')[-1]
    if ext in ['c', 'cc', 'cpp']:
        return 'c++'
    elif ext in ['java']:
        return 'java'
    elif ext in ['py']:
        return 'python'
    else:
        return 'text'

# TODO: check if this is everything we need
def texify(s):
    #s = s.replace('\'', '\\\'')
    #s = s.replace('\"', '\\\"')
    return s

def get_tex(sections):
    tex = ''
    for (section_name, subsections) in sections:
        tex += '\\section{%s}\n' % texify(section_name)
        for (relative_path, subsection_name, number_of_lines, hash_value) in subsections:
            tex += '\\subsection{\\small %s  \\scriptsize [%s lines] - %s}\n' % (texify(subsection_name), number_of_lines, hash_value)
            tex += '\\inputminted{%s}{%s}\n' % (get_style(relative_path), '"' + relative_path + '"')
    return tex

if __name__ == "__main__":
    sections = get_sections()
    tex = get_tex(sections)
    with open('contents.tex', 'w') as f:
        f.write(tex)
    latexmk_options = ["latexmk", "-pdf", "-shell-escape", "-cd", "-f", "-interaction=nonstopmode", "notebook.tex"]
    subprocess.call(latexmk_options)

