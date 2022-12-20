# ExpressionConversion
Change Infix, Postfix and Prefix to each other using Expression Tree.

## Example
```bash
Enter an expression: 1+2^3-4
Infix: ((1 + (2 ^ 3)) - 4)
Prefix: - + 1 ^ 2 3 4
Postfix: 1 2 3 ^ + 4 -
Eval: 5
```
<img src="img.png" height="300">

## Usage
First of all clone the project and install requirements.
```bash
git clone https://github.com/itsamirhn/ExpressionConversion.git && cd ExpressionConversion
pip install -r requirements.txt
```
Then run the following:
```bash
python main.py
```
