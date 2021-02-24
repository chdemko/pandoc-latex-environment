#!/usr/bin/env python

"""
Pandoc filter for adding LaTeX environement on specific div
"""

from pandocfilters import toJSONFilters, stringify, RawBlock, Para

import re

def environment(key, value, format, meta):
    # Is it a div and the right format?
    if key == 'Div' and format in ['latex', 'beamer']:

        # Get the attributes
        [[id, classes, properties], content] = value

        currentClasses = set(classes)

        for environment, definedClasses in getDefined(meta).items():
            # Is the classes correct?
            if currentClasses >= definedClasses:
                if id != '':
                    label = '\n\\label{' + id + '}'
                else:
                    label = ''

                currentProperties = dict(properties)
                if 'title' in currentProperties:
                    title = '[' + currentProperties['title'] + ']'
                else:
                    title = ''
                
                before = RawBlock('tex', '\\begin{' + environment + '}' + title + label)
                after = RawBlock('tex', '\\end{' + environment + '}')

                value[1] = [before] + content + [after]
                break

def getDefined(meta):
    # Return the latex-environment defined in the meta
    if not hasattr(getDefined, 'value'):
        getDefined.value = {}
        if 'pandoc-latex-environment' in meta and meta['pandoc-latex-environment']['t'] == 'MetaMap':
            for environment, classes in meta['pandoc-latex-environment']['c'].items():
                if classes['t'] == 'MetaList':
                    getDefined.value[environment] = []
                    for klass in classes['c']:
                        string = stringify(klass)
                        if re.match('^[a-zA-Z][\w.:-]*$', string):
                            getDefined.value[environment].append(string)
                    getDefined.value[environment] = set(getDefined.value[environment])
    return getDefined.value

def main():
    toJSONFilters([environment])

if __name__ == '__main__':
    main()
