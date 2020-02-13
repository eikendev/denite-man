Usage
-----

The `denite-man` plugin allows you to fuzzy-search man pages within [Neovim](https://neovim.io/) or [Vim](https://www.vim.org/).

Usage examples:
 * `:Denite man`               - get a list of all man pages (and then manually filter for the ones you want to open).
 * `:Denite man::2`            - get a list of all section 2 man pages.
 * `:Denite man:open:2,3`      - get a list of all man pages, mentioning 'open' in sections 2 and 3.
 * `:Denite man:open::name`    - get a list of all man pages with 'open' in name, in all sections.

See the [docs](doc/denite-man.txt) for full documentation.

`denite-man` uses the built-in man page viewer of Neovim.
You can enable it by adding the following line to your Neovim configuration.
```
runtime! ftplugin/man.vim
```

In Vim, the [man.vim](https://github.com/vim-utils/vim-man) plugin must be installed.

Installation
------------

The plugin depends on [denite](https://github.com/Shougo/denite.nvim) by [Shougo](https://github.com/Shougo).
You need to install it in order to use this plugin.

### Plug
```
Plug 'Shougo/denite.nvim'
Plug 'eikendev/denite-man'
```
### Vundle
```
Plugin 'Shougo/denite.nvim'
Plugin 'eikendev/denite-man'
```
### NeoBundle
```
NeoBundle 'Shougo/denite.nvim'
NeoBundle 'eikendev/denite-man'
```
