# NX_DataMatrix
Neuplex DataMatrix Generator

## First time build
`pyinstaller --add-binary ".venv/Lib/site-packages/pylibdmtx/libdmtx-64.dll;." --icon=logo.ico --add-data "logo.ico;." --windowed .\NX_DataMatrix.py`

## Build from spec
`pyinstaller .\NX_DataMatrix.spec`