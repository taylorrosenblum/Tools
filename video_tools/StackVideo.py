import cv2
import numpy as np
import argparse

def main(video1_path, video2_path, output_path):
    """Stacks two videos horizontally."""

    cap1 = cv2.VideoCapture(video1_path)
    cap2 = cv2.VideoCapture(video2_path)

    if not cap1.isOpened() or not cap2.isOpened():
        print("Error opening video files")
        return

    # Get video properties
    width1 = int(cap1.get(cv2.CAP_PROP_FRAME_WIDTH))
    height1 = int(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT))
    width2 = int(cap2.get(cv2.CAP_PROP_FRAME_WIDTH))
    height2 = int(cap2.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Ensure both videos have the same height
    if height1 != height2:
        print("Videos must have the same height")
        return

    # Create output video writer
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, 10, (width1, height1 + height2))

    while True:
        ret1, frame1 = cap1.read()
        ret2, frame2 = cap2.read()

        if not ret1 or not ret2:
            break

        # Stack the frames horizontally
        stacked_frame = np.vstack((frame1, frame2))

        # Write the stacked frame to the output video
        out.write(stacked_frame)

    cap1.release()
    cap2.release()
    out.release()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("vid1")
    parser.add_argument("vid2")
    parser.add_argument("out")
    args = parser.parse_args()
    main(args.vid1, args.vid2, args.out)