# Pizza-Project-Business
+
+## Features
+
+- Supports pizza sizes: Small (`S`), Medium (`M`), Large (`L`)
+- Optional pepperoni and extra cheese
+- Automatic pricing based on size and toppings
+- Input validation for size and topping choices
+- Clean order summary output
+
+## Pricing Rules
+
+- Base pizza prices:
+  - Small: `$15`
+  - Medium: `$20`
+  - Large: `$25`
+- Pepperoni:
+  - Small: `+$2`
+  - Medium/Large: `+$3`
+- Extra cheese: `+$1`
+
+## Requirements
+
+- Python 3.8+ (or any modern Python 3 version)
+
+## How to Run
+
+From the project root:
+
+```bash
+python3 Pizza_project.py
+```
+
+Then answer the prompts:
+
+- `What size pizza do you want? S, M, or L:`
+- `Do you want pepperoni? Y or N:`
+- `Do you want extra cheese? Y or N:`
+
+## Example
+
+```text
+Welcome to the Python Pizza Ordering System!
+What size pizza do you want? S, M, or L: M
+Do you want pepperoni? Y or N: Y
+Do you want extra cheese? Y or N: N
+
+--------------------------
+Order Summary
+--------------------------
+Size: Medium (M)
+Pepperoni: Yes
+Extra Cheese: No
+Final Bill: $23.00
+--------------------------
+Thank you for your order!
+```
+
+## Project Structure
+
+- `Pizza_project.py` — main program logic
+- `README.md` — project documentation
 
EOF
)
