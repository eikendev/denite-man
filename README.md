Usage
-----

The `denite-man` plugin allows you to fuzzy find man pages within [Neovim](https://neovim.io/).
Issue `:Denite man` inside Neovim to get a list of all man pages and filter for the ones you want to open.

`denite-man` uses the built-in man page viewer of Neovim.
You can enable it by adding the following line to your Neovim configuration.
```
runtime! ftplugin/man.vim
```

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
