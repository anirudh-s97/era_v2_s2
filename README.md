# Animal Viewer & File Upload

This project consists of a backend Flask application that serves animal images and a frontend HTML page that allows users to view the images and upload files.

## Backend

The backend is built using Flask, a popular Python web framework. It provides the following functionality:

1. **Get Animal Image**: The `/get-animal-image/<animal>` endpoint returns the specified animal image (cat, dog, or elephant) as a JPEG file.
2. **Upload File**: The `/upload` endpoint accepts a file upload and returns metadata about the uploaded file, including the file name, size, and type.

To run the backend, you will need to have Python and Flask installed. You can start the server by running the following command in the project directory:

```
python backend-code.py
```

The server will run on `http://localhost:5000`.

## Frontend

The frontend is a simple HTML page that interacts with the backend. It allows users to:

1. **View Animal Images**: Click on the cat, dog, or elephant buttons to view the corresponding animal image.
2. **Upload Files**: Click or drag a file into the upload area to upload it and see its metadata.

To run the frontend, simply open the `final_front_end_code.html` file in a web browser.

## Setup

1. Create a `static` directory in the project root to store the animal images.
2. Add the `cat.jpg`, `dog.jpg`, and `elephant.jpg` files to the `static` directory.
3. Install the required Python packages:
   - Flask
   - Flask-CORS
4. Run the backend server using the command mentioned above.
5. Open the `final_front_end_code.html` file in a web browser to access the frontend.
