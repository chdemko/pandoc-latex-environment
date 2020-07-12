#!/usr/bin/env python

"""
Pandoc filter for adding LaTeX environement on specific div
"""

from pandocfilters import toJSONFilters, stringify, RawInline, Para

import re
import sys

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
                    label = '\\label{' + id + '}'
                else:
                    label = ''

                currentProperties = dict(properties)
                if 'title' in currentProperties:
                    title = '[' + currentProperties['title'] + ']'
                else:
                    title = ''
                
                # fix an empty block not rendering any output
                if len(content) == 0:
                    content = [Para([])]

                #for line in content:
                #    sys.stderr.write(str(line))

                newconts = []
                pos = 0
                last = len(content)
                for node in content:
                    node_content = node['c']
                    #sys.stderr.write('Nodelength: {}; '.format(len(node['c'])))
                    #sys.stderr.write('Nodetype: {}; '.format(node['t']))
                    pos += 1
                    if pos == 1:
                        begin = [RawInline('tex', '\\begin{' + environment + '}' + title + '\n' + label)]
                        # Add the beginning Latex as a new paragraph to avoid conflict with bulletlists.
                        newconts.append(
                            {
                                't': 'Para',
                                'c': begin
                            }
                        )
                        # Now start adding the original content
                        newconts.append(
                            {
                                't': node['t'],
                                'c': node_content
                            }
                        )
                    elif pos == last:
                        end = [RawInline('tex', '\n\\end{' + environment + '}')]
                        # First add the original content.
                        newconts.append(
                            {
                                't': node['t'],
                                'c': node_content
                            }
                        )
                        # Then add the ending Latex as a new paragraph to avoid conflict with bulletlists.
                        newconts.append(
                            {
                                't': 'Para',
                                'c': end
                            }
                        )
                    else:
                        newconts.append(
                            {
                                't': node['t'],
                                'c': node_content
                            }
                        )
                        

                value[1] = newconts
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
