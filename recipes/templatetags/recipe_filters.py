import re
from django import template

# This creates a "library" where we'll store our custom filters
register = template.Library()

# The @register.filter decorator tells Django "this is a custom filter"
@register.filter
def clean_instructions(value):
    """Remove existing numbering from instructions"""
    
    # If there's no text, just return it as-is
    if not value:
        return value
    
    # Split the instructions into separate lines
    lines = value.split('\n')
    cleaned_lines = []
    
    # Go through each line one by one
    for line in lines:
        # Remove numbers and dots at the start (like "1. ", "2. ", "10. ")
        # The 're.sub' function finds patterns and replaces them
        cleaned_line = re.sub(r'^\s*\d+\.\s*', '', line.strip())
        
        # Only keep lines that have actual content
        if cleaned_line:
            cleaned_lines.append(cleaned_line)
    
    return cleaned_lines


@register.filter
def split(value, delimiter=','):
    """Split a string by delimiter and return as list"""
    if not value:
        return []
    items = str(value).split(delimiter)
    return [item.strip() for item in items if item.strip()]