
## Path
```
C:\Anaconda2\Lib\site-packages\notebook\static\custom
C:\Anaconda3\Lib\site-packages\notebook\static\custom
C:\Anaconda3\envs\py34\Lib\site-packages\notebook\static\custom
C:\Python27\ArcGIS10.1\Lib\site-packages\notebook\static\custom
```

```javascript
$([IPython.events]).on("app_initialized.NotebookApp", function () {

    IPython.keyboard_manager.command_shortcuts.add_shortcut('ctrl-k', function (event) {
        IPython.notebook.move_cell_up();
        return false;
    });

    IPython.keyboard_manager.command_shortcuts.add_shortcut('ctrl-j', function (event) {
        IPython.notebook.move_cell_down();
        return false;
    });

    IPython.keyboard_manager.command_shortcuts.add_shortcut('ctrl-b', function(event) {
        IPython.notebook.execute_all_cells();
        return false;
    });

    IPython.keyboard_manager.command_shortcuts.add_shortcut('alt-Minus', function(event) {
        IPython.notebook.split_cell();
        return false;
    });    
});
```
