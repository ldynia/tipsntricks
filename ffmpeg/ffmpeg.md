# FFMPEG

ffmpeg's handy commands.

#### Trim video

```bash
# Trim first 2 seconds (remove from the start)
ffmpeg -ss 3 -i input.mp4 -c:v copy output.mp4

# Trim to 225 seconds (remove fro the end)
ffmpeg -i input.mp4 -to 225 -c:v -an copy output.mp4

# Trim from 4 to 63 seconds (remove both ends)
ffmpeg -i input.mp4 -ss 7 -to 63 -c copy output.mp4
```
#### Convert to GIF

```bash
ffmpeg -i input.mp4 -filter_complex "fps=10,scale=1920:-1:flags=lanczos,split[o1][o2];[o1]palettegen[p];[o2]fifo[o3];[o3][p]paletteuse" out.gif
```

#### Play the middle section of video x4 faster

```bash
# Play video faster in the middle of the video from 10 to 125 seconds
ffmpeg -i input.mp4 -filter_complex \
  "[0:v]split=3[pre][mid][post]; \
  [pre]trim=0:15,setpts=PTS-STARTPTS[pre]; \
  [mid]trim=start=15:end=193,setpts=0.25*(PTS-STARTPTS)[mid]; \
  [post]trim=start=193,setpts=PTS-STARTPTS[post]; \
  [pre][mid][post]concat=n=3:v=1:a=0[v]" \
  -map "[v]" -an -c:v libx264 output-trim.mp4
```
