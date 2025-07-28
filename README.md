# Perspective-Warp-OpenCV
A beginner-level OpenCV project demonstrating how to extract and warp a region of interest using perspective transformation. This is commonly used in document scanning, object flattening, and computer vision applications.
## Project Structure
- img.png
- main.py
## Technologies Used
- Python 3.13
- OpenCV (cv2)
- NumPy
- OS (standard library)
## How It Works
1. The script loads an input image (`img.png`).
2. It defines 4 corner points of the region to be warped.
3. Using `cv2.getPerspectiveTransform()`, it calculates the transformation matrix.
4. Applies the warp using `cv2.warpPerspective()`.
5. Displays the original and transformed images side-by-side using `np.hstack()`.
## Learnings
- Understanding of how perspective transforms work in image processing.
- Matrix math behind flattening or "unwarping" an image region.
- Practical use of NumPy with OpenCV.
## TODO(for future improvement)
- Add GUI to select 4 points interactively.
- Allow saving the output image automatically.
- Expand for real-time document scanning.
