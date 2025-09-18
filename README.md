# Eigenfaces-FDW

## Project Overview
Eigenfaces-FDW is a face detection and recognition project built using Python, Flask, and OpenCV. It includes features for capturing snapshots, training eigenfaces, and processing images for data preparation.

## Folder Structure

- **auto_crop.py**: Script for auto-cropping images and saving them with unique names.
- **raw_pics/**: Directory for storing original images after processing.
- **server copy.py**: Backup or alternative version of the server script.
- **server.py**: Main server script for running the Flask application.
- **server1.py**: Another version of the server script.
- **snapshots/**: Directory for storing snapshots captured by the application.
- **static/**: Contains static files such as images, JavaScript, and CSS.
- **templates/**: Contains HTML templates for the Flask application.
- **train_results/**: Directory for storing results of eigenface training.
- **unprocessed/**: Directory for storing unprocessed raw images.
- **venv/**: Virtual environment for managing Python dependencies.

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/aqshaaqso/Eigenfaces-FDW.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Eigenfaces-FDW
   ```
3. Activate the virtual environment:
   ```bash
   .\venv\Scripts\activate
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Run the server:
   ```bash
   python server.py
   ```
6. Open your browser and navigate to `http://127.0.0.1:5000`.

## Features
- Snapshot capturing with sequential filenames.
- Eigenface training using snapshots.
- Auto-cropping and organizing images for data processing.

## Contributing
Feel free to fork this repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License
This project is licensed under the MIT License. See the LICENSE file for details.