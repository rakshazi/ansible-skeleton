# Ansible

Ansible skeleton for new projects

## Table of Contents

<!-- vim-markdown-toc GFM -->

* [Documentation](#documentation)
    - [Requirements](#requirements)
    - [Structure](#structure)
    - [Installation](#installation)
    - [(SKELETON) installation](#skeleton-installation)

<!-- vim-markdown-toc -->

## Documentation

### Requirements

* **ansible** >=2

### Structure

```
.
├── ansible.cfg       ## Ansible base configuration
├── inventories       ## Inventory files
│   └── default       ## Default inventory file
├── playbooks         ## Playbooks
│   └── init.yml      ## Example playbook
├── requirements.yml  ## Role dependensies from ansible-galaxy
├── roles             ## Your own roles
├── galaxy            ## Galaxy roles
└── tmp               ## Temporary files, like cached facts, logs, etc.
    ├── ansible.log   ## Main log file
    ├── facts.d       ## Facts cache
    └── ssh-...-...   ## SSH session persist
```

### Installation

1. Clone this repo
2. Download dependencies:

```bash
ansible-galaxy install -r requirements.yml
```

### (SKELETON) installation

```bash
git clone git@github.com:rakshazi/ansible-skeleton.git ansible
cd ansible
rm -rf .git
git init
git add --all
git add -f tmp/.gitkeep
git commit -m "Init skeleton"
echo -e "\033[0;32m[ansible]\033[0m Skeleton successfuly initialized, you should add your own origin repo with following command: \033[01;37mgit remote add origin <your origin url>\033[0m"
```
