# FFMPEG

ffmpeg's handy commands.

#### Trim video

```bash
ffmpeg -i input.mp4 -ss 00:00:09.500 -to 00:01:08 -c copy output.mp4
```
#### Convert to GIF

```bash
ffmpeg -i input.mp4 -filter_complex "fps=10,scale=1920:-1:flags=lanczos,split[o1][o2];[o1]palettegen[p];[o2]fifo[o3];[o3][p]paletteuse" out.gif
```
