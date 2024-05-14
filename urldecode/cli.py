from urllib.parse import unquote
from click_extra import extra_command, echo, argument

@extra_command()
@argument("url_string")
def urldecode(url_string):
    utf_string = unquote(url_string)
    echo(f"{utf_string}")
