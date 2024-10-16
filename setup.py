from setuptools import setup

APP = ['main.py']  # エントリーポイントとなるPythonスクリプトを指定します
DATA_FILES = []    # 必要なデータファイルをリスト形式で指定します（画像、設定ファイルなど）
OPTIONS = {
    'argv_emulation': True,          # コマンドライン引数のサポートを有効化
    'packages': ['PyQt6'],           # 使用するPythonパッケージ
    'includes': ['sip'],             # その他に含めたいパッケージ
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],       # py2appをビルドプロセスで使うため指定
)
