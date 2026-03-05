#!/usr/bin/env python3
import re

# Read the file
with open('src/bijeenkomst_6.md', 'r') as f:
    content = f.read()

# Find all slide separators (--- and ***)
# Split by lines to process
lines = content.split('\n')

# Calculate total number of slides
slide_count = 1  # First slide
for line in lines:
    if line.strip() == '---' or line.strip() == '***':
        slide_count += 1

print(f"Total slides: {slide_count}")

# Function to calculate gradient color
def calculate_gradient(slide_num, total):
    if total == 1:
        return "linear-gradient(to bottom right, #3498db, #3498db)"
    percentage = (slide_num - 1) / (total - 1)
    r = int(52 + 203 * percentage)
    g = int(152 + 103 * percentage)
    b = int(219 + 36 * percentage)
    color2 = f"#{r:02x}{g:02x}{b:02x}"
    return f"linear-gradient(to bottom right, #3498db, {color2})"

# Process the file
output_lines = []
current_slide = 1

for i, line in enumerate(lines):
    if i == 0:
        # Skip the first line if it already has a gradient comment
        if line.startswith('<!-- .slide: data-background-gradient'):
            # Replace with correct gradient
            gradient = calculate_gradient(current_slide, slide_count)
            output_lines.append(f'<!-- .slide: data-background-gradient="{gradient}" -->')
            continue
    
    if line.strip() == '---' or line.strip() == '***':
        # Add gradient comment before separator
        current_slide += 1
        gradient = calculate_gradient(current_slide, slide_count)
        output_lines.append(f'\n<!-- .slide: data-background-gradient="{gradient}" -->')
        output_lines.append(line)
    else:
        output_lines.append(line)

# Write back
with open('src/bijeenkomst_6.md', 'w') as f:
    f.write('\n'.join(output_lines))

print(f"Gradients added for {slide_count} slides")
print(f"Slide 1: {calculate_gradient(1, slide_count)}")
print(f"Slide {slide_count}: {calculate_gradient(slide_count, slide_count)}")
