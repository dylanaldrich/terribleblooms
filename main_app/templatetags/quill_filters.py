from django import template
from django.utils.safestring import mark_safe
from django.utils.html import linebreaks
import bleach

register = template.Library()

# Allowed HTML tags and attributes for sanitization
ALLOWED_TAGS = [
    'p', 'br', 'strong', 'em', 'u', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6',
    'ul', 'ol', 'li', 'a', 'blockquote', 'pre', 'code', 'span', 'div'
]
ALLOWED_ATTRIBUTES = {
    'a': ['href', 'title', 'target', 'rel'],
    'span': ['class'],
    'div': ['class'],
}

@register.filter
def quill_html(value):
    """
    Safely render QuillField content. Handles both Quill JSON format and plain text with HTML.
    Sanitizes HTML to prevent XSS attacks while allowing safe formatting tags.
    """
    if not value:
        return ''

    try:
        # Try to get the HTML from QuillField
        if hasattr(value, 'html'):
            # Sanitize the HTML content
            clean_html = bleach.clean(
                value.html,
                tags=ALLOWED_TAGS,
                attributes=ALLOWED_ATTRIBUTES,
                strip=True
            )
            return mark_safe(clean_html)
    except Exception:
        # If Quill parsing fails, fall through to handle as plain text/HTML
        pass

    # If it has a json_string attribute, it's a QuillField with stored content
    if hasattr(value, 'json_string'):
        content = value.json_string
        # If the content already contains HTML tags, sanitize it
        if '<' in content and '>' in content:
            clean_html = bleach.clean(
                content,
                tags=ALLOWED_TAGS,
                attributes=ALLOWED_ATTRIBUTES,
                strip=True
            )
            return mark_safe(clean_html)
        # Otherwise convert line breaks to HTML
        return mark_safe(linebreaks(content))

    # Fallback: if it's a string (plain text), convert line breaks to HTML
    if isinstance(value, str):
        if '<' in value and '>' in value:
            clean_html = bleach.clean(
                value,
                tags=ALLOWED_TAGS,
                attributes=ALLOWED_ATTRIBUTES,
                strip=True
            )
            return mark_safe(clean_html)
        return mark_safe(linebreaks(value))

    return ''
