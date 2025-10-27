from django import template
from django.utils.safestring import mark_safe
from django.utils.html import linebreaks

register = template.Library()

@register.filter
def quill_html(value):
    """
    Safely render QuillField content. Handles both Quill JSON format and plain text.
    """
    if not value:
        return ''
    
    try:
        # Try to get the HTML from QuillField
        if hasattr(value, 'html'):
            return mark_safe(value.html)
    except Exception:
        # If Quill parsing fails, treat as plain text
        pass
    
    # Fallback: if it's a string (plain text), convert line breaks to HTML
    if isinstance(value, str):
        return linebreaks(value)
    
    # If it has a json_string attribute, it's a QuillField with plain text
    if hasattr(value, 'json_string'):
        return linebreaks(value.json_string)
    
    return ''
