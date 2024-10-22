from PIL import Image, ImageEnhance, ImageFilter
import os

# Open the GIF file
gif_path = r'C:\Users\USER\Downloads\JARVIS-master\JARVIS-master\Jarvis\utils\images\home-ezgif.com-resize (1).gif'
gif = Image.open(gif_path)

# Create a directory to store the frames
frames_dir = 'frames'
os.makedirs(frames_dir, exist_ok=True)

# Split the GIF into individual frames
frames = []
for frame_number in range(gif.n_frames):
    gif.seek(frame_number)
    frame = gif.copy()
    frame = frame.convert("RGBA")

    try:
        # Enhance the quality of the frame
        print(f"Processing frame {frame_number + 1}/{gif.n_frames}")
        frame = frame.resize((frame.width * 2, frame.height * 2), Image.ANTIALIAS)  # Upscale the frame
        frame = frame.filter(ImageFilter.SHARPEN)  # Sharpen the frame

        # Save the frame
        frame_path = os.path.join(frames_dir, f'frame_{frame_number}.png')
        frame.save(frame_path)
        frames.append(frame)
    except Exception as e:
        print(f"Error processing frame {frame_number}: {e}")

# Save the enhanced frames back into a GIF
enhanced_gif_path = 'enhanced_home.gif'
if frames:
    frames[0].save(
        enhanced_gif_path,
        save_all=True,
        append_images=frames[1:],
        duration=gif.info['duration'],
        loop=0
    )
    print(f'Enhanced GIF saved as {enhanced_gif_path}')
else:
    print("No frames were processed.")
