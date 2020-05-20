# pip installの解説
## 更新日
- 2019-09-26

## 資料
- https://pip.pypa.io/en/stable/reference/pip_install/

## 目的
- option commandを理解、活用する

### Description
- Python packageのインストールツール
- PyPI, VCS, Local directoryからパッケージを取得
- “requirements files”に書いてある範囲で、関連packageをinstallしてくれる 

### 動作の概要
1. Identify the base requirements. The user supplied arguments are processed here.
2. Resolve dependencies. What will be installed is determined here.
3. Build wheels. All the dependencies that can be are built into wheels.
4. Install the packages (and uninstall anything being upgraded/replaced)

### Usage
```
pip install [options] <requirement specifier> [package-index-options] ...
pip install [options] -r <requirements file> [package-index-options] ...
pip install [options] [-e] <vcs project url> ...
pip install [options] [-e] <local project path>
```

### Options
|option|機能|
|------|----|
|`-U`, `--upgrade`|Upgrade all specified packages to the newest available version. The handling of dependencies depends on the upgrade-strategy used.|
|`-r`, `--requirement <file>`|Install from the given requirements file. This option can be used multiple times.|

### pipの一括インストールオプション: -r requirements.txt
以下のコマンドで設定ファイルrequirements.txtに従ってパッケージが一括でインストールされる

```
pip install -r requirements.txt
```

- 設定ファイル名は任意だがrequirements.txtという名前が使われることが多い。
- requirements.txtはコマンドを実行するディレクトリに置いておく。別ディレクトリにある場合はパスを指定する。

### 設定ファイルの例
```
###### Requirements without Version Specifiers ######`
nose
nose-cov
beautifulsoup4

###### Requirements with Version Specifiers ######`
docopt == 0.6.1             # Version Matching. Must be version 0.6.1
keyring >= 4.1.1, <5.0.0    # Minimum version 4.1.1, Maximum version 4.9.9
coverage != 3.5             # Version Exclusion. Anything except version 3.5
Mopidy-Dirble ~= 1.1        # Compatible release. Same as >= 1.1, == 1.*
```

### 現在の環境をrequirements.txtへ出力する
```
touch requirements.txt
pip freeze > requirements.txt
```
