# FFMPEG

ffmpeg's handy commands.

#### Trim video

```bash
# Remove from the beginning to 3 seconds
ffmpeg -ss 2 -i input.mp4 -c copy input-trimmed.mp4

# Removed at the end from 45 seconds
ffmpeg -i input.mp4 -to 36 -c copy input-trimmed.mp4

# Remove at the both ends to 4 seconds and from 63 seconds
ffmpeg -i input.mp4 -ss 4 -to 35 -c copy input-trimmed.mp4

# Remove in the middle from 68 to 70 seconds
ffmpeg -i input.mp4 -filter_complex \
  "[0:v]split=2[part1][part2]; \
  [part1]trim=end=83,setpts=PTS-STARTPTS[p1]; \
  [part2]trim=start=83.5,setpts=PTS-STARTPTS[p2]; \
  [p1][p2]concat=n=2:v=1:a=0[v]" \
  -map "[v]" -an -c:v libx264 input-trimmed.mp4
```

#### Play the middle section (from 15s to 200s) of the video x10 faster

```bash
# Play middle portion of the video 10x faster
ffmpeg -i websocket-tls.mp4 -filter_complex \
  "[0:v]split=3[pre][mid][post]; \
  [pre]trim=0:21,setpts=PTS-STARTPTS[pre]; \
  [mid]trim=start=21:end=55,setpts=0.1*(PTS-STARTPTS)[mid]; \
  [post]trim=start=55,setpts=PTS-STARTPTS[post]; \
  [pre][mid][post]concat=n=3:v=1:a=0[v]" \
  -map "[v]" -an -c:v libx264 websocket-tls-trimmed.mp4
```

#### Convert to GIF

```bash
ffmpeg -i rest-crud.mp4 -filter_complex "fps=30,scale=1920:-1:flags=lanczos,split[o1][o2];[o1]palettegen[p];[o2]fifo[o3];[o3][p]paletteuse" rest-crud.gif
```
#### Add countdown timer

```bash
# First, get the duration of the input file
DURATION=$(ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 input.gif | grep -Po '^\d+')

# Create GIF with remaining seconds countdown (one decimal place)
ffmpeg -i input.gif -filter_complex \
"[0:v]drawtext=fontfile=/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf:text='%{expr\:trunc(($DURATION-t)*10)/10}':fontsize=24:fontcolor=white:x=(w-text_w)/2:y=h-th-10:box=1:boxcolor=black@0.5:boxborderw=5,split[s0][s1]; \
[s0]palettegen[p]; \
[s1][p]paletteuse" \
input-timer.gif
```