import argparse
from moviepy.editor import VideoFileClip

# example command:   python mp4_to_gif.py input.mp4 output.gif -ss 00:00:10 -t 5 -s 320x240 -r 15

def mp4_to_gif(mp4_path, gif_path, start_time=0, end_time=None, fps=10):
    """
    Converts an MP4 video to a GIF.

    :param mp4_path: Path to the input MP4 file
    :param gif_path: Path to save the output GIF
    :param start_time: Start time in seconds (default: 0)
    :param end_time: End time in seconds (default: None, full video)
    :param fps: Frames per second for the GIF (default: 10)
    """
    clip = VideoFileClip(mp4_path).subclip(start_time, end_time)
    clip = clip.set_fps(fps)
    clip.write_gif(gif_path)
    print(f"GIF saved to {gif_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert MP4 to GIF using FFmpeg")
    parser.add_argument("input_file", help="Path to the input MP4 file")
    parser.add_argument("output_file", help="Path to the output GIF file")
    parser.add_argument("-ss", "--start_time", help="Start time in seconds (e.g., 00:00:10)", default=0)
    parser.add_argument("-t", "--duration", help="Duration in seconds (e.g., 5)", default=5)
    parser.add_argument("-r", "--fps", type=int, help="Frames per second (default: 10)", default=10)

    args = parser.parse_args()

    mp4_to_gif(args.input_file, args.output_file, args.start_time, args.duration, args.fps)