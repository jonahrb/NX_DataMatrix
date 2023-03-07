# NX_DataMatrix
Neuplex DataMatrix Generator

## First Time Setup

- Open GitHub Desktop and clone the repository
- Open the repository in VSCode
  - Ctrl + Shift + A
- Open a new terminal
  - Terminal > New Terminal
    OR
  - Ctrl + `

Create a virtual environment

```
py -m venv .venv
```

Activate the virtual environment

```
.venv/scripts/activate
```

Install all dependencies from requirements.txt

```
pip install -r requirements.txt
```


## First time build
```
pyinstaller --add-binary ".venv/Lib/site-packages/pylibdmtx/libdmtx-64.dll;." --icon=logo.ico --add-data "logo.ico;." --windowed .\NX_DataMatrix.py
```

## Build from spec
After you generate the .spec file from the first build, if you want to make changes to it and rebuild, use this command. If you use the previous command it will overwrite your .spec file.
```
pyinstaller .\NX_DataMatrix.spec
```
