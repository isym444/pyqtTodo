import os
import sys

qrc_file_path = "/Users/iseyuki/pyqtTodo/resources.qrc"
icons_folder = "/Users/iseyuki/pyqtTodo/icons"

icons = [
    os.path.join(icons_folder, f)
    for f in os.listdir(icons_folder)
    if os.path.isfile(os.path.join(icons_folder, f))
]


file_skeleton = """
<RCC>
    <qresource prefix="/">
FILES
    </qresource>
</RCC>
""".strip()

indent = " " * 8
lines = []
for icon in icons:
    base = os.path.basename(icon)
    path = os.path.relpath(icon, start=os.path.dirname(qrc_file_path))
    line = f'{indent}<file alias="icons/{base}">{path}</file>'
    lines.append(line)

with open(qrc_file_path, "w") as file:
    file.write(file_skeleton.replace("FILES", "\n".join(lines)))