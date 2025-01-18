# walled-library

<!--
[![paper](https://img.shields.io/badge/arxiv-2408.03837-b31b1b)](https://arxiv.org/abs/2408.03837)
[![PyPI Latest Release](https://img.shields.io/pypi/v/walled-library.svg?logo=python&logoColor=white&color=blue)](https://pypi.org/project/walled-library/)
[![PyPI Downloads](https://static.pepy.tech/badge/walled-library)](https://pepy.tech/project/walled-library)
[![GitHub Page Views Count](https://badges.toozhao.com/badges/01J0NWXGZ7XGDPFYWHZ9EX1F46/blue.svg)](https://github.com/walledai/walled-library)
[![GitHub Release Date](https://img.shields.io/github/release-date/walledai/walled-library?logo=github&label=latest%20release&color=blue)](https://github.com/walledai/walled-library/releases/latest)
[![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/walledai/walled-library/docs.yml?label=Docs%20CI&color=blue)](https://walledai.github.io/walled-library/)
-->

## 🛠️ Installation and Set-Up

<!--
<h3>Installing from PyPI</h3>

Yes, we have published walled-library on PyPI! To install walled-library and all its dependencies, the easiest method would be to use `pip` to query PyPI. This should, by default, be present in your Python installation. To, install run the following command in a terminal or Command Prompt / Powershell:

```bash
$ pip install walled-library
```

Depending on the OS, you might need to use `pip3` instead. If the command is not found, you can choose to use the following command too:

```bash
$ python -m pip install walled-library
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
$ git clone https://github.com/walledai/walled-library.git
```

This stores a copy in the folder `walled-library`. You can then navigate into it using `cd walled-library`.

#### Poetry

This project can be used easily via a tool known as Poetry. This allows you to easily reflect edits made in the original source code! To install `poetry`, you can also install it using `pip` by typing in the command as follows:

```bash
$ pip install poetry
```

Again, if you have any issues with `pip`, check out [here](#installing-from-pypi).

After this, you can use the following command to install this library:

```bash
$ poetry install
```

This script creates a virtual environment for you to work with this library.

```bash
$ poetry shell
```

You can run the above script to enter a specialized shell to run commands within the virtual environment, including accessing the Python version with all the required dependencies to use walled-library at its finest!



<div style="padding: 10px; display: inline-block; background-color: white;">
  <p align="center">
    <img width="350" alt="walledai_logo_shield" src="https://github.com/walledai/walledeval/assets/32847115/d8b1d14f-7071-448b-8997-2eeba4c2c8f6">
  </p>
</div>
