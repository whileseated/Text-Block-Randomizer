# Random Text Display Web Page

Create a simple page that automatically displays a randomly selected text block upon each reload or refresh. 

## File Structure

- `index.html`: The HTML file that defines the structure of the web page.
- `script.js`: The JavaScript file responsible for handling the logic to display random text.
- `output_for_script.js`: A JavaScript file generated by the Python script, containing an array of text options.
- `raw_to_array.py`: A Python script that processes `raw_text.txt` and generates `output_for_script.js`.
- `raw_text.txt`: The source text file containing the various text blocks used in the project.

## Setup and Execution

1. **Prepare the Text Data**:
    - Place your desired text in `raw_text.txt`. Each line in this file will be a separate entry in the array.
    - Run the `raw_to_array.py` Python script. This script converts the contents of `raw_text.txt` into a JavaScript array and outputs it to `output_for_script.js`.

2. **Integrate JavaScript Files**:
    - Paste the array from `output_for_script.js` into `script.js`. 

3. **Load the Page**:
    - Open `index.html` in your web browser. The web page will automatically display a randomly selected text block from `script.js` each time you reload or refresh the page.

![How this tool looks in a web browser.](https://i.imgur.com/dejdUTc.gif)

## Notes

- This project does not require a server setup. It can run locally in your web browser.
- Ensure that all files are in the same directory for the scripts to work correctly.
- You can customize the text in `raw_text.txt` to change the displayed content.
