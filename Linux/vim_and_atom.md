# Atom

```
ctrl+shift+alt+p  - get file scope
ctrl+shift+p+"markdow" - markdwon preview
```

```
'atom-text-editor:not([mini])':
  'ctrl-d': 'editor:delete-line'
'.platform-win32 atom-text-editor, .platform-linux atom-text-editor':
  'ctrl-l': 'go-to-line:toggle'

'atom-workspace atom-text-editor:not([mini])':
  'ctrl->': 'find-and-replace:select-next'
  'ctrl-<': 'find-and-replace:select-undo'
  'ctrl-shift-up': 'editor:move-line-up'
  'ctrl-shift-down': 'editor:move-line-down'
  'alt-u': 'editor:upper-case'
  'alt-shift-u': 'editor:lower-case'
  'shift-alt-left': 'window:focus-pane-on-left'
  'shift-alt-right': 'window:focus-pane-on-right'
```
