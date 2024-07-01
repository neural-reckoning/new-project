# (WIP) Template for new Neural Reckoning research projects

Use this repository to create new projects or just copy/paste bits you need.

Start by reading through [Patrick Mineault's Good Research Code Handbook](https://goodresearch.dev).

## Install

* [Miniconda](https://docs.anaconda.com/miniconda/). This is a small version of Anaconda with just the basics. Quicker to install than Anaconda and anyway you will make your own environments.
* [vscode](https://code.visualstudio.com/). I know it's Microsoft but it's just a really good IDE and will save you a lot of headaches.
* Copilot. In vscode, just install the Copilot extension. Use your Imperial College credentials for free access.

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

Some interesting packages to note in the template ``environment.yml`` file are:

* ``ipykernel``: Lets Jupyter notebook detect this environment. I always stick this in every environment I use.
* ``pip`` and ``pip:``: These lines let you install some packages that don't have Conda versions using Pip
* ``ipywidgets``: Interactive notebooks with sliders that recompute and regenerate figures, etc.

### Directory structure

Here's how I chose to do it for this repo based on [Patrick Mineault's recommendation](https://goodresearch.dev/setup#create-a-project-skeleton):

```
|-- scripts            Jupyter notebooks etc. go here
|-- newproject         reusable source code goes here, rename as appropriate
|-- paper              latex source code if you're using that
|-- data               input datasets, etc. excluded from git in .gitignore
|-- results            exclude from git if it's heavy, can include if it's just some light csv files
|-- docs               this folder is aspirational
|-- tests              so is this one
 -- .gitignore         use this to list files that shouldn't be included in the repo, e.g. binaries
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

Using [Overleaf](https://www.overleaf.com) is probably in general the easiest way to work together on a paper. You can still use the latex files in the ``paper/`` directory of this repository to initialise your Overleaf document.

You can also install TeX locally (on Windows I recommend MiKTeX). "LaTeX Workshop" is an OK extension to vscode for working with LaTeX that will do things like rebuild each time you save and show the pdf in a panel, like Overleaf does. An advantage of local development is that you can use Copilot to help with the writing.

You can also do both, see [Overleaf Git integration](https://www.overleaf.com/learn/how-to/Git_integration).

Read through the ``paper.tex`` file and comments for good practices on writing LaTeX docs.

A good way to organise the code is to have a separate ``supplementary.tex`` file for Supplmentary Materials because journals often ask for this. You can set up diffs by having a ``paper-old.tex`` and ``diff.tex`` file (useful for responding to reviews).

For the bibliography, I recommend using Zotero to track papers. You can get BiBTeX by clicking a paper in Zotero and pressing Ctrl-Shift-C to copy into clipboard, then paste that into the ``.bib`` file.