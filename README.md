# Weight Converter

This Python script converts weight between pounds (lbs) and kilograms (kg). The user inputs their weight and specifies the unit of measurement (lbs or kg), and the script outputs the converted weight in the desired unit.

## Features

- Accepts weight input from the user and validates that it is a numerical value.
- Prompts the user to specify the unit of measurement: pounds (L) or kilograms (K).
- Converts the weight to the other unit and displays the result.
- Handles invalid inputs gracefully and prompts the user to enter valid data.

## Usage

1. **Run the Script**: Execute the script in a Python environment.
2. **Input Weight**: Enter the weight when prompted. Ensure it's a numerical value.
3. **Specify Unit**: Enter `L` for pounds or `K` for kilograms.
4. **View Result**: The script will display the converted weight in the corresponding unit.

## Example

```bash
$ python weight_converter.py
weight: 150
(L)bs or (K)g: L
your weight is 68.0388555 kilos

$ python weight_converter.py
weight: 68.0388555
(L)bs or (K)g: K
your weight is 150.0 pounds
