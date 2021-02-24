# This Python file uses the following encoding: utf-8
from unittest import TestCase
from pandocfilters import Div, Str, RawBlock

import json

import pandoc_latex_environment

def init():
    if hasattr(pandoc_latex_environment.getDefined, 'value'):
        delattr(pandoc_latex_environment.getDefined, 'value')

def test_div():
    init()

    meta = {
        'pandoc-latex-environment': {
            'c': {
                'test': {
                    'c': [
                        {
                            'c': [
                                {
                                    'c': 'class1',
                                    't': 'Str'
                                }
                            ],
                            't': 'MetaInlines'
                        },
                        {
                            'c': [
                                {
                                    'c': 'class2',
                                    't': 'Str'
                                }
                            ],
                            't': 'MetaInlines'
                        }
                    ],
                    't': 'MetaList'
                }
            },
            't': 'MetaMap'
        }
    }

    src = json.loads(json.dumps(Div(
        [
            '',
            [
                'class1',
                'class2'
            ],
            []
        ],
        [
            {
                'c': [
                    {
                        'c': 'content',
                        't': 'Str'
                    }
                ],
                't': 'Plain'
            }
        ]
    )))
    dest = json.loads(json.dumps(Div(
        [
            '',
            [
                'class1',
                'class2'
            ],
            []
        ],
        [      
            {
                't': 'RawBlock',
                'c': ['tex', '\\begin{test}']
            },
            {
                'c': [
                {
                    'c': 'content',
                    't': 'Str'
                }],
                't': 'Plain'
            },
            {
                't': 'RawBlock',
                'c': ['tex', '\\end{test}']
            }
        ]
    )))

    pandoc_latex_environment.environment(src['t'], src['c'], 'latex', meta)

    assert json.loads(json.dumps(src)) == dest

def test_empty():
    init()

    meta = {
        'pandoc-latex-environment': {
            'c': {
                'test': {
                    'c': [
                        {
                            'c': [
                                {
                                    'c': 'class1',
                                    't': 'Str'
                                }
                            ],
                            't': 'MetaInlines'
                        },
                        {
                            'c': [
                                {
                                    'c': 'class2',
                                    't': 'Str'
                                }
                            ],
                            't': 'MetaInlines'
                        }
                    ],
                    't': 'MetaList'
                }
            },
            't': 'MetaMap'
        }
    }

    src = json.loads(json.dumps(Div(
        [
            '',
            [],
            []
        ],
        [
            {
                'c': [
                    {
                        'c': 'content',
                        't': 'Str'
                    }
                ],
                't': 'Plain'
            }
        ]
    )))
    dest = json.loads(json.dumps(Div(
        [
            '',
            [],
            []
        ],
        [
            {
                'c': [
                    {
                        'c': 'content',
                        't': 'Str'
                    }
                ],
                't': 'Plain'
            }
        ]
    )))

    pandoc_latex_environment.environment(src['t'], src['c'], 'latex', meta)

    assert json.loads(json.dumps(src)) == dest


def test_div_with_id():
    init()

    meta = {
        'pandoc-latex-environment': {
            'c': {
                'test': {
                    'c': [
                        {
                            'c': [
                                {
                                    'c': 'class1',
                                    't': 'Str'
                                }
                            ],
                            't': 'MetaInlines'
                        },
                        {
                            'c': [
                                {
                                    'c': 'class2',
                                    't': 'Str'
                                }
                            ],
                            't': 'MetaInlines'
                        }
                    ],
                    't': 'MetaList'
                }
            },
            't': 'MetaMap'
        }
    }

    src = json.loads(json.dumps(Div(
        [
            'identifier',
            [
                'class1',
                'class2'
            ],
            []
        ],
        [
            {
                'c': [
                    {
                        'c': 'content',
                        't': 'Str'
                    }
                ],
                't': 'Plain'
            }
        ]
    )))

    dest = json.loads(json.dumps(Div(
        [
            'identifier',
            [
                'class1',
                'class2'
            ],
            []
        ],
        [      
            {
                't': 'RawBlock',
                'c': ['tex', '\\begin{test}\n\\label{identifier}']
            },
            {
                'c': [
                {
                    'c': 'content',
                    't': 'Str'
                }],
                't': 'Plain'
            },
            {
                't': 'RawBlock',
                'c': ['tex', '\\end{test}']
            }
        ]
    )))

    pandoc_latex_environment.environment(src['t'], src['c'], 'latex', meta)

    assert json.loads(json.dumps(src)) == dest


def test_div_with_title():
    init()

    meta = {
        'pandoc-latex-environment': {
            'c': {
                'test': {
                    'c': [
                        {
                            'c': [
                                {
                                    'c': 'class1',
                                    't': 'Str'
                                }
                            ],
                            't': 'MetaInlines'
                        },
                        {
                            'c': [
                                {
                                    'c': 'class2',
                                    't': 'Str'
                                }
                            ],
                            't': 'MetaInlines'
                        }
                    ],
                    't': 'MetaList'
                }
            },
            't': 'MetaMap'
        }
    }

    src = json.loads(json.dumps(Div(
        [
            '',
            [
                'class1',
                'class2'
            ],
            [
                ['title', 'theTitle']
            ]
        ],
        [
            {
                'c': [
                    {
                        'c': 'content',
                        't': 'Str'
                    }
                ],
                't': 'Plain'
            }
        ]
    )))
    
    dest = json.loads(json.dumps(Div(
        [
            '',
            [
                'class1',
                'class2'
            ],
            [
                ['title', 'theTitle']
            ]
        ],
        [      
            {
                't': 'RawBlock',
                'c': ['tex', '\\begin{test}[theTitle]']
            },
            {
                'c': [
                {
                    'c': 'content',
                    't': 'Str'
                }],
                't': 'Plain'
            },
            {
                't': 'RawBlock',
                'c': ['tex', '\\end{test}']
            }
        ]
    )))

    pandoc_latex_environment.environment(src['t'], src['c'], 'latex', meta)

    assert json.loads(json.dumps(src)) == dest
