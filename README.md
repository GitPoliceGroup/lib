# git.police

<!--
[![PyPI Latest Release](https://img.shields.io/pypi/v/git-police.svg?logo=python&logoColor=white&color=blue)](https://pypi.org/project/git-police/)
[![PyPI Downloads](https://static.pepy.tech/badge/git-police)](https://pepy.tech/project/git-police)
[![GitHub Page Views Count](https://badges.toozhao.com/badges/01J0NWXGZ7XGDPFYWHZ9EX1F46/blue.svg)](https://github.com/GitPoliceGroup/lib)
[![GitHub Release Date](https://img.shields.io/github/release-date/GitPoliceGroup/lib?logo=github&label=latest%20release&color=blue)](https://github.com/GitPoliceGroup/lib/releases/latest)
[![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/GitPoliceGroup/lib/docs.yml?label=Docs%20CI&color=blue)](https://GitPoliceGroup.github.io/lib/)
-->

## 🛠️ Installation and Set-Up

<!--
<h3>Installing from PyPI</h3>

Yes, we have published git-police on PyPI! To install git-police and all its dependencies, the easiest method would be to use `pip` to query PyPI. This should, by default, be present in your Python installation. To, install run the following command in a terminal or Command Prompt / Powershell:

```bash
$ pip install git-police
```

Depending on the OS, you might need to use `pip3` instead. If the command is not found, you can choose to use the following command too:

```bash
python -m pip install git-police
```

Here too, `python` or `pip` might be replaced with `py` or `python3` and `pip3` depending on the OS and installation configuration. If you have any issues with this, it is always helpful to consult 
[Stack Overflow](https://stackoverflow.com/).
-->

<h3>Installing from Source</h3>

To install from source, you need to get the following:

#### Git

Git is needed to install this repository. This is not completely necessary as you can also install the zip file for this repository and store it on a local drive manually. To install Git, follow [this guide](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).

After you have successfully installed Git, you can run the following command in a terminal / Command Prompt:

```bash
git clone https://github.com/GitPoliceGroup/lib.git git-police
```

This stores a copy in the folder `git-police`. You can then navigate into it using `cd git-police`.

#### Poetry

This project can be used easily via a tool known as Poetry. This allows you to easily reflect edits made in the original source code! To install `poetry`, you can also install it using `pip` by typing in the command as follows:

```bash
pip install poetry
```

Again, if you have any issues with `pip`, check out [here](#installing-from-pypi).

After this, you can use the following command to install this library:

```bash
poetry install
```

This script creates a virtual environment for you to work with this library.

```bash
poetry shell
```

You can run the above script to enter a specialized shell to run commands within the virtual environment, including accessing the Python version with all the required dependencies to use git-police at its finest!
