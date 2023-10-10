# Ubuntu

### set mouse scrolling
```
$ xinput list
$ xinput list-props 12 | grep Wheel
$ xinput set-prop 12 "Evdev Scrolling Distance" 1, 3, 6
```
