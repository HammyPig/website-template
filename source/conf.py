extensions = ["myst_nb", "sphinx_design", "sphinx_copybutton"]
myst_enable_extensions = ["colon_fence"]

templates_path = ["_templates"]

html_theme = "pydata_sphinx_theme"

html_theme_options = {
    "navbar_start": ["navbar-logo"],
    "navbar_center": ["empty-space"],
    "navbar_end": ["navbar-icon-links"],

    "logo": {
        "text": "Title",
        "image_light": ""
    },
    
    "icon_links": [
        {
            "name": "GitHub",
            "url": "",
            "icon": "fa-brands fa-github",
            "type": "fontawesome"
        }
    ],
    
    "footer_start": [],
    "footer_center": [],
    "footer_end": [],
}
