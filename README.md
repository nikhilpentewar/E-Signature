# E-Signature Web Page

This is a project for creating an electronic signature web page using Django, Python, HTML, CSS, and JavaScript.

## Features

- Allows users to draw their signature using a mouse or touch screen device.
- Provides options to customize text color, background color, and font size.
- Supports saving and downloading signatures as PNG images.
- Stores signatures locally using browser local storage.

## Installation

1. Navigate to the project directory:
```bash
cd e-signature-webpage
```

2. Create a virtual environment (optional but recommended):
```bash
python -m venv env
```

3. Activate the virtual environment:
- On Windows:
```bash
env\Scripts\activate
```
- On macOS and Linux:
```bash
source env/bin/activate
```
4. Install the dependencies:
```bash
pip install -r requirements.txt
```
## Usage

1. Run the Django development server:
```bash
python manage.py runserver
```

2. Open a web browser and go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to access the e-signature web page.

3. Draw your signature using the mouse or touch screen device.

4. Customize the signature by changing text color, background color, and font size.

5. Click the "Save & download" button to save the signature as a PNG image.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](LICENSE)
