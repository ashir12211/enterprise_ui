# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Responsive UI',
    'author':"XAPP",
    'version': '20.0.1.0',
    'depends': ['web', 'base_setup'],
    'auto_install': ['web'],

'odoo_online': False,
    'license': 'LGPL-3',
    'support': 'teamxapp.dev@gmail.com',
    'live_test_url': 'https://responsive_ui.xappco.site/',
    'price': 2.00,
    'currency': 'USD',

    'images': [
        'static/description/enterprise_ui_cover.png',
        'static/description/enterprise_screenshot.png',
    ],

    'data': [
        'views/webclient_templates.xml',
    ],
    'assets': {
        'web._assets_primary_variables': [
            ('after', 'web/static/src/scss/primary_variables.scss', 'responsive_ui/static/src/**/*.variables.scss'),
            ('before', 'web/static/src/scss/primary_variables.scss', 'responsive_ui/static/src/scss/primary_variables.scss'),
        ],
        'web._assets_secondary_variables': [
            ('before', 'web/static/src/scss/secondary_variables.scss', 'responsive_ui/static/src/scss/secondary_variables.scss'),
        ],
        'web._assets_backend_helpers': [
            ('before', 'web/static/src/scss/bootstrap_overridden.scss', 'responsive_ui/static/src/scss/bootstrap_overridden.scss'),
        ],
        'web.assets_frontend': [
            'responsive_ui/static/src/webclient/home_menu/home_menu_background.scss', # used by login page
            'responsive_ui/static/src/webclient/navbar/navbar.scss',
        ],
        'web.assets_backend': [
            'responsive_ui/static/src/webclient/**/*.scss',
            'responsive_ui/static/src/views/**/*.scss',

            'responsive_ui/static/src/core/**/*',
            'responsive_ui/static/src/webclient/**/*.js',
            ('after', 'web/static/src/views/list/list_renderer.xml', 'responsive_ui/static/src/views/list/list_renderer_desktop.xml'),
            'responsive_ui/static/src/webclient/**/*.xml',
            'responsive_ui/static/src/views/**/*.js',
            'responsive_ui/static/src/views/**/*.xml',
            ('remove', 'responsive_ui/static/src/views/pivot/**'),

            # Don't include dark mode files in light mode
            ('remove', 'responsive_ui/static/src/**/*.dark.scss'),
        ],
        'web.assets_backend_lazy': [
            'responsive_ui/static/src/views/pivot/**',
        ],
        'web.assets_backend_lazy_dark': [
            ('include', 'web.dark_mode_variables'),
            # web._assets_backend_helpers
            ('before', 'responsive_ui/static/src/scss/bootstrap_overridden.scss', 'responsive_ui/static/src/scss/bootstrap_overridden.dark.scss'),
        ],
        'web.assets_web': [
            ('replace', 'web/static/src/main.js', 'responsive_ui/static/src/main.js'),
        ],
        # ========= Dark Mode =========
        "web.dark_mode_variables": [
            # web._assets_primary_variables
            ('before', 'responsive_ui/static/src/scss/primary_variables.scss', 'responsive_ui/static/src/scss/primary_variables.dark.scss'),
            ('before', 'responsive_ui/static/src/**/*.variables.scss', 'responsive_ui/static/src/**/*.variables.dark.scss'),
            # web._assets_secondary_variables
            ('before', 'responsive_ui/static/src/scss/secondary_variables.scss', 'responsive_ui/static/src/scss/secondary_variables.dark.scss'),
        ],
        "web.assets_web_dark": [
            ('include', 'web.dark_mode_variables'),
            # web._assets_backend_helpers
            ('before', 'responsive_ui/static/src/scss/bootstrap_overridden.scss', 'responsive_ui/static/src/scss/bootstrap_overridden.dark.scss'),
            # assets_backend
            'responsive_ui/static/src/**/*.dark.scss',
        ],
    },
    'license': 'LGPL-3',
}
