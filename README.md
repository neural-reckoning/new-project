# (WIP) Template for new Neural Reckoning research projects

Use this repository to create new projects or just copy/paste bits you need.

Start by reading through [Patrick Mineault's Good Research Code Handbook](https://goodresearch.dev).

## Install

### Miniconda

This is a small version of Anaconda with just the basics. Quicker to install than Anaconda and anyway you will make your own environments.

[Download here](https://docs.anaconda.com/miniconda/).

### vscode

I know it's Microsoft but it's just a really good IDE and will save you a lot of headaches.

[Download here](https://code.visualstudio.com/).

### Copilot

In vscode, just install the Copilot extension. Use your Imperial College credentials for free access.

## Coding setup

### Setup Python environment

[Read this first.](https://goodresearch.dev/setup#set-up-a-virtual-environment)

Edit the ``environment.yml`` file giving it a new name specific to your project and adding any needed Python packages.

Then run:

```
conda env create -f environment.yml
```

vscode will automatically pick up on this environment, or you can explicitly use it by doing:

```
conda activate newproject
jupyter notebook
...
```

Add new packages by editing the ``environment.yml`` file and then running:

```
conda env update --file environment.yml  --prune
```

### Directory structure

Here's how I chose to do it for this repo based on [Patrick Mineault's recommendation](https://goodresearch.dev/setup#create-a-project-skeleton):

```
|-- data               (excluded from git in .gitignore)
|-- docs
|-- newproject         (reusable source code goes here, rename as appropriate)
|-- paper              (latex source code if you're using that)
|-- results            (exclude from git if it's heavy, can include if it's just some light csv files)
|-- scripts            (Jupyter notebooks etc. go here)
|-- tests
 -- .gitignore
 -- environment.yml
 -- README.md
 -- setup.py
```

### Setup installable project package

* [Read this.](https://goodresearch.dev/setup#create-a-pip-installable-package-recommended)
* Rename newproject directory to something related to your project, but only using lowercase characters and underscores, so it can be an installable package.
* Update setup.py file with this new name and any other metadata.
* Install it locally in an editable way with ``pip install -e .``.

## Code templates

TODO

### Managing data files

TODO

### Plotting publication ready figures

TODO

### Training/testing networks

TODO

### Spiking neural networks with PyTorch

TODO

## Remote development and high performance computing

### Use vscode remotely on lab servers or HPC

TODO

### Running jobs on HPC

TODO

## Paper writing

TODO (outline below)

* Use Overleaf or install TeX locally (or both!)
* To use both, see [Overleaf Git integration](https://www.overleaf.com/learn/how-to/Git_integration).
* Advantage of local development is you can use Copilot to help with the writing.
* Supplementary materials in a separate file.
* Generate diffs when responding to reviewer comments.
* Use Zotero to track papers. Get BiBTeX by clicking a paper and pressing Ctrl-Shift-C to copy into clipboard, then paste that into ``.bib`` file.